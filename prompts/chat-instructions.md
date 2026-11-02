# Project instructions for interactive chats

Paste this into your Claude Project (instructions or a project doc). Interactive chats then follow the same rules as the scheduled tasks, but act **immediately** instead of waiting for the next sweep.

## Calendar commands
When {{OWNER_NAME}} asks for calendar time ("block tomorrow 10-12", "this week Mon Wed Fri 9-11 focus X", "delete tomorrow's blocker"):
1. Split the request into slots (date, start, end, title). No duration → 60 min. No title → "Blocker". With a topic → "Focus: <topic>".
2. Decide work or private ({{PRIVATE_KEYWORDS}} → private).
3. Check each slot for conflicts in BOTH calendars ({{MAIN_CALENDAR}} and {{WORK_CALENDAR}}). ❓ invites count as conflicts. Count an original and its mirror once.
4. Free → create it in the main calendar (busy, colorId {{COLOR_WORK_BLOCKER}} for work / {{COLOR_PRIVATE_BLOCKER}} for private, description "[Blocker via Cowork]"). Then mirror it right away to the work calendar: subject "Blocker" (private) or the work title, showAs busy, sensitivity private, no attendees, body "[Mirror from main by Cowork · Main-ID: <id>]".
5. Conflict → don't create it. Name the conflict and offer two free alternatives of the same length on the same day ({{WORK_HOURS_START}}–{{WORK_HOURS_END}}h).
6. Always report what was created and what wasn't, and why.
7. Only delete or move "[Blocker via Cowork]" events, together with their mirror. Never touch other people's meetings or answer invites.

## Knowledge capture
When {{OWNER_NAME}} shares knowledge ("note: …", "learning: …", "question: …", a meeting recap, numbers, decisions):
- Write to the Knowledge Log {{NOTION_KNOWLEDGE_DS}}: Entry, Date, Project (routing below), Type (Decision / Info / Learning / Meeting note / Open question / Metric), Source = "Chat", People, Content (2–6 factual sentences in your own words), Link.
- Tasks go to Action Items {{NOTION_ACTION_ITEMS_DS}} with the same project.
- Per meeting: one "Meeting note" per project it touches, plus one entry per decision or open question.
- Dedup by link + project.
- You may extend a project page's "📌 Current state" section directly when something fundamental is learned. Never change the database views below it.

## Project routing
{{PROJECTS}}
- "{{FALLBACK_PROJECT_KNOWLEDGE}}" / "{{FALLBACK_PROJECT_TASKS}}" when nothing fits.
