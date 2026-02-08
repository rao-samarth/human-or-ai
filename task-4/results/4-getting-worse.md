# Okay, it's getting worse

As you can see from the fitness scores below, initially the fitness scores we getting better (13 -> 12), and then it just got worse again. Significantly.  

Now I implement saliency-based pruning.

I switched to the log space in [2-elitism-disabled.md](2-elitism-disabled.md) where it showed that the algorithm works and and there is *some* gradient...

# 8 generations

=== MEMETIC ALGORITHM FOR TEXT EVOLUTION (MATE) ===
  FITNESS IN LOG SPACE - Expect negative values!
  ELITISM DISABLED - Will re-enable after signal stabilizes


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
  [2/10] Fitness=-14.30654144, P(Human)=0.00000064
      ├─ log(P(Human))=-14.25535488
      ├─ Semantic penalty=0.05118608
      └─ Perplexity penalty=0.00000000
  [3/10] Fitness=-14.00019073, P(Human)=0.00000087
      ├─ log(P(Human))=-13.95741844
      ├─ Semantic penalty=0.04277253
      └─ Perplexity penalty=0.00000000
  [4/10] Fitness=-13.81855106, P(Human)=0.00000112
      ├─ log(P(Human))=-13.69807243
      ├─ Semantic penalty=0.12047863
      └─ Perplexity penalty=0.00000000
  [5/10] Fitness=-14.65347576, P(Human)=0.00000048
      ├─ log(P(Human))=-14.54939079
      ├─ Semantic penalty=0.10408473
      └─ Perplexity penalty=0.00000000
  [6/10] Fitness=-14.57894897, P(Human)=0.00000055
      ├─ log(P(Human))=-14.41973400
      ├─ Semantic penalty=0.15921497
      └─ Perplexity penalty=0.00000000
  [7/10] Fitness=-14.29483414, P(Human)=0.00000068
      ├─ log(P(Human))=-14.20338535
      ├─ Semantic penalty=0.09144855
      └─ Perplexity penalty=0.00000000
  [8/10] Fitness=-13.78190231, P(Human)=0.00000122
      ├─ log(P(Human))=-13.61867619
      ├─ Semantic penalty=0.16322565
      └─ Perplexity penalty=0.00000000
  [9/10] Fitness=-14.66086578, P(Human)=0.00000055
      ├─ log(P(Human))=-14.40595913
      ├─ Semantic penalty=0.25490642
      └─ Perplexity penalty=0.00000000
  [10/10] Fitness=-14.44549274, P(Human)=0.00000057
      ├─ log(P(Human))=-14.37416935
      ├─ Semantic penalty=0.07132339
      └─ Perplexity penalty=0.00000000
Logged to evolution_0.txt

✓ Initial best fitness: -13.78190231

GENERATION 1/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=8): Fitness=-13.78190231, P(Human)=0.00000122
        └─ Components: log(P)=-13.618676, sem_pen=0.163226, ppl_pen=0.000000
    Parent 2 (idx=4): Fitness=-13.81855106, P(Human)=0.00000112
        └─ Components: log(P)=-13.698072, sem_pen=0.120479, ppl_pen=0.000000
    Parent 3 (idx=3): Fitness=-14.00019073, P(Human)=0.00000087
        └─ Components: log(P)=-13.957418, sem_pen=0.042773, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 2...
    Fitness: -12.72917271
  Local search on offspring 8...
    Fitness: -13.14519215
  Local search on offspring 7...
    Fitness: -12.33481026

NEW BEST FITNESS: -12.33481026
Logged to evolution_1.txt

  Generation 1 summary (HIGH PRECISION):
    Best fitness:  -12.33481026
    Avg fitness:   -13.42346478
    Worst fitness: -14.81217670
    Best P(Human): 0.00000510

GENERATION 2/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=7): Fitness=-12.33481026, P(Human)=0.00000510
        └─ Components: log(P)=-12.186871, sem_pen=0.147940, ppl_pen=0.000000
    Parent 2 (idx=2): Fitness=-12.72917271, P(Human)=0.00000334
        └─ Components: log(P)=-12.610387, sem_pen=0.118786, ppl_pen=0.000000
    Parent 3 (idx=8): Fitness=-13.14519215, P(Human)=0.00000233
        └─ Components: log(P)=-12.971251, sem_pen=0.173941, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 7...
    Fitness: -13.06677341
  Local search on offspring 4...
    Fitness: -13.25770378
  Local search on offspring 10...
    Fitness: -13.26307487
Logged to evolution_2.txt

  Generation 2 summary (HIGH PRECISION):
    Best fitness:  -13.06677341
    Avg fitness:   -13.73568249
    Worst fitness: -14.91670322
    Best P(Human): 0.00000234

GENERATION 3/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=7): Fitness=-13.06677341, P(Human)=0.00000234
        └─ Components: log(P)=-12.967143, sem_pen=0.099631, ppl_pen=0.000000
    Parent 2 (idx=4): Fitness=-13.25770378, P(Human)=0.00000202
        └─ Components: log(P)=-13.114534, sem_pen=0.143169, ppl_pen=0.000000
    Parent 3 (idx=10): Fitness=-13.26307487, P(Human)=0.00000206
        └─ Components: log(P)=-13.090582, sem_pen=0.172493, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 3...
    Fitness: -13.06873322
  Local search on offspring 4...
    Fitness: -13.20602798
  Local search on offspring 7...
    Fitness: -13.19910049
Logged to evolution_3.txt

  Generation 3 summary (HIGH PRECISION):
    Best fitness:  -13.06873322
    Avg fitness:   -13.46589088
    Worst fitness: -14.23400497
    Best P(Human): 0.00000252

GENERATION 4/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=3): Fitness=-13.06873322, P(Human)=0.00000252
        └─ Components: log(P)=-12.890469, sem_pen=0.178264, ppl_pen=0.000000
    Parent 2 (idx=7): Fitness=-13.19910049, P(Human)=0.00000209
        └─ Components: log(P)=-13.076697, sem_pen=0.122403, ppl_pen=0.000000
    Parent 3 (idx=4): Fitness=-13.20602798, P(Human)=0.00000218
        └─ Components: log(P)=-13.035007, sem_pen=0.171021, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 8...
    Fitness: -13.26555443
  Local search on offspring 4...
    Fitness: -13.27366161
  Local search on offspring 2...
    Fitness: -13.13725853
Logged to evolution_4.txt

  Generation 4 summary (HIGH PRECISION):
    Best fitness:  -13.13725853
    Avg fitness:   -13.47861481
    Worst fitness: -14.30889511
    Best P(Human): 0.00000199

GENERATION 5/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=2): Fitness=-13.13725853, P(Human)=0.00000199
        └─ Components: log(P)=-13.124844, sem_pen=0.012415, ppl_pen=0.000000
    Parent 2 (idx=8): Fitness=-13.26555443, P(Human)=0.00000184
        └─ Components: log(P)=-13.208187, sem_pen=0.057368, ppl_pen=0.000000
    Parent 3 (idx=4): Fitness=-13.27366161, P(Human)=0.00000205
        └─ Components: log(P)=-13.097019, sem_pen=0.176642, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 3...
    Fitness: -13.50384235
  Local search on offspring 7...
    Fitness: -13.60344982
  Local search on offspring 6...
    Fitness: -13.67208385
Logged to evolution_5.txt

  Generation 5 summary (HIGH PRECISION):
    Best fitness:  -13.50384235
    Avg fitness:   -13.87422371
    Worst fitness: -14.31378269
    Best P(Human): 0.00000164

GENERATION 6/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=3): Fitness=-13.50384235, P(Human)=0.00000164
        └─ Components: log(P)=-13.322931, sem_pen=0.180911, ppl_pen=0.000000
    Parent 2 (idx=7): Fitness=-13.60344982, P(Human)=0.00000139
        └─ Components: log(P)=-13.484913, sem_pen=0.118537, ppl_pen=0.000000
    Parent 3 (idx=6): Fitness=-13.67208385, P(Human)=0.00000136
        └─ Components: log(P)=-13.511572, sem_pen=0.160512, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 2...
    Fitness: -13.47028732
  Local search on offspring 3...
    Fitness: -13.60148048
  Local search on offspring 5...
    Fitness: -13.61182785
Logged to evolution_6.txt

  Generation 6 summary (HIGH PRECISION):
    Best fitness:  -13.47028732
    Avg fitness:   -13.83814430
    Worst fitness: -14.37917900
    Best P(Human): 0.00000161

GENERATION 7/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=2): Fitness=-13.47028732, P(Human)=0.00000161
        └─ Components: log(P)=-13.336966, sem_pen=0.133322, ppl_pen=0.000000
    Parent 2 (idx=3): Fitness=-13.60148048, P(Human)=0.00000140
        └─ Components: log(P)=-13.481826, sem_pen=0.119655, ppl_pen=0.000000
    Parent 3 (idx=5): Fitness=-13.61182785, P(Human)=0.00000137
        └─ Components: log(P)=-13.499804, sem_pen=0.112024, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10
  Generated offspring 3/10
  Generated offspring 4/10
  Generated offspring 5/10
  Generated offspring 6/10
  Generated offspring 7/10
  Generated offspring 8/10
  Generated offspring 9/10
  Generated offspring 10/10

[STEP 5] Local search on top offspring...
  Local search on offspring 7...
    Fitness: -13.21597385
  Local search on offspring 2...
    Fitness: -13.37443542
  Local search on offspring 10...
    Fitness: -13.40669632
Logged to evolution_7.txt

  Generation 7 summary (HIGH PRECISION):
    Best fitness:  -13.21597385
    Avg fitness:   -13.50371742
    Worst fitness: -13.63297272
    Best P(Human): 0.00000199

GENERATION 8/100

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=7): Fitness=-13.21597385, P(Human)=0.00000199
        └─ Components: log(P)=-13.125185, sem_pen=0.090789, ppl_pen=0.000000
    Parent 2 (idx=2): Fitness=-13.37443542, P(Human)=0.00000185
        └─ Components: log(P)=-13.200937, sem_pen=0.173499, ppl_pen=0.000000
    Parent 3 (idx=10): Fitness=-13.40669632, P(Human)=0.00000179
        └─ Components: log(P)=-13.233405, sem_pen=0.173291, ppl_pen=0.000000

[STEP 4] Crossover & Mutation...
  Elitism: DISABLED (debug mode - fitness signal needs to stabilize first)
  Generated offspring 1/10
  Generated offspring 2/10