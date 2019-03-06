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

This part you found experiments as:
```
The marbles experiments with complex coefficient
Experiments of multiple probabilistic classic slits, with more than two slits.
Experiment of multiple quantum slits.
```
## Running the tests

There are proofs of the last codes. The function is verify with base cases.

## References

* Quantum Computer for Computer Scientist - (S. Yanofsky, N., & A. Mannucci, M. (2008). Quantum Computing for Computer Scientists. New York: Cambridge University Press.)

## Reviewed
Luis Daniel Benavides Navarro, Ph.D 

## Authors

* **Maria Fernanda Hernandez Vargas** - [PurpleBooth](https://github.com/mariahv9)
Student of Systems Engineering of Escuela Colombiana de Ingenieria Julio Garavito 
