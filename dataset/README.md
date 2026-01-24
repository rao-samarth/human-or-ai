# The Dataset

> You will build a dataset where the primary variable is authorship, not topic.

I treated this instruction as the core constraint of the assignment. Since the end goal is to distinguish **human-written** text from **AI-generated** text, the dataset must minimize “shortcuts” where a classifier can succeed simply by learning **topic differences**. Instead, we want the signal to come primarily from **style** (lexical choices, sentence structure, punctuation habits, rhythm, etc.).

To achieve this, I designed the dataset so that:
- **Human text spans multiple authors** with highly distinct writing styles.
- **AI-generated text is constrained to a shared pool of topics**, so topic does not become a proxy for author/source.
- The dataset supports both the assignment baseline and additional robustness experiments.


As per the assignment instructions:
- **Class 1:** Human Written Text. This can be found in [class1-human-written/](class1-human-written/)
- **Class 2:** AI Generated Text. This can be found in [class2-ai-written/](class2-ai-written)
- **Class 3:** AI Mimicry. The AI is trained on the writing style of the author, it then generates essays on the topics as though written by the author. It exists as a harder class to the data, since the AI is purposely trying to mimic a human author. The question it's trying to answer is like *"Does style prompting actually make AI harder to detect"*


Further details regarding **Class 1** can be found in [class1-human-written/README.md](class1-human-written/README.md).

### Dataset Split for Fine-tuning and Testing

Within Class 1, each author's books are split 80/20:
- **80%** in `<author-surname>-for-finetuning/` subdirectories (for model training) which will be used for Class-4
- **20%** kept in main directories (for held-out testing/validation)

This allows fine-tuning experiments (especially for Class 3 AI mimicry) while maintaining unseen test data. The split was randomized with a fixed seed for reproducibility.


## Topic List used for Class 2 and Class 3

### 1. Why we use 20 shared topics (and not 5–10 topics per book)

We use **one common set of 20 topics** for the entire dataset (across all authors and books).

I specifically chose this for the dataset generation, rather than choosing 5-10 topics per book (as mentioned in the document).  
This was done since if we choose 5-10 topics per book, then the dataset will contain a lot of very book specific topics. Many of these would appear only in one book or on author's work. This would make the distribution uneven and may result in the model getting confused between topic being written about and the authorship itself.

Using [20 shared topics](topic-list.csv) has the following benefits:

- It keeps the topics consistent across authors and books.
- It reduces topic-based bias (topic does not reveal the author or source).
- It makes the human vs AI comparison fair, because both human and AI texts cover the same ideas.
- It makes Class 2 and Class 3 generation simpler and easier to balance across topics.
  


I made this decision after reading an interesting paper, regarding separation of writing style from topic itself.  
The paper, entitled *Separating Style from Substance: Enhancing Cross-Genre Authorship Attribution through Data Selection and Presentation*, and they quote *"[We] select training documents for the same author to be topically dissimilar… [to] force it to incorporate information more robustly indicative of style no matter the topic."* They speak about how they choose topics which span across many works of a single author, so that they can properly separate the writing style of the author him(/her)self, rather than the topics at hand.  



### 2. Reasoning behind the choice of the specific [20 topics](topic-list.csv)

The 20 topics were chosen to be:

- Broad and abstract (not tied to one specific story or setting)
- Common across many works of many of the authors.
- Different enough to avoid repetitive AI outputs

Examples of the kinds of topics included are ambition, deception, love vs duty, justice, guilt, power, and social hierarchy. These themes are general enough to appear across different time periods and writing styles, but still varied enough to produce many different paragraphs.

I am providing exaples of the authors speaking on the same topics in [examples-for-topic-list.txt](examples-for-topic-list.txt).