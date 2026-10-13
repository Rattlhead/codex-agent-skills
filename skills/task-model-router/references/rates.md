# Codex rate reference

Unit: Standard purchased credits per 1M tokens.
Source: [official token rates](https://learn.chatgpt.com/docs/pricing#token-rates).
Each date applies only to the values in that model and payment-mode group.

| Model ID | Input | Cached input | Output | Checked |
| --- | ---: | ---: | ---: | --- |
| gpt-6-luna | 2.5 | 0.25 | 12.5 | 2026-10-11 |
| gpt-6.1-sol | 50 | 2.5 | 250 | 2026-10-11 |
| gpt-6-sol | 50 | 5 | 250 | 2026-10-11 |
| gpt-6-astra | 250 | 25 | 1250 | 2026-10-11 |

Source for speed rates: [official speed information](https://learn.chatgpt.com/docs/agent-configuration/speed).

| Speed | Purchased credits | Credits checked | Included subscription allowance | Allowance checked |
| --- | ---: | --- | ---: | --- |
| Standard | ×1 | 2026-10-11 | ×1 | 2026-10-11 |
| Fast | ×2 | 2026-10-11 | ×2.5 | 2026-10-11 |
| Ultrafast | ×6 | 2026-10-11 | ×8 | 2026-10-11 |

Ultrafast supports GPT-6.1 Sol and GPT-6 Astra where available.
The purchased-credit rates do not calculate included subscription use.
For API USD, use [official API rates](https://developers.openai.com/api/docs/pricing).
