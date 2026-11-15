# What near-optimal final success guarantees

The main temporal result assumes exact preservation of optimal final clustering. This page gives a finite-size stability bound with explicit, computable conditioning parameters. It also records a three-qubit quantitative example. It does not establish a useful uniform-in-$`n`$ approximate-regret law.

## 1. Weighted leakage from the optimal supports

Use the [model](model.md), restrict all full-array operators to the occupied support $`\mathcal S_n`$, and write

**Equation (1).**

```math
D=\dim\mathcal S_n,\qquad
\Gamma=p_n\bigoplus_{k=0}^{\lfloor n/2\rfloor}
c_{n,k}I_{Q_{n,k}^{(d)}}\otimes I_{V_{n,k}}.
```

This is the full-rank dual operator on that support, with $`\mathrm{tr}\Gamma=P_{\mathrm{opt},d}(n)`$. It is zero on unoccupied sectors when considered on the entire tensor-product Hilbert space, so inverses and norms below are always taken on $`\mathcal S_n`$.

For a label $`x`$, let $`P_x`$ be the kernel projector of $`\Gamma-p_n\rho_x`$. The [optimal-measurement equality conditions](optimal_measurement.md) identify it as its minimal-sector spherical support. Define the positive relative slack

**Equation (2).**

```math
\alpha_{n,d}=
\min_{1\le j\le\lfloor n/2\rfloor}
\frac{(d-1)(n-2j+1)}{(n-j+1)(j+d-1)}.
```

The coefficients $`c_{n,j}`$ strictly decrease with $`j`$. Therefore the smallest relative difference between any two of them is attained between adjacent coefficients, and

**Equation (3).**

```math
\Gamma-p_n\rho_x
\succeq\alpha_{n,d}\,\Gamma(I-P_x).
```

Here $`\Gamma`$ commutes with $`P_x`$. For qubits, (2) is $`(n-2r'+1)/[(n-r'+1)(r'+1)]`$ with $`r'=\lfloor n/2\rfloor`$, and it is of order $`n^{-2}`$.

Consider any early instrument and continuation with joint effects $`B_{y,x}`$ and final deficit

**Equation (4).**

```math
\eta=P_{\mathrm{opt},d}(n)
-\sum_{y,x}p_n\mathrm{tr}(B_{y,x}\rho_x)\ge0.
```

Summing (3) against those effects gives

**Equation (5).**

```math
\sum_{y,x}\mathrm{tr}\!\left(
\Gamma(I-P_x)B_{y,x}\right)
\le\frac\eta{\alpha_{n,d}}.
```

Set $`\mathcal G(H)=\Gamma^{1/2}H\Gamma^{1/2}`$. For a positive operator $`B`$ and projector $`P`$ commuting with $`\Gamma`$, the Schatten Cauchy–Schwarz inequality gives

```math
\lVert \mathcal G(B-PBP)\rVert _1
\le2\sqrt{
\mathrm{tr}(\Gamma B)
\mathrm{tr}(\Gamma(I-P)B)}.
```

For example, apply $`\lVert XY\rVert _1\le\lVert X\rVert _2\lVert Y\rVert _2`$ to the two terms in $`C-PCP=(I-P)C+PC(I-P)`$, with $`C=\mathcal G(B)`$. A second Cauchy–Schwarz inequality over the joint outcomes, together with $`\sum_{y,x}\mathrm{tr}(\Gamma B_{y,x})=P_{\mathrm{opt},d}(n)`$, proves

**Equation (6).**

```math
\sum_{y,x}
\lVert \mathcal G(B_{y,x}-P_xB_{y,x}P_x)\rVert _1
\le2\sqrt{
\frac{P_{\mathrm{opt},d}(n)\eta}{\alpha_{n,d}}}.
```

This weighted estimate avoids substituting a dimension-dependent unweighted dual gap at this step.

## 2. A finite conditioning singular value

The conversion from supported refinements to prefix order information has its own conditioning cost. The following definition specifies it rather than assuming a favorable dependence on system size.

Let $`\mathcal A`$ be the real vector space of operators obtained by compressing $`F\otimes I_d`$ to $`\mathcal S_n`$, where $`F`$ is a Hermitian, common-$`U(d)`$-invariant operator on $`\mathcal S_{n-1}`$. Let

**Equation (7).**

```math
\mathcal B=
\bigoplus_k I_{Q_{n,k}^{(d)}}\otimes
\mathrm{span}_{\mathbb R}
\{|v_A\rangle\langle v_A|:|A|=k\}.
```

Retain one representative per complementary pair at balance. The [temporal branching theorem](temporal_rigidity.md) is precisely the linear-space identity

**Equation (8).**

```math
\mathcal C:=\mathcal A\cap\mathcal B
=\{\text{compressed central prefix operators}\}.
```

The induction proving (8) does not need positivity: it uses a scalar lowest prefix block and the linear branching lemma. This is why it applies to the spaces in (7).

Equip Hermitian operators with the Hilbert–Schmidt inner product. Write $`\widetilde{\mathcal A}=\mathcal G(\mathcal A)`$, and similarly for $`\widetilde{\mathcal B},\widetilde{\mathcal C}`$. If $`\widetilde{\mathcal A}\ominus\widetilde{\mathcal C}`$ is nonzero, define

**Equation (9).**

```math
\sigma_{n,d}=
\min_{\substack{X\in\widetilde{\mathcal A}\ominus
\widetilde{\mathcal C}\\\lVert X\rVert _2=1}}
\lVert (I-\Pi_{\widetilde{\mathcal B}})X\rVert _2.
```

If that space is zero, set $`\sigma_{n,d}=1`$. This number is strictly positive: the unit sphere is compact, and a zero would give a nonzero vector in $`\widetilde{\mathcal A}\cap\widetilde{\mathcal B}`$ orthogonal to $`\widetilde{\mathcal C}`$, contrary to (8) and the invertibility of $`\mathcal G`$.

It is a finite computable singular value. Construct orthonormal matrix-coordinate bases for the spaces in (7), apply $`\mathcal G`$, and let $`Q`$ have orthonormal columns spanning $`\widetilde{\mathcal A}\ominus\widetilde{\mathcal C}`$. Then $`\sigma_{n,d}`$ is the least singular value of $`(I-\Pi_{\widetilde{\mathcal B}})Q`$. Exact matrix constructions can certify positivity; a floating-point near-zero singular value alone is not such a certificate.

## 3. An operational finite-size bound

Let $`\mathcal T`$ average an early effect under prefix permutations, after the common-$`U(d)`$ twirl. On the prefix invariant algebra it is the projection onto central operators. Since $`\Gamma`$ commutes with every prefix permutation, it is also the Hilbert–Schmidt orthogonal projection from $`\widetilde{\mathcal A}`$ to $`\widetilde{\mathcal C}`$ after applying $`\mathcal G`$.

Twirling the joint effects preserves the deficit and early label statistics. Their pinched marginal $`C_y=\sum_xP_xB_{y,x}P_x`$ belongs to $`\mathcal B`$. Thus (9), (6), and $`\lVert H\rVert _1\le\sqrt D\lVert H\rVert _2`$ give

**Equation (10).**

```math
\sum_y\lVert \mathcal G(F_y\otimes I_d
-(\mathcal T F_y)\otimes I_d)\rVert _1
\le
\frac{2\sqrt D}{\sigma_{n,d}}
\sqrt{\frac{P_{\mathrm{opt},d}(n)\eta}{\alpha_{n,d}}}.
```

All operators in (10) are compressed to the occupied global support. The matrix norms, dimension factor, and singular value are explicit; no norm equivalence is suppressed.

For a concrete decision consequence, let the early record be decoded as a guess of the full prefix partition. The prior-weighted score operator for a guessed prefix label $`a`$ can be represented on $`\mathcal S_n`$ as

**Equation (11).**

```math
V_a=p_n(\rho_{a0}+\rho_{a1})\preceq2\Gamma.
```

Both extensions have prefix marginal $`\rho_{n-1;a}`$, so $`\mathrm{tr}[(F\otimes I_d)V_a]=p_{n-1}\mathrm{tr}(F\rho_{n-1;a})`$. Applying (10) to this score yields

**Equation (12).**

```math
|P_{\mathrm{early}}(F)-P_{\mathrm{early}}(\mathcal T F)|
\le
\frac{4\sqrt D}{\sigma_{n,d}}
\sqrt{\frac{P_{\mathrm{opt},d}(n)\eta}{\alpha_{n,d}}}.
```

The bound holds for any decoding of the record and therefore also for the difference of the two optimally decoded scores: apply the same estimate to each decoding before taking a maximum. The twirled measurement $`\mathcal T F`$ is a valid central POVM, so its score is at most the unrestricted central ceiling $`U_d(n)`$ from [prefix accuracy](prefix_accuracy.md). Equation (12) therefore bounds the early guessing advantage attributable to positional information. At $`\eta=0`$, the sharper exact compatibility theorem gives $`P_{\mathrm{free},d}(n)`$ instead.

No polynomial lower bound on $`\sigma_{n,d}`$ is established. Together with $`D`$, this conditioning may make (12) weak for large $`n`$. In particular, (12) is not a claim that a small relative final loss enforces the exponential early-accuracy law of the exact-preservation theorem.

## 4. A nonzero quantitative example: three qubits

For $`n=3,d=2`$, [Spencer-Wood, Jeffers, and Croke (2022)](https://doi.org/10.1103/PhysRevA.105.062447) determined the full two-then-three-specimen boundary. Write $`a`$ for the early two-qubit clustering success. Once $`7/12\le a\le5/8`$, the largest final success is

**Equation (13).**

```math
P_{\mathrm{final}}
=\frac1{12}+\frac a2+\frac1{24}\sqrt{15-24a}.
```

For $`1/2\le a\le7/12`$, the optimum final value $`5/12`$ is attainable. This prior result is the physical small-system example of the exact plateau; it is not an additional result claimed here.

Put $`x=a-7/12\ge0`$ and $`\eta=5/12-P_{\mathrm{final}}`$. The boundary gives

**Equation (14).**

```math
\eta
\ge\frac{1-12x-\sqrt{1-24x}}{24}
=\frac{6x^2}{1-12x+\sqrt{1-24x}}
\ge3x^2.
```

Thus an early success above $`7/12`$ requires a definite final loss, and

**Equation (15).**

```math
a\le\frac7{12}+\sqrt{\eta/3}.
```

For example, improving the early success by $`0.01`$ forces a final success loss of at least $`0.0003`$. The quadratic leading behavior at the plateau edge follows from the exact three-qubit boundary; no extension of its constant to arbitrary array sizes or local dimensions is asserted.
