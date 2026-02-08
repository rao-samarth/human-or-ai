# Saliency-based Pruning

Off to a great start already in cell 10 lol.

```
Testing saliency-guided mutation:
  Original: Technology has become an integral part of modern life.
  Mutated:  This tech stuff has become a huge part of everyday life.
```

I tried it for a few initial runs, but then that had to stop because I made a silly mistake in directory structure handling, which was messing everything up...

is this good? yes, much better. 
**EXTREMELY SLOW THOUGH!!** Like, mind numbingly slow.  
It being this slow led me to learning about seeding, and specifically *gradient-guided seeding*

This is kind of where

## First Run

=== MEMETIC ALGORITHM FOR TEXT EVOLUTION (MATE) ===
  FITNESS IN LOG SPACE - Expect negative values!
  USING SALIENCY-GUIDED MUTATIONS


[STEP 1] Initializing population...
Generating initial population of 10...
  [1/10] Original text saved
  [2/10] Generated variation
  [3/10] Generated variation
  [4/10] Generated variation
  [5/10] Generated variation
  [6/10] Generated variation
  [7/10] Generated variation
  [8/10] Generated variation
  [9/10] Generated variation
  [10/10] Generated variation
Initial population generated: 10 individuals

[STEP 2] Evaluating initial population...
  [1/10] Fitness=-14.04408646, P(Human)=0.00000080
      ├─ log(P(Human))=-14.04408646
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [2/10] Fitness=-14.88104057, P(Human)=0.00000035
      ├─ log(P(Human))=-14.86540985
      ├─ Semantic penalty=0.01563096
      └─ Perplexity penalty=0.00000000
  [3/10] Fitness=-14.31157017, P(Human)=0.00000076
      ├─ log(P(Human))=-14.09623432
      ├─ Semantic penalty=0.21533620
      └─ Perplexity penalty=0.00000000
  [4/10] Fitness=-13.74419403, P(Human)=0.00000128
      ├─ log(P(Human))=-13.56752300
      ├─ Semantic penalty=0.17667115
      └─ Perplexity penalty=0.00000000
  [5/10] Fitness=-13.60987282, P(Human)=0.00000144
      ├─ log(P(Human))=-13.45273018
      ├─ Semantic penalty=0.15714240
      └─ Perplexity penalty=0.00000000
  [6/10] Fitness=-14.03962135, P(Human)=0.00000089
      ├─ log(P(Human))=-13.92714310
      ├─ Semantic penalty=0.11247873
      └─ Perplexity penalty=0.00000000
  [7/10] Fitness=-14.26372051, P(Human)=0.00000071
      ├─ log(P(Human))=-14.15926647
      ├─ Semantic penalty=0.10445392
      └─ Perplexity penalty=0.00000000
  [8/10] Fitness=-14.84622860, P(Human)=0.00000037
      ├─ log(P(Human))=-14.80095196
      ├─ Semantic penalty=0.04527688
      └─ Perplexity penalty=0.00000000
  [9/10] Fitness=-13.75708389, P(Human)=0.00000129
      ├─ log(P(Human))=-13.56244850
      ├─ Semantic penalty=0.19463515
      └─ Perplexity penalty=0.00000000
  [10/10] Fitness=-13.51350594, P(Human)=0.00000143
      ├─ log(P(Human))=-13.45988369
      ├─ Semantic penalty=0.05362201
      └─ Perplexity penalty=0.00000000
Logged to evolution_0.txt

✓ Initial best fitness: -13.51350594

GENERATION 1/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=10): Fitness=-13.51350594, P(Human)=0.00000143
        └─ Components: log(P)=-13.459884, sem_pen=0.053622, ppl_pen=0.000000
    Parent 2 (idx=5): Fitness=-13.60987282, P(Human)=0.00000144
        └─ Components: log(P)=-13.452730, sem_pen=0.157142, ppl_pen=0.000000
    Parent 3 (idx=4): Fitness=-13.74419403, P(Human)=0.00000128
        └─ Components: log(P)=-13.567523, sem_pen=0.176671, ppl_pen=0.000000

[STEP 4] Crossover & Saliency-Guided Mutation...
  Elitism: Keeping best parent
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring (saliency-guided)...
  Local search on offspring 8...
    Fitness: -12.03369141
  Local search on offspring 3...
    Fitness: -13.02702713
  Local search on offspring 7...
    Fitness: -11.96261501

NEW BEST FITNESS: -11.96261501
Logged to evolution_1.txt

  Generation 1 summary (HIGH PRECISION):
    Best fitness:  -11.96261501
    Avg fitness:   -13.06735706
    Worst fitness: -13.59150982
    Best P(Human): 0.00000815

GENERATION 2/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=7): Fitness=-11.96261501, P(Human)=0.00000815
        └─ Components: log(P)=-11.717543, sem_pen=0.245072, ppl_pen=0.000000
    Parent 2 (idx=8): Fitness=-12.03369141, P(Human)=0.00000684
        └─ Components: log(P)=-11.893105, sem_pen=0.140587, ppl_pen=0.000000
    Parent 3 (idx=3): Fitness=-13.02702713, P(Human)=0.00000267
        └─ Components: log(P)=-12.832879, sem_pen=0.194148, ppl_pen=0.000000

[STEP 4] Crossover & Saliency-Guided Mutation...
  Elitism: Keeping best parent
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring (saliency-guided)...
  Local search on offspring 3...
    Fitness: -11.39088440
  Local search on offspring 1...

