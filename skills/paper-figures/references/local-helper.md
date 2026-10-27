# Simple reproducible SVG plots

Run with Python 3.10+ from any working directory, using the actual Skill directory:

```text
python <skill-directory>/scripts/plot_svg.py results.csv figure.svg --x step --y accuracy --kind line --title "Validation accuracy"
```

CSV must have numeric, finite values in the chosen columns. Line x values must be nondecreasing. Bar x positions must be unique; bar axes include zero. The helper rejects missing/nonfinite data and existing output files. It writes SVG and a `.provenance.json` containing the input SHA-256, selected columns and row count. No aggregation, error bars, statistical inference or PDF conversion is performed.

For multipanel plots, distributions, uncertainty, categorical plots and publication-specific styling, use a suitable available plotting library and retain its generation code. Inspect at final physical size; XML validity alone is not visual QA. To regenerate, use a new output path or explicitly replace only the intended prior artifact.
