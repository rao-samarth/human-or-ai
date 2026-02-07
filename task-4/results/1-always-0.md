# The first failed attempt

The P(Human) was always 0, causing the algorithm not to evolve at all. This is quite problematic. It makes things meaningless if children are evolving from a parent who itself is 0% human! As such, I realise that while the algorithm may be okay, there are a few things I need to change, because rn the memetic algorithm has nothing to optimize!!! This makes local search / global search / whatever you want to call it, meaningless...  

# How I resolved this

After getting this, I decided to temporarily turn of elitism. I will put elitism back after a few consecutive rounds of seen improvement 

```MEMETIC ALGORITHM FOR TEXT EVOLUTION (MATE)

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
  [1/10] Fitness=0.0000, P(Human)=0.0000
  [2/10] Fitness=-0.2414, P(Human)=0.0000
  [3/10] Fitness=-0.1449, P(Human)=0.0000
  [4/10] Fitness=-0.0143, P(Human)=0.0000
  [5/10] Fitness=-0.1866, P(Human)=0.0000
  [6/10] Fitness=-0.1744, P(Human)=0.0000
  [7/10] Fitness=-0.1397, P(Human)=0.0000
  [8/10] Fitness=-0.1980, P(Human)=0.0000
  [9/10] Fitness=-0.0749, P(Human)=0.0000
  [10/10] Fitness=-0.1578, P(Human)=0.0000
Logged to evolution_0.txt

Initial best fitness: 0.0000
GENERATION 1/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=0.0000, P(Human)=0.0000
    Parent 2 (idx=4): Fitness=-0.0143, P(Human)=0.0000
    Parent 3 (idx=9): Fitness=-0.0749, P(Human)=0.0000

[STEP 4] Crossover & Mutation...
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

[STEP 5] Local search on top offspring...
  Local search on offspring 2...
    Fitness: 0.0000
  Local search on offspring 1...
    Fitness: 0.0000
  Local search on offspring 7...
    Fitness: 0.0000

 NEW BEST FITNESS: 0.0000
Logged to evolution_1.txt

  Generation 1 summary:
    Best fitness:  0.0000
    Avg fitness:   -0.0041
    Best P(Human): 0.0000
GENERATION 2/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=0.0000, P(Human)=0.0000
    Parent 2 (idx=7): Fitness=0.0000, P(Human)=0.0000
    Parent 3 (idx=2): Fitness=0.0000, P(Human)=0.0000

[STEP 4] Crossover & Mutation...
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

[STEP 5] Local search on top offspring...
  Local search on offspring 1...
    Fitness: 0.0000
  Local search on offspring 3...
    Fitness: 0.0000
  Local search on offspring 4...
    Fitness: 0.0000
Logged to evolution_2.txt

  Generation 2 summary:
    Best fitness:  0.0000
    Avg fitness:   -0.0104
    Best P(Human): 0.0000
GENERATION 3/10

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=0.0000, P(Human)=0.0000
    Parent 2 (idx=3): Fitness=0.0000, P(Human)=0.0000
    Parent 3 (idx=4): Fitness=0.0000, P(Human)=0.0000

[STEP 4] Crossover & Mutation...
  Elitism: Keeping best parent
  Generated offspring 2/10
```