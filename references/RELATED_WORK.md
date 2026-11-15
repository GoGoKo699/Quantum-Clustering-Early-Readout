# Related work and attribution

This project asks which classical information may be released from an incomplete quantum dataset while preserving the optimal eventual probability of recovering its complete binary partition. Preservation refers to one specified Bayes decision score. It does not require the quantum state itself to remain unchanged.

The data model has two independent Haar-distributed pure prototypes in local dimension $`d\geq2`$, independent uniform binary labels, and one native specimen at each of $`n`$ positions. A partition identifies a label string with its global complement. All statements below retain that prior, loss and single-specimen interface.

## Closest scientific antecedents

| Source | Established ingredient | Addition in this project |
| --- | --- | --- |
| Sentís et al., *Unsupervised classification of quantum data* (2019) | The quantum binary-clustering model, Haar-averaged states, optimal collective measurement, Schur representation and exact full-dataset success. | A causal restriction on classical information available before all specimens arrive, with unrestricted early instruments. |
| Spencer-Wood, Jeffers and Croke, *Measurement disturbance tradeoffs in three-qubit unsupervised quantum classification* (2022) | The complete two-to-three-qubit tradeoff, including a region where an informative first classification leaves the final optimum unchanged. | The exact characterization for every dataset size and every local dimension, including the distinction between one and at least two missing arrivals. |
| Spencer-Wood, *Sequential measurement in quantum learning* (2024), Chapter 4 | A proposed all-size count-only structure, conditional no-order arguments, free-readout constructions and an improved candidate prefix classifier. | Removal of the conditional proof gaps, characterization of the full symmetry-reduced free cone, a maximal experiment under classical postprocessing, and the optimal free prefix decision. |
| Pellonpää, *On coexistence and joint measurability of rank-1 quantum observables* (2013/2014) | A rank-one POVM is compatible with another observable precisely when that observable is its classical postprocessing. | The clustering-specific optimal-support and locality intersection arguments needed before that general mechanism determines an early readout. |

## The inherited clustering problem

Sentís et al. [1] solve the unrestricted final clustering task. Their Schur decomposition reduces the Haar-averaged discrimination problem to two-row symmetric-group multiplicity spaces. We use that ensemble, its optimal measurement and its full-partition success as the benchmark; these are not new results here. For fixed $`d`$, their asymptotic optimum is

```math
P_{\mathrm{full}}(n,d)\sim \frac{8(d-1)}{n^2}.
```

Their analysis also studies increasing dimension and other cost functions. This project retains exact full-partition success. It does not transfer its early-information conclusion to the other losses.

## From the three-qubit tradeoff to an exact early-readout boundary

The three-qubit experiment in [2] demonstrates that informative early learning need not reduce the best eventual clustering score. Its free two-qubit prefix success reaches $`7/12`$. That example and its physical question are inherited. Here, the distinction becomes temporal: with two or more specimens still missing, an exactly free classical record has the same probability law for every hidden partition; with exactly one missing, its law may depend on the unordered prefix class sizes but cannot identify their positions.

The 2024 thesis [3] is especially close. Its Theorem 4.4.1 is conditional on the specified final optimal POVM and Conjecture 4.A.1. Chapter 4 and the conclusion identify the unresolved conjectural and uniqueness steps. Its Algorithm 1 supplies a candidate improved free prefix classifier; establishing its optimality was left open. These statements must be credited as antecedents of the question and construction, rather than treated as an independent discovery of the count-only idea.

Our proof does not establish Conjecture 4.A.1 as written. In the $`n=5,k=2`$ harmonic sector, unequal positive coefficients can cancel the cross-branch block while leaving nonscalar diagonal blocks. The required induction uses a stronger premise: one complete branch is already scalar. A harmonic-frame lemma then forces the other branch to be scalar. Together with the discrimination dual equality conditions and frame independence, this yields the unrestricted record-statistics statement and the exact reduced coefficient cone. The related optimal prefix classifier, including the qubit value $`47/270`$ at $`n=5`$, is proved rather than assumed.

## What is inherited from general measurement theory

Rank-one compatibility and classical postprocessing are established measurement-theoretic tools [4]. Likewise, “Blackwell maximal” uses the usual comparison of statistical experiments by randomization [5]. We prove maximality here by an explicit stochastic factorization, not by claiming a new comparison principle.

The new work lies in determining the relevant optimal supports, resolving their possible freedoms, and intersecting the resulting refinement cone with an operation available on an early prefix. Those steps depend on the clustering ensemble and symmetric-group branching. A generic no-information-without-disturbance slogan does not identify which information is free for this particular decision task.

There is an important distinction between a physical POVM and the likelihoods it produces on this ensemble. Twirling an early effect over the common unitary action preserves all label-conditioned probabilities. The complete coefficient characterization is therefore stated for symmetry-reduced effects. Every unrestricted free classical record has a likelihood-equivalent reduced representative and is a postprocessing of the canonical experiment. No uniqueness of every physical POVM is claimed.

## Source versions

1. G. Sentís, A. Monràs, R. Muñoz-Tapia, J. Calsamiglia and E. Bagan, *Unsupervised classification of quantum data*, **Physical Review X 9**, 041029 (2019). [DOI](https://doi.org/10.1103/PhysRevX.9.041029); [arXiv:1903.01391v3](https://arxiv.org/abs/1903.01391v3). Relevant locations: Section IV.1, Appendix B, Appendix C and Appendix D.
2. H. Spencer-Wood, J. Jeffers and S. Croke, *Measurement disturbance tradeoffs in three-qubit unsupervised quantum classification*, **Physical Review A 105**, 062447 (2022). [DOI](https://doi.org/10.1103/PhysRevA.105.062447); [accepted manuscript](https://eprints.gla.ac.uk/273595/1/273595.pdf), dated June 21, 2022; [arXiv:2202.05584](https://arxiv.org/abs/2202.05584). The accepted manuscript may differ in presentation from the journal version.
3. H. Spencer-Wood, *Sequential measurement in quantum learning*, PhD thesis, University of Glasgow (2024). [University record](https://theses.gla.ac.uk/84375/); [DOI](https://doi.org/10.5525/gla.thesis.84375). Relevant locations: Chapter 4, Theorem 4.4.1, Algorithm 1, Appendix 4.A and the Chapter 6 discussion of open proof steps. The university record was deposited June 20, 2024.
4. J.-P. Pellonpää, *On coexistence and joint measurability of rank-1 quantum observables*, **Journal of Physics A: Mathematical and Theoretical 47**, 052002 (2014). [DOI](https://doi.org/10.1088/1751-8113/47/5/052002); [arXiv:1308.3154v3](https://arxiv.org/abs/1308.3154v3), December 17, 2013. We use the corrected version; the arXiv record notes errors in earlier versions.
5. D. Blackwell, *Equivalent comparisons of experiments*, **The Annals of Mathematical Statistics 24**, 265–272 (1953). [DOI](https://doi.org/10.1214/aoms/1177729032).

These comparisons identify the nearest inspected mechanisms and open steps. They do not assert exhaustive priority coverage. Bibliographic entries are provided in [references.bib](references.bib).
