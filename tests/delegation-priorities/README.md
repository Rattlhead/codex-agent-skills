# Delegation priority routing observations

This folder records a bounded, read-only routing trial against the updated `subagent-manager`, `task-model-router`, and universal-project coordination instructions. The seven raw scenarios and observed decisions are in `results.json`.

The `mode` field uses only `primary_only` or `delegate`. A separate `status` field records a blocker or continuation state.

## Method

- Read the current manager, router, template entrypoint, and coordination profile at the recorded revisions.
- Applied their actual gates to the supplied case facts. Did not execute the underlying project tasks, start workers, change permissions, or test runtime behavior.
- Recorded unknown model, effort, rate, and forecast inputs where the scenarios do not provide them. A route observation is not proof that a worker or a specific configuration is available in another runtime.
- Kept raw case facts separate from observations. These observations are not new routing oracles and do not retune existing expected outputs.

## Limits

This is a document-level case analysis. It does not measure model quality, latency, cost, context savings, tool availability beyond the stated case facts, or actual completion. No tests or project checks were run. The trial did not establish a numerical cost forecast. The source revision hashes identify the exact files assessed.
