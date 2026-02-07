# Lagrangian Relaxation

In this file, I explain Lagrangian Relaxation very simply.

Basically, all Lagrangian relaxation does is covert a constrained problem into an unconstrained (or softly constrained) problem.  

e.g. `Minimise f(x) subject to g(x) ≤ 0` can be rewritten as `minimise f(x)+k.g(x)`  
Here, k>>0 is a penalty term. If `g(x)>0`, the term will become significantly bigger.

This is a simplified version of what lagrangian relaxation is.  
For any constrained function that we have, we add a penalty term.  