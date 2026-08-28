# Dynamic Programming Study

<p align="center">
<a href="https://github.com/oldratlee/dynamic-programming-study/actions/workflows/ci.yml">
<img src="https://img.shields.io/github/actions/workflow/status/oldratlee/dynamic-programming-study/ci.yml?branch=main&logo=github&logoColor=white" alt="Build CI"></a>
<a href="https://app.codecov.io/gh/oldratlee/dynamic-programming-study/tree/main">
<img src="https://img.shields.io/codecov/c/github/oldratlee/dynamic-programming-study/main?logo=codecov&logoColor=white" alt="Codecov"></a>
<a href="https://www.apache.org/licenses/LICENSE-2.0.html">
<img src="https://img.shields.io/github/license/oldratlee/dynamic-programming-study?color=4D7A97&logo=apache" alt="License"></a>
<a href="https://github.com/oldratlee/dynamic-programming-study">
<img src="https://img.shields.io/github/repo-size/oldratlee/dynamic-programming-study" alt="GitHub repo size"></a>
<a href="https://gitpod.io/#https://github.com/oldratlee/dynamic-programming-study">
<img src="https://img.shields.io/badge/Gitpod-ready to code-339933?label=gitpod&logo=gitpod&logoColor=white" alt="gitpod: Ready to Code"></a>
</p>

Personal notes and implementations for dynamic programming, drawn from
LeetCode, CLRS (4th ed.), and Levitin *Introduction to the Design and
Analysis of Algorithms* (3rd ed.). Python 3.12+.

The point of this repo is to **compare DP strategies on the same problem**.
A second implementation (space-optimized, top-down memo, brute force, …)
is more useful than a new abstraction.

## Practices

Keep solvers small and comparable. One spec, several implementations;
tests run all of them. When adding a problem, follow this loop.

- **Readability counts.**
  - Docstring: module, function, statement, source, examples, constraints.
  - Each public function: the state, the recurrence, then
    `Time` / `Space` with the symbols defined.
  - Comment the DP transition and any non-obvious cost.
- **Keep the logic simple and clean.**
  - Write the recurrence as one expression when it fits.
  - Public API is functions; classes only for data structures.
  - Prefer a dummy / index sentinel or an early return
    over a special-case branch.
  - Return `int | None` when the result is impossible or absent;
    do not use a magic value like `inf`.
  - No unused helpers or shared framework.
- **Strategy over abstraction.**
  - Prefer another solver of the same spec over a shared framework.
  - Keep *problem* variants separate from *algorithm* variants.
    Encode problem variants in the type.
- **Reliability.**
  - Types as contracts, `collections.abc.Sequence` for read-only inputs.
  - PEP 695 generics when a structure needs them.
  - `assert` preconditions.
- **Constant factors count.**
  - Avoid an intermediate slice when a cheaper equivalent exists.
  - Rolling state and index-based recursion are first-class variants.
- **One test body.**
  - Parametrize `impl` over every solver of a spec.
  - Empty and edge cases first, then book or LeetCode samples.

## Setup and commands

```bash
poetry sync                     # env + dependencies from pyproject.toml

poetry run pytest               # unit tests (benchmarks off)
poetry run pytest -m benchmark  # perf only
poetry run pytest -m ""         # everything, as in CI

poetry run flake8 src tests     # style lint
poetry run isort src tests      # sort imports
poetry run mypy src             # type check

./scripts/run.sh                # pytest + flake8 + isort + mypy
```

Default `pytest` skips `@pytest.mark.benchmark` cases (`-m "not benchmark"`).
Benchmark inputs stay small enough that brute-force variants can still run.

## Problems from Chapter 8 of Levitin IDAA 3e

- [`ch8_1_example1_coin_row.py`](src/idaa3e/ch8_1_example1_coin_row.py)
  — Chapter 8.1 Example 1 Coin-row
- [`ch8_1_example2_change_making.py`](src/idaa3e/ch8_1_example2_change_making.py)
  — Chapter 8.1 Example 2 Change-making
- [`ch8_1_example3_coin_collecting.py`](src/idaa3e/ch8_1_example3_coin_collecting.py)
  — Chapter 8.1 Example 3 Coin-collecting
- [`ch8_2_knapsack.py`](src/idaa3e/ch8_2_knapsack.py)
  — Chapter 8.2 Knapsack

## Problems from CLRS 4e

- [`ch14_1_rod_cutting.py`](src/clrs/ch14_1_rod_cutting.py)
  — Chapter 14.1 Rod Cutting

## LeetCode

- [`p3_longest_substring_without_repeating_characters.py`](
  src/leetcode/p3_longest_substring_without_repeating_characters.py)
  — [3. Longest Substring Without Repeating Characters](
  https://leetcode.com/problems/longest-substring-without-repeating-characters)
- [`p23_merge_k_sorted_lists.py`](src/leetcode/p23_merge_k_sorted_lists.py)
  — [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)
- [`p53_maximum_subarray.py`](src/leetcode/p53_maximum_subarray.py)
  — [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)
- [`p139_word_break.py`](src/leetcode/p139_word_break.py)
  — [139. Word Break](https://leetcode.com/problems/word-break)
