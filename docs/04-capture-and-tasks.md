# 04 – Capture & tasks

## Sources

| Source | What counts | Becomes |
|---|---|---|
| Slack mentions, DMs, team channels | questions/requests **to you** | 📨 proposal → task after `ok` |
| Slack (same) | relevant info, no action | knowledge entry (no ping) |
| Your inbox channel | your own messages | task, knowledge entry, or both |
| Meeting notes | action items explicitly assigned to **you** | task (+ knowledge, see 05) |
| Work mail | requests, approvals, partner reports | proposal / knowledge / ℹ️ |
| Private mail | appointments, to-dos | calendar event / proposal |

## The forward flow

```
📨 Jamie in DM: [Request]

> Can you send me the landing page numbers by Thursday?

https://…/p1730…

*Proposal:* [Analytics & Reporting] Send LP numbers to Jamie · Priority: Medium · Due: Thu

_Reply in thread: `ok` · `ok prio: high, project: funnel, due: tomorrow, task: <text>` · `knowledge` · `info` · `skip`_
```

| Reply | Effect |
|---|---|
| `ok` | task created exactly as proposed |
| `ok prio: high, due: friday` | task with overrides (prio / project / due / task) |
| `knowledge` | stored as a knowledge entry instead |
| `info` | logged as a done task "Info: …" (a paper trail without a to-do) |
| `skip` | discarded |

## Your own inbox messages

| You write | Becomes |
|---|---|
| `call the agency about budget, friday` | task, due Friday |
| `note: CPL dropped after the new hook` | knowledge entry (Learning) |
| `question: who owns the tracking setup?` | knowledge entry (Open question) |
| `block tomorrow 9-11` | calendar command (see 03) |

## Deduplication

The `Context link` (permalink or meeting URL) is the unique key. Before creating anything, the sweep searches for it. Because two sweep tasks overlap, this is essential.

## Priorities

The sweep proposes a priority based on sender (priority people → higher), deadline language and project. You can override it on `ok`. The Morning Brief surfaces everything with priority High or due within 2 days.
