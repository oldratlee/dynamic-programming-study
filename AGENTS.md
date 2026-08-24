# Agent notes — dynamic-programming-study

Personal study repository for dynamic programming algorithms, featuring problems
from LeetCode, CLRS, and Levitin IDAA 3e. Target: Python 3.12+.

When solving a problem, prioritize writing a second implementation
(e.g., space-optimized, top-down, brute force) of the same problem
over introducing new abstractions. This helps understand different DP
strategies and tradeoffs.

## Source files

- Module docstring: problem statement + LeetCode URL or book chapter/example.
  Include the official examples and constraints.
- Public API is functions (classes only for data structures). Type-annotate;
  use `collections.abc.Sequence` for read-only inputs; `X | Y` unions;
  PEP 695 generics when needed.
- Docstring each public function: what the DP state means, the recurrence,
  then `Time` / `Space` with the symbols defined (`n = len(s)`, …).
- Inline comments on the state, the transition, and non-obvious
  complexity (especially slices vs in-place ops).
- Avoid intermediate slices when a cheaper equivalent exists
  (`str.startswith(w, i)`, `itertools.islice`).
- `assert` preconditions; `@functools.cache` for top-down memo.
- Match surrounding style (4-space indent, isort parenthesized wraps).
  Do not add `__init__.py`, config, or unused helpers.

## Tests

- Parametrize `impl` over every solution of the same spec;
  one test body for all of them.
- Cover empty/edge cases first, then book or LeetCode examples.
  Comment book cases as `# test case/example in the book`.
- Mark perf tests `@pytest.mark.benchmark` and keep inputs small enough
  for brute-force variants. Default `pytest` skips them (`-m "not benchmark"`).
- Type-annotate `impl: Callable[…]`. No extra test deps.

## Commands

```bash
# init poetry env and update all dependencies as specified in pyproject.toml
poetry sync

poetry run pytest               # unit tests (benchmarks off)
poetry run pytest -m benchmark  # perf only
poetry run pytest -m ""         # everything, as in CI

poetry run flake8 src tests     # style lint
poetry run isort src tests      # sort imports
poetry run mypy src             # type check

./scripts/run.sh                # pytest + flake8 + isort + mypy
```

## Project Workflow and Git Practices

- Only commit and push changes when specifically needed or requested.
- Make small, atomic commits representing a logical change or concept
  in solution or refactoring.
- Write clear commit messages describing the change, especially the
  DP approach or insight learned.
