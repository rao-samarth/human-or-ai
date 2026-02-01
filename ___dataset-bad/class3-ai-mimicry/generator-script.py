import os
import time
import random
import csv
from pathlib import Path

# Note that for this code to work, you need to have a .env file with your GEMINI_API_KEY
# Your .env file should look like this:
# GEMINI_API_KEY=your_actual_api_key_here
from dotenv import load_dotenv
from google import genai


OUTPUT_DIR = Path(".")
TOPICS_CSV = Path("../topic-list.csv")

MIN_WORDS = 100
MAX_WORDS = 200

MODEL_NAME = "gemini-pro-latest"
SLEEP_SECONDS = 2.0  # Increased to avoid rate limits

# Class 3 requirement:
# 1000 paragraphs total = 250 per author (4 authors)
AUTHORS = [
    {"id": "DOYLE", "name": "Sir Arthur Conan Doyle", "dir": "01-arthur-conan-doyle"},
    {"id": "WODE",  "name": "P. G. Wodehouse", "dir": "02-pg-wodehouse"},
    {"id": "SHAKE",  "name": "William Shakespeare", "dir": "03-william-shakespeare"},
    {"id": "TWAIN",  "name": "Mark Twain", "dir": "04-mark-twain"},
]

# I am adding these 'DIVERSITY_MODES' to ensure that there is diversity in the output.
# Since it is writing style that matters and not the content, I deem it okay to have these modes.
DIVERSITY_MODES = [
    "a reflective inner monologue",
    "a short scene with dialogue",
    "a descriptive narrative moment",
    "a moral dilemma unfolding in real time",
    "a slightly comedic situation",
    "a tense confrontation between two people",
    "a letter-like voice (but still one paragraph)",
    "a calm, analytical tone",
    "a dramatic and emotional tone",
    "a cynical and sarcastic tone",
    "a hopeful and optimistic tone",
    "a melancholic and quiet tone",
    "a fast-paced, action-oriented tone",
    "a philosophical tone",
    "a courtroom/confession vibe without explicit legal terms",
    "an unreliable narrator vibe",
    "a third-person omniscient vibe",
    "a first-person casual vibe",
]

SETTINGS = [
    "in a small town",
    "in a crowded city",
    "in a quiet countryside setting",
    "inside a house late at night",
    "during a formal event",
    "while traveling",
    "in a workplace situation",
    "during a family gathering",
    "in a public place where strangers overhear",
    "in a tense private conversation",
]

def word_count(text: str) -> int:
    return len(text.strip().split())

def clean_output(text: str) -> str:
    # Gemini was adding titles, quotes, or extra newlines and whatnot so I am cleaning it here
    # We only want one paragraph, no titles or extra formatting.
    text = text.strip()

    # Remove surrounding quotes if any
    if (text.startswith('"') and text.endswith('"')) or (text.startswith("“") and text.endswith("”")):
        text = text[1:-1].strip()

    # Collapse multiple blank lines into one space
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    text = " ".join(lines)

    return text.strip()

def build_prompt(topic_name: str, topic_description: str, mode: str, setting: str, author_name: str) -> str:
    # Class 3: AI mimicry of a specific author.
    # IMPORTANT: we do NOT include the topic name in the output.
    return f"""
Write ONE standalone paragraph of {MIN_WORDS}-{MAX_WORDS} words.

Topic (do not mention this label explicitly): {topic_name}.
Topic description: {topic_description}.

You must mimic the writing style of: {author_name}

Style constraints:
- Strongly imitate the author's voice (sentence rhythm, vocabulary, tone, punctuation habits).
- Do NOT mention the author's name in the paragraph.
- Do NOT quote or copy lines from any existing work.
- Do NOT use famous character names or iconic named places from the author's works.
- The paragraph must feel like natural narrative prose, not like a list or an essay.
- Avoid numbered points, headings, or bullet lists.
- Avoid phrases like "In conclusion", "This essay discusses", or "Overall".
- Avoid the words: tapestry, delve, testament (overused AI-isms).
- Do not include the topic name as a phrase in the paragraph.

Diversity constraints:
- Write it as {mode}.
- Setting: {setting}.
- Vary sentence length and rhythm.
- Do not reuse the same plot structure as earlier outputs.

Output format:
- Return only the paragraph text.
""".strip()

def load_topics(csv_path: Path):
    topics = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            topics.append({
                "topic_id": row["topic_id"].strip(),
                "topic_name": row["topic_name"].strip(),
                "topic_description": row["topic_description"].strip(),
            })
    return topics

def get_counts_per_topic_for_author(topic_ids):
    """
    Returns dict: topic_id -> number_of_paragraphs
    Per author total must be 250 across 20 topics:
      10 topics get 13
      10 topics get 12
    """
    topic_ids = list(topic_ids)
    random.shuffle(topic_ids)  # shuffle to avoid always giving same topics the +1

    counts = {}
    for idx, tid in enumerate(topic_ids):
        counts[tid] = 13 if idx < 10 else 12
    return counts

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY. Put it in your .env file.")

    client = genai.Client(api_key=api_key)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    topics = load_topics(TOPICS_CSV)
    topic_by_id = {t["topic_id"]: t for t in topics}
    all_topic_ids = [t["topic_id"] for t in topics]

    # Keep a small memory of previous paragraphs per (author, topic) to discourage repetition
    topic_history = {(a["id"], tid): [] for a in AUTHORS for tid in all_topic_ids}

    for author in AUTHORS:
        author_id = author["id"]
        author_name = author["name"]
        author_dir = OUTPUT_DIR / author["dir"]
        author_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n==============================")
        print(f"Generating for author: {author_name} ({author_id})")
        print(f"==============================")

        counts_per_topic = get_counts_per_topic_for_author(all_topic_ids)

        for tid in all_topic_ids:
            tname = topic_by_id[tid]["topic_name"]
            tdesc = topic_by_id[tid]["topic_description"]

            target_count = counts_per_topic[tid]
            print(f"\n--- {author_id} | {tid}: {tname} | target={target_count} ---")

            for i in range(1, target_count + 1):
                outfile = author_dir / f"{author_id}_{tid}_{i:02d}.txt"
                if outfile.exists():
                    print(f"Skipping existing {outfile.name}")
                    continue

                mode = random.choice(DIVERSITY_MODES)
                setting = random.choice(SETTINGS)

                avoid_hint = ""
                key = (author_id, tid)
                if topic_history[key]:
                    recent = topic_history[key][-5:]
                    avoid_hint = (
                        "\nAvoid repeating these recent ideas:\n- "
                        + "\n- ".join(recent)
                    )

                prompt = build_prompt(tname, tdesc, mode, setting, author_name) + avoid_hint

                # Generate
                try:
                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=prompt,
                        config={
                            "temperature": 1.0,
                            "top_p": 0.95,
                            "max_output_tokens": 2048,
                        }
                    )

                    if response.candidates and response.candidates[0].content.parts:
                        raw_text = response.candidates[0].content.parts[0].text
                    else:
                        print(f"Warning: No text generated for {outfile.name}")
                        print(f"Finish reason: {response.candidates[0].finish_reason if response.candidates else 'No candidates'}")
                        time.sleep(2)
                        continue

                except Exception as e:
                    print(f"Error generating {outfile.name}: {e}")
                    time.sleep(5)
                    continue

                text = clean_output(raw_text)
                wc = word_count(text)

                # Retry if needed
                retries = 0
                while (wc < MIN_WORDS or wc > MAX_WORDS or len(text) < 50) and retries < 2:
                    retries += 1
                    print(f"Retry {retries} for {outfile.name} (wc={wc})")

                    try:
                        response = client.models.generate_content(
                            model=MODEL_NAME,
                            contents=prompt,
                            config={
                                "temperature": 1.1,
                                "top_p": 0.95,
                                "max_output_tokens": 2048,
                            }
                        )

                        if response.candidates and response.candidates[0].content.parts:
                            raw_text = response.candidates[0].content.parts[0].text
                            text = clean_output(raw_text)
                            wc = word_count(text)
                        else:
                            print(f"No text in retry for {outfile.name}")
                            break

                    except Exception as e:
                        print(f"Retry error: {e}")
                        time.sleep(5)

                outfile.write_text(text + "\n", encoding="utf-8")
                print(f"Wrote {outfile.name} ({wc} words)")

                idea_tag = " ".join(text.split()[:12])
                topic_history[key].append(idea_tag)

                time.sleep(SLEEP_SECONDS)

    print("\nDone. Generated Class 3 (AI mimicry) paragraphs.")

if __name__ == "__main__":
    main()
