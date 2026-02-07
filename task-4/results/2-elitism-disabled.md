# Another failed attempt

After running [1](1-always-0.md), I switched off elitism. In this output, you are able to see the marked improvement. If I may ask you to specifically look at either fitness or `log(P(human))`, you will see that it is improving.

While the improvements might look like nothing to the naked eye, mathematically these are pretty good. They show that in each generation, the text is about 30% more likely to classify as human than the previous section.

Slight problem though still. It's now going towards the realm of AI-mimicry instead.

**My Plan:** I will now set it such -
1. I will re-enable elitism when the best fitness has improved consistently for ~3 consecutive generations and the improvement is coming from different individuals, not the same one by chance.
2. I am going to change the model to remove AI-mimicry altogether. Let it be only AI-generated and human-generated text, and we'll see based on that.

A critic might argue that it will go from ai-mimicry into the realm of human written text... Plausible. I'm not taking that risk though.


## Cell Output

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
✓ Initial population generated: 10 individuals

[STEP 2] Evaluating initial population...
  [1/10] Fitness=-14.04408646, P(Human)=0.00000080
      ├─ log(P(Human))=-14.04408646
      ├─ Semantic penalty=0.00000000
      └─ Perplexity penalty=0.00000000
  [2/10] Fitness=-14.26171398, P(Human)=0.00000070
      ├─ log(P(Human))=-14.17290115
      ├─ Semantic penalty=0.08881271
      └─ Perplexity penalty=0.00000000
  [3/10] Fitness=-13.46456242, P(Human)=0.00000172
      ├─ log(P(Human))=-13.27543831
      ├─ Semantic penalty=0.18912411
      └─ Perplexity penalty=0.00000000
  [4/10] Fitness=-14.15458870, P(Human)=0.00000075
      ├─ log(P(Human))=-14.09905338
      ├─ Semantic penalty=0.05553532
      └─ Perplexity penalty=0.00000000
  [5/10] Fitness=-14.71243858, P(Human)=0.00000047
      ├─ log(P(Human))=-14.56390762
      ├─ Semantic penalty=0.14853084
      └─ Perplexity penalty=0.00000000
  [6/10] Fitness=-14.18745232, P(Human)=0.00000081
      ├─ log(P(Human))=-14.03028393
      ├─ Semantic penalty=0.15716839
      └─ Perplexity penalty=0.00000000
  [7/10] Fitness=-13.85217285, P(Human)=0.00000103
      ├─ log(P(Human))=-13.78927803
      ├─ Semantic penalty=0.06289482
      └─ Perplexity penalty=0.00000000
  [8/10] Fitness=-13.48809242, P(Human)=0.00000153
      ├─ log(P(Human))=-13.39238548
      ├─ Semantic penalty=0.09570730
      └─ Perplexity penalty=0.00000000
  [9/10] Fitness=-14.20878983, P(Human)=0.00000069
      ├─ log(P(Human))=-14.18442631
      ├─ Semantic penalty=0.02436376
      └─ Perplexity penalty=0.00000000
  [10/10] Fitness=-14.72011662, P(Human)=0.00000046
      ├─ log(P(Human))=-14.60155296
      ├─ Semantic penalty=0.11856365
      └─ Perplexity penalty=0.00000000
Logged to evolution_0.txt

✓ Initial best fitness: -13.46456242

GENERATION 1/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=3): Fitness=-13.46456242, P(Human)=0.00000172
        └─ Components: log(P)=-13.275438, sem_pen=0.189124, ppl_pen=0.000000
    Parent 2 (idx=8): Fitness=-13.48809242, P(Human)=0.00000153
        └─ Components: log(P)=-13.392385, sem_pen=0.095707, ppl_pen=0.000000
    Parent 3 (idx=7): Fitness=-13.85217285, P(Human)=0.00000103
        └─ Components: log(P)=-13.789278, sem_pen=0.062895, ppl_pen=0.000000

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
    Fitness: -13.20361900
  Local search on offspring 3...
    Fitness: -13.27826977
  Local search on offspring 9...
    Fitness: -13.39863777

NEW BEST FITNESS: -13.20361900
Logged to evolution_1.txt

  Generation 1 summary (HIGH PRECISION):
    Best fitness:  -13.20361900
    Avg fitness:   -14.04334259
    Worst fitness: -14.90683174
    Best P(Human): 0.00000205

GENERATION 2/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=2): Fitness=-13.20361900, P(Human)=0.00000205
        └─ Components: log(P)=-13.099806, sem_pen=0.103813, ppl_pen=0.000000
    Parent 2 (idx=3): Fitness=-13.27826977, P(Human)=0.00000205
        └─ Components: log(P)=-13.098353, sem_pen=0.179916, ppl_pen=0.000000
    Parent 3 (idx=9): Fitness=-13.39863777, P(Human)=0.00000165
        └─ Components: log(P)=-13.317354, sem_pen=0.081283, ppl_pen=0.000000

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
    Fitness: -13.04807758
  Local search on offspring 2...
    Fitness: -13.26416779
  Local search on offspring 5...
    Fitness: -13.27094555

NEW BEST FITNESS: -13.04807758
Logged to evolution_2.txt

  Generation 2 summary (HIGH PRECISION):
    Best fitness:  -13.04807758
    Avg fitness:   -13.63637829
    Worst fitness: -14.19784737
    Best P(Human): 0.00000263

GENERATION 3/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=3): Fitness=-13.04807758, P(Human)=0.00000263
        └─ Components: log(P)=-12.849195, sem_pen=0.198883, ppl_pen=0.000000
    Parent 2 (idx=2): Fitness=-13.26416779, P(Human)=0.00000215
        └─ Components: log(P)=-13.051438, sem_pen=0.212729, ppl_pen=0.000000
    Parent 3 (idx=5): Fitness=-13.27094555, P(Human)=0.00000216
        └─ Components: log(P)=-13.043862, sem_pen=0.227083, ppl_pen=0.000000

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
  Local search on offspring 1...
    Fitness: -13.06719303
  Local search on offspring 3...
    Fitness: -13.07224941
  Local search on offspring 7...
    Fitness: -13.13153648
Logged to evolution_3.txt

  Generation 3 summary (HIGH PRECISION):
    Best fitness:  -13.06719303
    Avg fitness:   -13.45651722
    Worst fitness: -14.47307205
    Best P(Human): 0.00000264

GENERATION 4/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=1): Fitness=-13.06719303, P(Human)=0.00000264
        └─ Components: log(P)=-12.846405, sem_pen=0.220788, ppl_pen=0.000000
    Parent 2 (idx=3): Fitness=-13.07224941, P(Human)=0.00000257
        └─ Components: log(P)=-12.871972, sem_pen=0.200277, ppl_pen=0.000000
    Parent 3 (idx=7): Fitness=-13.13153648, P(Human)=0.00000249
        └─ Components: log(P)=-12.904545, sem_pen=0.226992, ppl_pen=0.000000

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
  Local search on offspring 6...
    Fitness: -13.00923634
  Local search on offspring 8...
    Fitness: -13.04746532
  Local search on offspring 1...
    Fitness: -13.04746532

NEW BEST FITNESS: -13.00923634
Logged to evolution_4.txt

  Generation 4 summary (HIGH PRECISION):
    Best fitness:  -13.00923634
    Avg fitness:   -13.52441120
    Worst fitness: -14.76366234
    Best P(Human): 0.00000276

GENERATION 5/5

[STEP 3] Selection...
  Selected top 3 parents
    Parent 1 (idx=6): Fitness=-13.00923634, P(Human)=0.00000276
        └─ Components: log(P)=-12.800935, sem_pen=0.208302, ppl_pen=0.000000
    Parent 2 (idx=8): Fitness=-13.04746532, P(Human)=0.00000262
        └─ Components: log(P)=-12.851330, sem_pen=0.196135, ppl_pen=0.000000
    Parent 3 (idx=1): Fitness=-13.04746532, P(Human)=0.00000262
        └─ Components: log(P)=-12.851330, sem_pen=0.196135, ppl_pen=0.000000

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
    Fitness: -12.46549320
  Local search on offspring 2...
    Fitness: -12.93619728
  Local search on offspring 1...
    Fitness: -12.96134853

NEW BEST FITNESS: -12.46549320
Logged to evolution_5.txt

  Generation 5 summary (HIGH PRECISION):
    Best fitness:  -12.46549320
    Avg fitness:   -13.39245892
    Worst fitness: -14.22165012
    Best P(Human): 0.00000466

EVOLUTION COMPLETE

Best fitness achieved: -12.46549320
Best individual:
  P(Human): 0.00000466
  P(AI): 0.98721123
  P(AI-mimicry): 0.01278409
  Predicted: Class 2 (conf=0.9872)

Text:
I had always taken deep security from the comforting predictability of my street, a serene world where the greatest drama was a misaimed sprinkler or a potluck sign-up sheet. The man in the yellow house, with his perfectly manicured hedges, was the epitome of the good neighbor—a person whose unremarkable pleasantness I mistakenly believed I understood completely. My perception of him, and of my quiet life, was shattered one Tuesday by a simple postal error. The thick manila envelope I tore open contained no mundane mail, but a classified dossier, its pages a sea of black redactions. Clipped within was a photograph of him, two decades younger, his eyes holding a lethally sharp coldness that felt utterly alien. That envelope, suddenly a dead weight in my hand, revealed the truth: his harmless, mild-mannered persona was no accident but a disciplined performance, a meticulously built facade to conceal a past forged in a darker world, one that had no place among our block parties and bake sales.

Best individual saved to best_individual.txt

## Final Result after 5 generations
Best Individual from MATE Evolution
Fitness: -12.4655

Classification:
  P(Human): 0.0000
  P(AI): 0.9872
  P(AI-mimicry): 0.0128
  Predicted: Class 1 (conf=0.9872)

Text:
I had always taken deep security from the comforting predictability of my street, a serene world where the greatest drama was a misaimed sprinkler or a potluck sign-up sheet. The man in the yellow house, with his perfectly manicured hedges, was the epitome of the good neighbor—a person whose unremarkable pleasantness I mistakenly believed I understood completely. My perception of him, and of my quiet life, was shattered one Tuesday by a simple postal error. The thick manila envelope I tore open contained no mundane mail, but a classified dossier, its pages a sea of black redactions. Clipped within was a photograph of him, two decades younger, his eyes holding a lethally sharp coldness that felt utterly alien. That envelope, suddenly a dead weight in my hand, revealed the truth: his harmless, mild-mannered persona was no accident but a disciplined performance, a meticulously built facade to conceal a past forged in a darker world, one that had no place among our block parties and bake sales.
