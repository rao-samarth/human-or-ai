# Gradient-Guided Seeding approach

if you're wondering why I lost the offspring in [6-saliency-based-pruning.md](6-saliency-based-pruning.md), it's because I did `cp mate.ipynb new-mate.ipynb`, change the cell which was seeding the population, but forgot to change the directory paths.

Gradient guided seeding is a mathematical seeding approach wherein we replace words with synonyms whose vector differences match the gradient towards class-1 human written text.

This is what I implemented here.  
And I was quite surprised, honestly, by what I saw. Immediately, the sample population is off with a bang. I looked at one of the members of the new initial population

```
The quiet hum of this place always felt like, I dunno, safety, a soft little bubble of routine where the biggest deal was just a zoning dispute or an unkempt lawn. You know, I thought I knew the man living in the yellow house across the street. He was the kind of person who returned borrowed tools early and bought Girl Scout cookies by the case, practically boring in his decency. That whole idea fell apart the afternoon I accidentally opened his mail, a simple mix-up by the postman. The letter wasn't a utility bill or a birthday card, but no, it was a heavily redacted government dossier with a photo of him looking twenty years younger and terrifyingly cold. And standing there on my own porch, holding the thing that felt like it weighed a ton, I realized his whole quiet demeanor wasn't who he really was. It was a cover, perfect and, like, impossible to see through, hiding a history that had no business existing between the library and the bakery.
```

`I dunno` is crazy. It seems to be doing it's thing, I hope.

I plan to have this as a contest between [mate.ipynb](../mate.ipynb) and [new-mate.ipynb](new-mate.ipynb) to see which one can do better.

## Does GGS even work?

Well, I'm not so sure how statistically significant the difference is. The only change is being made to the initial population, and this has a difference of <1.0 in terms of fitness. So it is better, but not significantly. 


## Output

=== MEMETIC ALGORITHM FOR TEXT EVOLUTION (MATE) ===
  FITNESS IN LOG SPACE - Expect negative values!
  USING SALIENCY-GUIDED MUTATIONS


[STEP 1] Initializing population...
Generating Gradient-Guided population of 10...
  [1/10] Original text saved as baseline
Seeding Population: 100%|██████████| 9/9 [07:37<00:00, 50.80s/it]
Initial population generated: 10 individuals
  Strategy: Each seed underwent saliency-guided mutation

[STEP 2] Evaluating initial population...
  [1/10] Fitness=-14.04408646, P(Human)=0.00000080
      ├─ log(P(Human))=-14.04408646
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [2/10] Fitness=-13.27129936, P(Human)=0.00000172
      ├─ log(P(Human))=-13.27129936
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [3/10] Fitness=-13.66024399, P(Human)=0.00000117
      ├─ log(P(Human))=-13.66024399
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [4/10] Fitness=-14.51544762, P(Human)=0.00000050
      ├─ log(P(Human))=-14.51544762
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [5/10] Fitness=-13.88479233, P(Human)=0.00000093
      ├─ log(P(Human))=-13.88479233
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [6/10] Fitness=-14.04408646, P(Human)=0.00000080
      ├─ log(P(Human))=-14.04408646
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [7/10] Fitness=-13.97469616, P(Human)=0.00000085
      ├─ log(P(Human))=-13.97469616
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [8/10] Fitness=-13.84334373, P(Human)=0.00000097
      ├─ log(P(Human))=-13.84334373
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [9/10] Fitness=-14.19365597, P(Human)=0.00000069
      ├─ log(P(Human))=-14.19365597
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [10/10] Fitness=-13.07429123, P(Human)=0.00000210
      ├─ log(P(Human))=-13.07429123
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
Logged to evolution_0.txt

Initial best fitness: -13.07429123

GENERATION 1/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=10): Fitness=-13.07429123, P(Human)=0.00000210
        └─ Components: log(P)=-13.074291, sem_pen=0.000000, ppl_pen=0.000000
    Parent 2 (idx=2): Fitness=-13.27129936, P(Human)=0.00000172
        └─ Components: log(P)=-13.271299, sem_pen=0.000000, ppl_pen=0.000000
    Parent 3 (idx=3): Fitness=-13.66024399, P(Human)=0.00000117
        └─ Components: log(P)=-13.660244, sem_pen=0.000000, ppl_pen=0.000000

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
  Local search on offspring 10...
    Fitness: -10.74163532
  Local search on offspring 6...
    Fitness: -8.97389793
  Local search on offspring 7...
    Fitness: -11.86103058

NEW BEST FITNESS: -8.97389793
Logged to evolution_1.txt

  Generation 1 summary (HIGH PRECISION):
    Best fitness:  -8.97389793
    Avg fitness:   -12.70887089
    Worst fitness: -14.12473392
    Best P(Human): 0.00012667

GENERATION 2/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=6): Fitness=-8.97389793, P(Human)=0.00012667
        └─ Components: log(P)=-8.973898, sem_pen=0.000000, ppl_pen=0.000000
    Parent 2 (idx=10): Fitness=-10.74163532, P(Human)=0.00002163
        └─ Components: log(P)=-10.741635, sem_pen=0.000000, ppl_pen=0.000000
    Parent 3 (idx=7): Fitness=-11.86103058, P(Human)=0.00000706
        └─ Components: log(P)=-11.861031, sem_pen=0.000000, ppl_pen=0.000000

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
  Local search on offspring 10...
    Fitness: -6.43854904
  Local search on offspring 1...
    Fitness: -6.74655819
  Local search on offspring 9...
    Fitness: -6.58910942

NEW BEST FITNESS: -6.43854904
Logged to evolution_2.txt

  Generation 2 summary (HIGH PRECISION):
    Best fitness:  -6.43854904
    Avg fitness:   -10.44644356
    Worst fitness: -13.00171375
    Best P(Human): 0.00165250

GENERATION 3/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=10): Fitness=-6.43854904, P(Human)=0.00165250
        └─ Components: log(P)=-6.405464, sem_pen=0.033085, ppl_pen=0.000000
    Parent 2 (idx=9): Fitness=-6.58910942, P(Human)=0.00154958
        └─ Components: log(P)=-6.469772, sem_pen=0.119337, ppl_pen=0.000000
    Parent 3 (idx=1): Fitness=-6.74655819, P(Human)=0.00140138
        └─ Components: log(P)=-6.570301, sem_pen=0.176257, ppl_pen=0.000000

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
    Fitness: -5.82442236
  Local search on offspring 1...
    Fitness: -4.53151226
  Local search on offspring 9...
    Fitness: -6.17809391

NEW BEST FITNESS: -4.53151226
Logged to evolution_3.txt

  Generation 3 summary (HIGH PRECISION):
    Best fitness:  -4.53151226
    Avg fitness:   -8.25220680
    Worst fitness: -10.37861729
    Best P(Human): 0.02943760

GENERATION 4/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-4.53151226, P(Human)=0.02943760
        └─ Components: log(P)=-3.525483, sem_pen=1.006030, ppl_pen=0.000000
    Parent 2 (idx=3): Fitness=-5.82442236, P(Human)=0.00335406
        └─ Components: log(P)=-5.697584, sem_pen=0.126838, ppl_pen=0.000000
    Parent 3 (idx=9): Fitness=-6.17809391, P(Human)=0.00252833
        └─ Components: log(P)=-5.980196, sem_pen=0.197897, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -4.22970152
  Local search on offspring 6...
    Fitness: -2.12837553
  Local search on offspring 2...
    Fitness: -5.65202570

NEW BEST FITNESS: -2.12837553
Logged to evolution_4.txt

  Generation 4 summary (HIGH PRECISION):
    Best fitness:  -2.12837553
    Avg fitness:   -7.71936655
    Worst fitness: -11.81329060
    Best P(Human): 0.13685940

GENERATION 5/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=6): Fitness=-2.12837553, P(Human)=0.13685940
        └─ Components: log(P)=-1.988801, sem_pen=0.139575, ppl_pen=0.000000
    Parent 2 (idx=1): Fitness=-4.22970152, P(Human)=0.04876117
        └─ Components: log(P)=-3.020821, sem_pen=1.208881, ppl_pen=0.000000
    Parent 3 (idx=2): Fitness=-5.65202570, P(Human)=0.00397752
        └─ Components: log(P)=-5.527096, sem_pen=0.124929, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -2.12837553
  Local search on offspring 8...
    Fitness: -3.45915413
  Local search on offspring 9...
    Fitness: -2.51342773
Logged to evolution_5.txt

  Generation 5 summary (HIGH PRECISION):
    Best fitness:  -2.12837553
    Avg fitness:   -5.05612135
    Worst fitness: -7.10705519
    Best P(Human): 0.13685940

GENERATION 6/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-2.12837553, P(Human)=0.13685940
        └─ Components: log(P)=-1.988801, sem_pen=0.139575, ppl_pen=0.000000
    Parent 2 (idx=9): Fitness=-2.51342773, P(Human)=0.09455481
        └─ Components: log(P)=-2.358576, sem_pen=0.154852, ppl_pen=0.000000
    Parent 3 (idx=8): Fitness=-3.45915413, P(Human)=0.03784572
        └─ Components: log(P)=-3.274237, sem_pen=0.184917, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -2.07542801
  Local search on offspring 10...
    Fitness: -3.22722769
  Local search on offspring 4...
    Fitness: -3.61177802

NEW BEST FITNESS: -2.07542801
Logged to evolution_6.txt

  Generation 6 summary (HIGH PRECISION):
    Best fitness:  -2.07542801
    Avg fitness:   -4.44918346
    Worst fitness: -5.79515934
    Best P(Human): 0.15181303

GENERATION 7/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-2.07542801, P(Human)=0.15181303
        └─ Components: log(P)=-1.885106, sem_pen=0.190322, ppl_pen=0.000000
    Parent 2 (idx=10): Fitness=-3.22722769, P(Human)=0.04858294
        └─ Components: log(P)=-3.024483, sem_pen=0.202745, ppl_pen=0.000000
    Parent 3 (idx=4): Fitness=-3.61177802, P(Human)=0.03105698
        └─ Components: log(P)=-3.471932, sem_pen=0.139846, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -2.00123501
  Local search on offspring 7...
    Fitness: -2.82642961
  Local search on offspring 10...
    Fitness: -4.15914106

NEW BEST FITNESS: -2.00123501
Logged to evolution_7.txt

  Generation 7 summary (HIGH PRECISION):
    Best fitness:  -2.00123501
    Avg fitness:   -4.93176794
    Worst fitness: -6.39031506
    Best P(Human): 0.15519327

GENERATION 8/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-2.00123501, P(Human)=0.15519327
        └─ Components: log(P)=-1.863084, sem_pen=0.138151, ppl_pen=0.000000
    Parent 2 (idx=7): Fitness=-2.82642961, P(Human)=0.06556139
        └─ Components: log(P)=-2.724768, sem_pen=0.101661, ppl_pen=0.000000
    Parent 3 (idx=10): Fitness=-4.15914106, P(Human)=0.01802596
        └─ Components: log(P)=-4.015942, sem_pen=0.143199, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -1.24174976
  Local search on offspring 5...
    Fitness: -3.62963057
  Local search on offspring 4...
    Fitness: -2.13194942

NEW BEST FITNESS: -1.24174976
Logged to evolution_8.txt

  Generation 8 summary (HIGH PRECISION):
    Best fitness:  -1.24174976
    Avg fitness:   -5.56673384
    Worst fitness: -9.06436825
    Best P(Human): 0.33538195

GENERATION 9/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-1.24174976, P(Human)=0.33538195
        └─ Components: log(P)=-1.092485, sem_pen=0.149265, ppl_pen=0.000000
    Parent 2 (idx=4): Fitness=-2.13194942, P(Human)=0.15262690
        └─ Components: log(P)=-1.879759, sem_pen=0.252190, ppl_pen=0.000000
    Parent 3 (idx=5): Fitness=-3.62963057, P(Human)=0.03178654
        └─ Components: log(P)=-3.448712, sem_pen=0.180918, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -1.24174976
  Local search on offspring 9...
    Fitness: -2.86720657
  Local search on offspring 6...
    Fitness: -2.75259519
Logged to evolution_9.txt

  Generation 9 summary (HIGH PRECISION):
    Best fitness:  -1.24174976
    Avg fitness:   -4.57371712
    Worst fitness: -6.68650484
    Best P(Human): 0.33538195

GENERATION 10/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-1.24174976, P(Human)=0.33538195
        └─ Components: log(P)=-1.092485, sem_pen=0.149265, ppl_pen=0.000000
    Parent 2 (idx=6): Fitness=-2.75259519, P(Human)=0.08310574
        └─ Components: log(P)=-2.487641, sem_pen=0.264954, ppl_pen=0.000000
    Parent 3 (idx=9): Fitness=-2.86720657, P(Human)=0.07242440
        └─ Components: log(P)=-2.625212, sem_pen=0.241995, ppl_pen=0.000000

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
  Local search on offspring 1...
  Mutation failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
    Fitness: -1.24174976
  Local search on offspring 8...
    Fitness: -3.54134059
  Local search on offspring 10...
    Fitness: -4.64783001
Logged to evolution_10.txt

  Generation 10 summary (HIGH PRECISION):
    Best fitness:  -1.24174976
    Avg fitness:   -5.73357964
    Worst fitness: -8.73367310
    Best P(Human): 0.33538195

============================================================
EVOLUTION COMPLETE
============================================================

Best fitness achieved: -1.24174976
Best individual:
  P(Human): 0.33538195
  P(AI): 0.66416436
  P(AI-mimicry): 0.00045371
  Predicted: Class 2 (conf=0.6642)

Text:
you know how there was always this sort of a quiet feel to it in our little neighborhood here and it was just so safe i don ' t know, the quiet hum of this place we called home like a warm blanket of sameness, you know what i mean i really did think i did and i really did i thought i knew the guy living in the yellow house across the street and i mean, he was the kind of guy who returned borrowed stuff early and bought those girl scout cookies by the whole big old case almost too nice in his decency, you know what i mean right and and then it all came crashing down the afternoon i accidentally opened his mail after a little mix up by the postman and you know it so and the letter wasn ' t a power bill or a birthday card or anything like that not even close man like oh no no way, no, no way, this thing was some kind of like red - acted government file with a picture of him looking twenty years younger and scary as hell and it just gave me the creeps man i was just standing right there on my own porch and this dang letter felt like it weighed a ton of bricks and it just hit me that that his whole nice guy act wasn ' t just a personality thing at all no you know it was a cover - up, just perfect and impenetrable, hiding some whole other life that had no business existing between the library and the coffee shop here like what was going on here in a place like this things like that don ' t happen

Best individual saved to best_individual.txt