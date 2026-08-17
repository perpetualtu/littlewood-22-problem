"""Finite stress tests for the textbook proof.

These tests are diagnostic only; they are not substitutes for the analytic proof.
They use only Python's standard library and do not access the network.
"""

from __future__ import annotations

import itertools
import math
import random


def length_energy_scan() -> tuple[float, tuple[int, float]]:
    """Scan Lemma 4.1 on endpoint-heavy and uniform grids."""
    best = (float("inf"), (0, 0.0))
    for length in range(2, 161):
        points = [10.0 ** (-k) / length for k in range(1, 11)]
        points += [c / length for c in (0.1, 0.25, math.pi / 4, 1, 2, 3)]
        points += [math.pi * j / 4000 for j in range(1, 2001)]
        for t in points:
            if not (0.0 < t <= math.pi / 2):
                continue
            lhs = sum(math.sin(r * t) ** 2 for r in range(length, 2 * length)) / length
            rhs_scale = min((length * math.sin(t)) ** 2, 1.0)
            ratio = lhs / rhs_scale
            if ratio < best[0]:
                best = (ratio, (length, t))
    return best


def phase_scan() -> tuple[float, tuple[int, int, float, float]]:
    """Scan the non-resonant phase average in Lemma 5.2."""
    d = 4.0
    best = (float("inf"), (0, 0, 0.0, 0.0))
    for length in (2, 3, 4, 8, 16, 31):
        for q in (8, 9, 16, 31, 64):
            for ix in range(1, 4000):
                x = math.pi * ix / 4000
                if abs(math.sin(4 * length * x)) <= d / q:
                    continue
                for alpha in (0.0, 0.17, math.pi / 4, math.pi / 2, 2.3):
                    avg = sum(
                        math.cos(4 * length * j * x + alpha) ** 2
                        for j in range(q)
                    ) / q
                    if avg < best[0]:
                        best = (avg, (length, q, x, alpha))
    return best


def lo_bruteforce() -> tuple[float, tuple[tuple[float, ...], float, float]]:
    """Brute-force small weighted Bernoulli sums against Lemma 6.1's scale."""
    rng = random.Random(20260817)
    worst = (0.0, ((), 0.0, 0.0))
    for r in range(2, 13):
        for _ in range(200):
            weights = tuple(rng.choice((-1, 1)) * rng.randint(1, 7) for _ in range(r))
            atom = min(abs(v) for v in weights)
            sums = [
                sum(bit * weight for bit, weight in zip(bits, weights))
                for bits in itertools.product((0, 1), repeat=r)
            ]
            candidates = sorted(set(sums))
            for width in (0.0, atom / 4, atom / 2, atom, 2 * atom):
                for center in candidates:
                    probability = sum(abs(v - center) <= width for v in sums) / len(sums)
                    normalized = probability * math.sqrt(r) / (1 + width / atom)
                    if normalized > worst[0]:
                        worst = (normalized, (weights, center, width))
    return worst


def parameter_scan() -> list[tuple[int, int, int, int, bool]]:
    """Check support, exact term count, and n > m for sample large N."""
    rows = []
    for target in (10**3, 10**4, 10**6, 10**9):
        m = math.ceil(target ** (2 / 3) * math.log(target) ** (1 / 3))
        length = max(1, math.floor(math.log(m)))
        q = (m + 1) // (4 * length)
        max_k = 2 * length * q
        n = target + max_k - 1
        rows.append((target, m, length, q, n > m and n + 1 - max_k == target))
    return rows


def main() -> None:
    energy = length_energy_scan()
    phase = phase_scan()
    lo = lo_bruteforce()
    params = parameter_scan()
    print("length_energy_min_ratio", energy)
    print("nonresonant_phase_min", phase)
    print("LO_max_normalized", lo)
    print("parameter_rows", params)
    assert energy[0] > 1e-3
    assert phase[0] >= 3 / 8 - 1e-10
    assert lo[0] < 4.0
    assert all(row[-1] for row in params)


if __name__ == "__main__":
    main()
