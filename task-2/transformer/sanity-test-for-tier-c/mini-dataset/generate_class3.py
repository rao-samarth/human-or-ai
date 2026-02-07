"""
Generate Class 3 (AI mimicry) paragraphs that imitate Agatha Christie's writing style.
This script generates paragraphs that mimic Christie's voice, sentence structure, and style.
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
MODEL_NAME = "gemini-pro-latest"
SLEEP_SECONDS = 2.0
OUTPUT_DIR = "class-3"
THEMES_DIR = "themes"

# Author info
AUTHOR_NAME = "Agatha Christie"
AUTHOR_ID = "CHRISTIE"

# Diversity modes
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

def load_themes():
    """Load all themes from the themes directory."""
    themes = []
    
    if not os.path.exists(THEMES_DIR):
        print(f"Error: {THEMES_DIR} directory not found. Run generate_class2.py first.")
        return []
    
    for theme_file in os.listdir(THEMES_DIR):
        if theme_file.endswith('_themes.csv'):
            book_name = theme_file.replace('_themes.csv', '')
            filepath = os.path.join(THEMES_DIR, theme_file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    themes.append((book_name, int(row['theme_id']), row['theme']))
    
    return themes

def generate_paragraph_mimicking_author(client, theme, book_name, attempt=1):
    """Generate a paragraph that mimics Agatha Christie's style."""
    # Random diversity
    mode = random.choice(DIVERSITY_MODES)
    setting = random.choice(SETTINGS)
    
    prompt = f"""Write a short fictional paragraph about: {theme}

Requirements:
- EXACTLY {MIN_WORDS}-{MAX_WORDS} words (count carefully!)
- Write as {mode}
- Set in {setting}
- IMITATE {AUTHOR_NAME}'s voice, sentence rhythm, vocabulary, tone, and punctuation habits
- Create original content inspired by the theme
- AVOID these AI-detection words: "tapestry", "delve", "testament"
- DO NOT use essay structures, numbered points, or headings

Write the paragraph now in {AUTHOR_NAME}'s distinctive style:"""

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
                return generate_paragraph_mimicking_author(client, theme, book_name, attempt + 1)
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
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load themes from Class 2 generation
    all_themes = load_themes()
    
    if not all_themes:
        print("Error: No themes found. Please run generate_class2.py first.")
        return
    
    print(f"Loaded {len(all_themes)} themes")
    
    # Randomly select themes to generate from
    selected_themes = random.sample(all_themes, min(NUM_PARAGRAPHS, len(all_themes)))
    
    print(f"\nGenerating {NUM_PARAGRAPHS} paragraphs mimicking {AUTHOR_NAME}...")
    
    for i, (book_name, theme_id, theme) in enumerate(selected_themes, 1):
        print(f"\nParagraph {i}/{NUM_PARAGRAPHS}")
        print(f"Book: {book_name}, Theme: {theme}")
        
        paragraph = generate_paragraph_mimicking_author(client, theme, book_name)
        
        if paragraph:
            # Save paragraph
            output_file = os.path.join(OUTPUT_DIR, f"{AUTHOR_ID}_{book_name}_T{theme_id:02d}_P{i:02d}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(paragraph)
            print(f"  Saved to {output_file}")
        
        time.sleep(SLEEP_SECONDS)
    
    print(f"\n✓ Generation complete! {NUM_PARAGRAPHS} paragraphs saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
