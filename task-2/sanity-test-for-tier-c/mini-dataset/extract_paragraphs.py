"""
Extract 20 random paragraphs of 100-200 words from Agatha Christie books.
"""
import os
import re
import random

# Configuration
MIN_WORDS = 100
MAX_WORDS = 200
NUM_PARAGRAPHS = 20
INPUT_DIR = "."
OUTPUT_DIR = "class-1"

def count_words(text):
    """Count words in text."""
    return len(text.split())

def extract_paragraphs_from_file(filepath):
    """Extract paragraphs from a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by double newlines to get paragraphs
    paragraphs = re.split(r'\n\s*\n', content)
    
    # Filter paragraphs by word count
    valid_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        word_count = count_words(para)
        if MIN_WORDS <= word_count <= MAX_WORDS:
            valid_paragraphs.append(para)
    
    return valid_paragraphs

def main():
    # Find all .txt files in current directory (excluding this script's directory)
    txt_files = [f for f in os.listdir(INPUT_DIR) 
                 if f.endswith('.txt') and os.path.isfile(f)]
    
    print(f"Found {len(txt_files)} text files")
    
    # Extract all valid paragraphs from all books
    all_paragraphs = []
    for txt_file in txt_files:
        print(f"Processing {txt_file}...")
        paragraphs = extract_paragraphs_from_file(txt_file)
        book_name = os.path.splitext(txt_file)[0]
        # Store with book name for later reference
        for para in paragraphs:
            all_paragraphs.append((book_name, para))
        print(f"  Found {len(paragraphs)} valid paragraphs")
    
    print(f"\nTotal valid paragraphs across all books: {len(all_paragraphs)}")
    
    # Randomly select NUM_PARAGRAPHS paragraphs
    if len(all_paragraphs) < NUM_PARAGRAPHS:
        print(f"Warning: Only {len(all_paragraphs)} paragraphs available, less than requested {NUM_PARAGRAPHS}")
        selected = all_paragraphs
    else:
        selected = random.sample(all_paragraphs, NUM_PARAGRAPHS)
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Save selected paragraphs
    for i, (book_name, para) in enumerate(selected, 1):
        # Clean book name for filename
        clean_book_name = re.sub(r'[^\w\s-]', '', book_name).strip().replace(' ', '_')
        output_file = os.path.join(OUTPUT_DIR, f"{clean_book_name}_{i:02d}.txt")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(para)
        
        word_count = count_words(para)
        print(f"Saved paragraph {i} ({word_count} words) to {output_file}")
    
    print(f"\nExtraction complete! {len(selected)} paragraphs saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
