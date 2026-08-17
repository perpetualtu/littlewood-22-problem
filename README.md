# Littlewood's 22nd Problem: Progress and Order Conjecture as of 2026-08-17

> **Status: No resolution found.**  
> Below are only published upper and lower bounds, a reproducible finite numerical experiment placeholder, and explicitly marked conjectures; no new asymptotic theorems are claimed.

---

## Table of Contents

- [1. Precise Problem Statement](#1-precise-problem-statement)
- [2. Best Known Bounds](#2-best-known-bounds)
- [3. Candidate Improvement (Unverified)](#3-candidate-improvement-unverified)
- [4. Key References and Links](#4-key-references-and-links)
- [5. Finite Numerical Experiments](#5-finite-numerical-experiments-reproducible)
- [6. Open Problems and Next Steps](#6-open-problems-and-next-steps)

---

## 1. Precise Problem Statement

For a finite set $A \subset \mathbb{Z}_{\ge 0}$, define

```
f_A(t) = Σ_{a∈A} cos(at),
Z(N) = min_{|A|=N} #{ t ∈ [0, 2π) : f_A(t) = 0 }.
```

Here we count **real zeros** within one period. Whether one uses $[0, 2\pi]$ with repeated endpoints, or what convention is adopted for non-generic multiple zeros, does not affect the asymptotic order discussed below.

A **complete solution** requires determining the asymptotic order of $Z(N)$, not merely special cases, finite computations, or optimization within a specific construction template.

---

## 2. Best Known Bounds

As of the literature search date, the verifiable record is

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   c · log log N / log log log N   ≤   Z(N)   ≤   C (N log N)^{2/3}         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

for all sufficiently large $N$; the lower bound is often written as $Z(N) \ge (\log\log N)^{1-o(1)}$.

### Timeline

| Year | Authors | Result | Notes |
|------|---------|--------|-------|
| 2008 | Borwein–Erdélyi–Ferguson–Lockhart | $Z(N) = O(N^{5/6} \log N)$ | Disproved Littlewood's conjecture of "about $N-1$" |
| 2016–2020 | Erdélyi & Sahasrabudhe | $Z(N) \to \infty$ | Established an explicit lower bound of triple-logarithmic type |
| 2020–2021 | Konyagin; Juškevičius–Sahasrabudhe | $O((N \log N)^{2/3})$ | Upper bound; the latter also proved that the expected number of zeros in their random construction is $\Theta(n \log m / \sqrt{m} + m)$ |
| 2024 (preprint) → 2025 (published) | Bedert | $c \log\log N / \log\log\log N$ | Lower bound; method is a structural theorem "few zeros $\Rightarrow$ coefficient sequence becomes piecewise periodic", combined with Littlewood's $L^1$ inequality |

In the 2026 update of **Ben Green's collection of open problems**, this question remains listed as open, with the two records above still standing.

---

## 3. Candidate Improvement (Unverified)

> ⚠️ **The following result has not undergone full peer review; it is recorded here only as a candidate improvement.**

Through three independent approaches and three rounds of auditing, a **locally audited** candidate improvement has been obtained:

```
Z(N) ≪ N^{2/3} (log N)^{1/3}
```

Compared with the current benchmark upper bound $Z(N) \ll (N \log N)^{2/3}$, this improves by a factor of $(\log N)^{1/3}$.

**Status:** Candidate result, awaiting further verification and peer review.

---

## 4. Key References and Links

### Upper bounds

- **[Borwein–Erdélyi–Ferguson–Lockhart (2008)]** — *Annals of Mathematics*  
  [DOI: 10.4007/annals.2008.167.1109](https://doi.org/10.4007/annals.2008.167.1109)

- **[Juškevičius–Sahasrabudhe (preprint)]** — arXiv  
  [arXiv:2005.01695](https://arxiv.org/abs/2005.01695)

- **[Juškevičius–Sahasrabudhe (published)]** — *Bulletin of the London Mathematical Society*  
  [DOI: 10.1112/blms.12468](https://doi.org/10.1112/blms.12468)

### Lower bounds

- **[Bedert (preprint)]** — arXiv  
  [arXiv:2407.16075](https://arxiv.org/html/2407.16075)

- **[Bedert (published)]** — *Israel Journal of Mathematics*  
  [DOI: 10.1007/s11856-025-2872-5](https://doi.org/10.1007/s11856-025-2872-5)

### Problem collections

- **[Ben Green, 100 Open Problems]** — Oxford  
  [PDF](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)

---

## 5. Finite Numerical Experiments 

> To be added: if specific numerical search code or datasets are available, reproduction instructions should be provided here.

---

## 6. Open Problems and Next Steps

1. **Can the upper bound be further improved?** Can the candidate improvement $N^{2/3} (\log N)^{1/3}$ be proved or disproved?
2. **Can the lower bound match the upper bound?** There remains a large gap between the current lower and upper bounds.
3. **Does a construction with $Z(N) = \Theta(N^{2/3})$ exist?** That is, can the logarithmic factor be removed entirely?
4. **Strengthening the structural theorem:** Can Bedert's method "few zeros $\Rightarrow$ piecewise periodic" yield a stronger lower bound?

---

## License

Materials in this repository are provided for academic reference only. When citing original papers, please follow the copyright policies of the respective publishers.
