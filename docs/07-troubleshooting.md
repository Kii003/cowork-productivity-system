# 07 – Troubleshooting & lessons learned

| Symptom | Cause | Fix |
|---|---|---|
| "Minimum interval is 1 hour" when scheduling every 30 min | scheduled-task limit | two tasks at `:00` and `:30` (default setup) |
| Synced events show in default **blue** | older syncs never set a colorId; the sync only updated on *other* changes | the sweep's A0 color rule now enforces colors on every match; run a deep sweep once |
| Invites shown as accepted | `showAs` was used as the response signal | prefer explicit `responseStatus`; tentative → ❓ |
| Duplicate events or tasks | two runs overlapped | every create checks its dedup key first. Don't remove those lines |
| Ghost events remain after a meeting was cancelled | delete tool refused by the environment | the sweep posts "🗑 Please delete manually"; delete by hand |
| Mirror "Blocker" bounces back into the main calendar | missing loop protection | keep the `[Mirror from main …]` check in A0 |
| A task can't see a newly connected tool | task created before the connector | re-save or recreate the task |
| Each run stops waiting for approval | task not on auto-approve | enable auto-approval in the task settings (if your org allows it) |
| Notion view filters with "this week" fail | the view DSL has no relative dates | filter on Priority/Status instead, or create the view by hand |
| The Weekly Review wiped the database views on a project page | the replacement included the views | keep the italic marker line; the review must only replace text above it |
| Posts are too noisy | normal runs post summaries | "nothing happened → post nothing" is the default; only deep runs always summarize |

## Debugging a run
Open the scheduled task in Claude. Each run is a normal session you can read: which tools it called, what it found and why it skipped something. Usually the cause is a wrong ID in the config or a connector that isn't available to the task.

## Changing prompts safely
1. Edit `prompts/*.md` (or your rendered copy).
2. Re-render.
3. Update **both** sweep tasks.
4. Trigger one run manually and read the session.
