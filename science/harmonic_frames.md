# Harmonic frames for binary cluster patterns

The optimal clustering measurement uses one spherical line in each two-row Specht module. This page identifies those lines with projected subset vectors and proves that their rank-one projectors are linearly independent. The distinction between a subset and its complement matters only at a balanced partition.

The [model](model.md) fixes the ensemble and the [optimal-measurement account](optimal_measurement.md) identifies the relevant supports. The argument here concerns the permutation multiplicity spaces; it is independent of the physical qudit dimension $`d\ge2`$.

## The subset realization

Let $`M_k(n)`$ have orthonormal basis $`\{e_A: A\subseteq[n],\ |A|=k\}`$. We identify a vector with its homogeneous squarefree polynomial

```math
f(x)=\sum_{|A|=k}f_A x_A,
\qquad x_A=\prod_{a\in A}x_a,
\qquad \langle f,g\rangle=\sum_A\overline{f_A}g_A.
```

The lowering operator and its adjoint are

```math
(D_nf)_R=\sum_{a\notin R}f_{R\cup\{a\}},
\qquad U_n=D_n^*.
```

For $`0\le k\le n/2`$, the harmonic subspace

```math
H_k(n)=\ker D_n
\cong S^{(n-k,k)},
\qquad
f_{n,k}=\dim H_k(n)=\binom nk-\binom n{k-1}
```

is the two-row Specht module. At $`k=0`$, take $`H_0(n)=M_0(n)`$ and $`\binom n{-1}=0`$. Write $`P_{n,k}`$ for its orthogonal projector and define

```math
v_A=P_{n,k}e_A,
\qquad
\|v_A\|^2=\frac{f_{n,k}}{\binom nk}\gt 0.
```

The norm follows because the diagonal entries of the permutation-invariant projector are equal and sum to its rank. The vectors form a Parseval frame:

```math
\sum_{|A|=k}|v_A\rangle\langle v_A|=P_{n,k}.
```

Products of disjoint pair differences give concrete harmonic vectors:

```math
f(x)=\prod_{i=1}^k(x_{a_i}-x_{b_i}),
```

where all $`2k`$ vertices are distinct. Lowering differentiates each pair with total derivative zero, so $`D_nf=0`$. Its coefficient support consists of the transversals choosing one vertex from each pair, with signs determined by the choices. Such vectors are the matching form of two-row polytabloids.

## Why this is the spherical line used by clustering

Fix a cluster pattern whose minority set is $`A`$, with $`|A|=k`$. Its stabilizer is the Young subgroup $`S_A\times S_{A^c}`$. The permutation module

```math
M_k(n)=\mathrm{Ind}_{S_k\times S_{n-k}}^{S_n}\mathbf 1
=\bigoplus_{i=0}^k S^{(n-i,i)}
```

is multiplicity free. Hence the stabilizer-fixed line in $`S^{(n-k,k)}`$ has dimension one. The nonzero vector $`v_A`$ lies on that line: both $`e_A`$ and its harmonic projection are fixed by the stabilizer.

The source state for this pattern is proportional to the product of the symmetric projectors on $`A`$ and $`A^c`$. On its minimal two-row sector $`(n-k,k)`$, its multiplicity support is precisely this stabilizer-fixed line. Consequently the normalized projector occurring in the optimal-measurement support is

```math
\Omega_{n,k,A}
=\frac{|v_A\rangle\langle v_A|}{\|v_A\|^2}.
```

Only this minimal sector is being identified. In a source state of minority count $`j\gt i`$, its spherical vector in sector $`(n-i,i)`$ depends on the source pattern and on $`j`$; it should not be replaced by a vector indexed by an $`i`$-subset without a separate argument.

For $`n\gt 2k`$, the optimal multiplicity-space POVM effect is therefore $`|v_A\rangle\langle v_A|`$. At $`n=2k`$, the physical cluster pattern identifies $`A`$ with $`A^c`$, and the effect is $`2|v_A\rangle\langle v_A|`$ when one representative per pair is retained.

## Independence away from balance

**Theorem 1.** If $`n\ge2k+1`$, the operators $`\{|v_A\rangle\langle v_A|:|A|=k\}`$ are linearly independent over $`\mathbb C`$.

**Proof.** Suppose

```math
W=\sum_A z_A|v_A\rangle\langle v_A|
=P_{n,k}\mathrm{diag}(z_A)P_{n,k}=0.
```

Fix $`A=\{a_1,\ldots,a_k\}`$ and choose distinct vertices $`b_0,\ldots,b_k`$ outside $`A`$. Define

```math
f=\prod_{i=1}^k(x_{a_i}-x_{b_{i-1}}),
\qquad
g=\prod_{i=1}^k(x_{a_i}-x_{b_i}).
```

Both vectors are harmonic. The union of their matching edges is the alternating path

```math
b_0,a_1,b_1,a_2,\ldots,a_k,b_k.
```

A monomial common to their supports must choose exactly one endpoint of each edge. It cannot contain $`b_0`$, which is absent from $`g`$, or $`b_k`$, which is absent from $`f`$. Membership is then forced along the path, leaving only the monomial $`x_A`$. Its coefficient in both polynomials is one. Therefore

```math
0=\langle f,Wg\rangle
=\langle f,\mathrm{diag}(z_A)g\rangle=z_A.
```

The choice of $`A`$ was arbitrary. All coefficients vanish. The case $`k=0`$ consists of one nonzero operator. ∎

## Independence at balance

When $`n=2k`$, complementing a subset acts on $`H_k(2k)`$ as the scalar $`(-1)^k`$. One way to see this is to apply complementation to a matching polytabloid using all $`2k`$ vertices: every pair choice flips, producing $`(-1)^k`$. Complementation commutes with $`S_{2k}`$, and irreducibility gives the same scalar on the whole harmonic space. Thus

```math
v_{A^c}=(-1)^k v_A,
\qquad
|v_{A^c}\rangle\langle v_{A^c}|
=|v_A\rangle\langle v_A|.
```

**Theorem 2.** At $`n=2k`$, choosing one representative of each unordered pair $`\{A,A^c\}`$ gives a linearly independent family of rank-one projectors.

**Proof.** Write a putative relation as $`W=P\mathrm{diag}(z)P=0`$ with complement-even coefficients $`z_A=z_{A^c}`$; divide each representative coefficient equally between its two subsets. Fix a complementary pair, write $`A=\{a_1,\ldots,a_k\}`$ and $`A^c=\{b_1,\ldots,b_k\}`$, and take

```math
f=\prod_{i=1}^k(x_{a_i}-x_{b_i}),
\qquad
g=\prod_{i=1}^k(x_{a_i}-x_{b_{i+1}}),
\qquad b_{k+1}=b_1.
```

The union of the two matchings is an alternating cycle. Its only common transversals are $`A`$ and $`A^c`$. At each, the product of the two coefficients is one. The same statement holds for $`k=1`$, where the matchings coincide. Hence

```math
0=\langle f,Wg\rangle=z_A+z_{A^c}=2z_A.
```

Every complementary pair has zero coefficient. ∎

These theorems also show that no further identifications of orbit projectors occur. A matrix-valued relation $`\sum_A D_A\otimes\Omega_{n,k,A}=I_Q\otimes X`$ may be read one matrix element at a time. Independence forces every $`D_A`$ to be scalar on $`Q`$. This statement applies on the source-supported two-row sectors; it places no condition on Hilbert-space sectors absent from the ensemble.

## Appendix: block diagonality alone is insufficient

Hector Spencer-Wood's thesis, *Sequential measurement in quantum learning* (University of Glasgow, 2024), Chapter 4 and Conjecture 4.A.1, investigates the same no-order question for qubits. A proposed intermediate implication there would make outside-orbit weights constant from block diagonality alone. The following example shows why the additional scalar-bottom-block hypothesis in the [temporal-rigidity proof](temporal_rigidity.md) is needed.

Take $`n=5,k=2`$. In $`H_2(5)`$, let $`B`$ be the span of $`\{v_{i5}:1\le i\le4\}`$ and $`T=B^\perp`$. These are the $`S_4`$ branches of dimensions three and two. Put

```math
W=|v_{12}\rangle\langle v_{12}|
+|v_{34}\rangle\langle v_{34}|.
```

The outside coefficients are positive and unequal, yet $`P_TWP_B=0`$. Its top and bottom blocks each have rank one, with nonzero eigenvalues $`2/3`$ and $`1/3`$, respectively. Both blocks are nonscalar. Rescaling to normalized spherical projectors multiplies these eigenvalues by two and preserves the example.

An exact construction is $`P=I-D_5^*(D_5D_5^*)^{-1}D_5`$ on the ten-dimensional two-subset module, followed by the displayed definitions. Alternatively, in the $`n=2k+1`$ branching, complementary outside subsets have top components differing by $`(-1)^k`$ and bottom components differing by $`(-1)^{k-1}`$. Their offdiagonal terms cancel in a pair sum. This explains the five-point example directly.

The example does not contradict temporal rigidity: its bottom block is nonscalar. The new branching lemma uses the scalar block already established at the preceding induction step and avoids this stronger, unnecessary intermediate implication.

Source: [Hector Spencer-Wood, *Sequential measurement in quantum learning*, PhD thesis, University of Glasgow, May 2024](https://theses.gla.ac.uk/84375/).
