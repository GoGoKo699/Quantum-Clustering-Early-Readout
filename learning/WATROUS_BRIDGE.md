# From Watrous to early quantum clustering

This bridge uses one educational anchor: John Watrous, *The Theory of Quantum Information* (2018). Use the [standard-layout manuscript](https://jhwatrous.github.io/TQI.pdf) linked on the [author's books page](https://jhwatrous.github.io/books-and-courses.html). The linked manuscript is copyright 2018, describes itself as a pre-publication draft, and has a January 2018 preface. The author's page records publication by Cambridge University Press in April 2018. These locations refer to this manuscript's **printed page numbers**, not a PDF viewer's page counter. The author makes it available for personal use and prohibits redistribution; no book copy is included here.

The purpose is to translate textbook foundations into the repository's [specified source model](../science/model.md), then identify the arguments the book does not supply. This is a route through an exact Bayesian decision problem, rather than a survey of quantum machine-learning algorithms.

## Focused locations

The section numbers and named results below were checked against the author's standard-layout manuscript. The chapter links keep the selected readings within that same book.

| Location | Role here |
| --- | --- |
| [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.2–2.1.3, pp. 61–71 | States and reduced states; distinguish a physical specimen from its prior-averaged density operator. |
| Chapter 2, §§2.2.1–2.2.2, pp. 72–90; §§2.3.1–2.3.2, pp. 100–113 | Channels, POVMs and retained quantum outputs. The instruments discussion is on pp. 111–113. |
| [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §1.2.3, pp. 53–56; Theorem 1.18 and Proposition 1.19 | SDP duality and complementary slackness. |
| [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.1.1, pp. 125–131; Theorem 3.4 | Binary discrimination for the two-specimen example. |
| Chapter 3, §3.1.2, pp. 132–138; Theorem 3.9 | Ensemble discrimination and optimal-measurement certificates. |
| [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.1.1, pp. 391–399; Proposition 7.1 and Corollary 7.3 | Symmetric projectors and their dimensions. |
| Chapter 7, §7.1.2, pp. 400–407; Theorem 7.15 | The common-unitary commutant and permutation operators. |
| Chapter 7, §7.2.1, pp. 408–419; Lemma 7.24 | Haar averaging of repeated pure states. |

Section 1.1.2 (p. 8) and §1.1.3 (p. 24) are useful references for operator notation, positivity, spectral decompositions and norms. Entropy, channel-capacity and concentration chapters are not needed for the exact temporal theorem.

## Translate the notation first

Watrous uses column vectors and adjoints rather than Dirac notation. The repository sometimes uses both. In particular, a rank-one operator need not be a normalized pure state.

| Book convention or concept | Repository form and interpretation |
| --- | --- |
| $`u`$ and $`uu^*`$ | $`\lvert u\rangle`$ and $`\lvert u\rangle\langle u\rvert`$. The latter has trace $`\lVert u\rVert ^2`$, which need not be one for a frame vector. |
| $`\mathrm D(\mathcal X)`$ | Density operators on a specimen space $`\mathcal X=\mathbb C^d`$ or an array $`(\mathbb C^d)^{\otimes n}`$. |
| Ensemble $`\eta(a)`$ | The prior-weighted operator $`p_n\rho_{n;[x]}`$, not just the normalized state $`\rho_{n;[x]}`$. |
| Measurement $`\mu(a)\ge0`$, $`\sum_a\mu(a)=I`$ | Final effects $`M_{[x]}`$ or early effects $`F_y`$. Outcome probabilities are $`\mathrm{tr}(F_y\rho)`$. |
| Instrument branch $`\Phi_y`$ | A completely positive map with effect $`F_y=\Phi_y^*(I)`$. The effect fixes classical probabilities; the map also fixes the retained quantum state. |
| Dual discrimination operator $`Y`$ | The explicit certificate $`\Gamma_n`$ in [optimal measurement](../science/optimal_measurement.md). It is not an early POVM effect. |
| Symmetric projection | $`P_{\mathrm{sym},A}`$ on positions in $`A`$. Its rank is $`s_d(\lvert A\rvert)=\binom{d+\lvert A\rvert-1}{\lvert A\rvert}`$. |
| Permutation operator $`W_\pi`$ | A permutation of specimen positions. This differs from applying the same unknown-basis rotation $`U`$ to every specimen. |

The label $`[x]`$ is an unordered partition: $`x`$ and its global binary complement describe the same answer. Empty classes are allowed. Independent uniform binary labels therefore give each full partition prior $`p_n=2^{1-n}`$. Count classes do **not** have equal prior: different cardinalities contain different numbers of partitions. The score is the probability of guessing the whole partition correctly, with no partial credit for correctly labelled positions.

## From unknown prototypes to a known ensemble

Two prototype directions $`u,v\in\mathbb C^d`$ are drawn independently from the uniform pure-state prior. The learner receives one specimen at each known position, without descriptions of $`u`$ or $`v`$. Conditional on the hidden pattern, the preparations are pure; averaging the unavailable directions gives a mixed state.

Lemma 7.24 and the symmetric-space dimension formula provide the one-prototype moment. Applying this independently to the two groups gives the repository's source operator:

```math
\int (uu^\dagger)^{\otimes t}\,d\mu(u)
=\frac{P_{\mathrm{sym}}^{(t)}}{s_d(t)},
\qquad
\rho_{n;j,A}
=\frac{P_{\mathrm{sym},A}P_{\mathrm{sym},A^c}}
{s_d(j)s_d(n-j)},
\quad |A|=j\le n/2.
```

The two projectors act on disjoint sets of positions. This calculation explains why Bayesian state discrimination is the relevant starting point: the unknown directions have been integrated out, while the hidden partition remains the hypothesis.

The common-$`U(d)`$ invariance permits averaging a **whole sequential procedure's joint POVM** without changing its source statistics. Theorem 7.15 supplies the commutant foundation. A further representation-theoretic step, spelled out in [the model](../science/model.md), resolves the occupied space into two-row factors

```math
\mathcal S_n
=\bigoplus_{k=0}^{\lfloor n/2\rfloor}
Q_{n,k}^{(d)}\otimes V_{n,k},
\qquad V_{n,k}\cong S^{(n-k,k)}.
```

Here $`Q`$ carries the common-unitary action and $`V`$ the position-permutation action. This specific decomposition, its spherical lines and its one-box branching are additional ingredients; the reading list does not substitute for their project proofs. For $`d\gt 2`$, higher-row physical sectors are absent from this source ensemble. Statements restricted to $`\mathcal S_n`$ do not determine an instrument's action on those unused sectors.

## From discrimination duality to an exact timing constraint

Apply the ensemble-discrimination SDP to the prior-weighted states:

```math
\begin{aligned}
P_{\mathrm{opt},d}(n)
&=\max_{\substack{M_{[x]}\succeq0\\\sum_{[x]}M_{[x]}=I}}
\sum_{[x]}\mathrm{tr}\!\left(M_{[x]}p_n\rho_{n;[x]}\right),\\
&=\min_{\Gamma\succeq p_n\rho_{n;[x]}\ \forall[x]}
\mathrm{tr}\Gamma .
\end{aligned}
```

The book supplies the general optimization framework. The [project's optimal-measurement page](../science/optimal_measurement.md) supplies the particular dual certificate and its kernels, reconstructing the inherited clustering optimum of [Sentís et al. (2019)](https://doi.org/10.1103/PhysRevX.9.041029).

An arbitrary early instrument on the first $`m`$ specimens, followed by a record-dependent final decoder, induces effects $`B_{y,[x]}`$ satisfying

```math
B_{y,[x]}\succeq0,\qquad
\sum_{[x]}B_{y,[x]}=F_y\otimes I_{d^{n-m}}.
```

The tensor identity expresses the early operation's lack of access to future arrivals. Exact preservation of the final optimum makes the nonnegative dual gap vanish:

```math
0=\sum_{y,[x]}
\mathrm{tr}\!\left[
(\Gamma_n-p_n\rho_{n;[x]})B_{y,[x]}
\right].
```

Every summand must vanish. Positivity then puts each joint effect inside the corresponding dual-slack kernel. This is the operational use of complementary slackness: it applies to **every** optimal continuation, rather than assuming that a preselected covariant decoder is the only physically possible optimum.

Three further steps carry that equality to the temporal theorem:

1. [Harmonic frames](../science/harmonic_frames.md) identifies the kernel line using $`H_k(n)=\ker D_n`$ in the subset module, with $`v_A=P_{H_k(n)}e_A`$. Matching polytabloids isolate coefficients and prove independence of the rank-one projectors. At balance, complementary subsets share a line, so one representative per pair requires a factor of two.
2. [Temporal rigidity](../science/temporal_rigidity.md) proves the branching annihilator. In the restriction $`H_k(n)=T\oplus B`$, annihilating the lower branch forces the compressed diagonal operator to be scalar on the upper branch. Induction starts from the one-dimensional lowest block. Mere block diagonality is insufficient; the page gives the necessary scalar-bottom hypothesis and the five-point counterexample to the stronger implication.
3. [Free readout](../science/free_readout.md) combines that rigidity with positivity of the joint refinements. For $`m=n-1`$, a symmetry-reduced early POVM on the occupied prefix support is compatible with exact optimal final clustering precisely when

```math
F_y=\sum_{j=0}^{\lfloor m/2\rfloor}\theta_{y,j}\Pi_j,\qquad
\theta_{y,j}\ge0,\qquad
\sum_y\theta_{y,j}=1,\qquad
\theta_{y,j}\le(n-2j+2)\theta_{y,j-1}\quad(j\ge1).
```

These are project-specific proofs, not theorems attributed to Watrous. They establish an exact **decision** criterion: a record produced with two or more specimens still missing has partition-independent likelihoods; with one missing, a constrained noisy size statistic is possible but positional information is excluded.

The canonical compatible record dominates all other free records by classical postprocessing of their partition likelihoods. This does not identify a unique physical instrument or a unique quantum output. A sufficient physical implementation uses the local Lüders branches $`X\mapsto\sqrt{F_y}X\sqrt{F_y}`$, retains the prefix, and later uses a conditional global POVM. The constructive argument is in [optimal measurement, Section 5](../science/optimal_measurement.md#5-joint-povms-and-local-lüders-instruments).

## The two-then-three-qubit instance

The [physical tutorial](TUTORIAL.md) works through the complete $`d=2,n=3,m=2`$ case. Its two-prefix hypotheses are “same prototype” and “different prototypes,” each with prior one half:

```math
\rho_{\mathrm{same}}=\frac{P_{\mathrm{sym}}}{3},
\qquad
\rho_{\mathrm{different}}=\frac{I_4}{4}.
```

A sharp symmetric/antisymmetric measurement optimizes standalone early discrimination. Exact preservation of the later three-specimen optimum instead allows the softer effects

```math
K_0=\frac23P_{\mathrm{sym}},\qquad
K_1=\frac13P_{\mathrm{sym}}+P_{\mathrm{asym}}.
```

Guessing “same” on outcome zero and “different” on outcome one succeeds with probability $`\tfrac12(\tfrac23+\tfrac12)=\tfrac7{12}`$. The tutorial also supplies the retained quantum branches and a compatible later decoder; early outcome probabilities alone would not prove that final success is preserved. The final optimum is $`5/12`$ for the four three-position partitions. Comparing $`7/12`$ and $`5/12`$ directly does not compare performance on the same task.

The complete three-qubit tradeoff is inherited from [Spencer-Wood, Jeffers and Croke (2022)](https://doi.org/10.1103/PhysRevA.105.062447). The [related-work account](../references/RELATED_WORK.md) also places the arbitrary-length construction and the repaired proof gap in their research context.

## Boundaries of the bridge

The conclusion uses pure independent Haar prototypes, uniform independent labels and exact Bayesian whole-partition success. All branches count, including outcomes that are unfavorable for an early guess. “Free” is not a nondisturbance or state-recovery claim. A classical record with no partition information need not leave the quantum input useful.

The [stability page](../science/stability.md) proves a finite-size quantitative statement with an explicit conditioning singular value. It gives no favorable uniform bound on that quantity and hence no general claim that a small final loss enforces the exact theorem's early-accuracy scaling. The construction establishes physical finite-dimensional realizability, while [resource accounting](../science/resources.md) keeps memory and efficient gate synthesis separate.

For the broader public dependency sequence, continue to [the milestone map](MILESTONES.md). For the exact optimum of the compatible early decision problem, continue to [prefix accuracy](../science/prefix_accuracy.md).
