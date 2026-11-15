# The complete free-readout family

There is one canonical classical experiment that contains every exactly free early clustering record. It acts on the first $`m=n-1`$ systems. The statement concerns the outcome probabilities of the [Haar-pure binary source](model.md); it does not identify all physical instruments that produce those probabilities.

## 1. The compatibility cone

Put $`r=\lfloor m/2\rfloor`$, and let $`\Pi_j`$ project onto the occupied prefix sector $`Q_{m,j}^{(d)}\otimes V_{m,j}`$. By [temporal rigidity](temporal_rigidity.md), every free effect, after the common-$`U(d)`$ twirl, is

```math
F_y=\sum_{j=0}^r\theta_{y,j}\Pi_j
\quad\text{on }\mathcal S_m.
\tag{1}
```

The source likelihoods are unchanged by this twirl. Actions on unoccupied sectors can be completed independently and do not enter the statements below.

**Compatibility theorem.** A central prefix POVM (1) admits a continuation attaining optimal final clustering if and only if

```math
\theta_{y,j}\ge0,\qquad
\theta_{y,j}\le b_j\theta_{y,j-1}\quad(1\le j\le r),
\qquad
\sum_y\theta_{y,j}=1,
\qquad b_j=n-2j+2.
\tag{2}
```

These conditions hold for every local dimension $`d\ge2`$. The constants in the cone depend on the permutation-space branching, rather than on the dimensions of the $`U(d)`$ representations.

To prove necessity, restrict $`F_y\otimes I_d`$ to global two-row sector $`k`$. Its two multiplicity branches have values $`\theta_{y,k}`$ and $`\theta_{y,k-1}`$. For $`n>2k`$, put $`a=n-2k+1`$ and use the unnormalized Parseval vectors $`v_A`$ from [the harmonic frame](harmonic_frames.md). The unique expansion in $`|v_A\rangle\langle v_A|`$ has coefficients

```math
t_{y,A}=
\begin{cases}
\theta_{y,k},&n\notin A,\\[1mm]
\displaystyle\frac{(a+1)\theta_{y,k-1}-\theta_{y,k}}a,
&n\in A.
\end{cases}
\tag{3}
```

Indeed, subtract $`\theta_{y,k-1}I`$ and apply the branching lemma: the remaining operator is $`(\theta_{y,k}-\theta_{y,k-1})P_T`$, whose coefficients are that scalar outside the last position and its negative divided by $`a`$ inside it. Positivity of every joint refinement forces both coefficients in (3) to be nonnegative. This is (2). In a balanced terminal global sector there is only the lower branch; the coefficient relative to each balanced optimal effect is $`\theta_{y,r}`$, so it adds positivity and no further inequality.

Conversely, (2) makes the coefficients (3) nonnegative. Their sum over $`y`$ is one for every unbalanced optimal effect, and the same is true relative to the balanced optimal effects. Thus

```math
B_{y,A}=t_{y,A}M_A
\tag{4}
```

is a joint POVM on the occupied global support, with marginals $`F_y\otimes I_d`$ and the [optimal final POVM](optimal_measurement.md). Here the balanced convention is $`M_A=2I_Q\otimes|v_A\rangle\langle v_A|`$, one representative per complementary pair; its coefficient in (4) is $`\theta_{y,r}`$. On source-null global sectors, complete the joint POVM with any compatible splitting of the early marginal. The local Lüders construction in [optimal measurement, Section 5](optimal_measurement.md#5-joint-povms-and-local-lüders-instruments) realizes this joint POVM without access to the last specimen at the early time. This proves sufficiency.

## 2. A canonical maximal experiment

Define

```math
B_0=1,\qquad B_j=\prod_{t=1}^j b_t,
\qquad
w_l=
\begin{cases}
B_l^{-1}-B_{l+1}^{-1},&l<r,\\
B_r^{-1},&l=r.
\end{cases}
\tag{5}
```

All $`w_l`$ are strictly positive. The canonical free POVM is

```math
K_l=w_l\sum_{j=0}^l B_j\Pi_j,
\qquad l=0,\ldots,r.
\tag{6}
```

For each sector $`j`$, its total coefficient is $`B_j\sum_{l\ge j}w_l=1`$, so the effects sum to the identity on $`\mathcal S_m`$. Their coefficient vectors satisfy (2), hence they are free.

**Statistical maximality.** For every early record that preserves exact optimal final success, there is a stochastic matrix $`R(y\mid l)`$ such that

```math
\Pr(y\mid [x])
=\sum_{l=0}^r R(y\mid l)\operatorname{tr}(K_l\rho_{m;[x]})
\quad\text{for every prefix partition }[x].
\tag{7}
```

After twirling, this also holds as an equality of the supported POVM effects. To see it, set

```math
z_{y,l}=\frac{\theta_{y,l}}{B_l}
-\frac{\theta_{y,l+1}}{B_{l+1}},
\qquad
\frac{\theta_{y,r+1}}{B_{r+1}}:=0.
\tag{8}
```

The cone inequalities give $`z_{y,l}\ge0`$. Completeness gives $`\sum_yz_{y,l}=w_l`$. Therefore $`R(y\mid l)=z_{y,l}/w_l`$ is stochastic, and telescoping gives $`F_y=\sum_lR(y\mid l)K_l`$. Equation (7) follows from the unchanged source likelihoods under twirling.

This is Blackwell domination of the classical label experiment: any decision rule, score, or information calculation involving the early classical record and the clustering label can be reproduced by reading $`l`$ and then randomizing classically. It is not uniqueness of the instrument, a statement about information on the unknown pure-state directions, or a state-recovery assertion.

## 3. What the canonical outcome reveals

For a prefix of minority size $`k`$, use $`T_{m,k}=s_d(m-k)s_d(k)`$ and $`q_d(m,j)`$ from the [model](model.md). Its canonical likelihood is

```math
\Pr(l\mid k,A)
=\frac{w_l}{T_{m,k}}
\sum_{j=0}^{\min\{k,l\}}q_d(m,j)B_j.
\tag{9}
```

The ordering $`A`$ is absent. The outcome is a noisy cardinality statistic. It is generally less informative than a sharp measurement of the prefix Schur sector, because a sharp sector measurement need not satisfy the compatibility cone.

For $`n=3`$, the canonical effects are particularly simple in every dimension:

```math
K_0=\frac23\Pi_{\mathrm{sym}},\qquad
K_1=\frac13\Pi_{\mathrm{sym}}+\Pi_{\mathrm{asym}}.
\tag{10}
```

The optimal early clustering success for this example is $`(4d-1)/(6d)`$; for qubits it is $`7/12`$. A sharp symmetric/antisymmetric test has stronger early discrimination but does not preserve the optimal final decoder.

The [accuracy account](prefix_accuracy.md) derives the exact all-dimension optimum and its asymptotic behavior. The cone recurrence and its constructive strategy specialize to the arbitrary-$`n`$ construction in [Hector Spencer-Wood's 2024 thesis](https://theses.gla.ac.uk/84375/), Chapter 4, particularly Eq. (4.138) and Algorithm 1. The present compatibility and maximality proof establishes its optimality without the thesis's unproved intermediate implication. The inherited three-qubit boundary is due to [Spencer-Wood, Jeffers, and Croke (2022)](https://doi.org/10.1103/PhysRevA.105.062447).
