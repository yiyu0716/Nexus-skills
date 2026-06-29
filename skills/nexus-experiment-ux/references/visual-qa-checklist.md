# Visual QA Checklist

Do not call the experiment UI complete until this passes.

## Chart QA

- Hovering a point shows exact value.
- Multiple lines are visually distinct.
- Legends do not cover data.
- Axis labels are readable.
- Long metric names do not break layout.
- Empty or missing data states are clear.

## Layout QA

- First screen shows useful experiment or dataset information.
- Metric cards fit their numbers.
- Tables do not overflow horizontally without a deliberate scroll container.
- Mobile width does not overlap text, charts, or cards.
- Generated pages can open from disk or static hosting without broken assets.

## Data QA

- Latest/best values match source data.
- Metric direction is respected.
- Unknown-direction metrics are not ranked as if direction were known.
- Raw artifact links point to existing files or are omitted.
