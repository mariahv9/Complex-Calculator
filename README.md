# Complex Calculator

This project is about a complex operations of equations, matrix and vectors.

### Begining

Each function read tuples (a, b), this represents a as real part and b as imaginary part.

## Equations with complex numbers

The first part is composed for addition, subtraction, product, division, module, conjugate, conversion cartesian to polar and polar to cartesian.

```
    C1 = (a1, b1); C2 = (a2, b2)

ADDITION: C1 + C2 = (a1 + a2, b1 + b2)
SUSTRACTION: C1 - C2 = (a1 - a2, b1 - b2)
PRODUCT: C1 + C2 = (a1a2 - b1b2, a1b2 + a2b1)
DIVISION: C1 / C2 = (a1, b1) / (a2, b2)
```

## Matrix with complex numbers

The second part is composed for addition, subtraction, product, scalar, traspouse, conjugate, adjoint, inverse, trace, identity, equals, unitary, hermitiania, action, inner product; on matrix.

```
    m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] 
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]

ADDITION: M1 + M2 = M1 [j, k] + M2 [j, k]
SUSTRACTION: M1 - M2 = M1 [j, k] - M2 [j, k]
PRODUCT: (M1 x M2)[j, k] = SUMATORY (h=0, n-1)(M1 [j, h] x B [h, k])
SCALAR: C1 ∙ M = C ∙ M [j, k]
TRASPOUSE: M^T [j, k] = M [k, j]
CONJUGATE: M` [j,k] = M [j,k]
ADJOINT: M† [j, k] = M [k, j]
INVERSE: M [i, j] = M [-i, -j]
TRACE: Trace(M) = SUMATORY (n−1, i=0)(C[i, i ])
IDENTITY: M [i, i] == (1, 0)
EQUALS: M1 == M2
UNITARY: M† ∙ M
HERMITIANIA:
ACTION: M ∙ V
INNER PRODUCT: Trace(A† ⋆ B)
```
## Vectors with complex numbers

The first part is composed for addition, subtraction, product, division, module, conjugate, conversion cartesian to polar and polar to cartesian.

```
    C1 = (a1, b1); C2 = (a2, b2)

ADDITION: C1 + C2 = (a1 + a2, b1 + b2)
SUSTRACTION: C1 - C2 = (a1 - a2, b1 - b2)
PRODUCT: C1 + C2 = (a1a2 - b1b2, a1b2 + a2b1)
DIVISION: C1 / C2 = (a1, b1) / (a2, b2)
```




## Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
