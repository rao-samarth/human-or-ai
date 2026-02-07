"""
Generate Class 2 (AI-written, no mimicry) paragraphs for Agatha Christie books.
This script:
1. Generates themes from the Agatha Christie books
2. Generates 20 paragraphs based on those themes
"""
import os
import re
import csv
import time
import random
from pathlib import Path
from dotenv import load_dotenv
from google import genai
# Load environment variables
load_dotenv()

# Configuration
MIN_WORDS = 100
MAX_WORDS = 200
NUM_PARAGRAPHS = 20
THEMES_PER_BOOK = 3
MODEL_NAME = "gemini-pro-latest"
SLEEP_SECONDS = 2.0
OUTPUT_DIR = "class-2"
THEMES_DIR = "themes"

# Diversity modes for variation
DIVERSITY_MODES = [
    "a reflective inner monologue",
    "a short scene with dialogue",
    "a descriptive narrative moment",
    "a moral dilemma unfolding in real time",
    "a slightly comedic situation",
    "a tense confrontation between two people",
    "a letter-like voice",
    "a calm, observant tone",
    "a dramatic, urgent tone",
    "a cynical perspective",
    "a hopeful perspective",
    "a melancholic mood",
    "a nostalgic reflection",
    "an outsider's viewpoint",
    "a conversation overheard",
    "someone remembering a past event",
    "a moment of sudden realization",
    "a philosophical musing"
]

SETTINGS = [
    "a small town",
    "a crowded city",
    "the countryside",
    "a house at night",
    "a formal event",
    "while traveling",
    "a workplace",
    "a family gathering",
    "a public place",
    "a private conversation"
]

def count_words(text):
    """Count words in text."""
    return len(text.split())

def generate_themes_for_book(client, book_path, book_name, num_themes=3):
    """Generate themes from a book using Gemini."""
    print(f"\nGenerating {num_themes} themes for {book_name}...")
    
    # Read book content (sample from beginning and middle)
    with open(book_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Take samples to stay within token limits
    words = content.split()
    sample_size = min(5000, len(words))
    sample = ' '.join(words[:sample_size])
    
    prompt = f"""Based on this excerpt from a mystery novel, identify {num_themes} distinct themes or topics that could inspire short paragraphs. 

Excerpt:
{sample}

For each theme, provide a concise one-sentence description. The themes should be general enough to work as writing prompts (e.g., "the psychology of deception", "trust between friends", "the weight of secrets").

DO NOT mention:
- Character names from the book
- The book title or author
- Specific plot points

Provide exactly {num_themes} themes, one per line, numbered."""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": 0.7,
            }
        )
        
        themes = []
        if response.candidates and response.candidates[0].content.parts:
            raw_text = response.candidates[0].content.parts[0].text
            lines = raw_text.strip().split('\n')
            for line in lines:
                # Remove numbering and clean up
                line = re.sub(r'^\d+[\.\)]\s*', '', line.strip())
                if line:
                    themes.append(line)
        
        print(f"Generated themes: {themes}")
        return themes[:num_themes]
    
    except Exception as e:
        print(f"Error generating themes: {e}")
        return []

def generate_paragraph(client, theme, book_name, attempt=1):
    """Generate a single paragraph based on a theme."""
    # Random diversity
    mode = random.choice(DIVERSITY_MODES)
    setting = random.choice(SETTINGS)
    
    prompt = f"""Write a short fictional paragraph about: {theme}

Requirements:
- EXACTLY {MIN_WORDS}-{MAX_WORDS} words (count carefully!)
- Write as {mode}
- Set in {setting}
- Create original content, DO NOT reference or copy any existing books
- Use natural, varied language
- AVOID these AI-detection words: "tapestry", "delve", "testament"
- DO NOT use essay structures, numbered points, or headings
- DO NOT use phrases like "In conclusion" or "In summary"

Write the paragraph now:"""

    temperature = 1.0 if attempt == 1 else 1.1
    
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": temperature,
            }
        )
        
        paragraph = response.candidates[0].content.parts[0].text.strip() if response.candidates else ""
        word_count = count_words(paragraph)
        
        print(f"  Generated paragraph: {word_count} words (attempt {attempt})")
        
        if MIN_WORDS <= word_count <= MAX_WORDS:
            return paragraph
        else:
            if attempt < 3:
                print(f"  Word count out of range, retrying...")
                time.sleep(SLEEP_SECONDS)
                return generate_paragraph(client, theme, book_name, attempt + 1)
            else:
                print(f"  Warning: Could not get correct word count after 3 attempts")
                return paragraph
    
    except Exception as e:
        print(f"  Error generating paragraph: {e}")
        return None

def main():
    # Load API key and create client
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY. Set it in your .env file.")
    
    client = genai.Client(api_key=api_key)
    
    # Find all .txt files
    txt_files = [f for f in os.listdir('.') 
                 if f.endswith('.txt') and os.path.isfile(f)]
    
    print(f"Found {len(txt_files)} books")
    
    # Create directories
    os.makedirs(THEMES_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Step 1: Generate themes for each book
    all_themes = []
    for txt_file in txt_files:
        book_name = os.path.splitext(txt_file)[0]
        clean_name = re.sub(r'[^\w\s-]', '', book_name).strip().replace(' ', '_')
        
        themes = generate_themes_for_book(client, txt_file, book_name, THEMES_PER_BOOK)
        
        # Save themes to CSV
        theme_csv = os.path.join(THEMES_DIR, f"{clean_name}_themes.csv")
        with open(theme_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['theme_id', 'theme'])
            for i, theme in enumerate(themes, 1):
                writer.writerow([i, theme])
                all_themes.append((clean_name, i, theme))
        
        time.sleep(SLEEP_SECONDS)
    
    print(f"\nGenerated {len(all_themes)} themes total")
    
    # Step 2: Generate paragraphs from themes
    print(f"\nGenerating {NUM_PARAGRAPHS} paragraphs...")
    
    # Randomly select themes to generate from
    selected_themes = random.sample(all_themes, min(NUM_PARAGRAPHS, len(all_themes)))
    
    for i, (book_name, theme_id, theme) in enumerate(selected_themes, 1):
        print(f"\nParagraph {i}/{NUM_PARAGRAPHS}")
        print(f"Book: {book_name}, Theme: {theme}")
        
        paragraph = generate_paragraph(client, theme, book_name)
        
        if paragraph:
            # Save paragraph
            output_file = os.path.join(OUTPUT_DIR, f"{book_name}_T{theme_id:02d}_P{i:02d}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(paragraph)
            print(f"  Saved to {output_file}")
        
        time.sleep(SLEEP_SECONDS)
    
    print(f"\n✓ Generation complete! {NUM_PARAGRAPHS} paragraphs saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
