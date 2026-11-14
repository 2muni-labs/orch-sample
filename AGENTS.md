# AGENTS.md

Rules for every agent working in this repository. Codex reads this file
automatically; Claude Code imports it through `CLAUDE.md`.

## Project

`orch-sample` is a small library of text utilities. It is a sample target used
to verify `orch`, the orchestrator in `2muni-labs/orchestrator`. It is public.

## Technical conventions

- Python 3.14, standard library only at runtime.
- Type hints on all function signatures.
- `pytest` and `ruff` are development-only dependencies.
- Run tools from the environment that `uv sync --frozen` created, for example
  `.venv/bin/python -m pytest`. `uv run` does not work inside the sandbox.
- Code, identifiers, file names, commit messages and pull request text are in
  English.

## Layout

```
src/orch_sample/  library modules, one topic per module
tests/            tests, owned by the main agent
```

## Shared files

`pyproject.toml`, `uv.lock`, `.gitignore`, `AGENTS.md`, `CLAUDE.md`,
`.claude/` and `.github/` belong to the main agent. A sub-agent that needs one
changed reports `BLOCKED` with the request.
