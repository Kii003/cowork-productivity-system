# 03 – Calendar sync

## The two-calendar model

```
 WORK CALENDAR (Outlook)                     MAIN CALENDAR (private Google)
 ───────────────────────                     ──────────────────────────────
 Real meetings  ──────── A0 copy ─────────▶  "Weekly sync"  (yellow)
 Unanswered invite ───── A0 copy ─────────▶  "❓ Kickoff"   (grey)
                                             Dentist 10:00 (private)
 "Blocker" (private) ◀── A4 mirror ───────── │
                                             "Focus: Report" [Blocker via Cowork]
 "Focus: Report" ◀────── A4 mirror ───────── │
```

- **Main calendar = what you look at.** It shows everything: work, private, unanswered invites, blockers and to-dos.
- **Work calendar = what colleagues see.** Real meetings stay untouched. Your busy time appears as neutral `Blocker` events, so nobody books over your dentist appointment, and nobody learns about it either.

## Markers (the sync state)

| Where | Marker | Meaning |
|---|---|---|
| Main | `[Synced from work calendar by Cowork · Work-ID: <id>]` | copy of a work meeting |
| Main | `[Blocker via Cowork]` | blocker created by command |
| Main | `[Synced from mail by Cowork]` | booking found in private mail |
| Main | `[Task from Notion by Cowork · <url>]` | all-day to-do from Notion |
| Work | `[Mirror from main by Cowork · Main-ID: <id>]` | neutral mirror; **never synced back** |

## Colors

| State | Default colorId | Title |
|---|---|---|
| Accepted work meeting | 5 (banana) | subject |
| Not yet answered | 8 (graphite) | `❓ ` + subject |
| Work blocker | 9 (blueberry) | `Blocker` / `Focus: …` |
| Private blocker | 2 (sage) | `Blocker` |

The sweep **enforces** color and prefix on every run. An event without a colorId shows in the calendar's default blue, and that counts as a bug the sweep fixes.

## Response status heuristics

The best source is the explicit `responseStatus`. Otherwise:

- organizer, or showAs busy/oof → accepted;
- showAs tentative → unanswered;
- declined or cancelled (or a "Canceled:" prefix) → not mirrored, and the copy is removed.

## Ghost cleanup (A1)

A copy whose source disappeared gets deleted. Safety rules:

- skip if the work-calendar fetch failed or returned zero events;
- max 10 deletions per run;
- never delete without a Cowork marker;
- if the delete tool is refused (some environments block deletions), post `🗑 Please delete manually: …` once.

## Blocker commands (A2)

Post in your inbox channel (or say in a chat):

| You write | Result |
|---|---|
| `block tomorrow 10-12` | 2 h work blocker tomorrow |
| `block Mon Wed Fri 9-11 deep work` | 3 blockers titled "Focus: deep work" |
| `gym today 18-19:30` | private blocker; in Outlook just "Blocker" |
| `delete tomorrow's blocker` | removes it and its mirror |

On a conflict, nothing is created and the thread reply suggests two alternatives. Reply `1`, `2`, `anyway` or a new time.

## Slack status from your calendar

If your work calendar is Outlook, install Slack's official **Microsoft Outlook Calendar** app. It sets "In a meeting" automatically, and because the private time is mirrored as busy `Blocker` events, it covers your private appointments too.
