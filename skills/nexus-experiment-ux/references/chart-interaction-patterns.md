# Chart Interaction Patterns

## Line Charts

- Use SVG, canvas, or the project's existing chart library.
- Each run should have a distinct color.
- Add marker shapes or stroke patterns when many lines are present.
- Show exact values on hover.
- Keep labels and legends outside plotted data when possible.

## Tooltips

Tooltip should include:

- run/experiment label
- step or epoch
- metric name
- value
- split when present

## Comparison Charts

- Identify baseline clearly.
- Sort by metric direction when ranking.
- Show delta from baseline where meaningful.
- Avoid ranking metrics with unknown direction.

## Color

Avoid one-hue palettes. Use clearly separated colors for line identity. Do not rely on color alone when more than four runs are shown.
