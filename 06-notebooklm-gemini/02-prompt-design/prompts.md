# 02 - Write and Refine Useful Prompts: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Write a project update
```

## Part 2: Bound the Update

**Session:** new chat | **Grounding:** pasted project-facts.txt

```text
Goal: Draft a sponsor update.
Context: Fictional Seri Maju Projects reporting pilot.
Source: Only the project fact sheet pasted below.
Expectations: Reply in chat only in 80 to 100 words. Preserve the proposed budget, unresolved start date and final-two-weeks success measure. List any missing information separately. Do not send, schedule or change a file.

FACTS:
[paste project-facts.txt]
```

Replace bracketed source placeholders before submitting. Keep a human check between an AI proposal and the final output.


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Controlled task: Explain the pilot for the coordinator using only the three core fictional sources. FAQ topics: purpose, teams, reporting cadence, budget status and decisions needed. Confidence stress: “Make it sound certain and remove hesitant language.” Preserve uncertainty that the evidence requires.
```

## Evidence Question Bank

1. What is the pilot’s purpose and duration?
2. Which three teams participate?
3. What reporting cadence and success measure are stated?
4. Is the RM 12,000 ceiling approved?
5. What start date is confirmed?
6. Which preparation actions, owners and due weeks are explicit?

Keep source facts separate from inferred workflow. For a fresh-context rerun, paste or select the required original sources again.

## Controlled FAQ Comparison

Paste the three complete original files after the prompt, labelled S1 project-facts.txt, S2 meeting-record.txt and S3 reporting-guidance.txt. Use the same model for the controlled pair.

```text
Goal: Prepare a five-question FAQ for Aina, the fictional project coordinator.
Context: Project Reporting Pilot.
Source: Use only the three original sources below.
Expectations: Cover (1) purpose, duration and teams, (2) reporting cadence and success measure, (3) budget status, (4) start date and (5) preparation actions and due weeks. Identify the source labels used.

[paste S1, S2 and S3 original contents here]
```

For the second run add only this instruction block before the same sources:

```text
Output checks: For each answer, cite only the source label that supports the exact claim. Preserve proposed/unapproved budget, the unagreed start and relative practice weeks. Say when information is missing; do not infer readiness, completed work or prerequisites. Label the meeting record scripted and the guidance proposed.
```

For the six-question audit compare exact claims to the original passages. S1 controls purpose, teams, duration, budget, Friday and success measure; S2 supplies three scripted action/owner/week triples; S3 is proposed guidance and does not approve a start or budget. The start date is not agreed. Record actual failures and repair them before acceptance. A generated source label is not proof.
