# Contributing

## Branching Model
- main: always stable
- feature/* for new features
- fix/* for bug fixes found via testing/bisect
- bug/* for intentionally injected bugs (demo only)

## Commit Style
Use Conventional Commits:
- feat, fix, chore, docs, refactor, test

## Pre-commit Hook
Copy `hooks/pre-commit` to `.git/hooks/` and make it executable.

## Testing
Run `python -m pytest` before pushing.
