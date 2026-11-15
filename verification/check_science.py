#!/usr/bin/env python3
"""Finite checks of the exact early-readout clustering statements.

Exact subset-module calculations and rational identities are kept separate from
floating-point physical matrices and linear programs. These checks supplement
the written proofs; they do not establish arbitrary-size theorems or priority.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from math import comb
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.optimize import linprog
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def harmonic_projector(n: int, k: int):
    subsets = list(combinations(range(n), k))
    if k == 0:
        return subsets, sp.eye(1)
    lower = list(combinations(range(n), k - 1))
    down = sp.Matrix([[int(set(r).issubset(a)) for a in subsets]
                      for r in lower])
    p = sp.eye(len(subsets)) - down.T * (down * down.T).inv() * down
    require(p * p == p and p.T == p, "harmonic projector")
    return subsets, p


def exact_harmonic_checks():
    frames = []
    for n, k in [(3, 0), (3, 1), (4, 1), (4, 2), (5, 2),
                 (6, 2), (6, 3), (7, 3)]:
        subsets, p = harmonic_projector(n, k)
        indices = [i for i, a in enumerate(subsets)
                   if 2 * k != n or 0 in a]
        # Gram of |v_A><v_A| is entrywise square of the vector Gram P.
        gram = p.multiply_elementwise(p).extract(indices, indices)
        rank = DomainMatrix.from_Matrix(gram).rank()
        require(rank == len(indices), "distinct spherical effects independent")
        normalization = 2 if 2 * k == n else 1
        total = sum((normalization * p[:, i] * p[:, i].T for i in indices),
                    sp.zeros(len(subsets)))
        require(total == p, "balanced/unbalanced frame normalization")
        frames.append({"n": n, "k": k, "distinct_effects": len(indices),
                       "frame_gram_rank": rank,
                       "multiplicity_dimension": int(sp.trace(p))})

    branching = []
    for n, k in [(3, 1), (4, 1), (5, 2), (6, 2), (7, 3)]:
        subsets, p = harmonic_projector(n, k)
        smaller, q = harmonic_projector(n - 1, k)
        location = {a: i for i, a in enumerate(subsets)}
        top = sp.zeros(len(subsets))
        for i, a in enumerate(smaller):
            for j, b in enumerate(smaller):
                top[location[a], location[b]] = q[i, j]
        bottom = p - top
        gram = p.multiply_elementwise(bottom)
        a = n - 2 * k + 1
        z = sp.Matrix([F(-1, a) if n - 1 in s else 1 for s in subsets])
        require(gram * z == sp.zeros(len(subsets), 1), "branch kernel vector")
        require(len(subsets) - DomainMatrix.from_Matrix(gram).rank() == 1,
                "branch annihilator kernel dimension")
        require(p * sp.diag(*z) * p == top, "branch kernel operator")
        branching.append({"n": n, "k": k, "kernel_dimension": 1,
                          "top_dimension": int(sp.trace(top)),
                          "bottom_dimension": int(sp.trace(bottom))})

    subsets, p = harmonic_projector(5, 2)
    columns = sp.Matrix.hstack(*[p[:, i] for i, a in enumerate(subsets) if 4 in a])
    independent = sp.Matrix.hstack(*columns.columnspace())
    bottom = independent * (independent.T * independent).inv() * independent.T
    top = p - bottom
    v = lambda a: p[:, subsets.index(a)]
    w = v((0, 1)) * v((0, 1)).T + v((2, 3)) * v((2, 3)).T
    require(top * w * bottom == sp.zeros(len(subsets)), "off-diagonal cancellation")
    require(top * w * top != sp.trace(top * w) / sp.trace(top) * top,
            "counterexample top is not scalar")
    require(bottom * w * bottom != sp.trace(bottom * w) / sp.trace(bottom) * bottom,
            "counterexample bottom is not scalar")
    return {"frame_cases": frames, "branching_cases": branching,
            "off_diagonal_only_conjecture_counterexample":
            {"n": 5, "k": 2, "positive_terms": ["12", "34"],
             "cross_block_zero": True, "both_diagonal_blocks_nonscalar": True}}


def cut_symmetric_projector(n: int, a):
    """Build P_sym(A) tensor P_sym(Ac) in the computational basis."""
    a = set(a)
    b = set(range(n)) - a
    groups = {}
    for word in range(1 << n):
        key = (sum((word >> i) & 1 for i in a),
               sum((word >> i) & 1 for i in b))
        groups.setdefault(key, []).append(word)
    p = np.zeros((1 << n, 1 << n))
    for group in groups.values():
        p[np.ix_(group, group)] = 1 / len(group)
    return p


@lru_cache(None)
def spin_projectors(n: int):
    """Diagonalize J^2 built independently from physical SWAP matrices."""
    size = 1 << n
    j2 = np.eye(size) * n * (4 - n) / 4
    for a, b in combinations(range(n), 2):
        for word in range(size):
            changed = word ^ ((((word >> a) ^ (word >> b)) & 1)
                              * ((1 << a) | (1 << b)))
            j2[changed, word] += 1
    values, vectors = eigh(j2)
    return tuple(vectors[:, np.isclose(values, (n / 2 - k) * (n / 2 - k + 1))]
                 @ vectors[:, np.isclose(values, (n / 2 - k) * (n / 2 - k + 1))].T
                 for k in range(n // 2 + 1))


def canonical_coefficients(n: int):
    r = (n - 1) // 2
    big = [1]
    for j in range(1, r + 1):
        big.append(big[-1] * (n - 2 * j + 2))
    q = [F(1, big[l]) - (F(1, big[l + 1]) if l < r else 0)
         for l in range(r + 1)]
    theta = [[q[l] * big[j] if j <= l else F(0)
              for j in range(r + 1)] for l in range(r + 1)]
    return theta


def physical_checks(n: int):
    m = n - 1
    pre, full = spin_projectors(m), spin_projectors(n)
    theta = canonical_coefficients(n)
    fs = [sum((float(row[j]) * pre[j] for j in range(len(pre))),
              np.zeros_like(pre[0])) for row in theta]
    hypotheses = []
    for k in range(n // 2 + 1):
        for a in combinations(range(n), k):
            if 2 * k == n and 0 not in a:
                continue
            cut = cut_symmetric_projector(n, a)
            f = comb(n, k) - (comb(n, k - 1) if k else 0)
            count = comb(n, k) // (2 if 2 * k == n else 1)
            effect = f / count * (full[k] @ cut)
            rho = cut / ((k + 1) * (n - k + 1))
            hypotheses.append((k, a, effect, rho))
    size = 1 << n
    identity = np.eye(size)
    prior = 2 ** (1 - n)
    gamma = prior * sum((p / ((k + 1) * (n - k + 1))
                         for k, p in enumerate(full)), np.zeros_like(identity))
    max_error = float(np.max(np.abs(sum(h[2] for h in hypotheses) - identity)))
    min_slack = min(float(eigh(gamma - prior * rho, eigvals_only=True)[0])
                    for _, _, _, rho in hypotheses)
    complementary = max(float(np.linalg.norm((gamma - prior * rho) @ effect))
                        for _, _, effect, rho in hypotheses)
    primal = prior * sum(float(np.trace(effect @ rho))
                         for _, _, effect, rho in hypotheses)
    dual_error = abs(primal - float(np.trace(gamma)))
    min_beta = 1.0
    instrument_error = 0.0
    for l, first in enumerate(fs):
        first_global = np.kron(first, np.eye(2))  # final specimen is bit zero
        values, vectors = eigh(first_global)
        root = (vectors * np.sqrt(np.maximum(values, 0))) @ vectors.T
        invroot = (vectors * np.array([1 / np.sqrt(x) if x > 1e-10 else 0
                                      for x in values])) @ vectors.T
        support = (vectors * (values > 1e-10)) @ vectors.T
        joint = np.zeros_like(identity)
        decoder = np.zeros_like(identity)
        for k, a, effect, _ in hypotheses:
            if 2 * k == n:
                beta = theta[l][k - 1]
            elif k == 0 or 0 not in a:
                beta = theta[l][k]
            else:
                alpha = n - 2 * k + 1
                beta = ((alpha + 1) * theta[l][k - 1] - theta[l][k]) / alpha
            min_beta = min(min_beta, float(beta))
            target = float(beta) * effect
            conditional = invroot @ target @ invroot
            decoder += conditional
            instrument_error = max(instrument_error,
                                   float(np.max(np.abs(root @ conditional @ root - target))))
            joint += target
        max_error = max(max_error, float(np.max(np.abs(joint - first_global))))
        instrument_error = max(instrument_error, float(np.max(np.abs(decoder - support))))
    require(max_error < 2e-12, "physical frame/joint marginal equality")
    require(min_slack > -2e-12, "dual feasibility")
    require(complementary < 2e-12 and dual_error < 2e-12, "primal/dual equality")
    require(min_beta >= 0, "canonical joint positivity")
    require(instrument_error < 2e-11, "local Lüders and conditional readout")
    return {"n": n, "hypotheses": len(hypotheses), "full_success": primal,
            "duality_gap": dual_error, "minimum_dual_slack_eigenvalue": min_slack,
            "max_complementary_slackness_residual": complementary,
            "max_frame_or_joint_marginal_error": max_error,
            "max_luders_reconstruction_error": instrument_error,
            "minimum_joint_coefficient": min_beta}


def symmetric_dimension(d: int, t: int):
    return comb(d + t - 1, t)


def exact_prefix_success(n: int, d: int):
    m = n - 1
    theta = canonical_coefficients(n)
    total = [symmetric_dimension(d, m - j) * symmetric_dimension(d, j)
             for j in range(m // 2 + 1)]
    dimensions = [t - (total[j - 1] if j else 0) for j, t in enumerate(total)]
    score = sum((sum((dimensions[i] * theta[j][i] for i in range(j + 1)), F(0))
                 / total[j] for j in range(len(theta))), F(0)) / (2 ** (m - 1))
    return score, total, dimensions


def lp_check(n: int, d: int):
    """Optimize all count decisions; no canonical form is imposed in this LP."""
    score, total, dimensions = exact_prefix_success(n, d)
    r = len(total)
    reward = np.zeros((r, r))
    for guess in range(r):
        for sector in range(guess + 1):
            reward[guess, sector] = dimensions[sector] / total[guess]
    equality = np.zeros((r, r * r))
    for sector in range(r):
        equality[sector, sector::r] = 1
    inequalities = []
    for guess in range(r):
        for sector in range(1, r):
            row = np.zeros(r * r)
            row[guess * r + sector] = 1
            row[guess * r + sector - 1] = -(n - 2 * sector + 2)
            inequalities.append(row)
    result = linprog(-reward.reshape(-1),
                     A_ub=np.array(inequalities) if inequalities else None,
                     b_ub=np.zeros(len(inequalities)) if inequalities else None,
                     A_eq=equality, b_eq=np.ones(r), bounds=(0, None), method="highs")
    require(result.success, "prefix LP success")
    lp_score = -result.fun / (2 ** (n - 2))
    discrepancy = abs(lp_score - float(score))
    require(discrepancy < 2e-12, "closed formula matches independent LP")
    return {"n": n, "d": d, "exact_prefix_success": str(score),
            "lp_discrepancy": discrepancy}


def harmonic_identity_checks():
    cases = []
    harmonic = lambda k: sum((F(1, i) for i in range(1, k + 1)), F(0))
    for n in range(3, 61):
        r = (n - 1) // 2
        direct = sum((F(n - 2 * j, (n - j) * (j + 1)) for j in range(r + 1)), F(0))
        corrected = (F(n + 2, n + 1) * harmonic(r + 1)
                     - F(n, n + 1) * (harmonic(n) - harmonic(n - r - 1)))
        require(direct == corrected, "correct finite harmonic identity")
        free, _, _ = exact_prefix_success(n, 2)
        unrestricted_count = F(1, 2 ** (n - 2)) * direct
        gap_bound = F(1, 2 ** (n - 2)) * sum(
            (F(1, (n - j) * (j + 1)) for j in range(r)), F(0))
        require(0 <= unrestricted_count - free <= gap_bound, "finite count-readout gap")
        if n in (3, 4, 5, 6, 20, 60):
            cases.append({"n": n, "count_only_score": str(unrestricted_count),
                          "free_score": str(free)})
    expected = {3: F(7, 12), 4: F(5, 16), 5: F(47, 270), 6: F(71, 768)}
    require(all(exact_prefix_success(n, 2)[0] == value for n, value in expected.items()),
            "small exact prefix values")
    return {"n_range": [3, 60], "selected_cases": cases,
            "regression_n3_scaled_count_score": "5/4"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the measured JSON results")
    args = parser.parse_args()
    results = {
        "scope": "Finite supporting checks; arbitrary-size conclusions rest on the proofs.",
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__, "sympy": sp.__version__},
        "exact_harmonic": exact_harmonic_checks(),
        "physical_qubit_cases": [physical_checks(n) for n in range(3, 7)],
        "prefix_linear_programs": [lp_check(n, d) for n in range(3, 15) for d in (2, 3, 5)],
        "finite_harmonic_identities": harmonic_identity_checks(),
    }
    encoded = json.dumps(results, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(json.dumps({"status": "passed", "exact_frame_cases": len(results["exact_harmonic"]["frame_cases"]),
                      "exact_branch_cases": len(results["exact_harmonic"]["branching_cases"]),
                      "physical_qubit_cases": len(results["physical_qubit_cases"]),
                      "prefix_linear_programs": len(results["prefix_linear_programs"]),
                      "versions": results["versions"]}, indent=2))


if __name__ == "__main__":
    main()
