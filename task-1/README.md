# Task 1 - Mathematical Analysis of Human vs AI Text

This task explores how to mathematically distinguish between human-written and AI-generated text. I've analyzed lexical richness, syntactic complexity, punctuation patterns, readability, and information-theoretic signatures across three classes of text.

**IMPORTANT NOTE:** I have spoken in significant detail and provided sources for each claim I make in `markdown` boxes in [the Jupyter Notebook](task-1.ipynb).  
This README.md provides only a brief overview of my findings. For more details, please step by step read through the python notebook. 

## Dataset Classes

- **Class 1**: Human-written (Arthur Conan Doyle, P.G. Wodehouse, Mark Twain, William Shakespeare)
- **Class 2**: AI-generated (Gemini 3 Pro, temperature=1.0)
- **Class 3**: AI-mimicry (Gemini 3 Pro instructed to mimic human authors)

## Test Summary & Results

| Category | Test | Metric | Class 1 (Human) | Class 2 (AI) | Class 3 (AI-Mimicry) | Hypothesis Confirmed | Key Finding |
|----------|------|--------|-----------------|--------------|----------------------|---------------------|-------------|
| **I. Lexical Richness** | Type-Token Ratio (TTR) | Vocabulary diversity | Lower variance, mid-range | Higher, narrow band (0.6-0.8) | Higher, narrow band | Partially | AI has higher TTR but lower variance; humans show more dynamic range |
| | Hapax Legomena | Words appearing once | Lower | Moderately higher | Moderately higher | Yes | High temperature (1.0) leads to more rare words in AI |
| | Zipf's Law (α exponent) | Power-law distribution | α ≈ 2.7 (steeper) | α ≈ 2.5 (flatter) | α ≈ 2.5 (flatter) | Yes | AI has flatter distribution (heavier tail) due to temperature |
| | Zipf's Law (MAPE) | Fit quality | Higher error | Lower error | Lower error | N/A | AI follows Zipf more consistently |
| **II. Syntactic Complexity** | Dependency Tree Depth | Sentence nesting | Higher avg, wider range | Lower avg (2.56) | Highest avg (over-corrected) | Yes | Humans use more center-embedding; AI prefers right-branching |
| | POS: Adj/Noun Ratio | Descriptive density | Lower | **Higher** | Higher | Yes | AI over-describes compared to humans |
| | POS: Noun/Verb Ratio | Nominalization | Higher (2.32) | Lower (1.72) | Mid-range | Yes | Humans prefer nominalizations; AI prefers direct verbs |
| | POS: Adverb/Verb Ratio | Adverbial modification | Lower | **Higher** | Higher | Yes | AI over-modifies verbs with adverbs |
| **III. Punctuation** | Em-dashes | Stylistic interruption | Lowest | Mid | Highest | Yes | AI mimicry over-uses em-dashes |
| | Semicolons | Complex coordination | **Highest** | Lower | Lower | Yes | Humans use semicolons more for nuanced connections |
| | Colons | Explanatory structure | **Highest** | Lower | Lower | Yes | Humans introduce explanations more formally |
| | Exclamation Points | Emotional expression | **Highest** | Lower | Lower | Yes | Humans express emotion more freely |
| | Double Quotes | Dialogue/citation | **Highest** | Lower | Lower | Yes | Humans use dialogue/quotes more naturally |
| **IV. Readability** | Flesch-Kincaid Grade | Reading difficulty (mean) | 9th grade | 7th grade | 11th grade | Yes | AI writes simpler; mimicry over-corrects to harder |
| | Flesch-Kincaid (variance) | Consistency | **High** (σ ≈ 7) | Very low (σ ≈ 2) | Very low (σ ≈ 2) | Yes | AI maintains constant difficulty; humans modulate |
| **V. Information Theory** | Perplexity (GPT-2) | Predictability | Higher | Lower | Mid | Yes | AI-generated text is more predictable to language models |

## Statistical Significance

I used the Mann-Whitney U Test for all comparisons. 


## Methods & Tools

- **Lexical Analysis**: Custom TTR calculator, Zipf power-law fitting (MAPE optimization)
- **Syntactic Parsing**: SpaCy (`en_core_web_sm`) for dependency trees and POS tagging
- **Readability**: `textstat` library for Flesch-Kincaid calculations
- **Perplexity**: GPT-2 model via HuggingFace Transformers
- **Tokenization**: TikToken (`cl100k_base` encoding)
- **Statistics**: Mann-Whitney U test, Cohen's d effect sizes

## References

Academic papers cited:
- **Culda et al., 2024** - "TTR and Hapax in AI detection" - [Link](https://www.tandfonline.com/doi/full/10.1080/09540091.2025.2507183)
- **Tran et al., 2024** - "Lexical richness patterns in AI vs human text" - [Link](https://www.mdpi.com/2073-431X/13/12/328)
- **Mikhaylovskiy, 2025** - "Zipf's Law in LLMs" - [Link](https://aclanthology.org/2025.findings-emnlp.837.pdf)
- **Yang et al., 2026** - "Dependency tree analysis and syntactic complexity" - [Link](https://www.mdpi.com/2304-6775/14/1/1)
- **Kudryavtseva et al., 2025** - "Comparative statistical analysis of word frequencies" - [Link](https://www.researchgate.net/publication/394353951_Comparative_Statistical_Analysis_of_Word_Frequencies_in_Human-Written_and_AI-Generated_Texts)
- **Schephens et al., 2025** - "Hapax deficit mechanisms in AI text" - [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC12571048/)
- **POS Distribution Study** - "Noun-to-verb ratios in AI vs human writing" - [Link](https://ris.cdu.edu.au/ws/portalfiles/portal/121993038/computers-13-00328.pdf)
- **Flesch-Kincaid Analysis** - "AI readability in medical contexts" - [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC11905972/)
- **Fabio Chiusano** - "Perplexity explained with simple probabilities" - [Medium](https://medium.com/nlplanet/two-minutes-nlp-perplexity-explained-with-simple-probabilities-6cdc46884584)
- **Information Theory Blog** - "Chaos and predictability in language models" - [Link](https://kuiper2000.github.io/chaos_and_predictability/week9/week9)
- **Peeperkorn et al., 2024** - "Is Temperature the Creativity Parameter of Large Language Models" - [Link](https://arxiv.org/html/2405.00492v1)


All visualizations and statistical tests are included in the notebook with detailed markdown explanations.
