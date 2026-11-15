# Thirty milestones for Quantum Clustering Early Readout

This is the common conceptual map for the project, anchored in John Watrous, *The Theory of Quantum Information* (2018). Section references use the author's standard-layout manuscript identified in the [Watrous bridge](WATROUS_BRIDGE.md). The canonical scientific account is in [science/](../science/README.md); its specialized harmonic-frame and temporal results are not attributed to the textbook.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background must first make the native input, whole-partition Bayes objective, causal instrument, symmetry reduction and equality conditions intelligible. The longer narrative phase then follows the project's actual proof burden: a harmonic-frame argument and one-box branching force a timing law, whose remaining freedom becomes an exact compatibility cone, a maximal classical experiment and a calculable prefix score. Finite-size stability and resource accounting complete that account.

Each phase moves from local objects to their global role. M12 integrates the preliminary objects into the research question; M30 integrates the proof, operational construction and limits. Dependencies indicate conceptual prerequisites, not a learner's status. This map records no examinations, answers, retries or personal progress.

## Phase I — Background and preliminaries

### M01

**Native quantum data.** **Phase:** background/preliminaries.

**Central question:** What is supplied at one arrival, and what remains unknown?

**Understanding target:** Describe a specimen as one quantum system prepared in one of two unknown pure states. Distinguish receiving the system from receiving a state description, a preparation oracle or extra copies.

**Dependencies and story role:** Entry point; fixes the physical input before introducing a clustering algorithm.

**Conceptual connection:** Density operators describe available quantum data; classical knowledge about a preparation is a different resource.

**Sources:** [Model §1](../science/model.md#1-random-states-random-labels-and-the-success-criterion); [resource interface](../science/resources.md#input-and-output-interface); Watrous §2.1.2, “Quantum states of registers.”

### M02

**A partition has no class names.** **Phase:** background/preliminaries.

**Central question:** Which binary strings describe the same clustering answer?

**Understanding target:** Identify a string and its complement as one hypothesis, including the all-equal partition. For a short string, distinguish exchanging the two names from changing which positions belong together.

**Dependencies and story role:** M01; defines the hidden variable used by every later likelihood and success probability.

**Conceptual connection:** A decision problem depends on its hypothesis space, not merely its physical inputs.

**Sources:** [Model §§1–2](../science/model.md#1-random-states-random-labels-and-the-success-criterion); Watrous §3.1.2, “Discriminating quantum states of an ensemble,” for the ensemble-decision framework.

### M03

**The whole-partition Bayes score.** **Phase:** background/preliminaries.

**Central question:** What event counts as a successful final answer?

**Understanding target:** Express success as correctly guessing the entire unlabeled partition under the uniform label prior and independent Haar prototypes. Recognize that correctly classifying most positions is a different objective.

**Dependencies and story role:** M01–M02; fixes the quantity that “free” readout must preserve exactly.

**Conceptual connection:** The same measurement can have different values under whole-object success, coordinatewise loss or another prior.

**Sources:** [Model §1](../science/model.md#1-random-states-random-labels-and-the-success-criterion); [interpretation and boundaries](../science/interpretation.md#what-the-boundary-does-not-establish); Watrous §3.1.2.

### M04

**Averaging unknown prototypes.** **Phase:** background/preliminaries.

**Central question:** How does a random unknown pure state become a known mixed hypothesis?

**Understanding target:** Explain why averaging repeated copies over Haar measure produces a normalized symmetric-subspace projector. Apply that principle separately to the two classes, keeping hypothesis prior and density-operator normalization distinct.

**Dependencies and story role:** M01–M03; turns the preparation model into finite matrices that can be discriminated.

**Conceptual connection:** An ensemble average can be known even when each realized preparation is unknown.

**Sources:** [Model §2](../science/model.md#2-averaged-hypotheses-and-the-balanced-factor); Watrous §7.2.1, “Uniform spherical measure and Haar measure,” especially Lemma 7.24; §7.1.1 for symmetric subspaces.

### M05

**A classical record is a likelihood.** **Phase:** background/preliminaries.

**Central question:** How is the information in a measurement outcome specified?

**Understanding target:** Read a POVM effect through its trace probability on each averaged hypothesis. Recognize that two physical measurements with identical hypothesis-conditioned outcome probabilities provide the same classical experiment for this task.

**Dependencies and story role:** M03–M04; establishes the statistical meaning of an early record.

**Conceptual connection:** Information about the partition is a property of likelihoods, while a physical instrument also determines a retained quantum state.

**Sources:** [Model §§4–5](../science/model.md#4-an-early-record-and-an-optimal-continuation); Watrous §§2.3.1–2.3.2, measurement definitions and basic notions.

### M06

**Readout with quantum memory.** **Phase:** background/preliminaries.

**Central question:** What may an early operation keep after releasing an outcome?

**Understanding target:** Separate an instrument's classical outcome from its quantum output. Describe a later measurement conditioned on that outcome, and explain why exact final-score preservation does not require the prefix state to remain unchanged.

**Dependencies and story role:** M01, M05; prevents a restrictive “measure and discard” model from replacing the allowed protocol.

**Conceptual connection:** A measurement is part of a channel with classical and quantum outputs; nondisturbance depends on the task being preserved.

**Sources:** [Model §4](../science/model.md#4-an-early-record-and-an-optimal-continuation); [local instrument construction](../science/resources.md#a-local-early-instrument-and-a-conditional-final-readout); Watrous §2.3.2, “Basic notions concerning measurements,” especially the nondestructive-measurements and instruments discussion on pp. 111–113, and §§2.2.1–2.2.2.

### M07

**Causality as a joint marginal.** **Phase:** background/preliminaries.

**Central question:** How can a full-array joint POVM represent an operation performed before the last arrival?

**Understanding target:** Interpret the condition that summing over final answers gives a prefix effect tensored with identity on the missing systems. Explain why a local square-root instrument and a conditional later POVM realize such a joint measurement.

**Dependencies and story role:** M05–M06; translates the temporal protocol into an algebraic compatibility problem.

**Conceptual connection:** A causal marginal connects operational timing to positive-operator constraints.

**Sources:** [Model §4](../science/model.md#4-an-early-record-and-an-optimal-continuation); [optimal measurement §5](../science/optimal_measurement.md#5-joint-povms-and-local-lüders-instruments); Watrous §2.3.2 and §2.2.2 for instrument foundations; the causal equivalence is derived in the repository.

### M08

**An optimum comes with equality conditions.** **Phase:** background/preliminaries.

**Central question:** What more does a dual certificate say than the value of the best score?

**Understanding target:** Relate a feasible discrimination dual to an upper bound on success. Explain how zero dual slack against a positive effect restricts its support, and why this can constrain every optimal measurement rather than one chosen decoder.

**Dependencies and story role:** M03, M05; supplies the proof mechanism behind temporal necessity.

**Conceptual connection:** Complementary slackness turns exact optimization into a geometric support statement.

**Sources:** [Optimal measurement §§2–3](../science/optimal_measurement.md#2-an-explicit-optimal-dual); Watrous §1.2.3, Proposition 1.19, and §3.1.2, Theorem 3.9.

### M09

**Symmetry without changing the experiment.** **Phase:** background/preliminaries.

**Central question:** What can be averaged away without changing early partition likelihoods or final success?

**Understanding target:** Explain the common-unitary twirl of effects and joint effects. Distinguish replacing a protocol by a likelihood-equivalent representative from proving that the original physical instrument was symmetric or unique.

**Dependencies and story role:** M04–M08; justifies studying a smaller invariant operator algebra without restricting classical information.

**Conceptual connection:** Group averaging removes irrelevant coordinates while preserving invariant observables.

**Sources:** [Model §5](../science/model.md#5-twirling-preserves-the-early-likelihoods); [temporal rigidity: observable effects](../science/temporal_rigidity.md#statement-on-observable-effects); Watrous §7.2.1 and §7.1.2, “The algebra of permutation-invariant operators.”

### M10

**Two-row support and two different roles.** **Phase:** background/preliminaries.

**Central question:** Where do prototype orientation and cluster-position information sit after symmetry reduction?

**Understanding target:** Distinguish the unitary representation factor from the permutation multiplicity factor in an occupied two-row sector. Explain why higher-row sectors are source-null and why the qubit case fills the physical space while larger local dimensions need a harmless completion.

**Dependencies and story role:** M04, M09; identifies the supported algebra on which all exact claims are made.

**Conceptual connection:** A symmetry decomposition separates kinds of information and exposes physically present but statistically unused subspaces.

**Sources:** [Model §3](../science/model.md#3-the-occupied-schur-sectors); Watrous §7.1.2 for the commutant foundation. The two-row decomposition and its dimension formulas are supplied by the repository, not asserted as that section's theorem.

### M11

**From subsets to minimal-sector frames.** **Phase:** background/preliminaries.

**Central question:** How does a candidate cluster become a vector in the sector that matters to its optimal effect?

**Understanding target:** Describe projection of a subset basis vector onto the kernel of the lowering map. Track why complementary balanced subsets give the same rank-one projector, so choosing one representative halves the frame sum and requires a factor of two in the POVM.

**Dependencies and story role:** M02, M08, M10; introduces the concrete objects used in the new proof.

**Conceptual connection:** A frame can resolve identity without being an orthonormal basis; quotienting labels affects normalization.

**Sources:** [Harmonic subset realization](../science/harmonic_frames.md#the-subset-realization); [optimal measurement §1](../science/optimal_measurement.md#1-minimal-sector-frames-and-the-balanced-normalization); Watrous §§1.1.2–1.1.3 for projections and operator decompositions. The subset frame is repository-specific.

### M12

**The complete preliminary problem.** **Phase:** background/preliminaries.

**Central question:** What must a valid exact early-readout theorem connect?

**Understanding target:** Give one connected account from native specimens and averaged partition hypotheses to a joint POVM, a global Bayes benchmark and its slack kernels. Locate the remaining question: which local early marginals can occur inside those optimal supports?

**Dependencies and story role:** M01–M11; integrates Phase I and states the precise entry point for the project's narrative.

**Conceptual connection:** The problem combines statistical decision theory, temporal causality and representation geometry; none alone determines the answer.

**Sources:** [Model](../science/model.md); [global optimum](../science/optimal_measurement.md); Watrous §§2.3.2, 3.1.2 and 7.1.2 as the three foundational links.

## Phase II — Narrative and innovation

### M13

**Every optimal continuation has narrow supports.** **Phase:** narrative/innovation.

**Central question:** Why can temporal necessity start from an arbitrary successful protocol?

**Understanding target:** Follow strict decrease of the dual coefficients to identify a hypothesis's only occupied slack kernel. Apply positivity and complementary slackness to every early/final joint effect, not only the summed optimal final effect.

**Dependencies and story role:** M08, M10–M12; the first necessity step removes freedom outside the minimal spherical lines.

**Conceptual connection:** An exposed optimum can impose common structure on all its refinements without implying uniqueness of all instruments.

**Sources:** [Optimal measurement §§2–4](../science/optimal_measurement.md#2-an-explicit-optimal-dual); [temporal reduction](../science/temporal_rigidity.md#from-an-arbitrary-instrument-to-the-optimal-supports); Watrous Proposition 1.19 and Theorem 3.9.

### M14

**Isolating an unbalanced frame coefficient.** **Phase:** narrative/innovation.

**Central question:** Why cannot distinct unbalanced subset projectors cancel in a linear relation?

**Understanding target:** Explain the path-polytabloid construction: two harmonic vectors share exactly one subset coefficient, so their matrix element isolates its weight. Recognize linear independence of projectors as stronger than the frame's resolution of identity.

**Dependencies and story role:** M11, M13; makes supported joint refinements describable by identifiable scalar coefficients.

**Conceptual connection:** Choosing test vectors with sparse common support is a constructive method for proving operator independence.

**Sources:** [Independence away from balance](../science/harmonic_frames.md#independence-away-from-balance); Watrous §1.1.2 for operator matrix elements. The path-polytabloid proof is supplied here, not by the textbook.

### M15

**Balance changes the witness and normalization.** **Phase:** narrative/innovation.

**Central question:** What survives when a subset and its complement have equal size?

**Understanding target:** Replace the path witness by the cycle witness, whose common support is a complementary pair. Explain independence after selecting one projector per pair and keep the balanced coefficient sum of two separate from the unbalanced sum of one.

**Dependencies and story role:** M02, M11, M14; closes a boundary case needed for a theorem at every array length.

**Conceptual connection:** A quotient symmetry changes a proof's witness and counting, while leaving the physical density normalization intact.

**Sources:** [Independence at balance](../science/harmonic_frames.md#independence-at-balance); [optimal measurement §1](../science/optimal_measurement.md#1-minimal-sector-frames-and-the-balanced-normalization); Watrous §§1.1.2–1.1.3 as linear-algebra foundations.

### M16

**One missing specimen gives two branches.** **Phase:** narrative/innovation.

**Central question:** How is a final harmonic sector related to the prefix sectors when one position is removed?

**Understanding target:** Identify its top and embedded bottom summands, and explain how a prefix effect tensored with identity acts on them. Distinguish a zero cross block from the stronger statement that a diagonal block is scalar.

**Dependencies and story role:** M10–M11, M13–M15; sets up the temporal obstruction in a single final sector.

**Conceptual connection:** Restricting a representation links local operator constraints across adjacent sector labels.

**Sources:** [Branching lemma](../science/temporal_rigidity.md#a-branching-lemma); [why block diagonality is insufficient](../science/harmonic_frames.md#appendix-block-diagonality-alone-is-insufficient); Watrous §7.1.2 supplies commutant context, not this one-box branching lemma.

### M17

**The branching annihilator forces a scalar top.** **Phase:** narrative/innovation.

**Central question:** What additional fact turns branching into rigidity?

**Understanding target:** Trace how a harmonic operator annihilating the bottom summand forces two coefficient values, one for subsets containing the last position and one for subsets outside it. Explain how connected subset incidence makes these values global, and how subtracting a scalar bottom block yields a scalar top.

**Dependencies and story role:** M14–M16; supplies the specialized lemma that the induction actually needs.

**Conceptual connection:** Local coefficient identities propagate through a connected combinatorial graph to determine an operator.

**Sources:** [Branching lemma and proof](../science/temporal_rigidity.md#a-branching-lemma); Watrous §1.1.2 for operator restrictions and §7.1.2 for invariant-algebra context. The annihilator argument is the repository's proof.

### M18

**Scalar blocks remove prefix order information.** **Phase:** narrative/innovation.

**Central question:** How does the sector-by-sector lemma constrain the entire penultimate record?

**Understanding target:** Start from the scalar lowest prefix block and follow the induction through adjacent branches. Conclude that every twirled early effect is scalar on each prefix multiplicity space, so its likelihood can depend on unordered class size but not the placement of positions.

**Dependencies and story role:** M09, M13–M17; proves the penultimate necessity statement for all native local dimensions.

**Conceptual connection:** A common representation structure carries a dimension-independent form of argument even though dimension-dependent probabilities remain.

**Sources:** [Induction proving no early order information](../science/temporal_rigidity.md#induction-proving-no-early-order-information); Watrous §7.1.2 for the symmetry language; the temporal induction is established in the repository.

### M19

**Two missing specimens erase even count information.** **Phase:** narrative/innovation.

**Central question:** Why is exactly one remaining arrival a special time?

**Understanding target:** Extend a shorter-prefix effect by identities, then vary an unmeasured prefix label without changing that marginal. Explain why adjacent possible class counts must have equal likelihoods and hence why the entire record is independent of the partition when at least two specimens remain.

**Dependencies and story role:** M07, M18; turns penultimate order rigidity into the full timing law.

**Conceptual connection:** A local operation cannot depend on an unseen label; combined with symmetry this removes the last available statistic.

**Sources:** [Why a shorter prefix has no cluster information](../science/temporal_rigidity.md#why-a-shorter-prefix-has-no-cluster-information); Watrous §§2.1.3 and 2.3.2 for reduced systems and local instruments.

### M20

**The exact compatibility inequalities.** **Phase:** narrative/innovation.

**Central question:** Which noisy sector readouts are actually free at the penultimate arrival?

**Understanding target:** Read the nonnegative sector coefficients and their normalization as POVM conditions. Derive the adjacent upper bound from positivity of the two branching coefficients; explain why a sharp informative Schur-sector measurement can violate it.

**Dependencies and story role:** M15–M18; strengthens “count-only is necessary” into an exact necessary-and-sufficient cone.

**Conceptual connection:** Symmetry identifies possible statistics; compatibility with a later optimum determines how much noise they require.

**Sources:** [Free readout §1](../science/free_readout.md#1-the-compatibility-cone); Watrous §§2.3.1–2.3.2 for POVM positivity and normalization; the coefficient bounds are repository-specific.

### M21

**A canonical experiment from the cone.** **Phase:** narrative/innovation.

**Central question:** Can the entire free family be generated from one readout?

**Understanding target:** Rescale successive sector coefficients by their product factors so the compatibility inequalities become monotonicity. Interpret successive differences as nonnegative coefficients of threshold-shaped canonical effects, and check why those effects sum to the supported identity.

**Dependencies and story role:** M20; converts an inequality description into one explicit finite-outcome experiment.

**Conceptual connection:** A monotone sequence decomposes into threshold increments, here yielding a physical POVM rather than merely a numerical expansion.

**Sources:** [Free readout §2](../science/free_readout.md#2-a-canonical-maximal-experiment); Watrous §2.3.2 for measurement combinations. The cone decomposition is derived in the repository.

### M22

**Maximality is a classical information order.** **Phase:** narrative/innovation.

**Central question:** In what precise sense does the canonical outcome contain all free information?

**Understanding target:** Convert the nonnegative decomposition coefficients into a stochastic postprocessing matrix. Explain why every free partition decision can be simulated from the canonical record, including unrestricted instruments through likelihood-equivalent twirling, without claiming an ordering of retained quantum states.

**Dependencies and story role:** M05, M09, M21; gives the construction its decision-theoretic meaning.

**Conceptual connection:** Classical simulation of experiments orders all decision scores at once, while equality of effects does not specify backaction.

**Sources:** [Free readout §§2–3](../science/free_readout.md#2-a-canonical-maximal-experiment); [interpretation of maximality](../science/interpretation.md#one-canonical-readout-contains-all-free-classical-information); Watrous §2.3.2 for classical processing of measurements; the Blackwell conclusion follows from the explicit repository postprocessing.

### M23

**From compatible matrices to a causal protocol.** **Phase:** narrative/innovation.

**Central question:** How is the abstract canonical experiment performed before the missing specimen arrives?

**Understanding target:** Build the supported joint effects from their nonnegative frame coefficients, take the local square-root instrument, and recover the conditional final POVM with an inverse on its support. Explain why nullspace completion and zero-probability branches do not change source statistics.

**Dependencies and story role:** M07, M13, M20–M22; proves attainability of the maximal free record with the permitted physical interface.

**Conceptual connection:** A positive joint marginal gives a sequential implementation; existence does not supply an efficient gate decomposition or minimum memory.

**Sources:** [Optimal measurement §5](../science/optimal_measurement.md#5-joint-povms-and-local-lüders-instruments); [resource construction](../science/resources.md#a-local-early-instrument-and-a-conditional-final-readout); Watrous §2.3.2 and §1.1.3 for instruments and supported inverses.

### M24

**The first informative example.** **Phase:** narrative/innovation.

**Central question:** What distinguishes a free noisy readout from a damaging sharp readout in the two-then-three case?

**Understanding target:** Interpret the two canonical effects on symmetric and antisymmetric prefix sectors. For qubits, distinguish the free early success $`7/12`$, the unrestricted two-specimen success $`5/8`$, and the preserved final success $`5/12`$; each number answers a different decision question.

**Dependencies and story role:** M03, M20–M23; makes the general theorem tangible and connects it with the inherited small-system result.

**Conceptual connection:** More early information can reduce later decision performance even when both measurements use the same specimens.

**Sources:** [Free readout §3](../science/free_readout.md#3-what-the-canonical-outcome-reveals); [three-qubit boundary](../science/stability.md#4-a-nonzero-quantitative-example-three-qubits); Watrous §3.1.2 for comparing discrimination scores. The three-qubit frontier is attributed there to Spencer-Wood, Jeffers and Croke (2022).

### M25

**Optimal decoding of the free record.** **Phase:** narrative/innovation.

**Central question:** What is the best complete-prefix guess after a canonical outcome?

**Understanding target:** Follow the outcome likelihood's dependence on minority count rather than ordering. Use the dimension-sum identity and increasing weighted average to explain why outcome index selects an optimal minority count, then interpret the exact finite sum for any native local dimension.

**Dependencies and story role:** M03, M10, M21–M24; converts maximality into an exact attainable whole-prefix success probability.

**Conceptual connection:** A maximal experiment still requires loss-specific decoding; many positional guesses can tie because the record reveals no order.

**Sources:** [Prefix accuracy §1](../science/prefix_accuracy.md#1-exact-success-in-every-local-dimension); [canonical likelihood](../science/free_readout.md#3-what-the-canonical-outcome-reveals); Watrous §3.1.2 for optimal ensemble decisions.

### M26

**A logarithmic gain over blind guessing.** **Phase:** narrative/innovation.

**Central question:** How useful is exact free prefix clustering as the dataset grows?

**Understanding target:** Compare the sharp count-only ceiling with the compatible canonical score and its controlled gap. Explain why fixed local dimension gives $`\Theta_d(2^{-n}\log n)`$ whole-prefix success, whereas the inherited unrestricted final success is of inverse-square order; identify the distinct tasks in that comparison.

**Dependencies and story role:** M03, M25; puts the finite-size formula into its statistically meaningful regime.

**Conceptual connection:** A logarithmic improvement factor can coexist with exponentially small exact-recovery probability.

**Sources:** [Prefix accuracy §§2–3](../science/prefix_accuracy.md#2-comparison-with-an-unrestricted-count-only-readout); [global optimum](../science/optimal_measurement.md#2-an-explicit-optimal-dual); Watrous §3.1.2 supplies the decision-score setting, while the asymptotics and their fixed-dimension restriction are derived or attributed in the repository.

### M27

**Small final deficit limits support leakage.** **Phase:** narrative/innovation.

**Central question:** What quantitative remnant of complementary slackness survives away from exact optimality?

**Understanding target:** Relate a positive final deficit to weighted mass outside the optimal kernels using the relative dual slack. Explain why a square-root trace-norm estimate controls pinching error, and why weights and the occupied support must be specified.

**Dependencies and story role:** M08, M13, M26; begins the separate finite-size approximate-preservation analysis without treating it as the exact theorem.

**Conceptual connection:** Optimization gaps yield geometric proximity only through a stated spectral gap and norm.

**Sources:** [Stability §1](../science/stability.md#1-weighted-leakage-from-the-optimal-supports); Watrous §1.1.3 for operator norms and §1.2.3 for semidefinite-programming equality conditions.

### M28

**Conditioning controls the approximate conclusion.** **Phase:** narrative/innovation.

**Central question:** What extra cost is paid when translating support proximity into a bound on positional information?

**Understanding target:** Identify the two operator spaces and their central intersection. Explain the role of their finite conditioning singular value and the explicit dimension and slack factors in the record bound; recognize why positivity at each finite size gives no useful uniform-in-size guarantee.

**Dependencies and story role:** M17–M18, M27; states exactly what the general near-optimal result establishes and what remains open.

**Conceptual connection:** An exact linear-space intersection can be stable with poor conditioning; exact rigidity alone does not determine a scalable regret law.

**Sources:** [Stability §§2–3](../science/stability.md#2-a-finite-conditioning-singular-value); Watrous §1.1.3 for singular values and norms. The finite conditioning construction and operational bound are repository results.

### M29

**Resources and regime boundaries.** **Phase:** narrative/innovation.

**Central question:** What does implementing and interpreting the result require us to count?

**Understanding target:** Account for the supplied specimens, retained prefix, finite classical record, final partition and ideal measurement synthesis. Distinguish an available finite-matrix realization from a memory optimum or runtime advantage; keep the exact Haar-pure, uniform-prior, whole-partition and fixed-dimension asymptotic assumptions attached to the claims that use them.

**Dependencies and story role:** M01–M03, M23, M26–M28; reconciles mathematical conclusions with the actual input/output interface and approximation limits.

**Conceptual connection:** Statistical information, coherent storage and computation are separate resources.

**Sources:** [Resources](../science/resources.md); [interpretive boundaries](../science/interpretation.md#what-the-boundary-does-not-establish); Watrous §§2.2.1–2.3.2 for finite-dimensional channels, measurements and instruments.

### M30

**The complete temporal information boundary.** **Phase:** narrative/innovation.

**Central question:** How do the proof and construction jointly determine what can be learned before completion?

**Understanding target:** Give a connected account: exact global optimality forces supported refinements; harmonic branching removes order; an extra missing specimen removes count; with one missing specimen the compatibility cone gives one maximal noisy classical experiment; its optimal decoding and finite-size stability have precisely stated scopes. Separate inherited global and three-qubit results from the project's general closure and consequences.

**Dependencies and story role:** M12–M29; integrates Phase II and the whole project without adding a broader claim.

**Conceptual connection:** A temporal learning limit is both a necessity theorem and an attainable experiment, expressed modulo ensemble likelihoods rather than physical-instrument uniqueness.

**Sources:** [Science reading path](../science/README.md); [interpretation](../science/interpretation.md); [related work](../references/RELATED_WORK.md); Watrous §§3.1.2, 7.1.2 and 7.2.1 as the decision and symmetry foundations, with the [bridge](WATROUS_BRIDGE.md) recording their limits.
