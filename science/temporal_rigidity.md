# Temporal rigidity of an exactly lossless early readout

An early classical record can preserve the Bayes-optimal probability of clustering the entire dataset only by discarding positional information. On $`n-1`$ specimens it may retain information about cluster cardinality. On $`m\le n-2`$ specimens it retains no information about the binary cluster pattern at all.

The preservation condition is exact and concerns the probability of recovering the whole partition, modulo exchanging the two template names. It is not a Hamming-loss guarantee or a statement about a small allowed decrease in final success. The source model is the [uniform two-template Haar-pure ensemble](model.md). The theorem allows an arbitrary first instrument, retained quantum systems, ancillas, and a final measurement conditioned on the entire early classical record. Its nontrivial range begins at $`n=3`$; for $`n=2`$, a one-specimen prefix has only one cluster partition and the statistical conclusion is immediate.

## Statement on observable effects

Let $`E_y`$ be an early POVM effect on the first $`n-1`$ qudits. Average it under a common physical rotation:

```math
\overline E_y
=\int_{U(d)}U^{\otimes(n-1)}E_yU^{\dagger\otimes(n-1)}\,dU.
```

Every prefix source state is invariant under this rotation, so $`E_y`$ and $`\overline E_y`$ have identical outcome probabilities on the ensemble. This averaging is an analysis of observable statistics; it does not assume that averaging a chosen Lüders instrument leaves its back-action unchanged.

**Theorem.** If the complete sequential procedure attains the unrestricted optimal $`n`$-point clustering success probability, then, on the source-supported prefix sectors,

```math
\overline E_y
=\bigoplus_{i=0}^{\lfloor(n-1)/2\rfloor}
\theta_i^y I_{Q_{n-1,i}}\otimes I_{V_{n-1,i}},
\qquad
\theta_i^y\ge0,
\qquad
\sum_y\theta_i^y=1.
```

Here $`V_{r,i}\cong S^{(r-i,i)}`$ is the Specht multiplicity space and $`Q_{r,i}`$ the corresponding $`U(d)`$ representation. Thus the observable part of every early effect is central under prefix permutations. It may distinguish Schur sectors, but cannot distinguish two orderings with the same cluster cardinalities.

For $`d=2`$, these are all prefix Schur sectors. For $`d\gt 2`$, sectors with three or more rows never occur in the binary pure-template ensemble. The theorem places no restriction on effects there.

## From an arbitrary instrument to the optimal supports

Any first instrument and its conditional final decoder induce a joint POVM $`\{B_{y,A}\}`$ on the original dataset. Its marginals satisfy

```math
\sum_A B_{y,A}=E_y\otimes I_d,
\qquad
\sum_y B_{y,A}=G_A,
```

where $`\{G_A\}`$ is the resulting final clustering POVM. Since final success is optimal, the dual-equality argument in [Optimal measurement](optimal_measurement.md) applies to every $`G_A`$, without assuming an optimal decoder in advance.

For a label of minority size $`k`$, the only source-supported dual kernel is

```math
Q_{n,k}\otimes\mathrm{span}\{v_A\}.
```

Positivity gives $`0\le B_{y,A}\le G_A`$, so the same support restriction holds for every joint refinement. Averaging the joint POVM under $`U(d)`$ preserves its marginals and all ensemble probabilities. Its compression to a source-supported sector has the form

```math
\overline B_{y,A}
=\beta_{y,A}I_{Q_{n,k}}\otimes|v_A\rangle\langle v_A|,
\qquad \beta_{y,A}\ge0,
```

with a harmless change of coefficient if normalized spherical vectors are used. At balance, one representative per complementary pair is retained. The frame-independence proof in [Harmonic frames](harmonic_frames.md) controls those representatives as well.

The support assertion is the point where exact optimal final success enters. It does not follow from permutation covariance alone. It also does not require uniqueness on sectors absent from the source ensemble.

## A branching lemma

Use the subset realization $`H_k(n)=\ker D_n`$ from [Harmonic frames](harmonic_frames.md), and suppose $`n\ge2k+1`$. Write

```math
N=n-1,
\qquad a=n-2k+1\gt 0,
\qquad H_k(n)=T\oplus B,
\qquad T=H_k(N).
```

The second branch is an explicit copy of $`H_{k-1}(N)`$:

```math
\iota(h)=a x_nh-U_Nh,
\qquad B=\iota\bigl(H_{k-1}(N)\bigr).
```

On degree-$`r`$ squarefree polynomials, $`D_NU_N-U_ND_N=(N-2r)I`$. With $`r=k-1`$ and $`D_Nh=0`$, this gives $`D_NU_Nh=a h`$ and makes $`\iota(h)`$ harmonic. Its two parts have disjoint monomial supports, and $`U_Nh`$ is orthogonal to $`H_k(N)`$. Hence

```math
\lVert \iota(h)\rVert ^2=a(a+1)\lVert h\rVert ^2,
```

and these are precisely the two multiplicity-free $`S_N`$ branches.

**Lemma.** Let

```math
W=P_{n,k}\mathrm{diag}(z_A)P_{n,k}.
```

If $`WP_B=0`$, then a scalar $`c`$ exists with

```math
z_A=c\quad(n\notin A),
\qquad
z_{R\cup\{n\}}=-\frac ca\quad(|R|=k-1),
\qquad
W=cP_T.
```

Consequently, a block-diagonal $`W`$ in this frame span whose bottom block is $`bI_B`$ must have a scalar top block too.

**Proof.** Fix an outside set $`A`$ of size $`k`$, choose $`u\in A`$, and put $`R=A\setminus\{u\}`$. There are at least $`k`$ vertices outside $`R\cup\{u,n\}`$. Writing $`R=\{r_1,\ldots,r_{k-1}\}`$, choose distinct such vertices $`b_0,\ldots,b_{k-1}`$ and set

```math
h=\prod_{i=1}^{k-1}(x_{r_i}-x_{b_{i-1}}),
\qquad
h'=\prod_{i=1}^{k-1}(x_{r_i}-x_{b_i}).
```

Their coefficient supports meet only at $`R`$, by the alternating-path argument used for frame independence. Both are harmonic and avoid $`u,n`$. Now take

```math
f=(x_u-x_n)h\in H_k(n),
\qquad
g=a x_nh'-U_Nh'\in B.
```

On a monomial $`x_ux_S`$ from the outside part of $`f`$, the raising coefficient is $`(U_Nh')_{\{u\}\cup S}=h'_S`$, since $`h'`$ does not involve $`u`$. Thus the pointwise product of the coefficient functions of $`f`$ and $`g`$ is supported only on $`A`$ and $`R\cup\{n\}`$, with values $`-1`$ and $`-a`$. It follows that

```math
0=\langle f,Wg\rangle
=-z_A-a z_{R\cup\{n\}}.
```

This relation holds on every incidence edge $`R\subset A`$ between the $`(k-1)`$- and $`k`$-subsets of $`[N]`$. The incidence graph is connected. Its coefficients therefore have the stated two constant values.

For these values, $`W`$ acts as $`c`$ on $`T`$. On $`B`$, its compression vanishes because

```math
\lVert U_Nh\rVert ^2=a\lVert h\rVert ^2,
\qquad
c\lVert U_Nh\rVert ^2-\frac ca\lVert a x_nh\rVert ^2=0.
```

There are no cross terms, either by the two-branch invariance or by orthogonality to $`U_NH_{k-1}(N)`$. Hence $`W=cP_T`$. For the final claim, subtract $`bI_{H_k(n)}`$, which belongs to the frame span by its Parseval identity, and apply the proved statement. At $`k=1`$, use the empty polytabloids $`h=h'=1`$; the same proof applies. ∎

The scalar-bottom-block hypothesis is essential. Arbitrary block diagonality does not suffice; [the five-point counterexample](harmonic_frames.md#appendix-block-diagonality-alone-is-insufficient) gives the exact distinction.

## Induction proving no early order information

Write the twirled prefix effect on its two-row sectors as

```math
\overline E_y
=\bigoplus_i I_{Q_{N,i}}\otimes F_i^y.
```

Tensoring with the last qudit and restricting to global sector $`(n-k,k)`$ gives the multiplicity operator

```math
W_k^y=F_k^y\oplus F_{k-1}^y.
```

This is the ordinary one-box branching rule: the first term corresponds to adding a box in the first row, the second to adding one in the second row. An absent branch is omitted. The same $`F_i^y`$ acts on both its possible global extensions; no representation-dimension factors enter an identity operator under this unitary decomposition.

The joint-support argument also expresses $`W_k^y`$ as a linear combination of the rank-one harmonic frame projectors $`|v_A\rangle\langle v_A|`$. Begin with $`F_0^y`$, which is scalar because $`V_{N,0}`$ has dimension one. Suppose $`F_{k-1}^y`$ is scalar. The branching lemma then makes $`F_k^y`$ scalar. This applies for every

```math
1\le k\le\left\lfloor\frac{n-1}{2}\right\rfloor,
```

because precisely these steps have $`n\ge2k+1`$. If $`n`$ is even, its remaining balanced global sector has only the already-treated lower prefix branch and adds no new induction step. This proves the theorem for every $`d\ge2`$.

For clarity, let a prefix pattern have minority count $`j`$. Its early-outcome probability is explicitly

```math
\Pr(y\mid j,A)
=\frac{\displaystyle\sum_{i=0}^j q_d(N,i)\theta_i^y}
{s_d(N-j)s_d(j)},
\qquad
s_d(t)=\binom{t+d-1}{d-1}.
```

It does not depend on the ordering $`A`$. The right-hand side may depend on $`j`$, so the result allows the surviving cardinality information described in the [free-readout account](free_readout.md).

## Why a shorter prefix has no cluster information

Suppose the instrument acts on $`m\le n-2`$ specimens. Append identities to its effect to regard it as an $`N=n-1`$ prefix effect. The theorem says that its outcome probability depends only on the full prefix's minority count; call it $`p_j(y)`$.

At least one position in that prefix is unmeasured. For any $`j\lt \lfloor N/2\rfloor`$, choose a binary word with $`j`$ ones whose unmeasured position is zero, then change just that position to one. The reduced state of the measured specimens is unchanged, because the two unknown templates retain their same independent Haar prior. The full prefix minority count changes from $`j`$ to $`j+1`$. Therefore

```math
p_j(y)=p_{j+1}(y).
```

All admissible counts are connected in this way. Every outcome has the same probability on every binary cluster pattern. In particular, an early classifier on $`m\ge1`$ specimens cannot beat the blind-guess success $`2^{1-m}`$ while preserving exact optimal final success. The statement concerns only observable pattern information, so it remains valid for qudits without imposing conditions on unused higher-row sectors.

## Relation to earlier work

The optimal unsupervised clustering ensemble and measurement come from Sentís and collaborators' *Unsupervised Classification of Quantum Data* (Phys. Rev. X 9, 041029, 2019). Spencer-Wood, Jeffers, and Croke established the three-qubit measurement-disturbance tradeoff in [Phys. Rev. A 105, 062447 (2022)](https://doi.org/10.1103/PhysRevA.105.062447). Hector Spencer-Wood's 2024 Glasgow thesis developed the arbitrary-$`n`$ no-order conjecture and a constructive lossless prefix readout.

The present proof retains that scientific question while replacing the unproved intermediate implication with the branching lemma above. The all-optimal dual-support argument removes reliance on a preselected final decoder, and the permutation-space proof extends the exact statistical conclusion to every native qudit dimension. Approximate preservation and different loss functions require separate analysis.

Sources: [Sentís et al., 2019](https://doi.org/10.1103/PhysRevX.9.041029); [Spencer-Wood, Jeffers, and Croke, 2022](https://doi.org/10.1103/PhysRevA.105.062447); [Hector Spencer-Wood, *Sequential measurement in quantum learning*, PhD thesis, University of Glasgow, May 2024](https://theses.gla.ac.uk/84375/).
