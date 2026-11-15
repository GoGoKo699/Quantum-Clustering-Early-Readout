# The global optimum and what equality forces

The unconstrained binary clustering measurement is inherited from [Sentís et al., *Unsupervised Classification of Quantum Data*, *Physical Review X* **9**, 041029 (2019)](https://doi.org/10.1103/PhysRevX.9.041029), [arXiv:1903.01391v3](https://arxiv.org/abs/1903.01391v3). This page reconstructs its exact Bayes optimum and extracts the support condition needed for arbitrary early instruments. The additional temporal conclusions are developed in [temporal rigidity](temporal_rigidity.md).

Notation and the source prior are fixed in [the model](model.md). In particular, $`p_n=2^{1-n}`$, $`c_{n,j}=[s_d(n-j)s_d(j)]^{-1}`$, and $`\mathcal S_n`$ is the occupied two-row support.

## 1. Minimal-sector frames and the balanced normalization

Identify the Specht space $`V_{n,k}`$ with the harmonic subspace $`H_k^n`$ of the real vector space on $`k`$-subsets of $`[n]`$. Let $`P_{H_k^n}`$ be its orthogonal projector and define

```math
v_A=P_{H_k^n}|A\rangle,
\qquad
h_{n,k}=\|v_A\|^2=\frac{f_{n,k}}{\binom nk},
\qquad
\Omega_{n;k\mid k,A}=\frac{|v_A\rangle\langle v_A|}{h_{n,k}}.
\tag{1}
```

The norm is independent of $`A`$ by permutation symmetry. Summing over all subsets of size $`k`$ gives

```math
\sum_{|A|=k}|v_A\rangle\langle v_A|=I_{V_{n,k}}.
\tag{2}
```

If $`n=2k`$, complement acts on this harmonic space as $`(-1)^k`$, so $`v_{A^c}=(-1)^kv_A`$. Summing one representative from each complement class gives half the identity. The optimal POVM element for hypothesis $`(k,A)`$ is therefore

```math
M_{k,A}=
\begin{cases}
I_{Q_{n,k}^{(d)}}\otimes|v_A\rangle\langle v_A|,&2k<n,\\[1mm]
2I_{Q_{n,k}^{(d)}}\otimes|v_A\rangle\langle v_A|,&2k=n,
\end{cases}
\tag{3}
```

or, uniformly,

```math
M_{k,A}=\frac{f_{n,k}}{C_{n,k}}
I_{Q_{n,k}^{(d)}}\otimes\Omega_{n;k\mid k,A}.
\tag{4}
```

Each effect is zero in other Schur sectors. Equations (2)–(4) show that the effects sum to the identity on $`\mathcal S_n`$. Extend them arbitrarily to a POVM on $`\mathcal S_n^\perp`$; that extension has no source probability.

The same normalization must be used for a prefix of any length $`m`$: a balanced prefix has $`C_{m,m/2}=\frac12\binom m{m/2}`$ distinct patterns and the corresponding frame POVM uses the factor two in (3).

## 2. An explicit optimal dual

On $`\mathcal S_n`$, set

```math
\Gamma_n=p_n\bigoplus_{i=0}^{\lfloor n/2\rfloor}
c_{n,i} I_{Q_{n,i}^{(d)}}\otimes I_{V_{n,i}}.
\tag{5}
```

Set it to zero on source-null sectors. The coefficients strictly decrease with $`i`$. For $`1\le j\le\lfloor n/2\rfloor`$,

```math
\frac{c_{n,j}}{c_{n,j-1}}
=\frac{j(n-j+d)}{(n-j+1)(j+d-1)}<1,
\tag{6}
```

```math
1-\frac{c_{n,j}}{c_{n,j-1}}
=\frac{(d-1)(n-2j+1)}{(n-j+1)(j+d-1)}>0.
\tag{7}
```

For hypothesis $`(j,A)`$, its dual slack is

```math
\Gamma_n-p_n\rho_{n;j,A}
=p_n\!\left[
\bigoplus_{i=0}^{j}
I_{Q_{n,i}^{(d)}}\otimes
\big(c_{n,i}I-c_{n,j}\Omega_{n;i\mid j,A}\big)
\ \oplus\!
\bigoplus_{i=j+1}^{\lfloor n/2\rfloor}
c_{n,i}I
\right].
\tag{8}
```

For $`i<j`$, the two eigenvalues of the multiplicity-space part are $`c_{n,i}-c_{n,j}>0`$ on the rank-one spherical direction and $`c_{n,i}>0`$ on its orthogonal complement. For $`i=j`$, the kernel is the spherical direction and the other eigenvalue is $`c_{n,j}>0`$. All blocks $`i>j`$ are positive definite. Thus (8) is positive semidefinite.

The POVM (3) saturates this dual. Its success and the dual trace are

```math
P_{\mathrm{opt},d}(n)
=\operatorname{tr}\Gamma_n
=p_n\sum_{k=0}^{\lfloor n/2\rfloor}
c_{n,k}\,q_d(n,k)\,f_{n,k}.
\tag{9}
```

This proves the inherited optimum directly under the stated prior. For qubits it becomes

```math
P_{\mathrm{opt},2}(n)
=2^{1-n}\sum_{k=0}^{\lfloor n/2\rfloor}
\binom nk\frac{(n-2k+1)^2}{(n-k+1)^2(k+1)}.
\tag{10}
```

In particular, $`P_{\mathrm{opt},2}(2)=5/8`$ and $`P_{\mathrm{opt},2}(3)=5/12`$.

## 3. Equality constrains every optimal continuation

Let $`N_{j,A}`$ be any final POVM attaining (9). Its gap from the dual is

```math
0=\operatorname{tr}\Gamma_n-
\sum_{j,A}p_n\operatorname{tr}(N_{j,A}\rho_{n;j,A})
=\sum_{j,A}\operatorname{tr}\!\left[
(\Gamma_n-p_n\rho_{n;j,A})N_{j,A}\right].
\tag{11}
```

Every summand is nonnegative. For positive operators $`S,N`$, $`\operatorname{tr}(SN)=0`$ implies that the range of $`N`$ lies in the kernel of $`S`$. Applied to (8), this gives

```math
\operatorname{supp}\!\left(
P_{\mathcal S_n}N_{j,A}P_{\mathcal S_n}\right)
\subseteq Q_{n,j}^{(d)}\otimes\operatorname{span}\{v_A\}.
\tag{12}
```

Suppose an early record $`a`$ and final partition $`(j,A)`$ are represented by joint effects $`B_{a;j,A}`$. If the final success is optimal, (11) can be summed over the joint effects themselves. Therefore **every joint effect** obeys the same support condition (12).

This argument does not assume that a chosen covariant POVM is the only optimum. It allows arbitrary early ancillas, arbitrary instruments, and a final measurement depending on the early record. After the common $`U(d)`$ twirl, its occupied compression has the form

```math
P_{\mathcal S_n}\overline B_{a;j,A}P_{\mathcal S_n}
=b_{a;j,A}
I_{Q_{n,j}^{(d)}}\otimes|v_A\rangle\langle v_A|,
\qquad b_{a;j,A}\ge0.
\tag{13}
```

The coefficient in (13) uses the unnormalized $`v_A`$ from (1). Completeness gives $`\sum_a b_{a;j,A}=1`$ for $`2j<n`$ and $`\sum_a b_{a;j,A}=2`$ for $`2j=n`$, once the [frame-independence theorem](harmonic_frames.md) is applied. Equivalently, when joint effects are written as coefficients multiplying the optimal effect $`M_{j,A}`$ in (3), those coefficients sum to one in both cases.

Frame independence also fixes the compression of a final optimal POVM on the occupied support. It does not fix its action on source-null sectors or rule out physically different implementations. None of the temporal conclusions requires a stronger physical uniqueness assertion.

For reference, an explicit positive lower bound on every nonzero eigenvalue of (8), within the occupied support, is

```math
g_{n,d}=p_n\min\!\left\{
c_{n,r},\ \min_{1\le j\le r}(c_{n,j-1}-c_{n,j})
\right\}>0,
\qquad r=\lfloor n/2\rfloor.
\tag{14}
```

Equation (7) gives the adjacent differences exactly. The exact temporal theorem uses only their strict positivity. Formula (14) by itself is not an optimal approximate-disturbance bound.

## 4. From equality to temporal rigidity

For a penultimate readout, $`m=n-1`$. The early marginal of (13) must equal $`\overline F_a\otimes I_d`$ on occupied sectors. Restriction from $`S_n`$ to $`S_{n-1}`$ couples two neighboring prefix Specht modules. The [harmonic branching lemma](temporal_rigidity.md#a-branching-lemma) shows that this marginal constraint makes every multiplicity-space block $`E_{a,k}`$ in model equation (11) scalar.

The result is a statement about record likelihoods: a free penultimate record can reveal cluster-size information, but cannot distinguish reorderings of a prefix with the same cluster sizes. The [temporal theorem](temporal_rigidity.md) proves that a record produced at least two systems before the end is independent of the entire partition. The [free-readout characterization](free_readout.md) supplies the complete allowed scalar family and its optimal early clustering probability.

## 5. Joint POVMs and local Lüders instruments

The joint-POVM condition is exactly the correct causal condition for one early measurement followed by a final conditional measurement. To see the nontrivial direction, take any full physical joint POVM satisfying

```math
\sum_x B_{a,x}=F_a\otimes I_{d^{n-m}}.
```

Write $`L_a=\sqrt{F_a}\otimes I`$ and let $`L_a^+`$ be its Moore–Penrose inverse. Since $`0\le B_{a,x}\le L_a^2`$, each $`B_{a,x}`$ is supported on the range of $`L_a`$. On that range define

```math
C_{x\mid a}=L_a^+ B_{a,x}L_a^+.
\tag{15}
```

These are positive and sum to the range projector. Add any POVM on its orthogonal complement, whose state probability after outcome $`a`$ is zero. They are now a full conditional POVM and satisfy

```math
L_a C_{x\mid a}L_a=B_{a,x}.
\tag{16}
```

First apply the prefix Lüders instrument $`T\mapsto\sqrt{F_a}T\sqrt{F_a}`$, retaining the postmeasurement prefix. After the remaining systems arrive, measure $`\{C_{x\mid a}\}_x`$. Equation (16) reproduces the desired joint statistics. Conversely, any early instrument followed by a conditional final measurement induces a joint POVM with the stated marginal.

When a construction has first been specified only on $`\mathcal S_n`$, extend it to a physical POVM before using (15). For the twirled scalar effects used here, $`F_a\otimes I`$ is block diagonal in the global $`U(d)`$ sectors. On source-null sectors one may allocate its positive marginal among final outcomes arbitrarily. This supplies the extension without altering any source statistic or any of the compatibility inequalities.
