---
name: nexus-experiment-ux
description: Use when designing or improving ML experiment dashboards, comparison charts, EDA reports, metric cards, training-result pages, hover tooltips, or visual QA for experiment analysis interfaces.
---

# Nexus Experiment UX

## Principle

Show experiment and dataset evidence clearly. The UI is for recording, inspecting, analyzing, and comparing ML results, not for marketing or agent/workspace health.

## Design Defaults

- First screen should show meaningful experiment or dataset information.
- Use compact metric cards for current, best, delta, and baseline values.
- Use clear line charts for time-series metrics.
- Use comparison pages for baseline, rank, and per-metric deltas.
- Use EDA pages for rows, columns, missing values, detected types, distributions, outliers, and correlations.
- Prefer static HTML/SVG for simple projects; integrate with the existing frontend when one exists.

## Chart Requirements

- Hovering a plotted point must expose exact values.
- Multiple experiment lines must use distinct colors and markers or stroke patterns.
- Legends must not cover data.
- Axis labels and tick labels must not overlap.
- Long metric names must wrap or truncate professionally.
- Charts must stay readable on desktop and mobile.

## Avoid

- Landing pages unless explicitly requested.
- Agent health dashboards unless explicitly requested.
- Decorative dashboards with weak data density.
- One-color palettes where lines are hard to distinguish.
- Cards inside cards.
- Hero-scale typography inside tool panels.

## Visual QA

Before calling a generated UI complete, run the checklist in `references/visual-qa-checklist.md`. If using browser automation is available, inspect screenshots at desktop and mobile widths.

## References

- Read `references/dashboard-patterns.md` for page structure.
- Read `references/chart-interaction-patterns.md` for hover, comparison, and line clarity.
- Read `references/visual-qa-checklist.md` before completion.
- Use `assets/snippets/svg-line-chart-hover.html` as a small reference pattern, not as a fixed component.
