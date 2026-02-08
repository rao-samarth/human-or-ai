# Human-or-AI

This is a system to detect and analyze linguistic differences between human-written text and large language model (LLM) generated text, including attempts to evolve text to evade detection.

It was done as part of the recruitment task to Precog@IIIT-H. The task document is given in [task-document.pdf](task-document.pdf)

The task is split into 5 parts: 

0. [The Library of Babel](dataset/) - Dataset Creation
1. [The Fingerprint](task-1/) - Proof of Mathematical Distinctness between the classes in the dataset
2. [The Multi-Tiered Detective](task-2/) - Building 3 models
3. [The Smoking Gun](task-3/) - A Saliency Analysis
4. [The Turing Test](task-4/) - Jailbreaking / Creating an Imposter - 

I have completed **all 5 tasks**.  

More details about my implementation of each task, the decisions I made and why I made them, can be found by clicking the links above, to the specific task directories. For each task, I have explained my approach and reasoning significantly in the `README.md` files, as well as further analysis and implementation decisions, in the markdown blocks of all Python notebooks.

**My main contribution** is in task-4, wherein I present what I call **MATE**. MATE (Memetic Algorithm for Text Evolution) is a framework that evolves AI-generated text to bypass detection classifiers while preserving original meaning . It enhances standard genetic algorithms by integrating saliency-guided mutation to surgically target "AI-like" tokens, local search for fine-grained refinement, and Lagrangian relaxation to dynamically balance stealth with semantic constraints.