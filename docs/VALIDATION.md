# Validation record — 2026-10-27

Version: 0.1.0. Environment: Windows, bundled Python 3.12. Tests use temporary fixtures; no real compute job, external message, manuscript submission or account mutation was performed.

| Check | Result | Evidence and scope |
|---|---|---|
| Catalog and source targets | PASS | tools/validate.py: 69 Skills, 113 canonical mappings; local references and package layout checked |
| Bundled skill-creator validator | PASS | quick_validate.py accepted 69/69 Skill folders with PyYAML 6.0.3 available only in ignored validation dependencies |
| Local executable suite | PASS | `python -m unittest discover -s tests -v`: 29 tests, all passed |
| Codex-style installation | PASS, file-level only | Tests install a complete Skill into an isolated directory, execute its copied helper, check receipts, idempotency, conflict rejection and safe removal |
| Queue resume and failures | PASS | Successful job not relaunched; failed job not auto-retried; changed manifest, active lock and ambiguous launch rejected; timeout remains UNKNOWN |
| Numeric SVG helper | PASS | Real CSV fixture parsed; provenance hash checked; missing/nonfinite data and overwrite rejected; negative bar geometry checked |
| Diagram helper | PASS | XML and text escaping, border anchors, missing endpoints, schema mismatch and label overflow checked |
| SVG visual QA | PASS, two fixtures | accuracy.svg and diagram.svg rendered to PNG with Sharp and visually inspected for clipping, labels and arrows; synthetic data only |
| Debt scanner | PASS | Fixture line numbers preserved and dependency-directory matches excluded |
| ZIP packaging | PASS | Test archive has both Claude manifests and 69 Skills; each packaged file hash verified; validation dependencies excluded |
| Claude Code native validator | PASS | Linux, Claude Code 2.1.296: `claude plugin validate .` exited 0 with "Validation passed" |
| Claude Code marketplace install/discovery | PASS, live | Linux, Claude Code 2.1.296: `claude plugin marketplace add giaminhgist/Minh-Agent` cloned and validated the public repo; `claude plugin install minh-agent@minh-agent-marketplace` installed commit 09320a9ca80e3c545442145abbd6fad72ca8b4b8 (scope user). Skill discovery from this new install in a fresh session not separately observed |
| Codex live discovery | NOT_RUN | Installer packaging tested; no global installation or separate live-host reload performed |
| OpenCode live discovery | NOT_RUN | No OpenCode runtime test |
| 69 model-behavior acceptance cases | NOT_RUN | Cases are in tests/acceptance-cases.json; no independent model evaluator was run |
| External providers/services | NOT_RUN | Search/reviewer adapters, image backend, cloud compute, Overleaf, Lean and full forensic engine not exercised |

## Failures found and corrected

The first local suite could not write into sandbox temporary directories. It was stopped and rerun through the authorized execution mechanism. This environmental failure was not counted as a helper result.

The first unrestricted run exposed an uninstall failure: OneDrive source-directory read-only attributes were copied into installed folders. The installer now makes its newly staged copy owner-writable, then verifies content hashes before placement. The full suite passed after this fix.

The README install section still described a local-only flow and claimed no GitHub repository existed. It now documents the published marketplace flow (`claude plugin marketplace add giaminhgist/Minh-Agent`) and a regression test guards it.

## What the result does not prove

Passing these tests establishes specific local behaviors and packaging invariants. It does not establish model-level usefulness, every source mode/flag, every host integration, source-variant parity, or production reliability. No speed/token savings are claimed. The acceptance and runtime gaps remain visible in COVERAGE.md.

## Reproduction

```sh
python tools/validate.py
python -m unittest discover -s tests -v
```

For the authoritative Claude check on a machine with Claude Code:

```sh
claude plugin validate .
claude --plugin-dir .
```

Then invoke a plugin command and inspect the actual discovered name and output. Keep native-host results separate from the offline suite and append real evidence when available.
