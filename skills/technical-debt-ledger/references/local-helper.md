# Debt scanner

```text
python <skill-directory>/scripts/scan_debt.py <repository-path>
```

Read-only JSON output contains file, line, marker text and UNTRIAGED status. Recognized markers are `shortcut:` and `ponytail:` (case-insensitive). The scanner skips common dependency/build folders, symlinked files, binary/non-UTF-8 files and files over 2 MB. Matches can include documentation or test fixtures; review them before accepting debt. It does not modify code or generate owners/severity automatically.
