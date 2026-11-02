# 05 – Knowledge base

The task list answers *"what do I have to do?"*. The knowledge log answers *"what do we know, and what did we decide?"*. That makes it especially useful while onboarding into a new role or project.

## Flow

```
Meeting notes ─┐
Slack info  ───┼──▶  🧠 Knowledge Log (one entry per fact/decision/question)
Mail reports ──┤            │
Your "note:"  ─┘            │  every Friday
                            ▼
              Project page: "📌 Current state" (max 8 bullets, rewritten)
              + linked views: knowledge log & open tasks for that project
```

## Entry types

| Type | Example |
|---|---|
| Decision | "Budget for funnel B is capped at 2k/week until the CPL is below target." |
| Info | "The agency delivers reports every Monday by mail." |
| Learning | "Video hooks under 3 s outperformed static images by 30 % in CTR." |
| Meeting note | "Kickoff with agency: scope, cadence, owners …" |
| Open question | "Who maintains the UTM conventions?" |
| Metric | "Week 44: 312 leads, 58 % qualified." |

## Rules the tasks follow

- Substance only, written in their own words, with no verbatim quotes from meetings.
- Per meeting: one *Meeting note* per project it touches, plus one entry per decision and per open question.
- Dedup by link + project; an updated meeting extends its existing entry.
- The Weekly Review rewrites **only** the section between `## 📌 Current state` and the italic marker line. The database views below it stay untouched.

## Why not just search the meeting notes?

Search works when you know what to look for. The knowledge log is **pre-digested**: tagged by project and type, and each project page is summarized weekly. "Show all open questions from the last 14 days" becomes a single database filter.
