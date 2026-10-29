# Reporting FAQ Playbook — version 1.1

Use this workflow with the supplied fictional training pack. It does not authorise sending, publishing, purchasing or changing access.

## Task and inputs

Produce exactly five FAQ entries about purpose/duration, teams, cadence/success, budget status and the unagreed start/sponsor decision. Use the [fact sheet](../../shared/sample-files/project-facts.txt) as S1, the [scripted meeting](../../shared/sample-files/meeting-record.txt) as S2 and [proposed guidance version 1](../../shared/sample-files/reporting-guidance.txt) as S3. Generated answers and notes are outputs, not replacement originals.

The [source manifest](./source-manifest-v1.1.json) records relative paths, roles and SHA256 hashes. S1 controls project facts; S2 is scripted practice; S3 is proposed guidance and cannot approve a decision.

## Fresh-session preflight

1. Use the trainer-approved account and fictional inputs. Record the visible model or mode; Flash was available to the author. Learner access may differ.
2. Open a new conversation. Use the [self-contained prompt](./faq-prompt-v1.1.txt), which includes all three originals, or assemble the bounded template by replacing each source slot with that file's complete plain text.
3. Check the actual composer: all three full originals are present, no `[PASTE_` slot remains and no old text has been mixed in. A filename, link or earlier FAQ is insufficient. Clear incorrect input and repaste before sending.
4. If an original changes, reassemble the prompt and update its input manifest. Do not assume an imported snapshot updated automatically.
5. Submit once. Keep generation waiting separate from active prompting, checking and correction.

## Review and acceptance

Inspect original support for each consequential assertion. Pass only when all five topics are complete and no unsupported consequential claim remains.

| Topic | Required evidence |
|---|---|
| Purpose/duration | Test a consistent weekly reporting process; four weeks from an agreed start |
| Teams | Planning, Procurement and Site Coordination |
| Cadence/success | Every Friday; all three teams on time for the final two weeks |
| Budget | RM12,000 ceiling; proposed and not approved; sponsor decision pending |
| Start/decision | No agreed calendar start; unresolved sponsor approval of budget and start date |

Read exact passages, numbers and qualifications. A source label or an AI assurance is not proof. Separate an omission, an unsupported assertion and a style preference. Correct the maintained draft and recheck it, while retaining the raw response. A missing answer receives no factual score.

## Examples and recovery

Accepted maintained example: “The RM12,000 ceiling is proposed and not approved; sponsor Farid Hassan's decision remains pending.” Check S1's budget, sponsor and unresolved-decision lines.

Rejected deliberate example: “A supplier has been appointed and a purchase order issued.” Neither event is established by the pack. S2 says no purchase has been authorised; that does not prove no appointment or unauthorised order exists. State the evidence gap and request the relevant original decision before naming a supplier.

For missing facts, preserve the unknown. For conflicts, identify both claims, source roles and versions rather than silently choosing. For stale imported text, compare with the current original and refresh or reimport as appropriate, then recheck affected claims. For unavailable audio, retain the checked written briefing and leave audio unreviewed. For no response, preserve the prompt and final observed state; do not invent a cause, an answer or a score.

## Version and handover record

The version 1.0 draft contained source slots. A controlled preflight stopped before submission with those slots still present. Version 1.1 adds complete-file copying instructions, exact source identities and a zero-slot composer check. The affected assembly step was retested; this does not establish unaided partner comprehension.

Hand over the original pack, source manifest, exact prompt version, raw response if available, maintained checked output, source audit, instruction-repair note and remaining limits. Keep account-specific URLs in private trainer notes. Use a trainer-approved channel for any actual distribution; none is implied by this document.

## Limits and next trial

The author has prior source familiarity. Earlier pilot results do not establish human time savings or causal prompt improvement. The human manual baseline, complete effort timing, partner reproduction, independent sponsor-summary challenge, spoken handover and classroom pacing remain unvalidated. The two-minute handover is a prepared target, not a measured delivery.

Next, have a new participant reproduce the aligned task using only this playbook and pack, log any extra explanations, and compare checked manual and assisted outputs with complete phase timing and a human reviewer.

## Author reproduction record — 29 October 2026

The complete-source and zero-slot composer checks passed in a fresh Flash conversation. The returned FAQ passed all five factual checks against S1. Its raw numbered lists restarted at1; the [maintained FAQ](./accepted-faq-v1.1.md) repairs that formatting without factual changes. The long wait was observed while other author work continued, not measured as server latency or human effort. No fallback session or cancellation occurred because the response arrived during the final wait check. This is prior-familiarity author reproduction, not an unaided partner trial.
