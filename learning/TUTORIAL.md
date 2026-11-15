# Early quantum clustering, from a physical example to the timing theorem

Three qubits arrive one at a time. Two unknown pure states are drawn independently and uniformly from the qubit pure states. Each position independently uses either preparation with probability one half. There are no labelled examples or descriptions of the preparations: the data are the three physical specimens. The eventual answer must say which positions belong together. Exchanging the names of the two groups changes nothing.

After the second arrival, an apparatus can release a classical answer about the first two positions and retain their quantum state. Can that answer be informative while leaving the best possible three-position clustering success attainable? The answer is yes, with a constrained, noisy measurement. Working through it first makes the general theorem's distinction between a classical record and retained quantum data concrete.

This connected route previews [M24](MILESTONES.md#m24), then develops the background and proof dependencies in the [30-milestone map](MILESTONES.md). The [Watrous bridge](WATROUS_BRIDGE.md) gives checked locations in *The Theory of Quantum Information* (2018) for states, instruments, discrimination duality and symmetry. The specialized clustering proofs are in [science/](../science/README.md).

## Two specimens: hypotheses, effects and probabilities

For the first two qubits there are two possible partitions: **same preparation** and **different preparations**, each with prior one half. “Different” means the two preparation labels differ; the unknown pure states need not be orthogonal.

Let $`S_{12}`$ swap the first and second qubits. The projectors

```math
P_+=\frac{I_4+S_{12}}2,
\qquad
P_-=\frac{I_4-S_{12}}2
```

select the symmetric and antisymmetric subspaces, of dimensions three and one. An identical pure-state pair is symmetric. Averaging its unknown direction gives the maximally mixed state on that subspace. Independent unknown preparations instead average independently to $`I_2/2`$. Thus the two known, prior-averaged density operators are

```math
\rho_{\mathrm S}=\frac{P_+}{3},
\qquad
\rho_{\mathrm D}=\frac{I_4}{4}.
```

Both have trace one. These matrices describe uncertainty about the preparation under each hypothesis; they are not extra specimens supplied to the apparatus. This is the state-ensemble step of M01–M04 and [model §2](../science/model.md#2-averaged-hypotheses-and-the-balanced-factor).

A POVM is a family of positive operators that sum to identity. Its effect $`K_a`$ gives outcome probability $`\Pr(a\mid H)=\mathrm{tr}(K_a\rho_H)`$. Consider

```math
K_0=\frac23P_+,
\qquad
K_1=\frac13P_++P_-.
```

The effects are positive and sum to $`I_4`$. Their probabilities, obtained by taking the traces, are:

| Prefix hypothesis | Prior | Outcome 0 | Outcome 1 |
| --- | ---: | ---: | ---: |
| Same, $`\mathrm S`$ | $`1/2`$ | $`2/3`$ | $`1/3`$ |
| Different, $`\mathrm D`$ | $`1/2`$ | $`1/2`$ | $`1/2`$ |

Outcome zero favours “same”; outcome one favours “different.” Using those guesses gives

```math
P_{\mathrm{early}}
=\frac12\Pr(0\mid\mathrm S)
+\frac12\Pr(1\mid\mathrm D)
=\frac12\frac23+\frac12\frac12
=\frac7{12}.
```

This score includes both outcomes and both hypotheses. It exceeds blind guessing, whose success is $`1/2`$. A sharp measurement $`\{P_+,P_-\}`$ would achieve the larger standalone two-qubit score $`5/8`$, by guessing “same” on the symmetric outcome and “different” on the antisymmetric outcome. That sharper measurement cannot preserve the optimum for the later three-qubit task. The softer effects above can; the next step establishes that operational claim rather than inferring it from the early probabilities.

## Keep a quantum output, then decode all three specimens

An **instrument** specifies both the classical outcome and what quantum system remains. One implementation of the effects above uses the local square-root, or Lüders, branches

```math
\Phi_a(X)=\sqrt{K_a}\,X\sqrt{K_a},
\qquad
\sqrt{K_0}=\sqrt{\frac23}P_+,
\qquad
\sqrt{K_1}=\frac1{\sqrt3}P_++P_-.
```

The trace of a branch is its outcome probability. Dividing by that trace gives the conditional retained state. The apparatus keeps this quantum output, records $`a`$, and waits for qubit three. In particular, outcome one is not a projection onto the antisymmetric subspace. Its branch retains contributions from both subspaces. Physically measuring sharp symmetry and subsequently hiding or randomizing that result is a different instrument; equal visible effects do not guarantee equal retained quantum data. This is the distinction in M05–M07.

There are four three-position partitions, each with prior $`1/4`$. Label the all-equal partition by 0 and the partition with singleton position $`i`$ by $`i=1,2,3`$. Let $`P_{123}`$ project onto the fully symmetric three-qubit subspace. Let $`R_i`$ project onto symmetry of the other two positions, acting as identity on position $`i`$. For example, $`R_3=P_+\otimes I_2`$. Their averaged source states and a final POVM are

```math
\rho_0=\frac{P_{123}}4,
\qquad
\rho_i=\frac{R_i}{6},
\qquad
M_0=P_{123},
\qquad
M_i=\frac23(R_i-P_{123})\quad(i=1,2,3).
```

The subtraction defines a positive projector before its factor $`2/3`$: the fully symmetric space is contained in each pair-symmetric space. The identities $`\mathrm{tr}P_{123}=4`$, $`\mathrm{tr}R_i=6`$ and

```math
R_1+R_2+R_3=\frac32I_8+\frac32P_{123}
```

show that the source states are normalized and that $`\sum_{i=0}^3M_i=I_8`$. The four effects form a valid measurement. Its correctness probabilities are $`\mathrm{tr}(M_0\rho_0)=1`$ and $`\mathrm{tr}(M_i\rho_i)=2/9`$ for each singleton. Consequently

```math
P_{\mathrm{final}}
=\frac14\left(1+3\frac29\right)
=\frac5{12}.
```

The [optimal-measurement certificate](../science/optimal_measurement.md#2-an-explicit-optimal-dual) proves that $`5/12`$ is the unrestricted optimum, inherited from Sentís and collaborators. It concerns the whole three-position partition, so it is a different decision score from the early two-position value $`7/12`$.

To connect this final POVM to the actual early instrument, specify joint effects $`B_{a,i}`$ for early outcome $`a`$ and final answer $`i`$:

| Early outcome | All equal, $`i=0`$ | Singleton 1 | Singleton 2 | Singleton 3 |
| --- | --- | --- | --- | --- |
| $`a=0`$ | $`\tfrac23M_0`$ | $`0`$ | $`0`$ | $`M_3`$ |
| $`a=1`$ | $`\tfrac13M_0`$ | $`M_1`$ | $`M_2`$ | $`0`$ |

Every entry is positive. Each column sums to $`M_i`$, preserving the final measurement. Each row sums to $`K_a\otimes I_2`$; for example,

```math
\sum_{i=0}^3B_{0,i}
=\frac23P_{123}+\frac23(R_3-P_{123})
=\frac23R_3
=K_0\otimes I_2.
```

The last identity is the causal constraint: the early outcome probability depends only on the two available specimens. The occurrence of the future qubit in a joint-effect description does not let the first operation access it.

For a constructive conditional decoder, put $`L_a=\sqrt{K_a}\otimes I_2`$ and let $`L_a^+`$ be its inverse on its range, zero on its kernel. Define

```math
C_{i\mid a}=L_a^+B_{a,i}L_a^+.
```

These positive effects sum to the range projector of $`L_a`$. Complete them by any POVM on its orthogonal complement; that subspace has zero probability after branch $`a`$. They obey $`L_aC_{i\mid a}L_a=B_{a,i}`$. The physical protocol is therefore: apply the two-qubit Lüders instrument, retain its quantum output, receive qubit three, and perform $`\{C_{i\mid a}\}`$ conditional on the recorded outcome. Both early outcomes enter the final score; there is no postselection. This proves simultaneous attainability of early $`7/12`$ and final $`5/12`$.

The three-qubit tradeoff is prior work of [Spencer-Wood, Jeffers and Croke (2022)](https://doi.org/10.1103/PhysRevA.105.062447). The example illustrates the mechanism. It does not prove the theorem for arbitrary array length.

## The general Bayesian problem

Now allow $`n`$ specimens of local dimension $`d\ge2`$. The two independent Haar-pure prototypes are $`|\phi_0\rangle,|\phi_1\rangle\in\mathbb C^d`$, and the independently uniform binary pattern $`x`$ prepares

```math
|\Phi_x\rangle=\bigotimes_{t=1}^n|\phi_{x_t}\rangle.
```

The answer is the partition $`[x]=\{x,\bar x\}`$, where $`\bar x`$ exchanges the two names. There are $`2^{n-1}`$ answers, each with prior $`p_n=2^{1-n}`$, including the all-equal answer with an empty second group. Success means recovering this entire partition. It gives no partial credit for individual positions. These are the input and loss assumptions of M01–M03.

Let $`A`$ denote a minority group, of size $`j\le\lfloor n/2\rfloor`$. Averaging the unknown directions independently gives

```math
s_d(t)=\binom{d+t-1}{t},
\qquad
\rho_{n;j,A}
=\frac{P_{\mathrm{sym},A}P_{\mathrm{sym},A^c}}
{s_d(j)s_d(n-j)}.
```

Here $`s_d(t)`$ is the dimension of the symmetric subspace of $`t`$ qudits; $`s_d(0)=1`$. The projectors act on disjoint groups, so their product has exactly the denominator as its trace. The two-qubit states above are the first instance of this formula. When $`n=2j`$, $`A`$ and $`A^c`$ denote the same answer: retain one representative. This halves the number of hypotheses at that count, without changing a source state's normalization or its prior. The [Watrous bridge](WATROUS_BRIDGE.md#from-unknown-prototypes-to-a-known-ensemble) explains the Haar moment behind the formula.

After $`m\lt n`$ arrivals, an unrestricted instrument may release $`a`$, keep a quantum output and ancillas, and later use a conditional decoder. Its joint effects satisfy

```math
B_{a,[x]}\succeq0,
\qquad
\sum_{[x]}B_{a,[x]}=F_a\otimes I_{d^{n-m}},
\qquad
\sum_aF_a=I_{d^m}.
```

The same local square-root construction used in the example realizes any such joint POVM. “Free” means that its eventual whole-partition Bayes success equals the unrestricted optimum $`P_{\mathrm{opt},d}(n)`$ exactly. It means preservation of this decision performance, rather than recovery of every input state. M06–M08 and [model §4](../science/model.md#4-an-early-record-and-an-optimal-continuation) set out that distinction.

## Why exact optimality constrains every continuation

The source is invariant under applying the same $`U\in U(d)`$ to every specimen. Averaging a whole joint POVM over that common rotation preserves its causal marginal, all partition-conditioned probabilities and its final score. This **twirl** allows analysis within the common-unitary commutant. It does not average away specimen positions: positional information is precisely what the theorem must constrain.

The occupied space decomposes as

```math
\mathcal S_n
=\bigoplus_{k=0}^{\lfloor n/2\rfloor}
Q_{n,k}^{(d)}\otimes V_{n,k},
\qquad
V_{n,k}\cong S^{(n-k,k)}.
```

The $`Q`$ factor carries common basis rotations; the $`V`$ factor carries permutations of positions. Only two-row sectors occur because the source contains a product of two symmetric groups of specimens. For qubits they fill the Hilbert space. For $`d\gt 2`$, higher-row sectors are source-null, and physical POVMs can be completed there without changing source probabilities. This is the reduction of M09–M10, detailed in [model §3](../science/model.md#3-the-occupied-schur-sectors).

The discrimination dual supplies an operator $`\Gamma_n\succeq p_n\rho_{n;[x]}`$ for every answer. Its trace bounds the success of every final POVM. Here the explicit certificate is

```math
\Gamma_n
=p_n\bigoplus_k c_{n,k}I_{Q_{n,k}^{(d)}}\otimes I_{V_{n,k}},
\qquad
c_{n,k}=\frac1{s_d(k)s_d(n-k)}.
```

It is zero on source-null sectors. Its trace is attained by the inherited clustering measurement, hence equals the optimum. The coefficients strictly decrease with $`k`$. This makes each hypothesis's dual-slack kernel particularly narrow: in its minimal sector, only one spherical line in $`V_{n,k}`$ remains.

For any exactly optimal sequential procedure, the gap is

```math
0=P_{\mathrm{opt},d}(n)-P_{\mathrm{final}}
=\sum_{a,[x]}\mathrm{tr}
\left[(\Gamma_n-p_n\rho_{n;[x]})B_{a,[x]}\right].
```

Each summand is nonnegative because both operators are positive. Therefore every summand is zero, forcing each joint effect to be supported inside the corresponding slack kernel. This is complementary slackness used as a structural constraint. It applies to every optimal continuation, without choosing its decoder in advance. The textbook supplies the general duality principle; [optimal measurement §§2–3](../science/optimal_measurement.md#2-an-explicit-optimal-dual) identifies this ensemble's certificate and kernels. This joins M08, M12 and M13.

## The harmonic argument that removes position information

To describe those kernel lines concretely, use a vector space with an orthonormal basis $`e_A`$ indexed by the $`k`$-subsets of $`[n]`$. The lowering map sums coefficients over one-element extensions:

```math
(D_nf)_R=\sum_{a\notin R}f_{R\cup\{a\}},
\qquad
H_k(n)=\ker D_n,
\qquad
v_A=P_{H_k(n)}e_A.
```

The harmonic space $`H_k(n)`$ realizes $`V_{n,k}`$; $`v_A`$ is the projected subset vector. These vectors are generally not orthogonal. Their rank-one operators nevertheless resolve identity, and their normalized directions are the minimal-sector spherical lines in the slack kernels. The vectors' squared norms are $`f_{n,k}/\binom nk`$, where $`f_{n,k}=\binom nk-\binom n{k-1}`$. This supplies the concrete objects in M11.

Two facts about these frames carry M14–M17. First, the projectors $`|v_A\rangle\langle v_A|`$ are linearly independent when $`n\gt 2k`$. A constructive proof uses harmonic polynomials made from disjoint pair differences. Two such polynomials can share exactly one subset monomial, so a matrix element isolates its coefficient in a proposed operator relation. At balance, a cycle replaces that path witness: its shared monomials are $`A`$ and $`A^c`$. Since $`v_{A^c}=(-1)^kv_A`$, one projector per complementary pair is independent. The corresponding optimal balanced POVM requires a factor of two. The complete witnesses and normalization appear in [harmonic frames](../science/harmonic_frames.md).

Second, restricting a final sector to the first $`m=n-1`$ positions gives neighboring prefix branches:

```math
V_{n,k}\!\downarrow_{S_m}
\cong V_{m,k}\oplus V_{m,k-1}.
```

An absent branch is omitted. After the common-unitary twirl, write a prefix effect as $`\bigoplus_j I_Q\otimes E_{a,j}`$. Its extension by identity acts on these two branches as $`E_{a,k}\oplus E_{a,k-1}`$. Exact optimality simultaneously places that operator in the span of the harmonic frame projectors.

The key branching lemma says that, in this frame span, a scalar lower block forces a scalar upper block. Its proof subtracts the scalar lower block and studies an operator annihilating that branch. Harmonic test vectors give coefficient identities along the connected incidence graph of adjacent subset sizes, leaving just two constant weights: one for subsets containing the last position and one for subsets outside it. The resulting upper block is scalar. **Block diagonality alone is insufficient**; the [five-position counterexample](../science/harmonic_frames.md#appendix-block-diagonality-alone-is-insufficient) explains why the scalar lower block is essential.

Now $`E_{a,0}`$ is scalar because its multiplicity space is one-dimensional. Apply the lemma successively to force $`E_{a,1}`$, then $`E_{a,2}`$, and so on to be scalar. This proves M18:

```math
\overline F_a=\sum_{j=0}^{\lfloor m/2\rfloor}\theta_{a,j}\Pi_j
\quad\text{on }\mathcal S_m,
\qquad m=n-1,
```

where $`\Pi_j`$ is the prefix two-row sector projector. Such an operator is invariant under prefix permutations. Its outcome probability can depend on the unordered group sizes, but cannot distinguish two placements with those sizes. The original, possibly asymmetric instrument has the same source likelihoods as this representative. This is a statement about all observable classical records, rather than uniqueness of all physical effects or instruments. The full induction is in [temporal rigidity](../science/temporal_rigidity.md#induction-proving-no-early-order-information).

## Why another missing specimen removes even size information

Suppose the actual early operation acts on $`m\le n-2`$ positions. Extend its effect by identities until it is viewed as an operation on $`n-1`$ positions. The preceding theorem says its likelihood can depend only on that larger prefix's minority count.

At least one position in this larger prefix was never measured. Changing its preparation label leaves the reduced state of the measured positions unchanged, but can increase the larger prefix's minority count from $`j`$ to $`j+1`$. The two likelihoods must be equal. Connecting all adjacent counts shows that every early outcome has the same probability for every partition. This is M19 and [the shorter-prefix argument](../science/temporal_rigidity.md#why-a-shorter-prefix-has-no-cluster-information).

| Specimens still missing | Early classical partition information compatible with exact optimal final success |
| --- | --- |
| At least two | None: all partition-conditioned record distributions coincide. |
| Exactly one | A constrained noisy statistic of unordered prefix group sizes; no positional information. |

A record with no partition information is not automatically harmless: an operation may erase useful quantum data without announcing anything. The theorem is a necessity statement for a successful continuation.

## Exactly how much noise the penultimate record needs

Count-only dependence is necessary but not sufficient. The scalar prefix effects above admit an optimal continuation precisely when

```math
\theta_{a,j}\ge0,
\qquad
\sum_a\theta_{a,j}=1,
\qquad
\theta_{a,j}\le(n-2j+2)\theta_{a,j-1}\quad(j\ge1).
```

Positivity of the supported joint refinements produces the last inequalities. Conversely, those inequalities give nonnegative refinement coefficients, and the local Lüders construction realizes them causally. This necessary-and-sufficient cone is M20 and [free readout §1](../science/free_readout.md#1-the-compatibility-cone).

For the initial $`n=3`$ example, $`\Pi_0=P_+`$ and $`\Pi_1=P_-`$, so the only adjacent inequality is $`\theta_{a,1}\le3\theta_{a,0}`$. Outcome zero of $`K`$ has coefficient pair $`(2/3,0)`$; outcome one has $`(1/3,1)`$. Both satisfy it. A sharp antisymmetric effect has pair $`(0,1)`$ and violates it. The general theorem now explains the example's required softness, beyond merely exhibiting one valid protocol.

The cone also produces a single maximal classical experiment. Put $`r=\lfloor(n-1)/2\rfloor`$ and define scalar product factors and weights

```math
B_0=1,
\qquad B_j=\prod_{t=1}^j(n-2t+2),
\qquad
w_l=\begin{cases}
B_l^{-1}-B_{l+1}^{-1},&l\lt r,\\
B_r^{-1},&l=r.
\end{cases}
```

These $`B_j`$ are numbers, distinct from the joint effects $`B_{a,[x]}`$. The canonical POVM is

```math
K_l=w_l\sum_{j=0}^lB_j\Pi_j,
\qquad l=0,\ldots,r.
```

Each sector's total coefficient is $`B_j\sum_{l\ge j}w_l=1`$, so this is normalized on the occupied support. For $`n=3`$, it gives exactly the two effects already used.

Why is it maximal? Dividing the cone inequality by $`B_j`$ makes the sequence $`\theta_{a,j}/B_j`$ nonincreasing. Its successive differences are nonnegative, so every free effect decomposes into the canonical threshold-shaped effects. Normalization turns that decomposition into a stochastic matrix $`R(a\mid l)`$ satisfying

```math
\Pr(a\mid[x])
=\sum_lR(a\mid l)\Pr(l\mid[x]).
```

Thus one can reproduce any free classical record by reading $`l`$ and randomizing classically. This is Blackwell maximality: every decision about the partition that can be made from another free record can be simulated from this one. It orders classical experiments, not residual quantum states. The statement covers unrestricted instruments through their source likelihoods. M21–M23 and [free readout §2](../science/free_readout.md#2-a-canonical-maximal-experiment) give the exact decomposition and physical completion.

## What the record lets an early classifier guess

For $`m=n-1`$, define

```math
T_{m,k}=s_d(m-k)s_d(k),
\qquad
q_d(m,j)=T_{m,j}-T_{m,j-1},
\qquad T_{m,-1}=0.
```

Here $`q_d(m,j)`$ is the dimension of the common-unitary representation in prefix sector $`j`$. If the prefix's minority group has size $`k`$, its canonical likelihood is

```math
\Pr(l\mid k,A)
=\frac{w_l}{T_{m,k}}
\sum_{j=0}^{\min\{k,l\}}q_d(m,j)B_j.
```

The absence of $`A`$ is the absence of positional information. After outcome $`l`$, an optimal whole-prefix guess is any one partition with minority size $`l`$. All its positional representatives tie. The dimension-sum identity and an increasing weighted-average argument prove this decoding rule; [prefix accuracy §1](../science/prefix_accuracy.md#1-exact-success-in-every-local-dimension) supplies that step of M25.

Writing $`S_{d,l}=\sum_{j=0}^lq_d(m,j)B_j`$, the best possible free early success is

```math
P_{\mathrm{free},d}(n)
=2^{2-n}\sum_{l=0}^rw_l\frac{S_{d,l}}{T_{m,l}}.
```

The factor $`2^{2-n}`$ is the prior of each prefix partition, rather than a uniform prior on minority counts. The rule is attainable, and classical maximality proves that no other exactly free record does better. For qubits:

| Final length | Prefix length | Best free whole-prefix success |
| ---: | ---: | ---: |
| 3 | 2 | $`7/12`$ |
| 4 | 3 | $`5/16`$ |
| 5 | 4 | $`47/270`$ |
| 6 | 5 | $`71/768`$ |

At fixed $`d`$ and growing $`n`$, the exact formula gives

```math
P_{\mathrm{free},d}(n)=\Theta_d(2^{-n}\log n).
```

The free record gains a logarithmic factor over blind prefix guessing, while exact whole-prefix success still decays exponentially. The inherited unrestricted final success is asymptotic to $`8(d-1)/n^2`$. These are different decisions on different array lengths, both using whole-partition success. The comparison expresses a timing restriction on classical release while quantum data remain useful for a later joint decision. It is not a statement about per-position error. The bounds proving this fixed-dimension regime are M26 and [prefix accuracy §§2–3](../science/prefix_accuracy.md#2-comparison-with-an-unrestricted-count-only-readout).

## Exact timing, finite-size stability and resources

Exact complementary slackness does not by itself establish a useful theorem for approximately optimal procedures. With final deficit $`\eta=P_{\mathrm{opt},d}(n)-P_{\mathrm{final}}\gt 0`$, a positive relative dual gap bounds weighted leakage outside the optimal supports. A square-root trace-norm estimate then bounds the error from pinching back to those supports. This is the quantitative remnant of the equality argument, developed in M27 and [stability §1](../science/stability.md#1-weighted-leakage-from-the-optimal-supports).

Converting that leakage to a restriction on positional information incurs another cost: a conditioning singular value $`\sigma_{n,d}`$ between the relevant operator spaces, along with explicit dimension and gap factors. It is positive and computable at each fixed size. No favorable uniform lower bound in $`n`$ is proved. Consequently the finite-size estimate does not show that small allowed final regret enforces the exact theorem's exponential early-recovery law. This distinction is M28 and [stability §§2–3](../science/stability.md#2-a-finite-conditioning-singular-value).

The three-qubit problem does have a known quantitative boundary. For early success $`a`$ in $`[1/2,7/12]`$, final $`5/12`$ remains attainable. Above that plateau, $`7/12\le a\le5/8`$, the inherited optimum is

```math
P_{\mathrm{final}}
=\frac1{12}+\frac a2+\frac1{24}\sqrt{15-24a}.
```

This displays the finite physical cost of requesting a stronger early answer. Its associated lower bound $`\eta\ge3(a-7/12)^2`$ does not supply a constant for arbitrary $`n`$ or $`d`$. See [the attributed three-qubit frontier](../science/stability.md#4-a-nonzero-quantitative-example-three-qubits).

The constructive protocol retains a quantum prefix and later performs a conditional global POVM. It proves finite-dimensional physical realizability, without proving minimum memory or efficient gate synthesis. The [resource account](../science/resources.md) distinguishes supplied specimens, retained registers, classical outcomes and measurement implementation. Independent Haar-pure prototypes, uniform labels, the whole-partition loss and exact final optimality remain attached to the timing theorem; mixed clusters, different priors, noise and different loss functions require separate analysis.

The global connection in M29–M30 is now explicit: the exact Bayes optimum constrains every joint refinement; harmonic branching removes prefix order; an additional missing specimen removes even count information; with one missing specimen, positivity leaves a precisely characterized noisy experiment. That experiment is physically attainable and maximal for classical partition decisions, while its retained quantum output remains available for the final task. The [milestone map](MILESTONES.md), [source bridge](WATROUS_BRIDGE.md) and [canonical science path](../science/README.md) give the dependencies, educational foundations and complete proofs of that same account.
