# Complex Calculator

This project is about a complex operations of equations, matrix and vectors.

### Begining

Each function read tuples (a, b), this represents a as real part and b as imaginary part.

## Equations with complex numbers

The first part is composed for addition, subtraction, product, division, module, conjugate, conversion cartesian to polar and polar to cartesian.

```
    C1 = (a1, b1); C2 = (a2, b2)

ADDITION: C1 + C2 = (a1 + a2, b1 + b2)
SUBTRACTION: C1 - C2 = (a1 - a2, b1 - b2)
PRODUCT: C1 + C2 = (a1a2 - b1b2, a1b2 + a2b1)
DIVISION: C1 / C2 = (a1, b1) / (a2, b2)
```

## Matrix with complex numbers

The second part is composed for addition, subtraction, product, scalar, traspouse, conjugate, adjoint, inverse, trace, identity, equals, unitary, hermitiania, action, inner product; on matrix.

```
    m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] 
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]

ADDITION: M1 + M2 = M1 [j, k] + M2 [j, k]
SUBTRACTION: M1 - M2 = M1 [j, k] - M2 [j, k]
PRODUCT: (M1 x M2)[j, k] = SUMATORY (h=0, n-1)(M1 [j, h] x B [h, k])
SCALAR: C1 ∙ M = C ∙ M [j, k]
TRASPOUSE: M^T [j, k] = M [k, j]
CONJUGATE: M` [j,k] = M [-j,-k]
ADJOINT: M† [j, k] = M [k, j]
INVERSE: -M [i, j] = -(M [i, j])
TRACE: Trace(M) = SUMATORY (n−1, i=0)(C[i, i ])
IDENTITY: M [i, i] == (1, 0)
EQUALS: M1 == M2
UNITARY: M† ∙ M
HERMITIANIA:
ACTION: M ∙ V
INNER PRODUCT: Trace(A† ⋆ B)
```
## Vectors with complex numbers

The first part is composed for addition, subtraction, product, inverse, conjugate, norm, equals, distance, inner product; on vectors.

```
    v1 = [(c1, c2), (c1, c2),...,(c1, c2)] 
    v2 = [(c1, c2), (c1, c2),...,(c1, c2)]

ADDITION: (V1 + V2) [i] = V1 [i] + V2 [i]
SUBTRACTION: (V1 - V2) [i] = V1 [i] - V2 [i]
PRODUCT: (C · V)[j] = C × V[j]
INVERSE: (−V)[ j ] = −(V[ j ])
CONJUGATE: V [i] = V [-i]
NORM: |V| = sqrt (x2 +y2 +z2)
EQUALS: V1 == V2
DISTANCE: |V1 − V2| = sqrt⟨V1 − V2,V1 − V2⟩
INNER PRODUCT: ⟨V1, V2⟩ = V† ⋆ V2
```

## Experiments

### This part you found experiments as:
#### The marbles experiments with complex coefficient 
We are concerned not only with the states of the system, but also with the way the states change. How they change – or the dynamics of the system – can be repre- sented by a graph with directed edges. We do not permit an arbitrary graph. Rather, we insist that every vertex in the graph has exactly one outgoing edge. This require- ment will coincide with our demand that the system be deterministic. In other words, each marble must move to exactly one place. In plain English, this states that the number of marbles that will reach vertex i after one time step is the sum of all the marbles that are on vertices with edges connecting to vertex i.
Notice that the top two entries of Y are 0. This corresponds to the fact that there are no arrows going to vertex 0 or vertex 1.

#### Experiments of multiple probabilistic classic slits, with more than two slits
In quantum mechanics, there is an inherent indeterminacy in our knowledge of a physical state. Furthermore, states change with probabilistic laws. This simply means that the laws governing a system’s evolution are given by describing how states tran- sition from one to another with a certain likelihood.
In order to capture these probabilistic scenarios, let us modify what we did in
the last section. Instead of dealing with a bunch of marbles moving about, we shall
work with a single marble. The state of the system will tell us the probabilities of the
marble being on each vertex. We must modify the dynamics as well. Rather than exactly one arrow leaving each vertex, we will have several arrows shooting out of each vertex with real num- bers between 0 and 1 as weights. These weights describe the probability of our marble moving from one vertex to another in one time click. The adjacency matrices for our graphs will have real entries between 0 and 1 where the sums of the rows and the sums of the columns are all 1. Such matrices are called doubly stochastic.

#### Experiment of multiple quantum slits
This matrix is not unitary. The reason this matrix fails to be unitary is that we have not placed all the arrows in our graph. There are many more possible ways the pho- ton can travel in a real-life physical situation. In particular, the photon might travel from right to left. The diagram and matrix would become too complicated if we put in all the transitions. We are simply trying to demonstrate the phenomenon of interference and we can accomplish that even with a matrix that is not quite unitary. The adjacency matrix, P (for “photons”).

#### Probability ket
We say that the state |ψ⟩ is a superposition of the basic states. |ψ⟩ represents the particle as being simultaneously in all {x0, x1, . . . , xn−1} locations, or a blending of all the |xi ⟩. There are, however, different possible blendings (much like in the recipe for baking an apple pie you can vary the proportions of the ingredients and obtain different flavors). The complex numbers c0,c1,...,cn−1 tell us precisely which su- perposition our particle is currently in. The norm square of the complex number ci divided by the norm squared of |ψ⟩ will tell us the probability that, after observing the particle, we will detect it at the point xi. Let us assume that the particle can only be at the four points {x0, x1, x2, x3}. Thus, we are concerned with the state space C4. We shall calculate the probability that our particle can be found at position x2.  

## Running the tests

There are proofs of the last codes. The function is verify with base cases.

## References

* Quantum Computer for Computer Scientist - (S. Yanofsky, N., & A. Mannucci, M. (2008). Quantum Computing for Computer Scientists. New York: Cambridge University Press.)

## Reviewed
Luis Daniel Benavides Navarro, Ph.D 

## Authors

* **Maria Fernanda Hernandez Vargas** - [PurpleBooth](https://github.com/mariahv9)
Student of Systems Engineering of Escuela Colombiana de Ingenieria Julio Garavito 
