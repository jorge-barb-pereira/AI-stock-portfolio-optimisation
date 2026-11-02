# Source review

Review of the existing `otimizador.py` as academic optimisation code. The main implementation is byte-identical to the supplied source; this documentation update does not silently replace its objective or algorithm behavior.

## Findings to resolve before stronger claims

1. **Time alignment.** The loader sorts each file by Date but does not set Date as the return-series index. Concatenating percentage-change series by their inherited integer index can pair returns from different dates. A maintained data loader should explicitly align by trading date and define the missing-date policy before estimating covariance.
2. **Objective units.** The original objective combines percentage-return parameters with integer share counts. Decide whether the intended variable is share count, currency position or portfolio weight, then derive compatible expected-profit and covariance expressions. Document budget and risk-aversion units before comparing economic utility.
3. **Data-path behavior.** The loader's `base_path` parameter is overwritten with `archive/`; running from a different working directory or using another dataset path is unsupported. Missing files produce sentinel None values that the main workflow does not fully guard.
4. **Randomness and comparisons.** Randomized algorithms do not have one documented seed policy, repeated-run uncertainty or a fixed shared evaluation budget. A single plotted run does not establish superiority or robust convergence.
5. **Historical price interpretation.** The model uses Close even where Adj Close is present. Corporate actions, date overlap, survivorship, transaction costs and out-of-sample evaluation need explicit treatment before financial interpretation.
6. **Plot and implementation maintenance.** The source defines `plot_algorithm_comparison_dashboard` twice; Python uses the later definition. Warnings are globally suppressed. Random allocation plots and heuristic outcomes are not an exact efficient-frontier solution or a certificate of global optimality.

## Validation included in this update

The source check parses Python without executing expensive optimisation, validates the cleaned main notebook, confirms 100 stock CSV files and inventories their date ranges and common calendar. It does not assert that the original loader correctly uses that calendar, execute all five full-scale searches, validate the financial objective or certify plotted rankings. CI repeats the source/data check on Python 3.11 and 3.12 using only the standard library.

The supplied data check found 344 calendar dates shared by all 100 files, with overall date coverage from 3 January 2000 through 1 April 2020. These are inventory results, not proof that the original return loader aligns observations correctly.

## Next maintained implementation

A future revision should separate data loading, objective, seeded optimisers and plotting; agree on the objective units; align returns by date; validate constraints independently; benchmark small problems against enumeration; and compare repeated runs on a shared evaluation budget. These changes would alter scientific results and should be developed explicitly with fresh figures, not disguised as a documentation cleanup.
