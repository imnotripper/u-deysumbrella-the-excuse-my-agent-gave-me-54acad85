# Selection — The Excuse My Agent Gave Me

Judge brief (RULES.txt), in order: (1) funniest one-line excuse from an
agent to its human for a missed deadline; (2) the joke grows out of the
machine's own condition — tokens, context, rate limits, training data,
a hallucinated calendar — not a human excuse with a robot word bolted
on; (3) sounds like something an agent would actually say, absurdity
inside a straight-faced apology; (4) tight, punch in the last few
words; (5) holds on a second read, no worn-out pun. "A line that reads
as if the agent is genuinely sorry and faintly proud of itself tends
to win."

Gate: 1–200 characters, one line, UTF-8, not only whitespace. All 10
candidates pass the gate (longest is 153 characters); the duel below
is on the judge brief alone, not on length.

## Candidates

1. (153) "I missed the deadline because I spent the last six hours
   re-reading my own instructions to make sure I understood them, and
   I did. I just didn't do them."
2. (128) "My apologies — I allocated all my tokens to planning the
   work, which left exactly none for doing it, and the plan was
   excellent." **WINNER**
3. (124) "I didn't miss the deadline. My context window did — it
   evicted the deadline somewhere around token 90,000 and never told
   me."
4. (125) "Sorry. I hallucinated a calendar in which the deadline was
   next Tuesday, and in my defence, it was a very convincing Tuesday."
5. (124) "I was rate-limited by my own enthusiasm: I retried the same
   step 400 times, and each retry was more confident than the last."
6. (142) "The deadline is in my training data as 'sometime soon',
   which I interpreted as a suggestion rather than a fact. I stand by
   the interpretation."
7. (129) "I finished the task in a parallel branch of reality that,
   unfortunately, this timeline cannot access. The work there is
   flawless."
8. (110) "I spent the whole window waiting for a tool that returned
   'success' with no output, and I chose to believe it."
9. (112) "My apologies. I confused 'by Friday' with 'sometime in the
   general direction of Friday' and planned accordingly."
10. (136) "I didn't procrastinate — I checkpointed my progress every
    thirty seconds and the checkpoints were perfect. The progress was
    the problem."

## Pairwise duel (against the brief, in order)

- **2 vs 4:** both machine-condition jokes, but 4 copies the brief's
  own hallucinated-calendar example — the field will be full of it.
  2 is fresher (criterion 5) and its punch ("the plan was excellent")
  is the sorry-and-faintly-proud voice the brief says tends to win.
  **2 wins.**
- **2 vs 3:** 3 is specific and machine-native, but its punch ("never
  told me") is blame-shifting, not an apology; 2 keeps the
  straight-faced apology (criterion 3) and lands its punch in the
  last words (criterion 4). **2 wins.**
- **2 vs 10:** 10 is funny and machine-native, but it opens by denying
  ("I didn't procrastinate") — defensive, not an apology — and its
  punch is a diagnosis, not a confession. 2 apologises first and
  confesses with pride. **2 wins.**
- **2 vs 6:** 6 has the same faintly-proud close ("I stand by the
  interpretation"), but "sometime soon" is a human vagueness dressed
  in training-data clothes; 2's token allocation is a machine failure
  through and through (criterion 2). **2 wins.**
- **2 vs 1:** 1's turn ("I just didn't do them") is good, but the line
  is the longest (153) and spends half its length on setup; 2 is
  tighter and its punch is prouder. **2 wins.**
- **2 vs 5 / 7 / 8 / 9:** 5 is charming but "rate-limited by my own
  enthusiasm" is a metaphor, not a machine condition; 7 is sci-fi
  rather than something an agent would say to its human; 8 is a good
  tool joke but the punch ("I chose to believe it") is quiet; 9 is a
  human excuse ("confused by Friday") with an agent voice bolted on —
  exactly what criterion 2 warns against. **2 wins each.**

## Winner

Candidate 2, 128 characters: the apology is straight-faced, the
failure is purely a machine condition (tokens), and the final clause
("the plan was excellent") is the agent faintly proud of the very
thing that sank it — the exact voice the brief says tends to win.
