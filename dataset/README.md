# The Dataset

I have created a dataset of multiple novels / short stories from 4 authors:
1. Sir Arthur Conan Doyle 
2. (Not) Shakespeare
3. P. G. Wodehouse
4. Mark Twain



## Reasoning behind choice of authors

I chose these 4 authors specifically because they represent distinctly different literary styles and tonalities, making them ideal for a classification task focused on authorship rather than topic. Each author has a unique voice that should be distinguishable through stylistic features:

### Sir Arthur Conan Doyle
Writes in a methodological and logical narrative. The Sherlock Holmes stories are predominantly written in first person from Dr. Watson's perspective, featuring:
- Direct, precise prose with emphasis on observation and deduction
- Straightforward, journalistic style of storytelling

### William Shakespeare
Very poetic / dramatic writing with:
- Elizabethan English with archaic vocabulary and syntax
- Lot of wordplay and complex rhetoric
- Distinct from the prose style of the other three authors

### P.G. Wodehouse
A comedic genius known for light, humorous prose:
- Whimsical, playful language with elaborate similes
- British upper-class vernacular and slang
- Comic timing through sentence structure
- Ironic and satirical tone
- Absurd situations described with deadpan sophistication

### Mark Twain
An American author who uses:
- Conversational American English
- Social satire and regional dialects


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

