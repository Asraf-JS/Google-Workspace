# 03 - Apply Gemini Across Workspace

In this chapter you will draft and revise from supplied files; verify cross-file references where available.

> **Prompts:** the [prompts page](./prompts.md) has every value and prompt for this chapter, each with a Copy button.

**Estimated time:** 55 minutes, planned as 10 explanation and demonstration, 25 guided build and casework, 15 independent practice and 5 verification and repair, with 45 active minutes by design. Not yet timed with learners.

**Your result:** A checked project update and communication draft from explicit sources.

> **Status:** author reference with 11 staged captures. The guided route, a native lineage table and a separate delay scenario were checked. The independent challenge, reviewer agreement and classroom timing remain pending.

---

## What You Will Learn

- Draft and refine across Workspace.
- Use explicit file references where supported.
- Check an action proposal before execution.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Download [project-facts.txt](../../shared/sample-files/project-facts.txt), [reporting-guidance.txt](../../shared/sample-files/reporting-guidance.txt) and [meeting-record.txt](../../shared/sample-files/meeting-record.txt). If attaching a Drive file to Gemini isn't available, paste the file's text into the panel instead and record that fallback.

## 3.1 Draft in Context

1. In **GW - AI - Practice** click **New > Google Docs > Blank document**, paste the complete text of project-facts.txt and name the Doc. Open **Ask Gemini**.

![A practice Doc containing the full project fact sheet](./images/c06-03-01-practice-source-fact-sheet.png)

*The Doc holds only the supplied fact sheet.*

![The Gemini side panel open beside the fact sheet](./images/c06-03-02-gemini-panel-open.png)

*Ask Gemini opens the panel on the right.*

2. Create a separate Doc from the supplied proposed reporting guidance. In the panel choose **Add sources → Add from Drive**, select the exact guidance document and confirm its chip. If the picker is unavailable, paste the complete guidance and record that fallback.

> **Reference run:** It was named **GW - AI - Proposed Reporting Guidance v1**.

![A separate Doc with the proposed reporting guidance](./images/c06-03-03-proposed-guidance-source.png)

*The guidance is version 1, proposed, not approved policy.*

![The guidance Doc attached as a chip in the Gemini prompt](./images/c06-03-04-guidance-attached.png)

*Check the chip names the exact guidance document.*

3. Request a coordinator update using both the current document and the named source (the first prompt in Part 3 of the [prompts page](./prompts.md)). Ask for plain chat text only, without document edits, and review any proposed change before accepting it.

![The coordinator-update request typed in the Gemini panel](./images/c06-03-05-update-prompt.png)

*The request asks for a reply in the panel only.*

4. If Gemini proposes inserting text into the document, reject the proposal, check the original is unchanged and resend the request with “Do not insert, edit, or propose changes”.

> **Reference run:** the first author request said panel only, yet Gemini proposed inserting text into the source document. A second request explicitly saying “Do not insert, edit, or propose changes” returned a panel answer with links to both documents.

A link is a pointer, not proof: inspect the original passages.

> **Reference run:** The author rejected it and verified that the original remained intact.

![Gemini proposing to insert a coordinator update into the document, with Reject and Accept](./images/c06-03-06-unexpected-proposed-edit.png)

*Despite the panel-only request, Gemini proposed an edit. Reject it.*

5. Check the unagreed start, proposed and unapproved RM 12,000 ceiling, four-week duration, Friday cadence and final-two-week success measure.

> **Reference run:** The answer stated “Operations follow” the proposed guidance; the author corrected this to describe proposed training practice, not established operations or approved policy.

![The checked coordinator update in the Output Lineage Doc](./images/c06-03-10-checked-update.png)

*The checked version describes proposed practice, not established operations.*

## 3.2 Adapt a Communication

1. Ask for example message wording based on the checked update (the second prompt in Part 3 of the prompts page). Keep recipients blank and do not send. Explicitly request plain chat text and prohibit creating a Gmail draft, using tools or editing a file; inspect the result before proceeding.
2. If Gemini creates a Gmail draft anyway, check it has no recipients, leave it unsent, delete it and resend with an explicit no-tools, no-draft request. Instructions alone do not guarantee that Gemini will avoid actions; inspect the interface and saved drafts, and stop an unintended action when possible.

> **Reference run:** **Observed behaviour:** despite a panel-only request, Gemini created an unaddressed Gmail draft before the author could cancel.
3. Copy or manually adapt the checked wording to a playbook. Preserve the unresolved decisions and proposed guidance; do not claim a launch or accepted commitment.

![An unsent draft message with no recipient](./images/c06-03-11-unsent-message.png)

*The message stays a draft. No one received it.*

## 3.3 Review Cross-App Actions

1. Using the third prompt in Part 3 of the prompts page, paste the complete scripted meeting record into the panel and ask Gemini to extract action, owner and relative practice week in chat only. Explicitly prohibit creating tasks, events, drafts or file changes.
2. Check the output against the original: Aina prepares a draft template in week 1, Bala reviews status definitions in week 1, and Siti collects a fictional sample update in week 2.

> **Reference run:** The author response correctly extracted those rows, but grouped “no purchase authorised” and “no external announcement planned” with unresolved decisions; those are stated constraints, not proof of additional pending approvals.
3. Record the checked list as text. A proposed action or extracted owner is not an assigned task, and a practice week is not a calendar date.

![The extracted action list with owners and practice weeks](./images/c06-03-12-action-lineage.png)

*Extracted rows aren't assigned tasks, and practice weeks aren't calendar dates.*

## 3.4 Trace One Evidence Set Through Three Outputs

1. Create an **Output Lineage** table mapping each output to its input and check: fact sheet and proposed guidance → checked coordinator update; checked update → unsent message; scripted meeting record → action list.

> **Reference run:** The author used an editable Google Docs table after building the three outputs.

![The Output Lineage table linking each output to its source and check](./images/c06-03-14-lineage-table.png)

*Each output traces back to its source.*

2. Compare the three outputs. Ensure that proposed practice has not become approved policy, an unsent request has not become an accepted commitment, and an extracted row is not an assigned task. Record the exact attached source title and the pasted meeting-record route.
3. Make a separate named scenario copy. Apply the delay card in Part 1 of the prompts page: Bala’s status-definition review is delayed and no replacement week is confirmed. Update the related follow-up wording and Bala’s row; retain Aina’s and Siti’s actions, the budget status and the unagreed start date. Keep the original baseline intact.

![The delay scenario copy with Bala's review marked delayed](./images/c06-03-13-delay-scenario.png)

*Only Bala's row and the follow-up wording change. Everything else stays.*

> **Reference run:** author-run scope: source attachment, panel response, manually checked update and message, meeting-record extraction, lineage table and separate scenario copy were verified. The Gmail draft side effect and rejected document proposal are recorded above. The independent challenge, separate human review and 55-minute classroom allocation have not been validated.

## Independent Practice

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Independently prepare a short escalation note for the delayed action with no new due week. Identify what is known, unknown and requested next.

2. Audit the Doc, unsent email and action table for consistency after the scenario change. Correct one mismatch or record evidence for each consistent field.

3. Explain which steps would require a deliberate separate application action before sending, assigning or scheduling anything.

### Evidence to Hand Over

- Lineage table and three checked output types with consistent facts.
- Delay-scenario update retaining an unknown replacement deadline.
- Independent escalation note and explicit distinction between text and application actions.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A downstream email adds a commitment absent from the checked update | Compare the output lineage and remove the unsupported assertion before using the draft. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Cross-app drafting is useful when sources and proposed actions remain explicit.

**Check yourself:** How can you tell which file a cross-file answer actually used?
