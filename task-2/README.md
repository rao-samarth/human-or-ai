# Task 2 - The Multi-Tiered Detective

- In this section, we will build 3 detectors to separate AI generated text from human written text.  
- To be even more specific, each of our detectors will attempt to separate class-1 from class-2 and class-1 from class-3. We will also see if our detector can separate class-2 from class-3. Here, the classes refer to the dataset classes which can be seen in [../dataset/](../dataset/)

The 3 approaches are as follows.
1. *Tier A: The Statistician* - Here we aim to see if with mathematical backing from task-1, we can separate the AI generated text from humans. This can be found in [statistician.ipynb](statistician.ipynb). In the markdown blocks of this file, I have spoken in significantly more detail about XGBoost and Random forest and the results. In [xgboost_misclassified/](xgboost_misclassified/) you can see all the misclassified files. Cell 7 corresponds to this output.
2. *Tier B: The Semantisist* - Here we use [Stanford's GloVe](https://nlp.stanford.edu/projects/glove/). Here, a MLP tries to classify the text solely on the basis of vector embeddings. This is in a way a test to see if our dataset is separating texts on the basis of topics, or on the basis of authorship.
3. *Tier C: The Transformer*. This is a bit more complicated. We use DistilBERT, which is a transformer. Transformers use a method known as self-attention, which is a mechanism allowing the models to weigh the importance of different words with context-awareness. For example, in the clause *"The girl and her brother"*, the transformer will associate *her* with *The girl* and will not treat it independently. A traditional model would instead treat each word in the clause with equal importance.

