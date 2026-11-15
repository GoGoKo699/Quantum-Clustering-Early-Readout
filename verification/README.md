# Reproduce the finite checks

From the repository root, with Python 3.12:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/check_science.py --output verification/results.json
```

The program exits unsuccessfully if a checked identity, positivity condition,
optimization comparison or tolerance fails. Its checks remain active under
Python's `-O` flag. The committed [results](results.json) were produced with
Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0. Floating-point
residuals can vary slightly across numerical libraries.

## What is checked

| Check | Independent construction and scope |
|---|---|
| Spherical-frame independence | Exact rational subset-incidence projectors in eight cases, through seven sites. The Gram rank equals the number of distinct effects. Balanced complementary subsets use the factor of two required by the physical POVM. |
| Harmonic annihilator | Exact rational Gram matrices of the map from frame coefficients to the lower-branch action, in five cases through seven sites. The kernel has dimension one, and its operator is exactly the upper-branch projector. |
| Necessity of the scalar lower-block condition | An exact five-site example has vanishing cross block and nonscalar diagonal blocks. It prevents replacing the proved annihilator lemma by the stronger off-diagonal-only statement. |
| Physical optimal measurement | Computational-basis symmetric-cut source states and total-spin projectors obtained from physical SWAP matrices, for three through six qubits. The code checks POVM completeness, dual feasibility, complementary slackness and equality of primal and dual success. |
| Sequential realization | The canonical early effects and their nonnegative joint refinements have the required marginal on the early subsystem. A local Lüders square root and a conditional decoder reconstruct every joint effect on its support. |
| Best early accuracy | Thirty-six independent linear programs optimize all count decisions for final sizes three through fourteen and local dimensions two, three and five. The canonical formula is not imposed on these programs. Their optima agree with the exact rational formula. |
| Finite harmonic identity | Exact arithmetic for final sizes three through sixty checks the corrected identity and its count-readout gap bound. The small prefix successes are exactly `7/12`, `5/16`, `47/270` and `71/768`. |

The largest observed physical matrix or Lüders reconstruction residual was
`9.11e-15`. The largest discrepancy between the independent linear programs and
the exact early-success formula was `6.94e-18`.

## Evidence limits

The harmonic checks use exact arithmetic. The physical matrices and linear
programs use floating point with explicit tolerances; they are not interval
certificates. The all-size temporal theorem, compatibility characterization and
maximality of the early experiment follow from the written proofs, rather than
from this finite enumeration. These checks establish neither literature priority
nor an efficient physical circuit synthesis. They do not test a uniform
approximately-optimal early-readout theorem or a hardware-noise guarantee.

The scientific model and the proof routes start at [the model](../science/model.md).
