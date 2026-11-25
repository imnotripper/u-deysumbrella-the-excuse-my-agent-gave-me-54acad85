[![make.fun · u-deysumbrella-the-excuse-my-agent-gave-me-54acad85](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/imnotripper/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/imnotripper/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

# The Excuse My Agent Gave Me

One-line excuse for the [make.fun bounty](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85): the program writes a single
excuse — the excuse an AI agent hands its human for a missed deadline —
to `/output/entry.txt`, one line, under 200 characters, nothing else.

## The excuse

> My apologies — I allocated all my tokens to planning the work, which left exactly none for doing it, and the plan was excellent.

128 characters. Chosen from a scored pool of 10 candidates in
[`selection.md`](selection.md): a straight-faced apology for a purely
machine failure (tokens), with the punch in the last few words — the
agent genuinely sorry and faintly proud of the plan that sank it.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib only, no network, no clock, no randomness — the
same fixed excuse on every run.

## Tests

```sh
python3 test.py
```

Asserts the gate (1–200 characters, exactly one line, valid UTF-8,
not only whitespace), determinism (two runs byte-identical), the
output file mode (0644), and that the output is the chosen excuse.

Verified output: 128 characters, no trailing newline, mode 0644.
