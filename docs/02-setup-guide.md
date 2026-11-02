# 02 – Setup guide

Plan for about 45 minutes. You'll end up with three or four scheduled tasks, two Notion databases, project pages and one Slack channel.

## 1. Connect your tools in Claude

In Claude → Settings → Connectors, connect at least:

- **Slack**
- **Notion**
- **Google Calendar** (your main calendar)

Optional:

- **Microsoft 365** for a work calendar and mail, read-only plus blocker mirrors
- **Gmail** for private mail
- **Granola** or another meeting-notes connector
- **Google Sheets** / **Metabase** as a KPI source for the brief

> Scheduled tasks use the connectors of the account that creates them. If you connect a tool later, the existing tasks may need to be re-saved or recreated before they can see it.

## 2. Create your Slack inbox channel

1. Create a **private** channel such as `#yourname-inbox` with only you in it.
2. Get its ID: right-click the channel → *View channel details* → the ID (starting with `C0…`) is at the bottom.
3. Get your user ID: your profile → ⋮ → *Copy member ID* (`U0…`).
4. Optional: find the DM IDs of your priority people (`D0…`) from the same details panel. Alternatively, just list their names, and the task looks them up.

## 3. Create the Notion structure

Follow [`notion/schemas.md`](../notion/schemas.md). The quickest path is the "Create with Claude" prompt. Note:

- the **data source IDs** (`collection://…`) of *Action Items* and *Knowledge Log*;
- the **URL** of the Action Items database;
- the **page IDs** of your project pages.

## 4. Decide your calendar model

| You have… | Main calendar | Work calendar |
|---|---|---|
| Outlook at work + private Google | Google (primary) | Outlook |
| Two Google accounts | private Google | work Google |
| One calendar only | that one | `none`: delete sections A0, A1, A4 from the sweep |

Pick colors (Google `colorId`): `5` banana, `8` graphite, `9` blueberry, `2` sage, `11` tomato, `10` basil, `6` tangerine, `3` grape, `4` flamingo, `7` peacock, `1` lavender.

## 5. Fill in the config and render the prompts

```bash
cp config/config.example.yaml config/config.yaml
# edit config/config.yaml
pip install pyyaml
python scripts/render_prompts.py
```

The rendered prompts land in `build/`. No Python? Open the files in `prompts/` and use search-and-replace on each `{{PLACEHOLDER}}` instead.

## 6. Create the scheduled tasks

In Claude, create these scheduled tasks and paste the matching file from `build/` as the prompt. Use your own time zone; the examples use `Europe/Berlin`.

| Name | Prompt | Schedule (cron) |
|---|---|---|
| Sweep A | `build/sweep.md` | `CRON_TZ=Europe/Berlin 0 8-19 * * 1-5` |
| Sweep B | `build/sweep.md` (identical) | `CRON_TZ=Europe/Berlin 30 8-19 * * 1-5` |
| Morning Brief | `build/morning-brief.md` | `CRON_TZ=Europe/Berlin 30 7 * * 1-5` |
| Weekly Review | `build/weekly-review.md` | `CRON_TZ=Europe/Berlin 0 16 * * 5` |

Tips:

- You can also ask Claude in a chat: *"Create a scheduled task named Sweep A with cron … and this prompt: …"*.
- Set the tasks to **auto-approve actions** if your organization allows it. Otherwise each run stops at the first write and waits for approval.
- The server may shift the start minute a little (for example to `:03`). That's fine.

## 7. Make interactive chats follow the same rules

Create a Claude **Project** such as "Productivity" and add `build/chat-instructions.md` as a project doc or paste it into the instructions. When you write "block tomorrow 10-12" in that project, Claude executes it immediately.

## 8. Test it

1. Post `block tomorrow 10-11` in your inbox channel and trigger *Sweep A* manually ("Run now").
2. Check: a blocker in the main calendar, a `Blocker` in the work calendar and a ✅ thread reply.
3. Ask a colleague to mention you with a question. The next run posts a 📨 forward; reply `ok`.
4. Post `note: we decided to pause campaign X` and check the Knowledge Log.

Done. See the [cheat sheet](cheat-sheet.md) for everything you can type.
