# Specimens, instruments and implementation resources

This is a decision-theoretic result for native quantum inputs. It determines which early classical information is compatible with the optimal final clustering score. All supplied specimens count; implementation costs are distinct from that statistical statement.

## Input and output interface

There are $`n`$ arrivals, each a $`d`$-dimensional system. Two unknown pure prototypes are drawn independently from Haar measure, and each position chooses a prototype with independent probability $`1/2`$. The learner receives one specimen at that position. It receives no prototype description, preparation seed, purification, preparation inverse, additional-copy oracle or labeled training set.

The final output is a partition of the $`n`$ positions into two unlabeled groups. The two complementary binary strings describe the same answer. The early output is a classical record; the early operation may also retain an arbitrary quantum output. The necessity theorem permits such general instruments and arbitrary final processing conditioned on the record.

| Resource | Accounting in the theorem and construction |
| --- | --- |
| Native specimens | Exactly the supplied $`n`$ systems; early readout does not create replacements. |
| Inter-arrival quantum storage | Permitted. The explicit construction retains the prefix; it is not memory optimal. |
| Early classical storage | The canonical penultimate readout has $`r+1`$ outcomes, with $`r=\lfloor(n-1)/2\rfloor`$. Its label can be stored in $`\lceil\log_2(r+1)\rceil`$ bits. |
| Final classical output | A partition can be encoded by $`n-1`$ bits; no compressed-output complexity claim is made. |
| Known operations | Ideal finite-dimensional instrument and POVM synthesis is assumed available. No efficient elementary-gate bound is established. |
| Success convention | All outcomes are retained and averaged. There is no uncharged postselection or discarded failure branch. |

The canonical outcome count measures one sufficient classical record, not the least storage required by every useful free task. Extra classical randomization can produce other compatible records without adding information about the partition.

## A local early instrument and a conditional final readout

The canonical effects $`F_\ell`$ act on the prefix. They sum to the identity on the ensemble support. If $`d>2`$, complete them arbitrarily on the unoccupied Schur sectors, for example by assigning that orthogonal complement to one outcome. This gives a normalized POVM on the full physical space without changing any source probabilities. A realization uses its local Lüders instrument:

```math
\mathcal I_\ell(X)=\sqrt{F_\ell}\,X\sqrt{F_\ell}.
```

The outcome $`\ell`$ is recorded, and the quantum output is kept. This map need not leave the prefix state unchanged. Its purpose is to preserve the particular final decision score when combined with a suitable later measurement.

Sufficiency is established by constructing a joint POVM $`\{E_{\ell,x}\}`$ on all specimens whose marginals are the early effects and an optimal final clustering POVM $`\{\Pi_x\}`$:

```math
\sum_x E_{\ell,x}=F_\ell\otimes I,
\qquad
\sum_\ell E_{\ell,x}=\Pi_x.
```

The tensor identity acts on specimens not yet received at the early stage. Positivity implies that each $`E_{\ell,x}`$ is supported inside the support of $`F_\ell\otimes I`$. After the remaining arrivals, define on this support

```math
G_{x\mid\ell}
=(F_\ell^{-1/2}\otimes I)
E_{\ell,x}
(F_\ell^{-1/2}\otimes I),
```

using the inverse only on the support. Completing the POVM arbitrarily on the orthogonal complement yields a valid conditional final measurement. Its joint outcome probabilities coincide with those of $`E_{\ell,x}`$, so summing over $`\ell`$ gives the optimal final clustering score. Zero-probability branches require no conditioning on an impossible event.

This construction is local at the early time: it acts only on specimens already received. The later measurement may be global. Classical postprocessing of $`\ell`$ produces any other free record; retaining $`\ell`$ internally is permitted when it is needed for the final decoder. Maximality concerns the released record's likelihoods, not a unique retained quantum state.

## Storage and synthesis bounds that are, and are not, claimed

A direct realization keeps all $`m`$ prefix specimens after the early operation, requiring a Hilbert space of dimension $`d^m`$, or $`m\log_2d`$ qubits in logarithmic dimension. After all arrivals, a direct global implementation can hold all $`n`$ specimens, together with ancillas and the classical early outcome. This is a sufficient implementation description. The theorem does not prove a minimal coherent width, minimum storage time, optimal compression or a gate-optimal Schur transform.

The effects and conditional POVMs are known finite matrices determined by the prior, $`n`$ and $`d`$. Abstract finite-dimensional measurement synthesis therefore exists. Their potentially large classical descriptions, gate decompositions, controlled operations, ancillas, precision and runtime are not made free by that existence statement. The scalar success formulas do not imply efficient quantum hardware execution.

The analysis assumes ideal supplied systems, storage and operations. It gives no fixed-noise, finite-coherence-time or fault-tolerant overhead theorem. An implementation approximating the instruments needs its own error budget; exact Bayes preservation cannot be inferred from a floating-point matrix calculation.

Finally, the comparison does not pit a complete quantum algorithm against every classical computational algorithm. It contrasts early classical information release with retaining the final optimal score on the same quantum dataset. No QRAM, classical-data loading speedup, unrestricted runtime advantage, heat bound or energy advantage follows.
