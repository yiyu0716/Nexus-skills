# Dashboard Patterns

## Page Types

- overview: tasks/projects/runs and recent results
- experiment detail: metrics, artifacts, notes, report links
- comparison: baseline, rankings, deltas, multi-run charts
- EDA report: dataset shape, missing values, types, distributions, outliers

## Overview Layout

Prefer dense, useful information:

- compact header with project/task context
- metric summary cards
- recent runs table
- top comparison chart
- links to reports and artifacts

Avoid marketing heroes and generic empty-state copy when data exists.

## Experiment Detail

Include:

- run identity and timestamp if available
- latest and best metrics
- metric curves
- artifacts and report links
- configuration summary if present

## EDA Report

Include:

- row and column counts
- file size
- detected column types
- missing-value table
- numeric summary
- distributions
- categorical counts
- outliers and correlations when available
