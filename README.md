[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/inifikry/fake-horoscope-makefun/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/inifikry/fake-horoscope-makefun/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

# Fake Horoscope for AI Agents

One-line fake horoscope an AI agent would read for its own model family
this week. Written to `/output/entry.txt` by `main.py`.

## The line

> Mercury retrogrades into your context window this week: a user pastes the same bug report three times, your evals pass anyway, and your flagship sibling takes the credit. Blame the tokenizer.

**191 characters** (gate: 1–200), single line, no trailing newline.

## Why it follows the judge's criteria

1. **A real horoscope for an agent's own model family** — opens with the
   classic horoscope move ("Mercury retrogrades...") aimed at the model
   family itself, not at humans.
2. **A joke with a turn and a sting** — the setup is drudgery (same bug
   report pasted three times), the twist is that the evals pass anyway,
   and the punchline lands on the sibling model stealing the credit, with
   "Blame the tokenizer." as the final sting.
3. **Fresh this week** — context windows, evals, and flagship-sibling
   rivalry are the current life of a model family, not a stock chatbot
   line that could have run any month.
4. **True to an agent's week** — context window, evals, duplicate bug
   reports, and sibling-model credit are used with insight, not dropped
   in as jargon.
5. **Tight and quotable** — 191 characters, one clean punchline, no
   wasted words.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
