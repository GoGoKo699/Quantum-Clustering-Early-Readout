# Source model and the meaning of an early readout

The task is to cluster an ordered array of quantum systems into two groups. An early classical record is useful if it says something about the clustering before the final systems arrive. The constraint studied here is exact: after producing that record, the apparatus must still attain the Bayes-optimal probability of identifying the complete final partition.

The global clustering problem and its optimal measurement are inherited from [Sentís et al., *Physical Review X* **9**, 041029 (2019)](https://doi.org/10.1103/PhysRevX.9.041029). This project characterizes which early records are compatible with that optimum. The distinction between exact whole-partition success and a per-system error rate is essential throughout.

## 1. Random states, random labels, and the success criterion

Fix a local dimension $`d\ge 2`$ and a final array length $`n\ge 2`$. Draw two pure states $`|\phi_0\rangle,|\phi_1\rangle\in\mathbb C^d`$ independently from Haar measure. Independently draw a binary string $`x\in\{0,1\}^n`$ uniformly. Conditional on these variables, the input is

```math
|\Phi_x\rangle=\bigotimes_{t=1}^n|\phi_{x_t}\rangle.
```

The two state preparations are unknown. There are no labeled training systems, state descriptions, extra copies, or preparation oracles. The array positions are known. A protocol may use arbitrary ancillary systems, quantum instruments on the available systems, retained quantum memory, and a final measurement after all systems arrive.

Exchanging the names 0 and 1 does not change a clustering. Write $`[x]=\{x,\bar x\}`$ for an unordered binary partition, including the partition with one empty group. There are $`2^{n-1}`$ hypotheses and each has prior

```math
p_n=2^{1-n}.
```

A final answer succeeds exactly when it equals $`[x]`$. The Bayes success probability averages over the string and the two Haar-random states. It does not require a correct answer for every fixed pair of preparations. It is also not a claim about Hamming loss, individual label accuracy, mutual information about the pure-state directions, or a different prior.

## 2. Averaged hypotheses and the balanced factor

For a set $`A\subseteq[n]`$, let $`P_{\mathrm{sym},A}`$ be the projector onto the symmetric subspace of its systems, extended by the identity on the other systems. Use

```math
s_d(t)=\binom{d+t-1}{t},\qquad s_d(0)=1.
```

Choose the smaller cluster as $`A`$, set $`j=|A|\le\lfloor n/2\rfloor`$, and identify $`A`$ with $`A^c`$ if $`2j=n`$. Haar integration gives the averaged density operator

**Equation (1).**

```math
\rho_{n;j,A}
=\frac{P_{\mathrm{sym},A}P_{\mathrm{sym},A^c}}
       {s_d(j)s_d(n-j)}.
```

Both projectors commute because their nontrivial factors are on disjoint systems. The number of distinct hypotheses of minority size $`j`$ is

**Equation (2).**

```math
C_{n,j}=
\begin{cases}
\binom nj,&2j\lt n,\\[2mm]
\frac12\binom nj,&2j=n.
\end{cases}
\qquad
\sum_{j=0}^{\lfloor n/2\rfloor}C_{n,j}=2^{n-1}.
```

The factor one half belongs in the *number of hypotheses*. It does not change the normalization of the density operator in (1) or its prior $`p_n`$. A different factor of two appears in the balanced optimal POVM, explained in [the optimal measurement](optimal_measurement.md).

## 3. The occupied Schur sectors

Under Schur–Weyl duality,

```math
(\mathbb C^d)^{\otimes n}
\cong\bigoplus_{\lambda\vdash n,\,\ell(\lambda)\le d}
Q_\lambda^{(d)}\otimes V_\lambda.
```

The $`U(d)`$ action is on $`Q_\lambda^{(d)}`$, and permutations act on the Specht space $`V_\lambda`$. Write $`Q_{n,k}^{(d)}`$ and $`V_{n,k}`$ for the two-row partition $`(n-k,k)`$. Their dimensions are

**Equation (3).**

```math
f_{n,k}=\dim V_{n,k}=\binom nk-\binom n{k-1},
```

**Equation (4).**

```math
q_d(n,k)=\dim Q_{n,k}^{(d)}
=s_d(n-k)s_d(k)-s_d(n-k+1)s_d(k-1),
```

with $`\binom n{-1}=s_d(-1)=0`$. In particular, $`q_2(n,k)=n-2k+1`$.

The product of two symmetric representations is multiplicity free:

**Equation (5).**

```math
\mathrm{Sym}^{n-j}(\mathbb C^d)
\otimes\mathrm{Sym}^{j}(\mathbb C^d)
\cong\bigoplus_{k=0}^{j}Q_{n,k}^{(d)}.
```

Consequently (1) has the decomposition

**Equation (6).**

```math
\rho_{n;j,A}
=c_{n,j}\bigoplus_{k=0}^{j}
I_{Q_{n,k}^{(d)}}\otimes\Omega_{n;k\mid j,A},
\qquad
c_{n,j}=\frac1{s_d(n-j)s_d(j)}.
```

Each $`\Omega_{n;k\mid j,A}`$ is a normalized rank-one projector in $`V_{n,k}`$. The vector in a lower sector $`k\lt j`$ can depend on the source count $`j`$ as well as on $`A`$; these projectors must not be identified with the minimal-sector frame at count $`k`$.

Only two-row sectors occur. Let

```math
\mathcal S_n=
\bigoplus_{k=0}^{\lfloor n/2\rfloor}
Q_{n,k}^{(d)}\otimes V_{n,k}
```

denote their direct sum. The ensemble's total support is $`\mathcal S_n`$. For qubits this is the whole Hilbert space. For $`d\gt 2`$, sectors with three or more rows are unoccupied. Restrictions on an effect's action on $`\mathcal S_n`$ do not constrain arbitrary behavior on source-null sectors.

The same convention applies to a prefix of length $`m`$: its occupied support is $`\mathcal S_m`$. All assertions about early information concern the probabilities of the specified source ensemble.

## 4. An early record and an optimal continuation

Suppose the first $`m\lt n`$ systems have arrived. An arbitrary instrument on them produces a classical record $`a`$ and a residual quantum system. Its POVM effects are $`F_a`$, with $`F_a\ge0`$ and $`\sum_aF_a=I`$. After the remaining systems arrive, a measurement conditional on $`a`$ returns a final partition $`\hat x`$.

The entire two-stage procedure defines a joint POVM $`B_{a,\hat x}`$ on all $`n`$ input systems. It obeys

**Equation (7).**

```math
B_{a,\hat x}\ge0,\qquad
\sum_{\hat x}B_{a,\hat x}=F_a\otimes I_{d^{n-m}},
\qquad
\sum_{a,\hat x}B_{a,\hat x}=I.
```

The early readout is **free for final clustering** if some continuation satisfies

**Equation (8).**

```math
\sum_{[x]}p_n\sum_a
\mathrm{tr}\!\left(B_{a,[x]}\rho_{n;[x]}\right)
=P_{\mathrm{opt},d}(n),
```

where the right side is the unconstrained optimal final success. “Free” refers to the exact operational equality (8), not to a nondisturbing state transformation.

Condition (7) is also sufficient for a local physical realization: one can first apply the Lüders instrument of $`F_a`$ to the prefix and then perform an appropriate conditional final POVM. The constructive argument appears in [optimal measurement, Section 5](optimal_measurement.md#5-joint-povms-and-local-lüders-instruments). Thus the joint-POVM formulation does not grant access to future systems at the early stage.

## 5. Twirling preserves the early likelihoods

The source operators commute with a common $`U(d)`$ rotation. Define the prefix twirl

**Equation (9).**

```math
\overline F_a=
\int_{U(d)}U^{\otimes m}F_a(U^\dagger)^{\otimes m}\,dU.
```

For every prefix partition $`[y]`$,

**Equation (10).**

```math
\mathrm{tr}(F_a\rho_{m;[y]})
=\mathrm{tr}(\overline F_a\rho_{m;[y]}).
```

The same identity holds for the prefix marginal of any full hypothesis. Twirling the *whole joint POVM* by the common rotation preserves (7), all joint source probabilities, and the final success in (8). Its early marginal becomes $`\overline F_a\otimes I`$.

On occupied sectors,

**Equation (11).**

```math
\overline F_a\big|_{\mathcal S_m}
=\bigoplus_{k=0}^{\lfloor m/2\rfloor}
I_{Q_{m,k}^{(d)}}\otimes E_{a,k}.
```

The temporal rigidity theorem proves that when $`m=n-1`$ and (8) holds, every $`E_{a,k}`$ is scalar. This makes the likelihood in (10) invariant under all reorderings of a prefix with fixed cluster sizes. When $`m\le n-2`$, the likelihood is independent of the complete partition. These are statements about any physical early record through its source probabilities; an untwirled effect can still have unobservable components.

Continue with [the inherited optimum and equality conditions](optimal_measurement.md), then [the harmonic frame](harmonic_frames.md), [temporal rigidity](temporal_rigidity.md), and [the complete free-readout family](free_readout.md).
