# Task 2 - The Multi-Tiered Detective

In this section, we built 3 different detectors to separate AI-generated text from human-written text. Each detector attempts to classify between class-1 (human-written), class-2 (AI-written), and class-3 (AI-mimicry). The classes refer to the dataset folders in [../dataset/](../dataset/).

The 3 approaches are:

## 1. Tier A: The Statistician

Using the mathematical features we identified in Task 1, we trained two ensemble models: XGBoost and Random Forest. The detailed implementation is in [statistician.ipynb](statistician.ipynb).

### Results

**XGBoost Performance:**
- Class 1 vs Class 2: **88.98% accuracy**
- Class 1 vs Class 3: **93.00% accuracy**
- Class 2 vs Class 3: **87.74% accuracy**
- Multi-class (all 3 classes): **82.29% accuracy**

**Random Forest Performance:**
- Class 1 vs Class 2: **87.00% accuracy**
- Class 1 vs Class 3: **93.00% accuracy**  
- Class 2 vs Class 3: **85.32% accuracy**
- Multi-class (all 3 classes): **81.91% accuracy**

### Key Findings

Both models performed remarkably well, but they revealed something fascinating: **em-dash frequency** was by far the most important feature for XGBoost (importance score >0.28), while it only scored 0.11 for Random Forest. Why?

- **XGBoost** is greedy by nature. Once it discovered that em-dashes were a high-signal feature (remember from Task 1: AI-mimicry massively overuses em-dashes), it exploited this finding aggressively.
- **Random Forest** builds trees in parallel using random subsets of features. In many trees, em-dashes weren't even available as a choice, forcing the model to find other reliable predictors like hapax ratio.

This difference in feature importance rankings between the two models actually strengthens our confidence—both approaches successfully identify AI text, just through slightly different lenses.

Meanwhile, TTR (Type-Token Ratio) scored essentially zero in both models. This makes sense: our Task 1 analysis showed that while AI had slightly higher TTR, the variance was low and distributions overlapped significantly, making it a poor discriminator.

The misclassified examples from both models are saved in [xgboost_misclassified/](xgboost_misclassified/) and [randomforest_misclassified/](randomforest_misclassified/), organized by misclassification type.

## 2. Tier B: The Semanticist

Here we'll use [Stanford's GloVe](https://nlp.stanford.edu/projects/glove/) embeddings with a Multi-Layer Perceptron (MLP). The MLP will classify text based purely on semantic vector embeddings. This is a test to see if our dataset separates texts based on topics or on actual authorship patterns.

## 3. Tier C: The Transformer

This uses DistilBERT, a lighter transformer model. Transformers use self-attention—a mechanism that lets models understand which words matter most in context. For example, in the phrase *"The girl and her brother"*, the transformer associates *her* with *The girl* rather than treating each word independently. This context-awareness could help it pick up on the subtle stylistic patterns we identified in Task 1.

