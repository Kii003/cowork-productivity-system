# Notion setup

You need **two databases** and **one page per project**. Put them anywhere in your workspace. A common layout is a top-level "PROJECTS" page with the project pages underneath and the two databases next to it.

> **Fastest way:** open a Claude chat that has the Notion connector, paste the "Create with Claude" prompt at the bottom of this page, and fill in your project names. Then copy the returned `collection://…` IDs into `config/config.yaml`.

---

## 1. 🎯 Action Items

| Property | Type | Values / notes |
|---|---|---|
| Task | title | |
| Status | select | Open · In progress · Done |
| Priority | select | High · Medium · Low |
| Project | select | your project names + fallback (e.g. "Personal goals") + "Archive" |
| Due | date | |
| Source | select | Meeting notes · Slack · Mail · Calendar · Manual · Other |
| Context link | url | **dedup key**: Slack permalink, meeting URL, mail link |
| Note | text | original message / context |
| Next step | text | one concrete next action |

**Recommended views**

- **🔥 Focus**: Status ≠ Done, Priority = High, sorted by Due.
- **📋 By project**: board grouped by Project.
- **✅ Done**: Status = Done, sorted by last edited.

## 2. 🧠 Knowledge Log

| Property | Type | Values / notes |
|---|---|---|
| Entry | title | concise headline |
| Date | date | |
| Project | multi_select | your project names + "General" |
| Type | select | Decision · Info · Learning · Meeting note · Open question · Metric |
| Source | select | Meeting notes · Slack · Mail · Manual · Chat |
| People | text | names involved |
| Content | text | 2–6 factual sentences |
| Link | url | **dedup key** |

## 3. Project pages

Create one page per project with exactly this structure. The Weekly Review relies on the heading and the italic marker line.

```markdown
# <Project name>

<one-line description of the project>

## 📌 Current state
- (filled in automatically every Friday)

_Updated every Friday by the Weekly Review from the knowledge log._

## 📥 Knowledge log & 🎯 Tasks
<linked view of Knowledge Log, filtered: Project contains "<Project name>", sorted by Date desc>
<linked view of Action Items, filtered: Project = "<Project name>" and Status ≠ Done>
```

---

## Create with Claude (paste into a chat with the Notion connector)

```text
In my Notion workspace, under a new page "PROJECTS", create:

1) A database "🎯 Action Items" with properties:
   Task (title), Status (select: Open, In progress, Done), Priority (select: High, Medium, Low),
   Project (select: <PROJECT 1>, <PROJECT 2>, …, Personal goals, Archive), Due (date),
   Source (select: Meeting notes, Slack, Mail, Calendar, Manual, Other),
   Context link (url), Note (text), Next step (text).
   Views: "🔥 Focus" (Status != Done AND Priority = High, sort Due asc),
          "📋 By project" (board grouped by Project), "✅ Done" (Status = Done).

2) A database "🧠 Knowledge Log" with properties:
   Entry (title), Date (date), Project (multi_select: <PROJECT 1>, …, General),
   Type (select: Decision, Info, Learning, Meeting note, Open question, Metric),
   Source (select: Meeting notes, Slack, Mail, Manual, Chat), People (text), Content (text), Link (url).

3) One sub-page per project (<PROJECT 1>, <PROJECT 2>, …) with this content:
   "## 📌 Current state" + one placeholder bullet,
   the italic line "_Updated every Friday by the Weekly Review from the knowledge log._",
   "## 📥 Knowledge log & 🎯 Tasks", then two linked views:
   Knowledge Log filtered to this project (sort Date desc) and
   Action Items filtered to this project and Status != Done.

Finally, list the data source IDs (collection://…) of both databases and the page IDs of all project pages.
```
