# My first attempt fine-tuning the model

This was my first time fine-tuning the model. I trained it on approximately 80% of the data of Arthur Conan Doyle.  
The main issues we faced were as follows:
1. **Overfitting:** The model started **(a)** using Sherlock Holmes and Dr. Watson as characters in it's paragraphs, but more importantly (and worse), **(b)** it would just directly take quoted text from Doyle's books as it's own for the paragraphs.
2. **Prompt Leakage + Instruction Non-compliance:** It would initially just flat out disobey anything I told it in the prompt. If I told it not to mention the topic, it would just copy-paste that part of the prompt etc. etc.

In my first attempt, I did not know that I needed to keep 3 sets for training, validation and testing respectively, and then do cross-fold validation.  
I only kept 2 sets, for training and testing, and these were slightly overlapping as well, which caused significant issues.  
  
Another issue I deem somewhat pertinent is the length of the output itself... It was not as long as it should be.


## Why I believe these issues arose


**1.**  
(a) **Holmes / Watson character injection:** The training data consisted of raw book text from Doyle, and a large portion of it contains recurring characters (Holmes/Watson).

Since the fine-tuning objective was essentially “predict the next tokens in Doyle text”, the model learned that Holmes/Watson are extremely high-probability tokens whenever the output resembles Doyle-style prose.

This effect becomes stronger when training is done on a single author corpus without strong constraint conditioning.

(b) **Verbatim copying / quoting the book**  
In several cases, the model directly reproduced long passages that exist in the training books.

Why this happened (from our data + training format):

The JSONL training format used was simply:

> {"text": "< chunk from the original novel >"}


This is effectively classic language model continuation training.

The chunks were long (often 150–350 words or more, previously even larger in earlier attempts), which increases the chance that the model memorizes patterns rather than generalizes style.

Training for even 1 epoch on a small single-author dataset can produce strong memorization, especially with LoRA where the fine-tune quickly reinforces dominant author-specific phrasing.

As a result, the model’s outputs sometimes resembled direct “Gutenberg continuation” instead of producing fresh text on a topic.



**2.**  
Prompt Leakage  
The second major issue was that the model frequently violated the output constraints. Instead of returning only the paragraph text, it would sometimes include:

- repeated parts of the prompt itself
- meta-instructions such as “If you return more than one paragraph…”
- formatting artifacts like “Theme: …”
- multi-paragraph or partial continuation outputs
  

Why this happened (from our generation + training mismatch):
- During training, the model never learned a structured mapping like:
instruction → answer,  
It only learned:
text → more text
- Since the training dataset contained no explicit “prompt/response” formatting, the model treated the prompt at inference time as just more text to continue, so it sometimes continued the prompt itself.
- Additionally, in generation we used sampling (temperature, top_p), so when the model is uncertain, it may start emitting high-frequency instruction-like patterns (especially if the prompt includes many repeated constraints).

This caused outputs where prompt fragments were included in the generated paragraph, which is undesirable for dataset creation since it pollutes the stylistic signal.


*Onto attempt 2 now...*