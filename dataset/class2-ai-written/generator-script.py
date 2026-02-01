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


# Directory structure
CLASS1_DIR = Path("../class1-human-written")
TOPIC_DATA_DIR = Path("../topic-data")
OUTPUT_DIR = Path("./ai-generated-paragraphs")

# Generation parameters
THEMES_PER_BOOK = 5
PARAS_PER_THEME = 2
MIN_WORDS = 100
MAX_WORDS = 200

MODEL_NAME = "gemini-pro-latest"
SLEEP_SECONDS = 2.0  # Increased to avoid rate limits

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
    if (text.startswith('"') and text.endswith('"')) or (text.startswith(""") and text.endswith(""")):
        text = text[1:-1].strip()

    # Collapse multiple blank lines into one space
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    text = " ".join(lines)

    return text.strip()


def get_all_authors():
    """Get all author directories from class1-human-written."""
    authors = []
    if CLASS1_DIR.exists():
        for item in sorted(CLASS1_DIR.iterdir()):
            if item.is_dir() and item.name.startswith(('01-', '02-', '03-', '04-')):
                authors.append(item)
    # Explicitly handles: 01-arthur-conan-doyle, 02-pg-wodehouse, 03-mark-twain, 04-william-shakespeare
    return authors


def read_extraction_log(author_dir: Path):
    """Read extraction_log.csv from an author's extracted_paragraphs directory."""
    log_file = author_dir / "extracted_paragraphs" / "extraction_log.csv"
    books = []
    
    if not log_file.exists():
        print(f"Warning: {log_file} not found")
        return books
    
    with open(log_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        seen_books = set()
        for row in reader:
            book_name = row.get("book_name", "").strip()
            if book_name and book_name not in seen_books:
                seen_books.add(book_name)
                books.append(book_name)
    
    return books


def read_full_book(author_dir: Path, book_name: str):
    """Read the full book text from the full-books directory."""
    # Try to find the book file - it might be .txt or other extension
    full_books_dir = author_dir / "full-books"
    
    if not full_books_dir.exists():
        print(f"Warning: {full_books_dir} not found")
        return None
    
    # Files have number prefixes like "001_A-Man-of-Means.txt"
    # Try to find a file that ends with the book name
    for book_file in full_books_dir.iterdir():
        if book_file.is_file() and book_file.suffix == ".txt":
            # Check if the filename (after removing number prefix) matches book_name
            # e.g., "001_A-Man-of-Means.txt" should match "A-Man-of-Means"
            if book_file.stem.endswith(f"_{book_name}") or book_file.stem == book_name:
                try:
                    with open(book_file, "r", encoding="utf-8") as f:
                        return f.read()
                except Exception as e:
                    print(f"Error reading {book_file}: {e}")
                    return None
    
    print(f"Warning: Could not find book file for {book_name} in {full_books_dir}")
    return None


def generate_themes_for_book(client, book_name: str, author_name: str):
    """Generate 5 themes for a book using Gemini, without mentioning the book name."""
    # Don't send the full text - these are famous books that Gemini knows
    # Clean up author name to remove number prefix
    author_clean = author_name.split('-', 1)[-1].replace('-', ' ').title()
    book_clean = book_name.replace('-', ' ')
    
    prompt = f"""List 5 themes from "{book_clean}" by {author_clean}. Each theme must be 3-8 words. Do not mention book title, characters, or author. Output ONLY 5 numbered lines.""".strip()
    
    print(f"     Prompt: {prompt}")
    print(f"     Model: {MODEL_NAME}")
    
    try:
        print(f"     Making API call...")
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": 0.7,
                "top_p": 0.9,
                "max_output_tokens": 8192,  # High limit to accommodate thinking tokens
            }
        )
        
        if response.candidates and response.candidates[0].content.parts:
            raw_text = response.candidates[0].content.parts[0].text
            
            # Parse the numbered themes
            themes = []
            for line in raw_text.strip().split('\n'):
                line = line.strip()
                # Remove numbering (e.g., "1.", "1)", "1 -", etc.)
                for prefix in ["1.", "2.", "3.", "4.", "5.", "1)", "2)", "3)", "4)", "5)"]:
                    if line.startswith(prefix):
                        line = line[len(prefix):].strip()
                        break
                # Also try to remove "N. " or "N - " patterns
                if line and line[0].isdigit():
                    parts = line.split(None, 1)
                    if len(parts) > 1:
                        line = parts[1].strip(". -")
                
                if line:
                    themes.append(line)
            
            if not themes:
                print(f"     ERROR: Could not parse themes from response:")
                print(f"     Raw response: {raw_text[:500]}")
            
            return themes[:THEMES_PER_BOOK]  # Ensure we only return 5
        else:
            print(f"     ERROR: No content in response")
            if response.candidates:
                print(f"     Finish reason: {response.candidates[0].finish_reason}")
                print(f"     Safety ratings: {response.candidates[0].safety_ratings if hasattr(response.candidates[0], 'safety_ratings') else 'N/A'}")
            return []
            
    except Exception as e:
        print(f"     ERROR generating themes: {e}")
        import traceback
        traceback.print_exc()
        return []


def save_themes_to_csv(book_name: str, themes: list):
    """Save themes to a CSV file in topic-data directory."""
    TOPIC_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Clean book name for filename
    safe_book_name = book_name.replace(" ", "_").replace("/", "_")
    csv_path = TOPIC_DATA_DIR / f"{safe_book_name}-themelist.csv"
    
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["theme_id", "theme_description"])
        for i, theme in enumerate(themes, 1):
            writer.writerow([f"T{i:02d}", theme])
    
    print(f"Saved themes to {csv_path}")
    return csv_path


def pass1_generate_all_themes(client):
    """PASS 1: Generate theme CSVs for all books from all authors."""
    print("\n" + "="*60)
    print("PASS 1: Generating themes from books")
    print("="*60 + "\n")
    
    authors = get_all_authors()
    
    if not authors:
        print("No authors found in class1-human-written!")
        return
    
    total_books = 0
    
    for author_dir in authors:
        author_name = author_dir.name
        print(f"\n### Processing author: {author_name} ###")
        
        books = read_extraction_log(author_dir)
        print(f"Found {len(books)} books for {author_name}")
        
        for book_name in books:
            print(f"\n  -> Processing book: {book_name}")
            
            # Check if themes already exist
            safe_book_name = book_name.replace(" ", "_").replace("/", "_")
            csv_path = TOPIC_DATA_DIR / f"{safe_book_name}-themelist.csv"
            
            if csv_path.exists():
                print(f"     Themes already exist, skipping...")
                total_books += 1
                continue
            
            # Generate themes (no need to read full book - Gemini knows these famous works)
            themes = generate_themes_for_book(client, book_name, author_name)
            
            if themes:
                print(f"     Generated {len(themes)} themes:")
                for i, theme in enumerate(themes, 1):
                    print(f"       {i}. {theme}")
                
                # Save to CSV
                save_themes_to_csv(book_name, themes)
                total_books += 1
            else:
                print(f"     Failed to generate themes")
            
            # Sleep to avoid rate limits
            time.sleep(SLEEP_SECONDS)
    
    print(f"\n{'='*60}")
    print(f"PASS 1 COMPLETE: Generated themes for {total_books} books")
    print(f"{'='*60}\n")


def build_paragraph_prompt(theme_description: str, mode: str, setting: str) -> str:
    """Build prompt for generating a paragraph based on a theme."""
    return f"""
Write ONE standalone paragraph of exactly {MIN_WORDS}-{MAX_WORDS} words.

Theme (do not mention this label explicitly): {theme_description}

Style constraints:
- Neutral modern English (not imitating any specific author).
- The paragraph must feel natural and human-like, not like a list or an essay.
- Avoid numbered points, headings, or bullet lists.
- Avoid phrases like "In conclusion", "This essay discusses", or "Overall".
- Avoid the words: tapestry, delve, testament (overused AI-isms).
- Do not reference any specific book titles, character names, or authors.

Diversity constraints:
- Write it as {mode}.
- Setting: {setting}.
- Vary sentence length and rhythm.
- Make it feel original and spontaneous.

Output format:
- Return only the paragraph text, nothing else.
""".strip()


def generate_paragraph(client, theme_description: str, mode: str, setting: str, max_retries: int = 3):
    """Generate a single paragraph for a theme, with retry logic for word count."""
    prompt = build_paragraph_prompt(theme_description, mode, setting)
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config={
                    "temperature": 1.0,
                    "top_p": 0.95,
                    "max_output_tokens": 8192, 
                    "safety_settings": [
                        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
                        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
                        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
                        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
                    ],
                }
            )
            
            # Debug: Print the full response structure
            if not response.candidates:
                print(f"     Attempt {attempt+1}: No candidates in response")
                print(f"     Response: {response}")
                time.sleep(1)
                continue
            
            candidate = response.candidates[0]
            print(f"     Finish reason: {candidate.finish_reason}")
            
            # Check for safety ratings blocking content
            if hasattr(candidate, 'safety_ratings'):
                print(f"     Safety ratings: {candidate.safety_ratings}")
            
            if not candidate.content or not candidate.content.parts:
                print(f"     Attempt {attempt+1}: No content/parts in candidate")
                if hasattr(candidate, 'finish_reason'):
                    print(f"     Finish reason: {candidate.finish_reason}")
                time.sleep(1)
                continue
                
            raw_text = candidate.content.parts[0].text
            text = clean_output(raw_text)
            wc = word_count(text)
            
            # Check word count
            if MIN_WORDS <= wc <= MAX_WORDS:
                return text, wc
            else:
                print(f"     Attempt {attempt+1}: Word count {wc} out of range, retrying...")
                time.sleep(1)
                
        except Exception as e:
            print(f"     Attempt {attempt+1}: Error - {e}")
            time.sleep(2)
    
    # If all retries failed, return None
    return None, 0


def pass2_generate_all_paragraphs(client):
    """PASS 2: Generate paragraphs for all themes in all CSV files."""
    print("\n" + "="*60)
    print("PASS 2: Generating paragraphs from themes")
    print("="*60 + "\n")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get all theme CSV files
    theme_csvs = list(TOPIC_DATA_DIR.glob("*-themelist.csv"))
    
    if not theme_csvs:
        print("No theme CSV files found! Run PASS 1 first.")
        return
    
    print(f"Found {len(theme_csvs)} theme CSV files\n")
    
    total_paragraphs = 0
    
    for csv_path in sorted(theme_csvs):
        book_name = csv_path.stem.replace("-themelist", "").replace("_", " ")
        print(f"\n### Processing themes from: {book_name} ###")
        
        # Read themes from CSV
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            themes = [(row["theme_id"], row["theme_description"]) for row in reader]
        
        print(f"Found {len(themes)} themes")
        
        for theme_id, theme_desc in themes:
            print(f"\n  Theme {theme_id}: {theme_desc}")
            
            # Generate 4 paragraphs for this theme
            for para_num in range(1, PARAS_PER_THEME + 1):
                # Create filename: bookname_themeID_paranum.txt
                safe_book_name = csv_path.stem.replace("-themelist", "")
                filename = f"{safe_book_name}_{theme_id}_P{para_num:02d}.txt"
                outfile = OUTPUT_DIR / filename
                
                if outfile.exists():
                    print(f"    P{para_num}: Already exists, skipping...")
                    total_paragraphs += 1
                    continue
                
                # Random diversity settings
                mode = random.choice(DIVERSITY_MODES)
                setting = random.choice(SETTINGS)
                
                # Generate paragraph
                text, wc = generate_paragraph(client, theme_desc, mode, setting)
                
                if text:
                    # Save to file
                    outfile.write_text(text + "\n", encoding="utf-8")
                    print(f"    P{para_num}: Generated ({wc} words) -> {filename}")
                    total_paragraphs += 1
                else:
                    print(f"    P{para_num}: Failed after retries")
                
                # Sleep to avoid rate limits
                time.sleep(SLEEP_SECONDS)
    
    print(f"\n{'='*60}")
    print(f"PASS 2 COMPLETE: Generated {total_paragraphs} paragraphs")
    print(f"{'='*60}\n")


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY. Put it in your .env file.")

    client = genai.Client(api_key=api_key)
    
    # PASS 1: Generate themes from books
    pass1_generate_all_themes(client)
    
    # PASS 2: Generate paragraphs from themes
    pass2_generate_all_paragraphs(client)
    
    print("\nAll done! Generated AI paragraphs in 2-pass approach.")


if __name__ == "__main__":
    main()
