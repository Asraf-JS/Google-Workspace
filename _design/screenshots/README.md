# Screenshot Editing Sources

These PNGs preserve the full dimensions of the retained captures, with account identities, private native URLs and mailbox surroundings masked. They have not been cropped or resized during this export. Unredacted originals stay local.

The source library contains **150 application-window captures, six focused captures and three PDF-page renders**. Three early images have no retained original. A full application capture contains the browser application viewport, not necessarily browser tabs, the address bar or the Windows desktop.

Participant notes continue to use the existing approved crops. Inspect the whole frame before replacing a lesson image: surrounding content may fall outside the illustrated step. Two procedure-plan sources explicitly need an earlier-stage recapture before whole-frame use.

## Find and Adjust an Image

The table links each lesson image to its retained source. The [manifest](./manifest.json) records dimensions, source type, privacy masks and the approved crop rectangle where it was retained. Coordinates use the original PNG pixels.

Use Pillow to render an adjusted crop without editing the source:

```text
python _design/screenshots/render-crop.py --image 02-google-docs/03-styles-navigation/images/c02-03-renamed-subsection.jpg --box 0 0 2128 1002 --output preview.jpg
```

Review the output before replacing a participant image or rebuilding books.

## Missing Originals

These three early workspace images need recapture for a wider view:

- [c01-01-01.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-01.jpg)
- [c01-01-02-folders.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02-folders.jpg)
- [c01-01-02-sources.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02-sources.jpg)

## Available Sources

| Lesson image | Retained source | Size | Source type |
|---|---|---|---|
| [c01-01-02-convert.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02-convert.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-02-convert.png) | 2360 x 1111 | application-window |
| [c01-01-02-links.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02-links.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-02-links.png) | 2360 x 1112 | application-window |
| [c01-01-02-search.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02-search.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-02-search.png) | 1912 x 948 | application-window |
| [c01-01-02-summary.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02-summary.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-02-summary.png) | 2360 x 1112 | application-window |
| [c01-01-02.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-02.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-02.png) | 2360 x 1112 | application-window |
| [c01-01-03-matrix.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-03-matrix.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-03-matrix.png) | 2360 x 1112 | application-window |
| [c01-01-03-restricted.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-03-restricted.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-03-restricted.png) | 2360 x 1112 | application-window |
| [c01-01-03-shortcut-menu.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-03-shortcut-menu.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-03-shortcut-menu.png) | 1912 x 948 | application-window |
| [c01-01-03-shortcut.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-03-shortcut.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-03-shortcut.png) | 1912 x 948 | application-window |
| [c01-01-03.jpg](../../01-collaborative-tools/01-workspace-governance/images/c01-01-03.jpg) | [PNG](full/01-collaborative-tools/01-workspace-governance/c01-01-03.png) | 2360 x 1112 | application-window |
| [c01-02-01-start.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-01-start.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-01-start.png) | 2360 x 1112 | application-window |
| [c01-02-01-panel.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-01-panel.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-01-panel.png) | 2360 x 1112 | application-window |
| [c01-02-01-audit.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-01-audit.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-01-audit.png) | 2360 x 1112 | application-window |
| [c01-02-01.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-01.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-01.png) | 2360 x 1112 | application-window |
| [c01-02-02-headings.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-02-headings.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-02-headings.png) | 2360 x 1112 | application-window |
| [c01-02-02.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-02.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-02.png) | 2360 x 1112 | application-window |
| [c01-02-02-version.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-02-version.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-02-version.png) | 2360 x 1112 | application-window |
| [c01-02-03-comment.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03-comment.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03-comment.png) | 2360 x 1112 | application-window |
| [c01-02-03-purpose.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03-purpose.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03-purpose.png) | 2360 x 1112 | application-window |
| [c01-02-03-reject.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03-reject.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03-reject.png) | 2360 x 1112 | application-window |
| [c01-02-03.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03.png) | 2360 x 1112 | application-window |
| [c01-02-03-version.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03-version.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03-version.png) | 2360 x 1112 | application-window |
| [c01-02-03-download.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03-download.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03-download.png) | 2360 x 1112 | application-window |
| [c01-02-03-export.jpg](../../01-collaborative-tools/02-checked-brief/images/c01-02-03-export.jpg) | [PNG](full/01-collaborative-tools/02-checked-brief/c01-02-03-export.png) | 716 x 1011 | pdf-page |
| [c01-03-01-start.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-01-start.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-01-start.png) | 2360 x 1112 | application-window |
| [c01-03-01-agenda.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-01-agenda.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-01-agenda.png) | 2360 x 1112 | application-window |
| [c01-03-01-links.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-01-links.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-01-links.png) | 2360 x 1112 | application-window |
| [c01-03-01-preparation.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-01-preparation.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-01-preparation.png) | 2360 x 1112 | application-window |
| [c01-03-01.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-01.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-01.png) | 2360 x 1112 | application-window |
| [c01-03-02.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-02.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-02.png) | 2360 x 1112 | application-window |
| [c01-03-03-table.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-03-table.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-03-table.png) | 2360 x 1112 | application-window |
| [c01-03-03.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-03.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-03.png) | 2360 x 1112 | application-window |
| [c01-03-03-version.jpg](../../01-collaborative-tools/03-meeting-actions/images/c01-03-03-version.jpg) | [PNG](full/01-collaborative-tools/03-meeting-actions/c01-03-03-version.png) | 2360 x 1112 | application-window |
| [c01-04-01-freeze.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-freeze.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-freeze.png) | 2360 x 1168 | application-window |
| [c01-04-01-baseline.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-baseline.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-baseline.png) | 2360 x 1168 | application-window |
| [c01-04-01-intake-raw.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-intake-raw.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-intake-raw.png) | 2360 x 1168 | application-window |
| [c01-04-01-intake.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-intake.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-intake.png) | 2360 x 1168 | application-window |
| [c01-04-01-validation.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-validation.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-validation.png) | 2360 x 1168 | application-window |
| [c01-04-01-reject-setting.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-reject-setting.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-reject-setting.png) | 2360 x 1168 | application-window |
| [c01-04-01-invalid.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01-invalid.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01-invalid.png) | 2360 x 1168 | application-window |
| [c01-04-01.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-01.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-01.png) | 1833 x 733 | focused-capture |
| [c01-04-02-counts.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02-counts.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02-counts.png) | 1278 x 378 | focused-capture |
| [c01-04-02-team-labels.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02-team-labels.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02-team-labels.png) | 1556 x 389 | focused-capture |
| [c01-04-02-reconciled.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02-reconciled.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02-reconciled.png) | 1722 x 367 | focused-capture |
| [c01-04-02-first-chart.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02-first-chart.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02-first-chart.png) | 1722 x 822 | focused-capture |
| [c01-04-02-charts.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02-charts.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02-charts.png) | 1722 x 822 | focused-capture |
| [c01-04-02-filter.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02-filter.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02-filter.png) | 2913 x 1441 | application-window |
| [c01-04-02.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-02.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-02.png) | 2913 x 1441 | application-window |
| [c01-04-03-link.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03-link.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03-link.png) | 2360 x 1168 | application-window |
| [c01-04-03-baseline.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03-baseline.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03-baseline.png) | 2360 x 1168 | application-window |
| [c01-04-03-source-changed.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03-source-changed.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03-source-changed.png) | 2913 x 1441 | application-window |
| [c01-04-03-changed.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03-changed.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03-changed.png) | 2360 x 1168 | application-window |
| [c01-04-03-refresh-panel.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03-refresh-panel.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03-refresh-panel.png) | 2360 x 1168 | application-window |
| [c01-04-03-restored.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03-restored.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03-restored.png) | 2360 x 1168 | application-window |
| [c01-04-03.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-03.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-03.png) | 2360 x 1168 | application-window |
| [c01-04-challenge-new-task.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-new-task.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-new-task.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-range-failure.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-range-failure.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-range-failure.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-repaired.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-repaired.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-repaired.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-rule.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-rule.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-rule.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-positive.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-positive.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-positive.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-restored.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-restored.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-restored.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-final.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-final.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-final.png) | 2913 x 1441 | application-window |
| [c01-04-challenge-brief.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-brief.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-brief.png) | 2360 x 1168 | application-window |
| [c01-04-challenge-log.jpg](../../01-collaborative-tools/04-reporting-dashboard/images/c01-04-challenge-log.jpg) | [PNG](full/01-collaborative-tools/04-reporting-dashboard/c01-04-challenge-log.png) | 2360 x 1168 | application-window |
| [c01-05-created.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-created.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-created.png) | 2360 x 1112 | application-window |
| [c01-05-first-message.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-first-message.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-first-message.png) | 2360 x 1112 | application-window |
| [c01-05-story-plan.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-story-plan.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-story-plan.png) | 2360 x 1112 | application-window |
| [c01-05-status-link.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-status-link.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-status-link.png) | 2360 x 1112 | application-window |
| [c01-05-status-chart.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-status-chart.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-status-chart.png) | 2360 x 1112 | application-window |
| [c01-05-cost-link.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-cost-link.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-cost-link.png) | 2360 x 1112 | application-window |
| [c01-05-cost-chart.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-cost-chart.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-cost-chart.png) | 2360 x 1112 | application-window |
| [c01-05-process.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-process.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-process.png) | 2360 x 1112 | application-window |
| [c01-05-present-baseline.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-present-baseline.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-present-baseline.png) | 2360 x 1112 | application-window |
| [c01-05-version.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-version.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-version.png) | 2360 x 1112 | application-window |
| [c01-05-download.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-download.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-download.png) | 2360 x 1112 | application-window |
| [c01-05-correction-before.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-correction-before.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-correction-before.png) | 2360 x 1112 | application-window |
| [c01-05-correction-after.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-correction-after.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-correction-after.png) | 2360 x 1112 | application-window |
| [c01-05-corrected-summary.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-corrected-summary.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-corrected-summary.png) | 2360 x 1112 | application-window |
| [c01-05-update-available.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-update-available.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-update-available.png) | 2360 x 1168 | application-window |
| [c01-05-links-current.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-links-current.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-links-current.png) | 2360 x 1168 | application-window |
| [c01-05-corrected-message.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-corrected-message.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-corrected-message.png) | 2360 x 1168 | application-window |
| [c01-05-brief-current.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-brief-current.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-brief-current.png) | 2360 x 1112 | application-window |
| [c01-05-correction-log.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-correction-log.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-correction-log.png) | 2360 x 1112 | application-window |
| [c01-05-present-revised.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-present-revised.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-present-revised.png) | 2360 x 1168 | application-window |
| [c01-06-draft-banner.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-draft-banner.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-draft-banner.png) | 3399 x 1600 | application-window |
| [c01-06-three-pages.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-three-pages.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-three-pages.png) | 3399 x 1600 | application-window |
| [c01-06-visitor-action.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-visitor-action.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-visitor-action.png) | 3399 x 1600 | application-window |
| [c01-06-overview.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-overview.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-overview.png) | 3399 x 1600 | application-window |
| [c01-06-reporting-guidance.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-reporting-guidance.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-reporting-guidance.png) | 3399 x 1600 | application-window |
| [c01-06-decisions.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-decisions.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-decisions.png) | 3399 x 1600 | application-window |
| [c01-06-tracker-embed.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-tracker-embed.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-tracker-embed.png) | 3399 x 1600 | application-window |
| [c01-06-presentation-preview.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-presentation-preview.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-presentation-preview.png) | 3399 x 1600 | application-window |
| [c01-06-access-warning.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-access-warning.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-access-warning.png) | 3399 x 1600 | application-window |
| [c01-06-links-captions.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-links-captions.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-links-captions.png) | 3399 x 1600 | application-window |
| [c01-06-site-access.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-site-access.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-site-access.png) | 3399 x 1600 | application-window |
| [c01-06-deck-access.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-deck-access.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-deck-access.png) | 2360 x 1168 | application-window |
| [c01-06-tracker-access.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-tracker-access.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-tracker-access.png) | 2360 x 1112 | application-window |
| [c01-06-access-matrix.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-access-matrix.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-access-matrix.png) | 2360 x 1111 | application-window |
| [c01-06-operating-guide.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-operating-guide.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-operating-guide.png) | 2360 x 1111 | application-window |
| [c01-06-navigation-before.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-navigation-before.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-navigation-before.png) | 3399 x 1600 | application-window |
| [c01-06-navigation-after.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-navigation-after.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-navigation-after.png) | 3399 x 1600 | application-window |
| [c01-06-author-check.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-author-check.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-author-check.png) | 2360 x 1111 | application-window |
| [c01-06-readable-links.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-readable-links.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-readable-links.png) | 3399 x 1600 | application-window |
| [c01-06-readable-decisions.jpg](../../01-collaborative-tools/06-hub-handover/images/c01-06-readable-decisions.jpg) | [PNG](full/01-collaborative-tools/06-hub-handover/c01-06-readable-decisions.png) | 3399 x 1600 | application-window |
| [c01-05-pdf-r1.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-pdf-r1.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-pdf-r1.png) | 1224 x 689 | pdf-page |
| [c01-05-pdf-r2.jpg](../../01-collaborative-tools/05-evidence-update/images/c01-05-pdf-r2.jpg) | [PNG](full/01-collaborative-tools/05-evidence-update/c01-05-pdf-r2.png) | 1224 x 689 | pdf-page |
| [c02-01-folder.jpg](../../02-google-docs/01-document-sources/images/c02-01-folder.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-folder.png) | 1912 x 948 | application-window |
| [c02-01-starter-brief.jpg](../../02-google-docs/01-document-sources/images/c02-01-starter-brief.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-starter-brief.png) | 2360 x 1112 | application-window |
| [c02-01-requirements.jpg](../../02-google-docs/01-document-sources/images/c02-01-requirements.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-requirements.png) | 2360 x 1112 | application-window |
| [c02-01-saved-folder.jpg](../../02-google-docs/01-document-sources/images/c02-01-saved-folder.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-saved-folder.png) | 1912 x 948 | application-window |
| [c02-01-restricted-access.jpg](../../02-google-docs/01-document-sources/images/c02-01-restricted-access.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-restricted-access.png) | 2360 x 1112 | application-window |
| [c02-01-source-register.jpg](../../02-google-docs/01-document-sources/images/c02-01-source-register.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-source-register.png) | 2360 x 1112 | application-window |
| [c02-01-reader-questions.jpg](../../02-google-docs/01-document-sources/images/c02-01-reader-questions.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-reader-questions.png) | 2360 x 1112 | application-window |
| [c02-01-uploaded-sources.jpg](../../02-google-docs/01-document-sources/images/c02-01-uploaded-sources.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-uploaded-sources.png) | 1912 x 948 | application-window |
| [c02-01-descriptive-links.jpg](../../02-google-docs/01-document-sources/images/c02-01-descriptive-links.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-descriptive-links.png) | 2360 x 1112 | application-window |
| [c02-01-facts-source.jpg](../../02-google-docs/01-document-sources/images/c02-01-facts-source.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-facts-source.png) | 1912 x 901 | application-window |
| [c02-01-brief-source.jpg](../../02-google-docs/01-document-sources/images/c02-01-brief-source.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-brief-source.png) | 1912 x 901 | application-window |
| [c02-01-guidance-source.jpg](../../02-google-docs/01-document-sources/images/c02-01-guidance-source.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-guidance-source.png) | 1912 x 901 | application-window |
| [c02-01-memo-classification.jpg](../../02-google-docs/01-document-sources/images/c02-01-memo-classification.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-memo-classification.png) | 2360 x 1112 | application-window |
| [c02-01-purpose-scope.jpg](../../02-google-docs/01-document-sources/images/c02-01-purpose-scope.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-purpose-scope.png) | 2360 x 1112 | application-window |
| [c02-01-authoring-boundary.jpg](../../02-google-docs/01-document-sources/images/c02-01-authoring-boundary.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-authoring-boundary.png) | 2360 x 1112 | application-window |
| [c02-01-reopened-log.jpg](../../02-google-docs/01-document-sources/images/c02-01-reopened-log.jpg) | [PNG](full/02-google-docs/01-document-sources/c02-01-reopened-log.png) | 2360 x 1112 | application-window |
| [c02-02-source-grounded-prompt.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-source-grounded-prompt.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-source-grounded-prompt.png) | 2360 x 1112 | application-window |
| [c02-02-unreviewed-response.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-unreviewed-response.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-unreviewed-response.png) | 2360 x 1112 | application-window |
| [c02-02-response-checks.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-response-checks.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-response-checks.png) | 2360 x 1112 | application-window |
| [c02-02-human-review.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-human-review.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-human-review.png) | 2360 x 1112 | application-window |
| [c02-02-checked-draft.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-checked-draft.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-checked-draft.png) | 2360 x 1112 | application-window |
| [c02-02-open-decisions.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-open-decisions.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-open-decisions.png) | 2360 x 1112 | application-window |
| [c02-02-plan-first-steps.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-plan-first-steps.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-plan-first-steps.png) | 2360 x 1112 | application-window |
| [c02-02-plan-final-steps.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-plan-final-steps.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-plan-final-steps.png) | 2360 x 1112 | application-window |
| [c02-02-normal-and-exception.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-normal-and-exception.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-normal-and-exception.png) | 2360 x 1112 | application-window |
| [c02-02-status-repair.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-status-repair.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-status-repair.png) | 2360 x 1112 | application-window |
| [c02-02-clarity-rewrite.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-clarity-rewrite.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-clarity-rewrite.png) | 2360 x 1112 | application-window |
| [c02-02-paper-walkthroughs.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-paper-walkthroughs.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-paper-walkthroughs.png) | 2360 x 1112 | application-window |
| [c02-02-submission-distinction.jpg](../../02-google-docs/02-draft-procedure/images/c02-02-submission-distinction.jpg) | [PNG](full/02-google-docs/02-draft-procedure/c02-02-submission-distinction.png) | 2360 x 1112 | application-window |
| [c02-03-title-style.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-title-style.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-title-style.png) | 2360 x 1112 | application-window |
| [c02-03-heading-outline.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-heading-outline.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-heading-outline.png) | 2360 x 1112 | application-window |
| [c02-03-generated-contents.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-generated-contents.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-generated-contents.png) | 2360 x 1112 | application-window |
| [c02-03-stale-contents.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-stale-contents.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-stale-contents.png) | 2360 x 1112 | application-window |
| [c02-03-refreshed-contents.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-refreshed-contents.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-refreshed-contents.png) | 2360 x 1112 | application-window |
| [c02-03-bookmark.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-bookmark.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-bookmark.png) | 2360 x 1112 | application-window |
| [c02-03-opening-bookmark.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-opening-bookmark.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-opening-bookmark.png) | 2360 x 1112 | application-window |
| [c02-03-subsection-outline.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-subsection-outline.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-subsection-outline.png) | 2360 x 1112 | application-window |
| [c02-03-quick-start.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-quick-start.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-quick-start.png) | 2360 x 1112 | application-window |
| [c02-03-missing-owner-destination.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-missing-owner-destination.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-missing-owner-destination.png) | 2360 x 1112 | application-window |
| [c02-03-sponsor-destination.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-sponsor-destination.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-sponsor-destination.png) | 2360 x 1112 | application-window |
| [c02-03-practice-copy.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-practice-copy.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-practice-copy.png) | 2360 x 1112 | application-window |
| [c02-03-examples-tab.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-examples-tab.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-examples-tab.png) | 2360 x 1112 | application-window |
| [c02-03-examples-return.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-examples-return.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-examples-return.png) | 2360 x 1112 | application-window |
| [c02-03-return-main.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-return-main.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-return-main.png) | 2360 x 1112 | application-window |
| [c02-03-main-examples-link.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-main-examples-link.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-main-examples-link.png) | 2360 x 1112 | application-window |
| [c02-03-examples-contents.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-examples-contents.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-examples-contents.png) | 2360 x 1112 | application-window |
| [c02-03-main-contents.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-main-contents.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-main-contents.png) | 2360 x 1112 | application-window |
| [c02-03-move-selection.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-move-selection.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-move-selection.png) | 2360 x 1112 | application-window |
| [c02-03-moved-subsection.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-moved-subsection.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-moved-subsection.png) | 2360 x 1112 | application-window |
| [c02-03-renamed-subsection.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-renamed-subsection.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-renamed-subsection.png) | 2360 x 1112 | application-window |
| [c02-03-renamed-contents.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-renamed-contents.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-renamed-contents.png) | 2360 x 1112 | application-window |
| [c02-03-incoming-link-retested.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-incoming-link-retested.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-incoming-link-retested.png) | 2360 x 1112 | application-window |
| [c02-03-navigation-check.jpg](../../02-google-docs/03-styles-navigation/images/c02-03-navigation-check.jpg) | [PNG](full/02-google-docs/03-styles-navigation/c02-03-navigation-check.png) | 2360 x 1112 | application-window |
