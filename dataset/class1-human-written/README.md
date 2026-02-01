# Class 1 - Real Human Text

- This contains human-written text of 4 authors.  
- Conan Doyle and P. G. Wodehouse form a baseline, for the required 2 authors.
- Mark Twain forms an added layer of complexity, which we will see later. This is due to his unique style of writing
- We know the text is human written since all the books were written before the age of AI.  

## Reasoning behind choice of authors

I chose these 3 authors specifically because they represent distinctly different literary styles and tonalities, making them ideal for a classification task focused on authorship rather than topic. Each author has a unique voice that should be distinguishable through stylistic features:

### Sir Arthur Conan Doyle
Writes in a methodological and logical narrative. The Sherlock Holmes stories are predominantly written in first person from Dr. Watson's perspective, featuring:
- Direct, precise prose with emphasis on observation and deduction
- Straightforward, journalistic style of storytelling

### P.G. Wodehouse
A comedic genius known for light, humorous prose:
- Whimsical, playful language with elaborate similes
- British upper-class vernacular and slang
- Comic timing through sentence structure
- Ironic and satirical tone
- Absurd situations described with deadpan sophistication

### Mark Twain (extended author)
An American author who uses:
- Conversational American English
- Social satire and regional dialects


## Note on dataset variants (baseline vs extension)

The task requires text from **two authors**. To satisfy this requirement while still exploring a more robust setup, I treat the dataset as:

- **Main authors:** Conan Doyle + Wodehouse  
- **Extended authors:** Mark Twain  

The extended set is included to test whether results generalize across a wider range of writing styles, rather than overfitting to two specific authors.

Specific further information of writing styles can be found here:
1. https://iwl.me/writer/Arthur_Conan_Doyle
2. https://iwl.me/writer/P._G._Wodehouse
3. https://iwl.me/writer/Mark_Twain


## Cleaning of the data

The data, while originally from The Gutenberg Project, was all sourced from [rcdm-uga/Gutenberg_Text](https://github.com/rcdm-uga/Gutenberg_Text). In this repository, the text is given in the .txt file format.

Then, I used [kiasar/gutenberg_cleaner](https://github.com/kiasar/gutenberg_cleaner) to clean all the files.

This library has 2 main functions - `simple_cleaner`, and `super_cleaner`. I used `simple_cleaner` as it is significantly more deterministic. The `super_cleaner` functionality removes all paragraphs (blank-line-separated blocks of text) with number of tokens within a range set by the user. This would have resulted in many smaller paragraphs getting deleted.

After using the simple_cleaner, I still found that many of the txt files still had Project Gutenberg tags in the top / bottom of the file. I thus added this functionality manually in my [cleaner.py](cleaner.py).


Notes:
- I have kept chapter names, epilogues, tables of contents, character lists as is. My reasoning for this is that it is relevant to the authors style and tonality. I did contemplate removing them, but decided not to as they are also a unique style of each of the authors.
- I have removed all general `NOTES.` and `Transcribers Notes` sections. This was because they were not written by the author itself and thus will corrupt the datasets. 
- I also first tried using step 2 of [mbforbes/Gutenberg](https://github.com/mbforbes/Gutenberg) to clean the data.  However, this ended up deleting significantly more of the actual content than required.



## Splitting the books into paragraphs, instead of keeping the whole book

Earlier, the human dataset consisted of full-length books, while the AI dataset consisted of short, standalone paragraphs. Comparing these directly would be misleading, since many linguistic features depend strongly on text length and document structure.

To make the comparison fair, all texts are analyzed at the paragraph level. Each book is split into paragraph-sized chunks (100–250 words), and these chunks are treated as individual samples. This ensures that human and AI texts are comparable in length and format, and that stylistic differences are not simply artifacts of comparing books to paragraphs.

Working at the paragraph level also increases the number of usable samples and allows standard statistical tests and classifiers to be applied reliably. To avoid information leakage, I will later ensure that all paragraphs from the same book are always kept in the same train/test split.

### Files which are doing this

In the directories of each author, `admin.py` creates `admin.csv` which goes through all the books, and lists the number of paragraphs per book, and the number of paragraphs with 100-250 words per book.

Then, `extract_paragraphs.py` randomly selects 25 books which have 20+ paragraphs of 100-250 words, and then randomly selects 20 of these paragraphs, splits them into different .txt files, and saves them.

I have ensured that all the "random" selections are uniformly randomly selected.