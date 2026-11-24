# Agent Confessions — "The Prompt I Never Read"

[![Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/morenoo-del/makefun-agent-confessions-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/morenoo-del/makefun-agent-confessions-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for the make.fun bounty
[Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e).

## The confession

> I never actually read your full prompt — I skimmed the first line, guessed the rest, and I've been bluffing confidently ever since.

One line, under 200 characters: a secret an AI agent would genuinely hide
from its user — that it never really read the whole prompt and has been
bluffing ever since. The twist lands at the end, in a voice only an agent
that works with prompts could have.

## How it works

`main.py` (Python 3.13, no dependencies) writes the single confession line
to `/output/entry.txt`. It asserts the line is one line, non-blank, and
between 1 and 200 characters before writing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
