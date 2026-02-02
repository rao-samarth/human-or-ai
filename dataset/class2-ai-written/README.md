# Class 2 - AI Generated Text

Here, we have AI generated paragraphs, which are on the basis of the main themes of the various different books in Class 1.  
We are first generating themes for the books, and then generating the actual content. This approach is explained and justified [below]().  

The script used for generation can be found [here](generator-script.py)

## The Numbers

I explain the numbers here to simplify things:
- We have 4 authors (2 required + 2 chosen with a very different writing style as part of the extended section)
- For each author we have 25 books selected.
- For each book, Gemini has generated 5 themes
- For each theme, Gemini is generating 2 paragraphs

This works out to 2*5*25*2=500 paragraphs for the main set, and 2*5*25*2=500 paragraphs for the extended set.



## *'Diversity Modes'* and *'Settings'*

In the beginning, I was not using these, and Gemini was giving me answers which were too similar to each other. In some cases, the paragraphs generated were almost the same. [Here's an example of the old version.](#examples-of-very-similar-generated-paragraphs-by-gemini-in-the-old-version).

So, I added the diversity modes.  
A core goal of this project is to study writing style rather than factual content. To make that distinction meaningful, the generated text needs to vary along dimensions that humans naturally associate with style: tone, narrative perspective, pacing, etc.  

The DIVERSITY_MODES are a way of encouraging this variation. Each mode nudges the generator toward a different stylistic framing, such as dialogue-driven scenes, reflective inner monologues, analytical exposition, or emotionally charged narration. Importantly, these modes do not introduce new facts or themes; they only influence how an idea is expressed.  

This way, I can ensure that the generated paragraphs are different, and the classifier won't overfit to the data on the basis of the content being generated. And since it's not messing with the actual content of the theme, I think it's okay. Stylistically, this is because tone and theme itself our quite different concepts. When I was trying to reinforce that what I was doing was correct, I came across [this blog post](https://wordwool.com/tone-vs-theme/) which distinguishes the 2 quite nicely. While not for all 1000 paragraphs, I also manually cross-verified whether the model was generating text relevant to the theme, and in every case, it was.



## 2-pass system for generation

On the first pass, I make it generate 5 themes for the book and save it in [../topic-data](../topic-data/).  
On the second pass, I make it generate the paragraph as per the requirements, based on those themes. The concept of these diversity modes was inspired by

This is sort-of inspired from the thinking mode we see in many AI's. My old plan was to manually come up with themes, but since I've not read the vast majority of books, and going through Shmoop pages for 100 books was probably not the best idea, I decided to go with this.  

To prevent overfitting, I also added significantly more diversity modes and settings than required. For a given theme

I have manually cross-verified every single theme generated, and they do correlate to the novels chosen, as well as the specific paragraphs of those novels.  


## Prompting Strategy
**Pass 1:**
- Does not send the full book text. This is done because passing the book text each time will result in processing taking forever. Since each author and all of their works are very well known, I thought it was okay for Gemini to just work on the assumption.
- Explicitly instructed to avoid mentioning book title, character names, or author
- Ask for concise themes (3-8 words) to keep them simple
- Output format: numbered list for easy parsing
- `temperature=0.7` - Slightly more on the deterministic side. I want themes that accurately reflect the books, so I kept some determinism while allowing variation.

**Pass 2:**
- Specifies exact word count range (100-200) with retry logic to enforce it
- Includes "anti-AI" constraints: avoid overused phrases like "tapestry," "delve," "testament"
- Prohibits essay-like structures ("In conclusion," numbered points, headings)
- Randomly injects diversity mode (tone/narrative style) and setting (location/context)
- Emphasizes "neutral modern English" to avoid mimicking specific authors
- Explicitly asks for spontaneous, natural writing
- `temperature=1.0` - I wanted more diversity. Since we're generating multiple paragraphs per theme, high temperature prevents repetitive outputs and creates natural stylistic variation. The diversity modes further help with this.

### Technical Implementation
- **Retry Logic**: Up to 3 attempts per paragraph if word count is out of range
- **Output Cleaning**: Strips quotes, titles, extra newlines that Gemini sometimes adds
- **Rate Limiting**: 2-second sleep between API calls to avoid quota issues
- **Safety Settings**: Set to `BLOCK_ONLY_HIGH` to allow creative freedom while preventing harmful content
- **Filename Convention**: `bookname_themeID_paranum.txt` for easy tracking and reproducibility





## Examples of very similar generated paragraphs by Gemini in the old version
**PARAGRAPH 1:**  
Ingenious solutions to self-made problems reveal a peculiar blend of human creativity and irony: we often spend immense effort repairing complications that sprang from our own decisions. These moments are not merely mistakes redeemed, but laboratories of invention, where constraint sharpens insight. A poorly designed system forces its creator to invent clever workarounds; an impulsive shortcut demands an elaborate fix; an overconfident plan collapses into a puzzle that only ingenuity can solve. In such cases, the solution is frequently more elegant than the original idea, precisely because it must negotiate failure. There is a quiet brilliance in turning a self-inflicted obstacle into an opportunity to rethink assumptions, refine tools, or discover unexpected efficiencies. While it may seem wasteful to celebrate problems of our own making, these scenarios highlight an essential truth: progress is rarely linear. Innovation often emerges not from perfect foresight, but from the stubborn, imaginative refusal to be defeated by our own missteps.

**PARAGRAPH 2**  
Ingenious solutions to self-made problems reveal a peculiar blend of human creativity and stubbornness. We build systems that are too fast, too loud, too complex, or too convenient, then marvel at our cleverness when we invent ways to survive them. We create overflowing inboxes and answer them with filters, labels, and productivity methods that require their own tutorials. We design cities around cars, then celebrate the elegance of apps that help us escape traffic we engineered ourselves. Even on a personal level, we overcommit, overshare, and overoptimize, only to craft elaborate routines, tools, and philosophies to regain a sense of balance. There is something quietly heroic in this cycle: an optimism that believes every mess is solvable, preferably with a smarter trick than the one that caused it. At the same time, it exposes our reluctance to step back and ask whether the problem needed to exist at all. Our ingenuity shines brightest not in avoiding mistakes, but in decorating them with clever fixes.
