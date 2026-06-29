# Data Model Patterns

Design concepts, not fixed table names.

## Core Entities

- task: problem, dataset, benchmark, or research question
- project: model family, method, or experiment group
- experiment/run: one concrete training or evaluation attempt
- metric: scalar or time-series result
- artifact: raw file, processed file, figure, model, report
- report: generated human-readable page
- note/event: optional comments and timeline entries

## Minimal File Model

```text
experiments/
  {task}/
    {project}/
      {run_id}_{short_name}/
        raw/
        metrics/
        analysis/
        figures/
        reports/
```

## Metric Normalization

A useful normalized metric row usually contains:

- step or epoch
- split: train, val, test, all
- metric name
- numeric value
- optional timestamp

## Metric Direction

Encode whether higher or lower is better. Common defaults:

- higher: accuracy, precision, recall, f1, auc, mAP, bleu, rouge, r2
- lower: loss, perplexity, mse, mae, rmse, smape, error_rate

When unsure, mark direction unknown and avoid ranking that metric.

## Safety Rules

- Never mutate raw input files.
- Copy, reference, or summarize raw artifacts.
- Never overwrite a run without an explicit update policy.
- Use generated directories for reports and derived files.
