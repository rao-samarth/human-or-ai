# This is a script to clean Gutenberg text files in specified directories.
# It uses the `gutenberg_cleaner` library which can be found at: https://github.com/kiasar/gutenberg_cleaner.
# The script has been generated using Claude.

import os
from pathlib import Path
from gutenberg_cleaner import simple_cleaner, super_cleaner

def remove_gutenberg_mentions(text):
    """
    Remove all lines that mention 'Project Gutenberg' (case-insensitive).
    
    Args:
        text: The text to clean
        
    Returns:
        Text with Project Gutenberg mentions removed
    """
    lines = text.split('\n')
    filtered_lines = [line for line in lines if 'project gutenberg' not in line.lower() and 'gutenberg' not in line.lower() and 'project' not in line.lower() and 'end of this etext of the complete works of william shakespeare' not in line.lower()]
    return '\n'.join(filtered_lines)

def clean_gutenberg_files(directories, output_dir=None):
    """
    Clean all .txt files in the specified directories using gutenberg_cleaner.
    
    Args:
        directories: List of directory paths containing .txt files
        output_dir: Optional directory to save cleaned files. If None, files are overwritten.
    """
    
    # Track statistics
    total_files = 0
    successful = 0
    failed = 0
    
    # Process each directory
    for directory in directories:
        dir_path = Path(directory)
        
        # Check if directory exists
        if not dir_path.exists():
            print(f"Warning: Directory '{directory}' does not exist. Skipping...")
            continue
        
        # Find all .txt files in the directory
        txt_files = list(dir_path.glob('*.txt'))
        
        if not txt_files:
            print(f"No .txt files found in '{directory}'")
            continue
        
        print(f"\nProcessing {len(txt_files)} files in '{directory}'...")
        
        # Process each file
        for txt_file in txt_files:
            total_files += 1
            
            try:
                # Read the original file
                with open(txt_file, 'r', encoding='utf-8') as f:
                    book_text = f.read()
                
                # Clean the text using simple_cleaner (removes headers/footers only)
                cleaned_text = simple_cleaner(book_text)
                
                # Remove lines mentioning Project Gutenberg
                cleaned_text = remove_gutenberg_mentions(cleaned_text)
                
                # Determine output path
                if output_dir:
                    output_path = Path(output_dir)
                    output_path.mkdir(parents=True, exist_ok=True)
                    # Preserve original filename
                    output_file = output_path / txt_file.name
                else:
                    # Overwrite original file
                    output_file = txt_file
                
                # Write the cleaned text
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(cleaned_text)
                
                successful += 1
                print(f"✓ Cleaned: {txt_file.name}")
                
            except Exception as e:
                failed += 1
                print(f"✗ Failed to clean {txt_file.name}: {str(e)}")
    
    # Print summary
    print("\n" + "="*50)
    print("CLEANING SUMMARY")
    print("="*50)
    print(f"Total files processed: {total_files}")
    print(f"Successfully cleaned: {successful}")
    print(f"Failed: {failed}")
    print("="*50)


if __name__ == "__main__":
    # Define your 4 directories here
    directories_to_clean = [
        "01-arthur-conan-doyle",
        "02-william-shakespeare",  
        "03-pg-wodehouse",  
        "04-mark-twain"
    ]
    
    # Option 1: Overwrite original files (default)
    clean_gutenberg_files(directories_to_clean)
    
    # Option 2: Save cleaned files to a new directory (uncomment to use)
    # clean_gutenberg_files(directories_to_clean, output_dir="cleaned_books")