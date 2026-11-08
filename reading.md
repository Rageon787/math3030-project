# Reading List 
Split reading by effort, start with lower effort reading first and then move to higher effort reading:

1. *Low Effort* (15 minutes - 30 Minutes) 

- [ ] Karl Sims’ reaction-diffusion page or Robert Munafo’s “Reaction-Diffusion by the Gray-Scott Model” (mrob.com) — interactive/visual explainers of the Gray-Scott model with parameter maps and pattern galleries, no equations required to get the gist. Good for building intuition for what “spots vs. stripes vs. chaos” actually looks like before you touch the maths.

- [ ] Wikipedia: “Reaction–diffusion system” and “Turing pattern” — standard overview, gives you vocabulary (activator-inhibitor, diffusion-driven instability) you’ll need before reading the original papers.

- [ ] The Coding Train (Daniel Shiffman) — Reaction-Diffusion video/tutorial — if you like a more visual/coding-first explanation, this walks through implementing Gray-Scott step by step; useful for building intuition for your own simulation too.


2. *Medium Effort*  (30 Minutes to 60 Minutes) 

- [ ]  Karl Sims (1991) or Pearson (1993) treated as a “read for the figures” pass — don’t try to follow the full derivation yet, just read the intro/abstract and look at the pattern diagrams to connect the visuals from step 1 to the actual parameter names (F, k).


3. *High Effort* 
- [ ] Original paper on the topic. Turing's paper on Chemical basis of Morphogenesis

- [ ] Murray, Mathematical Biology II, Turing instability chapter — the rigorous general derivation; this is the one to save for when you’re ready to actually write your own stability analysis.

- [ ] Witkin & Kass (1991) and Pearson (1993) in full, if your scope ends up needing the parameter-space/pattern-classification detail.

# Notes by source 

## Wikipedia 
- *Semi-Linear Parabolic Partial Differential Equations*
- Solutions can display a wide range of behaviours including self-organized patterns called "turing patterns"
- Reaction Diffusion Systems can have multiple components 
    - One component 
    - Two components 
    - Three or more Components 
- Alan turing proposed: "Stable solutions in a local system can become unstable in the presence of local diffusion" 


Taking down notes from my reading, grouped by each resource:

### Chapter 4: Fractals, noise and agents with applications to landscapes.

- Describes stochastic methods for terrain generations
    - Diamond Square 
    - Perlin Noise

- Video games have different terrain requirements. For instance, in games like GTA 5, a level of realism is expected. 

- Voxels:
    - Dividing the structure of terrain by cubes. It's similar to how we divide continous functions in calculus.

- "Minecraft has unusually large voxels."
    - Referring to the blockyness of minecraft.



## Advantages of procedural noise functions 
``` 
Procedural noise has many advantages: it is typically very
fast to evaluate, often allowing evaluation of complex and
intricate patterns on-the-fly, and it has a very low memory
footprint, making it an ideal candidate for compactly gener-
ating complex visual detail. In addition, with a suitable set of
parameters, procedural noise can be used to easily generate a
large number of different patterns. Finally, procedural noise
is often randomly accessible, so that it can be evaluated inde-
pendently at every point in constant time. This last property
has always been a great advantage, but takes on even higher
significance with the advent of massively parallel GPU’s and
multi-core CPU systems.
```


```
Noise is the random number generator of computer graph-
ics. It is a random and unstructured pattern, and is useful
wherever there is a need for a source of extensive detail
that is nevertheless lacking in evident structure. Random pat-
terns are often described in the frequency domai
```
"Noise creates random and unstructured patterns".







