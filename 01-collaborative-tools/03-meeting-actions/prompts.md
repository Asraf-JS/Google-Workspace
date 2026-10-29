# 03 - Turn a Meeting Record into Accountable Actions: Prompts

## Part 1: Extraction Prompt
**Session:** new chat | **Grounding:** pasted scripted record only
```text
Reply in the side panel only. Do not edit files, send messages or create tasks. Extract only explicit commitments from the RECORD below into Action, Owner and Due practice week. Separately list unresolved decisions. Do not infer completion, invent dates or treat the budget proposal as approval. Use British English.
RECORD:
[paste meeting-record.txt in full]
```
## Part 2: Table Headings
```text
ActionID | Action | Owner | Due practice week | Status | Evidence
```
## Part 3: Practice Event
```text
Practice only - Project Reporting Pilot kick-off
Duration: 30 minutes
Time zone: Asia/Kuala_Lumpur
Guests: none
Pilot start date: To be confirmed
```
Use the assigned practice slot, not a guessed project start date.
