# Exact accuracy before the final specimen

The [canonical free readout](free_readout.md) maximizes every classical decision score on the prefix labels. Here the score is exact recovery of the entire prefix partition, modulo exchanging the two template names. The final clustering success is required to remain exactly optimal.

## 1. Exact success in every local dimension

Let

```math
m=n-1,\qquad r=\lfloor m/2\rfloor,\qquad
p_m=2^{1-m}=2^{2-n},\qquad
T_{m,k}=s_d(m-k)s_d(k),
\tag{1}
```

and use $`B_j,w_l`$ from [free readout, Eq. (5)](free_readout.md#2-a-canonical-maximal-experiment). Define

```math
S_{d,l}=\sum_{j=0}^l q_d(m,j)B_j.
\tag{2}
```

**Exact early-accuracy theorem.** The largest prefix clustering success compatible with optimal final clustering is

```math
P_{\mathrm{free},d}(n)
=2^{2-n}\sum_{l=0}^r
w_l\frac{S_{d,l}}{T_{m,l}}.
\tag{3}
```

On canonical outcome $`l`$, guess any one prefix partition of minority size $`l`$. The ordering representative is arbitrary because all such hypotheses have the same likelihood.

To prove the decision rule, a candidate of minority size $`k`$ has prior-weighted likelihood

```math
p_m w_l\frac{S_{d,\min\{k,l\}}}{T_{m,k}}.
\tag{4}
```

The quantity $`T_{m,k}`$ increases for $`k\le r`$, so among $`k\ge l`$ the best choice is $`k=l`$. For $`k<l`$, use the multiplicity-free dimension identity

```math
\sum_{j=0}^{k-1}q_d(m,j)=T_{m,k-1},\qquad
q_d(m,k)=T_{m,k}-T_{m,k-1}.
\tag{5}
```

Since $`B_j\le B_k`$ for $`j<k`$, one has $`S_{d,k-1}\le B_kT_{m,k-1}`$. Consequently

```math
\frac{S_{d,k}}{T_{m,k}}
-\frac{S_{d,k-1}}{T_{m,k-1}}
=\frac{q_d(m,k)}{T_{m,k}}
\left(B_k-\frac{S_{d,k-1}}{T_{m,k-1}}\right)
\ge0.
\tag{6}
```

Thus $`k=l`$ is optimal among all hypotheses. The statistical maximality of the canonical readout proves that no other exactly free instrument can do better, yielding (3).

For qubits, $`q_2(m,j)=n-2j`$, and the first values are

| Final length $`n`$ | Prefix length | Exact free prefix success |
|---:|---:|---:|
| 3 | 2 | $`7/12`$ |
| 4 | 3 | $`5/16`$ |
| 5 | 4 | $`47/270`$ |
| 6 | 5 | $`71/768`$ |

The first three values reproduce the improved construction in Spencer-Wood's thesis. Equation (3) establishes the optimum for every $`n`$ and $`d\ge2`$ rather than interpreting those values as lower bounds.

## 2. Comparison with an unrestricted count-only readout

If preserving final clustering is not required, a sharp measurement of the prefix Schur sector is the most informative central measurement. Its best exact-partition guessing score is

```math
U_d(n)=p_m\sum_{j=0}^r\frac{q_d(m,j)}{T_{m,j}}.
\tag{7}
```

The ratio is explicitly

```math
\frac{q_d(m,j)}{T_{m,j}}
=\frac{(d-1)(n-2j)}{(n-j)(j+d-1)}.
\tag{8}
```

Writing $`H_t=\sum_{a=1}^t1/a`$ and $`H_0=0`$, its exact sum is

```math
\frac{U_d(n)}{p_m}
=(d-1)\left[
\frac{n+2d-2}{n+d-1}
\left(H_{r+d-1}-H_{d-2}\right)
-\frac{n}{n+d-1}
\left(H_n-H_{n-r-1}\right)
\right].
\tag{9}
```

In particular, for qubits the two prefactors are $`(n+2)/(n+1)`$ and $`n/(n+1)`$. Replacing both by one would give an incorrect finite-size identity.

The canonical free score is close to this central ceiling in an explicit additive sense:

```math
0\le U_d(n)-P_{\mathrm{free},d}(n)
\le p_m(d-1)\sum_{j=0}^{r-1}
\frac1{(n-j)(j+d-1)}.
\tag{10}
```

For the proof, swap the sums in (3) and use $`\sum_{l\ge j}w_l=B_j^{-1}`$. The difference from (7), divided by $`p_m`$, is

```math
\sum_{j=0}^r q_d(m,j)B_j
\sum_{l>j}w_l\left(\frac1{T_{m,j}}-\frac1{T_{m,l}}\right).
```

It is nonnegative. Bound the parenthesis by $`1/T_{m,j}`$ and use $`\sum_{l>j}w_l=1/B_{j+1}`$. Since $`B_{j+1}/B_j=n-2j`$, (8) gives (10).

## 3. The fixed-dimension asymptotic

Hold the native local dimension $`d\ge2`$ fixed and let $`n\to\infty`$. Equations (9) and (10) give

```math
P_{\mathrm{free},d}(n)
=2^{2-n}(d-1)
\left[
\log n+\gamma-H_{d-2}-\log4
+O_d\!\left(\frac{\log n}{n}\right)
\right],
\tag{11}
```

where logarithms are natural and $`\gamma`$ is Euler's constant. In particular,

```math
P_{\mathrm{free},d}(n)=\Theta_d(2^{-n}\log n).
\tag{12}
```

This is a fixed-$`d`$ limit. No uniform estimate in a growing local dimension is asserted.

The distinction from the inherited final optimum is substantial: for fixed $`d`$, Sentís et al.'s full-array success has asymptotic $`8(d-1)/n^2`$, whereas exact free prefix recovery has the exponential form (11). An almost complete prefix can release a cardinality statistic, but exactly preserving the final joint decoder prevents it from identifying the prefix's positional partition with polynomial success. Both scores concern recovery of an entire partition; this comparison does not describe per-system accuracy.

The result does not say that a small allowed loss in final success permits only exponentially small early recovery. The [stability account](stability.md) separates the proved finite-size quantitative statement from that unresolved scaling question.

## Attribution

The global ensemble, Schur decomposition, and final optimum are inherited from [Sentís et al., *Unsupervised Classification of Quantum Data* (2019)](https://doi.org/10.1103/PhysRevX.9.041029). The early strategy and low-$`n`$ qubit values appeared as a proposed improved lower bound in [Spencer-Wood's thesis (2024)](https://theses.gla.ac.uk/84375/), Section 4.4. The contribution here is its complete compatibility proof, statistical maximality, exact optimum in every local dimension, and the resulting fixed-dimension early-recovery law.
