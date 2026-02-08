# It got a little better, then got worse

**Fluke** I think. Fitness scores got significantly better (went to 11.7) but then got worse again. It might've gotten worse because elitism was disabled. Let me run it again to check if fluke


# Results
*sorry for the formatting, idk what happened*

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
   ├─ log(P(Human))=-14.04408646 ├─ Semantic penalty=0.00000000 └─ Perplexity penalty=0.00000000 [2/10] Fitness=-13.89471531, P(Human)=0.00000097 ├─ log(P(Human))=-13.84578323 ├─ Semantic penalty=0.04893243 └─ Perplexity penalty=0.00000000 [3/10] Fitness=-14.57273674, P(Human)=0.00000051 ├─ log(P(Human))=-14.49621391 ├─ Semantic penalty=0.07652235 └─ Perplexity penalty=0.00000000 [4/10] Fitness=-13.66294193, P(Human)=0.00000174 ├─ log(P(Human))=-13.26440811 ├─ Semantic penalty=0.39853382 └─ Perplexity penalty=0.00000000 [5/10] Fitness=-14.48919964, P(Human)=0.00000061 ├─ log(P(Human))=-14.31114101 ├─ Semantic penalty=0.17805839 └─ Perplexity penalty=0.00000000 [6/10] Fitness=-14.68707561, P(Human)=0.00000045 ├─ log(P(Human))=-14.61386395 ├─ Semantic penalty=0.07321179 └─ Perplexity penalty=0.00000000 [7/10] Fitness=-14.52969837, P(Human)=0.00000063 ├─ log(P(Human))=-14.27635098 ├─ Semantic penalty=0.25334716 └─ Perplexity penalty=0.00000000 [8/10] Fitness=-14.40263939, P(Human)=0.00000060 ├─ log(P(Human))=-14.32630348 ├─ Semantic penalty=0.07633603 └─ Perplexity penalty=0.00000000 [9/10] Fitness=-13.84537125, P(Human)=0.00000106 ├─ log(P(Human))=-13.76018810 ├─ Semantic penalty=0.08518326 └─ Perplexity penalty=0.00000000 [10/10] Fitness=-13.59927559, P(Human)=0.00000155 ├─ log(P(Human))=-13.37889290 ├─ Semantic penalty=0.22038221 └─ Perplexity penalty=0.00000000 Logged to evolution_0.txt ✓ Initial best fitness: -13.59927559 GENERATION 1/100 [STEP 3] Selection... Selected top 3 parents Parent 1 (idx=10): Fitness=-13.59927559, P(Human)=0.00000155 └─ Components: log(P)=-13.378893, sem_pen=0.220382, ppl_pen=0.000000 Parent 2 (idx=4): Fitness=-13.66294193, P(Human)=0.00000174 └─ Components: log(P)=-13.264408, sem_pen=0.398534, ppl_pen=0.000000 Parent 3 (idx=9): Fitness=-13.84537125, P(Human)=0.00000106 └─ Components: log(P)=-13.760188, sem_pen=0.085183, ppl_pen=0.000000 [STEP 4] Crossover & Mutation... Elitism: DISABLED (debug mode - fitness signal needs to stabilize first) Generated offspring 1/10 Generated offspring 2/10 Generated offspring 3/10 Generated offspring 4/10 Generated offspring 5/10 Generated offspring 6/10 Generated offspring 7/10 Generated offspring 8/10 Generated offspring 9/10 Generated offspring 10/10 [STEP 5] Local search on top offspring... Local search on offspring 10... Fitness: -12.47657394 Local search on offspring 6... Fitness: -12.68679237 Local search on offspring 7... Fitness: -11.79275131 NEW BEST FITNESS: -11.79275131 Logged to evolution_1.txt Generation 1 summary (HIGH PRECISION): Best fitness: -11.79275131 Avg fitness: -13.24843025 Worst fitness: -14.06253338 Best P(Human): 0.00000811 GENERATION 2/100 [STEP 3] Selection... Selected top 3 parents Parent 1 (idx=7): Fitness=-11.79275131, P(Human)=0.00000811 └─ Components: log(P)=-11.722035, sem_pen=0.070716, ppl_pen=0.000000 Parent 2 (idx=10): Fitness=-12.47657394, P(Human)=0.00000458 └─ Components: log(P)=-12.293521, sem_pen=0.183053, ppl_pen=0.000000 Parent 3 (idx=6): Fitness=-12.68679237, P(Human)=0.00000426 └─ Components: log(P)=-12.367207, sem_pen=0.319586, ppl_pen=0.000000 [STEP 4] Crossover & Mutation... Elitism: DISABLED (debug mode - fitness signal needs to stabilize first) Generated offspring 1/10 Generated offspring 2/10 Generated offspring 3/10 Generated offspring 4/10