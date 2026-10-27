# Local queue adapter

Requires Python 3.10+. This is a serial local adapter, not a replacement for SSH/screen, GPU wave scheduling, Modal or Vast. Use trusted executable argv lists; a manifest is executable code, not harmless data.

```json
{"schema":"local-queue-v1","jobs":[{"id":"seed-1","argv":["python","train.py","--seed","1"],"cwd":".","timeout_seconds":300}]}
```

The working directory is relative to the manifest. Use an absolute interpreter executable if `python` does not resolve in the host.

```text
python <skill-directory>/scripts/local_queue.py jobs.json run-state.json
python <skill-directory>/scripts/local_queue.py jobs.json run-state.json --execute
```

The first command is a dry-run. Execution persists `running` before launch, captures stdout/stderr, and records completion. Successful and failed jobs are skipped on resume; failed jobs require an explicit reviewed retry manifest. A changed manifest cannot reuse prior state. A crash leaves a lock and/or running state; inspect the recorded owner, processes, logs and outputs before manually reconciling them. Never delete a lock simply because it is old.

Timeout is UNKNOWN: Python kills the directly launched process, but child processes may remain. Reconcile them before resuming. No process-tree cleanup or automatic retry is claimed. The helper does not launch background monitors or send notifications.
