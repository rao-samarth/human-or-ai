# The Dataset

> You will build a dataset where the primary variable is authorship, not topic.

I treated this instruction as the core constraint of the assignment. Since the end goal is to distinguish **human-written** text from **AI-generated** text, the dataset must minimize “shortcuts” where a classifier can succeed simply by learning **topic differences**. Instead, we want the signal to come primarily from **style** (lexical choices, sentence structure, punctuation habits, rhythm, etc.).

To achieve this, I designed the dataset so that:
- **Human text spans multiple authors** with highly distinct writing styles.
- **AI-generated text is constrained to a shared pool of topics**, so topic does not become a proxy for author/source.
- The dataset supports both the assignment baseline and additional robustness experiments.


As per the assignment instructions:
**Class 1:** Human Written Text. This can be found in [class1-human-written/](class1-human-written/)
**Class 2:** AI Generated Text. This can be found in [class2-ai-written/](class2-ai-written)
**Class 3:** AI Mimicry. The AI is trained on the writing style of the author, it then generates essays on the topics as though written by the author. It exists as a harder class to the data, since the AI is purposely trying to mimic a human author. The question it's trying to answer is like *"Does style prompting actually make AI harder to detect"*


Further details regarding **Class 1** can be found in [class1-human-written/README.md](class1-human-written/README.md).


## Topic List used for Class 2 and Class 3