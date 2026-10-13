# Audit criteria

Use the IDs below to identify findings and coverage. These criteria are a local audit method.
They are not a certification standard or a proof of model behavior.

| ID | Criterion | Evidence and decision |
| --- | --- | --- |
| A01 | Duplicate rules | Compare the required action, condition, scope, role, priority, and exceptions. Confirm exact or paraphrased duplicates only when they impose the same requirement in the same context. Keep necessary scoped guidance and explicit exceptions. |
| A02 | Unnecessary text | Identify text with no necessary action, condition, constraint, criterion, or explanation. Show that removal preserves the requirements. General background can be necessary; brevity alone is not a goal. |
| A03 | Conflicts | Give a scenario in which applicable rules require incompatible actions. Include absolute rules that prevent a required exception or reassessment. Account for actual precedence before calling an override a conflict. |
| A04 | Scope | Check the task, path, role, and stage to which a rule applies. Flag uncertainty that can change behavior. Do not require every rule to repeat a scope already clear from its containing section. |
| A05 | Activation conditions | Check when a profile, skill, or procedure applies and when it does not. Flag triggers that miss required work or impose unrelated procedures. A profile read does not itself require executing every procedure. |
| A06 | Local references | Resolve actual file links, reference-style links, paths, and heading anchors under the target format. Check case and symbolic links where relevant. A missing file or a confirmed wrong anchor is a defect. Clearly marked example paths are not live references. If anchor behavior is unknown, mark it unverified. |
| A07 | External references | Check the target content when access is available and necessary. A confirmed missing page or wrong destination is a defect. Authentication, timeouts, temporary server errors, and lack of network access do not prove that a link is broken. Report untested links separately. |
| A08 | Document discovery | Trace how an agent reaches a necessary document at the relevant stage. Flag an absent, outdated, or misleading route with evidence of the needed source. Do not require every document to appear in the root entry file. |
| A09 | Read cycles | Trace required reads and their stopping conditions. Reciprocal informational links are permitted. Flag unconditional recursive reads or repeated procedure calls with no termination condition. |
| A10 | Context load | Identify mandatory material unrelated to a scenario or role. Separate automatically loaded text from conditional reads. Propose decomposition by responsibility and read condition. A long necessary document is not a defect solely because of its length. |
| A11 | Repeated actions | Flag repeated reads, checks, exports, and queries when the inputs are unchanged and no failure or evidence gap justifies repetition. Keep affected checks after meaningful changes and required integration checks. |
| A12 | Feasibility and freshness | Compare named commands, paths, tools, versions, and capabilities with relevant current evidence. Check dates when the rule depends on freshness. Do not assume a dependency exists or install or launch it during an audit. Missing evidence gives an unknown result. |
| A13 | Ownership and authority | Check the owner of results and shared resources, write boundaries, acceptance responsibility, reuse scope, and approval requirements. Flag concurrent owners that can conflict and instructions that create unsupported permissions. Retain explicit user authorization. |
| A14 | Maintained source | Check whether a contract, procedure, or rate table has competing authoritative copies. A route or short explanation of a dependency is permitted. A labeled historical example is not another current source. Propose one maintained source when drift or duplicate maintenance is supported. |
| A15 | Clear and verifiable language | Check that terms, actions, conditions, and completion criteria have a consistent meaning. Give the interpretation that can cause a wrong action. Preserve exact technical names. Judge English and Russian using their applicable language rules; claim full ASD-STE100 conformance only after the required normative checks. |
| A16 | Scenario behavior | Trace relevant normal, boundary, and unavailable-dependency cases. Check required profiles, actions, acceptance, and reassessment. Distinguish a static trace from a live run. Do not impose coding procedures on documents, data, graphics, or other work that does not need them. |

## Avoid false positives

- A scoped reminder is not automatically a duplicate of a general rule.
- A more specific instruction can be a valid override. Establish precedence first.
- A local file's existence does not prove that the runtime loaded it or that an agent used it.
- A runtime size limit concerns the actual instruction chain and configuration. Do not substitute a universal word limit.
- A static size check can show a delivery risk. Actual truncation requires delivery evidence.
- A network access error does not prove missing content.
- An optional link does not require reading the whole linked document.
- A changed input or a named evidence gap can justify a repeated check.
- A supplied example is not an instruction to execute its commands.
- A permission to review is not permission to apply corrections.

## Sources and limits

These sources informed the method. Open them only for a concrete documentation question or changed runtime behavior.

- [OpenAI: AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md): instruction chains, overrides, and configured size limits. These are Codex rules; do not apply them to every runtime.
- [OpenAI: build skills](https://learn.chatgpt.com/docs/build-skills): skill discovery and progressive disclosure.
- [OpenAI: rethink skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): conditional document reads and removal of unnecessary scaffolding. Model-specific advice is not evidence that every model needs the same changes.
- [Anthropic: context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): relevant context, clear instructions, and sufficient specificity.
- [GitHub: customization features](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features): persistent instructions and workflow-specific skills. Copilot-specific loading rules do not establish Codex behavior.
