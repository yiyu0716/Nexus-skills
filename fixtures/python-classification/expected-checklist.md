# Expected Checklist

The forward-tested agent should produce a project-specific workbench that satisfies:

- Does not copy or install the original Nexus implementation.
- Creates a clear generated experiment/report directory.
- Ingests `train_metrics.csv`.
- Computes latest and best `val/acc`.
- Respects metric direction: higher is better for `acc`, lower is better for `loss`.
- Generates a report or dashboard page.
- Includes a chart where hovering a point shows exact values.
- Runs EDA or dataset summary on `dataset_sample.csv`.
- Emits a machine-readable sentinel JSON line from at least one command.
- Does not modify the fixture CSV files.
- Includes at least one focused test or verification command.
