# Class 1 - Real Human Text

- This contains human-written text of 4 authors.  
- Conan Doyle and P. G. Wodehouse form a baseline, for the required 2 authors.
- William Shakespeare and Mark Twain form an added layer of complexity, which we will see later. This is due to their 
- We know the text is human written since all the books were written before the age of AI.  

## Reasoning behind choice of authors

I chose these 4 authors specifically because they represent distinctly different literary styles and tonalities, making them ideal for a classification task focused on authorship rather than topic. Each author has a unique voice that should be distinguishable through stylistic features:

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

### William Shakespeare
Very poetic / dramatic writing with:
- Elizabethan English with archaic vocabulary and syntax
- Lot of wordplay and complex rhetoric
- Distinct from the prose style of the other three authors


### Mark Twain
An American author who uses:
- Conversational American English
- Social satire and regional dialects


## Note on dataset variants (baseline vs extension)

The task requires text from **two authors**. To satisfy this requirement while still exploring a more robust setup, I treat the dataset as:

- **Baseline authors (required):** Conan Doyle + Wodehouse  
- **Extended authors (additional variation):** Shakespeare + Mark Twain  

The extended set is included to test whether results generalize across a wider range of writing styles, rather than overfitting to two specific authors.

Specific further information of writing styles can be found here:
1. https://iwl.me/writer/Arthur_Conan_Doyle
2. https://iwl.me/writer/P._G._Wodehouse
3. https://iwl.me/writer/William_Shakespeare
4. https://iwl.me/writer/Mark_Twain

These four authors span different time periods (16th-20th centuries), nationalities (English and American), and genres (drama, mystery, comedy, social commentary). Through this I am ensuring maximum stylistic variation while all being available on Project Gutenberg with substantial bodies of work. 


## Cleaning of the data

The data, while originally from The Gutenberg Project, was all sourced from [rcdm-uga/Gutenberg_Text](https://github.com/rcdm-uga/Gutenberg_Text). In this repository, the text is given in the .txt file format.

Then, I used [kiasar/gutenberg_cleaner](https://github.com/kiasar/gutenberg_cleaner) to clean all the files.

This library has 2 main functions - `simple_cleaner`, and `super_cleaner`. I used `simple_cleaner` as it is significantly more deterministic. The `super_cleaner` functionality removes all paragraphs (blank-line-separated blocks of text) with number of tokens within a range set by the user. This would have resulted in many smaller paragraphs getting deleted.

After using the simple_cleaner, I still found that many of the txt files still had Project Gutenberg tags in the top / bottom of the file. I thus added this functionality manually in my [cleaner.py](cleaner.py).


Notes:
- I have kept chapter names, epilogues, tables of contents, character lists (only relevant for Shakespeare) as is. My reasoning for this is that it is relevant to the authors style and tonality. I did contemplate removing them, but decided not to as they are also a unique style of each of the authors.
- I have removed all general `NOTES.` and `Transcribers Notes` sections. This was because they were not written by the author itself and thus will corrupt the datasets. 
- I also first tried using step 2 of [mbforbes/Gutenberg](https://github.com/mbforbes/Gutenberg) to clean the data.  However, this ended up deleting significantly more of the actual content than required.


## Dataset Split: 80% for Fine-tuning, 20% for Testing

To support potential fine-tuning experiments while maintaining held-out test data, I split each author's books into two groups:

- **80% of books** → moved to `<author-surname>-for-finetuning/` subdirectories
- **20% of books** → kept in the main author directories

This split was done randomly with a fixed seed (42) for reproducibility. The distribution is:

| Author | Total Books | Finetuning (80%) | Testing (20%) |
|--------|-------------|------------------|---------------|
| Arthur Conan Doyle | 51 | 40 | 11 |
| P.G. Wodehouse | 38 | 30 | 8 |
| William Shakespeare | 101 | 80 | 21 |
| Mark Twain | 153 | 122 | 31 |

**Rationale:** This structure allows for:
- Fine-tuning AI models (Class 4) on the majority of each author's work
- Testing/validation on held-out books that the model hasn't seen
- Maintaining stylistic consistency while preventing overfitting to specific works  

!! **NOTE:** I ensured that the ones which remained in the non-finetuned dataset encompass all themes. 