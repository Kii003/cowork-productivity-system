# 06 – Customization

## Change projects
1. Add or rename the select options in **both** Notion databases (Action Items → Project, Knowledge Log → Project).
2. Create the project page (see `notion/schemas.md`).
3. Update `PROJECTS` in `config.yaml`, then re-render and re-paste the prompts into **all** tasks.

The routing keywords after the project name decide where items land. Use the words your team actually says.

## Change the language
Set `OUTPUT_LANGUAGE`. The prompts stay in English and the posts come out in your language. If you also want the inbox commands in your language, add aliases to section B2 of the sweep, for example `notiz:` = `note:`.

## Remove parts you don't need

| Don't have… | Delete from `sweep.md` |
|---|---|
| a separate work calendar | A0, A1, A4 and the work-calendar half of the conflict check |
| meeting notes | B3, C2 |
| private mail | A3a, B5 |
| a KPI source | the KPI lines in the brief/review (or set them to `none`) |

## Add a source
Add a section to part B following the same pattern: **window** (35 min) → **filter** → **dedup key** → **forward / C1 / ℹ️**. Possible sources include Jira, Linear, Asana, GitHub issues and a CRM.

## Change the cadence
- **Hourly:** keep only Sweep A and set the lookback windows from 35 to 65 minutes.
- **Every 30 min:** two tasks (default).
- **Lighter load:** run normal sweeps hourly, but schedule a separate deep run in the morning.

## KPIs in the brief
Point `KPI_SOURCE` at a Google Sheet tab or a saved Metabase question and describe how to read it (for example by row labels). Keep it read-only. If you want history, add a "📈 KPIs per week" Notion database and let the Monday brief upsert one row per week, using the week title as the dedup key.

## Organizations with API quotas
If one of your tools has a strict API quota (CRMs often do), add a line to the prompt such as *"Never fetch more than N records from <tool> per run."*
