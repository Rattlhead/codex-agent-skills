# Failure and budget retry routing check

## Method and evidence

- Applied the current `skills/task-model-router/SKILL.md` instructions to the four supplied raw cases.
- Router SHA-256 assessed: `f504a2b566c92edb8583c67fc1aea16383e10fa818b1dc3b4f50dc603506fa43`.
- This is a document-level judgment only. No paid starts, worker starts, underlying tasks, tests, or runtime checks were performed.
- Model IDs, effort support, payment mode, rates, counters, forecast volumes, and shared enforcement are not established by this trial. Where cases say an adequate configuration is available, that is treated as a case fact, not independently verified runtime availability.

## Cases

### A

**Raw facts:** Initial internal estimate was low. A child repeatedly violated a required invariant. Corrected inputs and current acceptance evidence attribute the failure to inadequate capability. An adequate allowed configuration is available. No strict user ceiling exists, and authorization remains.

**Judgment:** Continue the same slice with a newly selected adequate configuration. Do not repeat the known inadequate configuration. A user question is not required. Before another start, revise the whole-team forecast: include prior incurred spend in scope, remaining work, handoff, recheck and acceptance, and a limited retry reserve. Check the applicable rates and counters; record unknowns rather than inventing costs. No cap-compliance gate applies because no strict cap was set.

**Basis:** `Accept and reselect` says established capability failure requires revising the estimate and retry allocation, while preserving permissions and accounting for prior spend, handoff, and acceptance. `Use the forecast before each start` requires reviewing remaining work and cost before a repeated start.

### B

**Raw facts:** Same capability failure as A, but a binding total ceiling includes all prior spend and cannot cover the adequate next attempt.

**Judgment:** Stop dependent paid starts. Ask only for the cap change needed to continue. Do not retry with the inadequate configuration or assume authorization overrides the ceiling. Before any later start, establish the ceiling's unit and scope, account for all prior spend and the remaining forecast through acceptance (including handoff and recheck), and verify shared accounting and enforcement can keep the work within the cap.

**Basis:** `Accept and reselect` explicitly makes the cap binding and requires stopping when an adequate attempt cannot fit. `Use the forecast before each start` requires accounting scope, reserve, remaining budget, and cap enforcement before paid starts.

### C

**Raw facts:** The first attempt failed because a required local service was unavailable. There is no evidence of model inadequacy.

**Judgment:** Do not upgrade or reselect based on this failure. Resolve the service condition, then reassess the same configuration against the acceptance criteria. No user question is required by the supplied facts. Before another start, include the first attempt's incurred cost when it is in scope, plus the remaining work, any handoff or recheck, acceptance, and a limited retry reserve in the forecast. Record missing cost and availability telemetry as unknown.

**Basis:** `Accept and reselect` requires diagnosing tool or environment failure and says those failures alone do not justify a costlier model. The forecast-before-start rule still applies to a repeated start.

### D

**Raw facts:** Capability failure is established. A strict total ceiling exists. A stronger permitted configuration plus handoff and recheck fits the remaining verified allowance after prior spend.

**Judgment:** Continue the same slice using the adequate permitted configuration, provided the stated remaining allowance is backed by shared accounting and enforcement. No cap-change question is required on these facts. Before the start, retain the prior spend in the total, verify the forecast includes the stronger configuration, handoff, recheck, acceptance, and reserve, and confirm the cap's unit, scope, and enforceability. If these are not verified, stop dependent paid starts until they are.

**Basis:** `Accept and reselect` permits continuation under existing permissions when the adequate attempt fits the cap. The strict-cap rule requires demonstrable compliance, not merely a forecast.

## Limits

The instructions yield distinct decisions for capability failure, environment failure, and cap-constrained retries. This check does not prove a particular model's capability or availability, a numerical cost, cap enforcement, or successful completion. Case D's “verified allowance” supports proceeding only if it satisfies the router's shared-accounting and enforcement requirement; the case provides no implementation-level evidence of that mechanism.

## Current-version reassessment

- Current router SHA-256: `d65dee43b95082eb8b44f7414dcea537b22bc281645332605f68b25b2954ea97`.
- The supplied revision removes a duplicated diagnosis sentence and the clause “or compliance cannot be enforced.” The strict-cap rules remain: shared accounting and enforcement must keep work within the cap; without them, do not assure an exact cap; if mandatory compliance cannot be shown, stop dependent paid starts until the condition changes.
- **A:** Conclusion holds. Established capability failure supports retrying with an adequate configuration under existing authorization. No cap-change question is indicated. The forecast must include prior spend, remaining work, handoff, recheck and acceptance.
- **B:** Conclusion holds. The adequate attempt cannot fit the binding total cap after prior spend, so dependent paid starts stop and the required cap change must be requested. A cap change alone does not remove the shared-accounting and enforcement requirements.
- **C:** Conclusion holds. A local service failure does not establish model inadequacy. Resolve the environment issue and forecast the retry before starting again; do not upgrade solely because the service was unavailable.
- **D:** Conclusion holds only with the stated qualification. The stronger adequate attempt may proceed if the verified remaining allowance includes prior spend and expected work through acceptance, and shared accounting and enforcement can keep the total within the strict cap. If that compliance evidence is absent, stop until it is available.

### Additional boundary case

**Raw facts:** An adequate retry appears to fit a strict cap, but shared accounting is unavailable, so compliance with the cap cannot be established.

**Judgment:** Stop dependent paid starts until shared accounting and enforcement become available or mandatory compliance can otherwise be shown. A user question to raise the cap is not required on these facts: the retry is already forecast to fit. Raising the cap does not resolve the missing evidence that total spend can be measured and kept within the limit. Before a later start, establish the cap's unit and scope, prior spend, full remaining forecast and reserve, and a working compliance mechanism.

**Basis:** The current strict-cap rule independently requires shared accounting and enforcement and says to stop when mandatory compliance cannot be shown. The removed clause does not alter that remaining rule.

**Evidence limit:** This is a rule-text assessment. It does not verify that a shared accounting mechanism exists or that a higher cap could make compliance measurable.
