# Example: growth marketing role

This is the setup the system was originally built for, anonymized. It suits someone on a growth team who has just moved over from another team and owns a **paid-social funnel**:

> Native-style ads → landing pages → form → CRM → automated messaging follow-up, plus offline print campaigns. An external agency runs the ads; KPIs live in a shared Google Sheet.

## Projects

| Project | Routing keywords | What the knowledge log collects |
|---|---|---|
| Funnel | funnel, landing page, form, CRM handover, budget, scaling, tracking, UTM | flow changes, budget decisions, tracking issues |
| Creatives | angle, creative, ad copy, hook, test, agency briefing | test results, winning angles, briefings |
| Messaging Journey | WhatsApp, follow-up, voice memo, reactivation | flow logic, response rates, assets |
| Print | print, newspaper, circulation | placements, costs, results |
| Analytics & Reporting | dashboard, sheet, KPI, conversion, report | metric definitions, weekly numbers |
| Personal goals / General | fallback | everything else |
| Archive | — | the previous role's projects, kept for reference and never used for new items |

## Switching roles mid-flight

When the owner changed teams, the old projects were **not deleted**. Instead:

1. A select option "Archive" was added and all old open tasks were moved there.
2. The old project page was moved under an "Archive" page.
3. The prompts got an explicit rule: *never assign new items to "Archive"*.

## Extra KPI databases (optional)

Next to the two core databases, this setup also used:

- **📈 Funnel per week**: one row per calendar week (budget, leads, qualified, cost per qualified lead …). The Monday brief upserts it from the KPI sheet, using the week title as the dedup key.
- **🧭 Landing pages**: one row per page per week. The Weekly Review fills it and recommends budget shifts.
- **📣 Daily lead pulse**: one row per day, counted from a Slack bot feed that posts every new lead.

These are specific to a funnel role. Copy the pattern ("read-only source → upsert by a stable title → chart view in Notion") for your own metrics.

`config.yaml` in this folder holds the full example configuration with placeholder IDs.
