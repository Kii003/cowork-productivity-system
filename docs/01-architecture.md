# 01 – Architecture

## The problem

Knowledge workers juggle:

- **two calendars**: a work calendar (Outlook/M365) and a private one, and only one gets looked at;
- **requests scattered across Slack, mail and meetings**;
- **knowledge that evaporates**, because decisions from a meeting three weeks ago are gone.

Classic automation (Zapier, Make, n8n) handles fixed pipelines well. It struggles with judgment calls: *Is this Slack message a request to me? Which project does it belong to? Is this invite accepted?*

## The approach

Each job is a **scheduled Claude task**: a natural-language prompt that runs in a fresh cloud session with your connectors (Slack, Notion, calendars, mail, meeting notes). The prompt *is* the program.

```
          ┌───────────── every 30 min (2 tasks, :00 and :30) ─────────────┐
          │                         SWEEP                                  │
          │  A  Calendar   A0 work→main sync · A1 ghost cleanup            │
          │                A2 blocker commands · A4 main→work blockers     │
          │                A3 (deep) mail bookings, Notion to-dos, reports │
          │  B  Tasks      B1 Slack forward flow · B2 inbox notes/replies  │
          │                B3 meeting action items · B4/B5 mail            │
          │  C  Knowledge  C1 entries · C2 meeting → knowledge             │
          └────────────────────────────────────────────────────────────────┘
   weekday morning: MORNING BRIEF           Friday: WEEKLY REVIEW
```

### Data stores

| Store | Role | Written by |
|---|---|---|
| Main calendar (e.g. private Google) | Single source of truth for time | Sweep (A0/A2/A3), chat |
| Work calendar (e.g. Outlook) | Read-only, except neutral `Blocker` mirrors | Sweep (A4), chat |
| Notion Action Items | All tasks | Sweep (B), chat |
| Notion Knowledge Log | Facts, decisions, open questions per project | Sweep (C), chat |
| Notion project pages | Human-readable "Current state" | Weekly Review |
| Slack inbox channel | UI: commands in, confirmations and summaries out | everyone |

### Key design decisions

1. **Slack as the UI.** You talk to the system by posting in your own private channel and replying in threads. It works on any device and needs no app.
2. **Propose, don't impose.** Requests from others become a 📨 *proposal*. Only your `ok` creates a task, which keeps the task list clean.
3. **Markers instead of a database.** Every event the system creates carries a text marker with the source ID (`[Synced from work calendar by Cowork · Work-ID: …]`). The marker is the sync state. No extra storage is needed, and the system never touches anything without a marker.
4. **Loop protection.** Mirrors in the work calendar carry `[Mirror from main …]` and are never synced back.
5. **Deep vs. normal runs.** The first run of the day does the expensive work: a 45-day horizon, mail bookings, Notion to-dos and reports. Later runs only look 14 days ahead and 35 minutes back.
6. **Idempotent everything.** Two overlapping runs, or a re-run, must not create duplicates. Dedup keys: Work-ID, permalink, meeting URL, mail link.
7. **Safety limits.** Max 10 deletions per run. Skip cleanup if fetching the source failed. Never touch unmarked events.

### Why two sweep tasks?

Scheduled tasks have a **minimum interval of one hour**. For a 30-minute cadence, create two identical tasks, one at `:00` and one at `:30`. The prompt knows about this and deduplicates every write. **Always edit both tasks together.**
