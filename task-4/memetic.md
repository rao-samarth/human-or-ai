# Local Search in Memetic Algorithms explained

The main difference between a memetic algorithm and a genetic algorithm, is that a memetic algorithm uses a local search technique in addition to the global search of a genetic algorithm, while a genetic algorithm does not do this...

The name comes from *memes*, a unit of information that evolves and improves as it spreads, and also what I sometimes doomscroll.

Let me explain with an example. Take the metric TSP problem. (This is basically the Travelling Salesman Problem, but where the triangle inequality applies between any 3 give cities in the problemspace).  
Let there be 6 cities A,B,C,D,E,F

## Global Search Approach in GA's

**Initial Population**  
S1: A → D → B → F → C → E   (length = 120)  
S2: B → C → A → E → D → F   (length = 135)  
S3: F → E → D → C → B → A   (length = 150)  
S4: A → B → C → D → E → F   (length = 140)  

**Selection**  
Select S1 and S4  

**Crossover**  
Combine Parents  
Parent 1: A → D → B → F → C → E
Parent 2: A → B → C → D → E → F

One possible offspring  
Child: A → D → B → C → E → F   (length = 118)  -------------> (1)

- No guarantee it’s the best arrangement nearby
- it is better though

**Mutation**
We swap some 2 of the nodes in the offspring  
A → D → C → B → E → F   (length = 125)


## Where Memetic comes in?

Memetic algorithms come in at step (1).  
We have the child  
Child: A → D → B → C → E → F   (length = 118)  


We now immediately apply a `local search` over here.  
Define a neighbourhood (FOR TSP):  
- Pick two edges
- Reverse the segment between them
- Keep the change only if distance improves

Try some local moves. For example,

Swap B and C  
A → D → C → B → E → F (length = 112)

Reverse the segment D → C → B  
A → B → C → D → E → F (length = 108)

Try even more local changes. Nothing better? Then just stop.  
**108 is the final length. Put it back in the population**

We are using memetic algorithms because of this local search feature.