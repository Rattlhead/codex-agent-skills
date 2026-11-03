# Provenance and conditional choices

## Evidence boundaries

The user-supplied research describes 51 sources, 37 principles, and 10 tensions. It states an original check date of 2026-11-01. These numbers and that date describe the supplied research. They do not establish that this package independently checked each source.

The full registry of 51 sources was not located. Do not invent entries, source titles, quotations, or a reconstructed registry.
This skill combines the stated requirements and selected verified material. It is not a joint vendor standard or a certification.

Directly fetched source facts are recorded separately below. A source can support a limited design choice without supporting the full method.
Keep fetch status and content scope explicit.

## Directly fetched facts

The authoring team fetched the following addressed sources on 2026-11-01. This was not a verification of the full 51-source registry. Publication dates were not established except where stated.

- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) recommends compact routing, progressive disclosure, and reassessment of rigid recipes. Its advice is model-specific. It does not establish universal measured savings for this skill.
- [OpenAI: Run long-horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex) describes one example with goals, non-goals, milestones, acceptance commands, and decision notes. Its multiple files and checks at each milestone are example practices, not mandatory rules for all work.
- [OpenAI: Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) describes an objective, outcome evidence, and constraints as a thread-scoped contract. Budget exhaustion does not mean completion. Product-specific behavior does not authorize this skill to create Goals or assume background execution support.
- [Anthropic: When to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop), dated 2026-10-22, reports enterprise comparisons that favor fewer contexts in some cases. It retains uses for verification, parallel work, and modular permissions. It does not establish a general agent-count rule.
- [Google Cloud: Choose a design pattern for an agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) discusses independent parallel subtasks and final synthesis with cost and complexity tradeoffs. Pattern selection depends on the task.
- [LangGraph: Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) distinguishes native thread graph checkpoints from durable stores. A written plan is not a substitute for a native runtime checkpoint.

The 37 normative requirements and the 10 choices below are an engineering synthesis from the explicit user contract. These source observations support limited choices; they do not make the whole method an official joint standard.

## Conditional choices

These are design decisions for this skill, not claims that all sources recommend one recipe.

A bounded source refresh on 2026-11-02 checked [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), particularly context retrieval and structured note-taking, and the durable project memory example in the OpenAI long-horizon article linked above. They support selective retrieval by paths/identifiers and durable notes outside active context. Retrieval overhead can itself waste context. The OpenAI example remains one coding experiment. The user-required index plus one file per step, single status authority, and delta/affected-frontier read protocol are engineering choices here, not official prescribed layouts or evidence of measured savings. This refresh does not reverify or redate the original research registry.

| Tension | Choose according to the task |
| --- | --- |
| Detailed or brief plan | Use an action and check for small work. Add explicit ownership and dependencies when work becomes long or coupled. |
| Staged roles or one cycle | Separate roles when handoffs or independent judgment add value. Otherwise keep one coherent owner. |
| Parallel or sequential | Run ready independent work concurrently when benefit exceeds coordination cost. Serialize shared resources or coupled decisions. |
| Full history or bounded contract | Supply minimum sufficient context through the actual supported API. Include critical constraints explicitly. |
| New check or reuse | Use valid evidence for unchanged relevant conditions. Run checks for changed content, named risks, or mandatory requirements. |
| Waves or ready dispatch | Dispatch ready work as prerequisites clear. Use waves when a shared boundary provides a concrete coordination benefit. |
| Mandatory TDD or project and risk checks | Obey the request and project rules. Select checks for actual risk and acceptance; do not impose TDD on every artifact. |
| Extra approval or existing authorization | Keep existing authorization. Obtain approval only for applicable scope changes or actions beyond it. |
| Upfront or rolling detail | First define outcomes and dependencies. Add detail to ready work when inputs become known. |
| Fixed recipe or reassessment | Reassess workflow, model, effort, and environment when evidence changes. Use current capabilities and available selection guidance. |
