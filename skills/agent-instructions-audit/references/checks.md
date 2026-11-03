# Audit criteria

Use the IDs below to identify findings and coverage. These criteria are a local audit method.
They are not a certification standard or a proof of model behavior.

| ID | Criterion | Evidence and decision |
| --- | --- | --- |
| A01 | Duplicate rules | Compare the action, condition, scope, role, priority, and exceptions. Record rules as duplicates only when they give the same requirement in the same context. Use this criterion for exact and paraphrased duplicates. Keep necessary scoped guidance and explicit exceptions. |
| A02 | Unnecessary text | Find text with no necessary action, condition, constraint, criterion, or explanation. Show that removal keeps the requirements unchanged. General background can be necessary. Brevity alone is not a goal. |
| A03 | Conflicts | Give a scenario where applicable rules make incompatible actions mandatory. Include absolute rules that prevent a necessary exception or reassessment. If instruction precedence lets one rule override another, do not record the override as a conflict. |
| A04 | Scope | Examine each rule's task, path, role, and stage. Record uncertainty that can change behavior. If its section gives clear scope, do not make each rule give that scope again. |
| A05 | Activation conditions | Examine activation and exclusion conditions for a profile, skill, or procedure. Record triggers that do not start necessary work or that make unrelated procedures mandatory. Reading a profile does not make every procedure mandatory. |
| A06 | Local references | Use the target format to find targets of actual file links, reference-style links, paths, and heading anchors. Examine case and symbolic links where necessary. A missing file or a confirmed wrong anchor is a defect. Example paths with explicit labels are not live references. If anchor behavior is unknown, record it as unverified. |
| A07 | External references | If access is available and necessary, examine the target content. A confirmed missing page or wrong destination is a defect. Authentication failures, timeouts, temporary server errors, and no network access do not prove that a link is broken. Record untested links as untested. |
| A08 | Document discovery | Show how an agent gets a necessary document at the relevant stage. Record missing, outdated, or misleading routes with evidence for the necessary source. Do not make a root entry file list every document. |
| A09 | Read cycles | Show the sequence of necessary reads and their stopping conditions. Links can refer to each other for information. Record mandatory recursive reads or repeated procedure calls with no stopping condition. |
| A10 | Context load | Find mandatory material unrelated to a scenario or role. Show automatic loads and conditional reads as different categories. Give a decomposition proposal by responsibility and read condition. Length alone is not a defect in a necessary document. |
| A11 | Repeated actions | Find reads, checks, exports, and queries that occur again with unchanged inputs. Record a defect only if no failure or evidence gap gives a reason to do the action again. Keep affected checks after meaningful changes and necessary integration checks. |
| A12 | Feasibility and freshness | Compare named commands, paths, tools, versions, and capabilities with relevant current evidence. If current data is necessary for the rule, examine its dates. Without evidence, do not say that a dependency exists. Do not install or start it during an audit. Missing evidence gives an unknown result. |
| A13 | Ownership and authority | Examine owners of results and shared resources. Examine write boundaries, acceptance responsibility, reuse scope, and approval requirements. Record concurrent owners who can cause conflicts and instructions that give permissions without authority. Keep explicit user authorization. |
| A14 | Maintained source | Examine whether a contract, procedure, or rate table has competing authoritative copies. A route or short explanation of a dependency is permitted. An explicit historical example is not another current source. If evidence shows drift or duplicate maintenance, give a proposal for one maintained source. |
| A15 | Clear and verifiable language | Compare description and UI fields with the applicable user or project language policy. Examine the language of the instruction body separately. English can be permitted. If ambiguity can change behavior, examine the actor, condition, action, and observable completion result. Context and imperative form can make these clear. Use one consistent term per concept. If necessary, give its meaning at first use. Keep exact technical names and identifiers. Do not use new abbreviations or remove constraints and exceptions for brevity. Use the applicable English or Russian language rules. Before an ASD-STE100 conformance statement, do the normative rule and dictionary checks. Do not give that statement for Russian text. |
| A16 | Scenario behavior | Show the paths for relevant normal, boundary, and unavailable dependency cases. Examine necessary profiles, actions, acceptance, and reassessment. Record a static trace and a live run as different evidence levels. If coding procedures are unnecessary, do not make them mandatory for documents, data, graphics, or other work. |

## Avoid false positives

- A local file's existence does not prove that the runtime loaded it or that an agent used it.
- A runtime size limit concerns the actual instruction chain and configuration. Do not substitute a universal word limit.
- A static size check can show a delivery risk. For actual truncation, evidence of instruction delivery is necessary.
- An optional link does not make reading the whole linked document mandatory.
- A supplied example is not an instruction to run its commands.
- A permission to review is not permission to apply corrections.

## Sources and limits

These sources informed the method. Open them only for a concrete documentation question or changed runtime behavior.

- [OpenAI: AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md): instruction chains, overrides, and configured size limits. These are Codex rules; do not apply them to every runtime.
- [OpenAI: build skills](https://learn.chatgpt.com/docs/build-skills): skill discovery and progressive disclosure.
- [OpenAI: rethink skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): conditional document reads and removal of unnecessary scaffolding. Model-specific advice is not evidence that every model needs the same changes.
- [Anthropic: context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): relevant context, clear instructions, and sufficient specificity.
- [GitHub: customization features](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features): persistent instructions and workflow-specific skills. Copilot-specific loading rules do not establish Codex behavior.
