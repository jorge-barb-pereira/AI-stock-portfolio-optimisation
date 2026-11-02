# Stock Portfolio Optimisation with Metaheuristic Search

An academic artificial-intelligence project comparing five search methods for an integer share-allocation problem: **Hill Climbing, Simulated Annealing, Genetic Algorithm, Tabu Search and discrete Particle Swarm Optimisation**.

**Original work: November 2025.** Existing Git history records development by 17 November 2025; the academic presentation is dated November 2025. Authors credited in the presentation: **Jorge Barbosa Pereira, Julio Cesar Cisneros Rios and Rafael Santos Novais**. Documentation and source review were added in October 2026.

## Project overview

The program loads historical Australian stock-price CSVs, estimates annualized return and covariance parameters, searches for nonnegative integer share allocations, and produces convergence, composition and algorithm-comparison figures. Defaults use a budget of 5,000 and a maximum investment of 1,000 per asset.

| Path | Contents |
| --- | --- |
| `otimizador.py` | Original five-algorithm implementation and plotting workflow |
| `archive/` | 100 existing historical stock-price CSVs |
| Root PNG files | Original comparison figures |
| `notebooks/optimization.ipynb` | Original project's main notebook, with saved outputs and execution metadata removed |
| `docs/REVIEW.md` | Objective definition, reproducibility findings and scientific limitations |
| `docs/PROVENANCE.md` | Development dates, authorship and source mapping |
| `tools/check_sources.py` | Syntax, notebook and data inventory checks |

## Run the historical program

Use Python 3.11 or newer from the repository root:

```bash
python -m venv .venv
# Windows PowerShell: .venv/Scripts/Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python tools/check_sources.py
python otimizador.py
```

The full program runs all five methods, including 40,000 annealing iterations, and writes figures in the current directory. Runtime depends on hardware and parameters in the main block. Original comments and notebook text retain their historical language. The documentation describes the source as it exists; it does not claim reproducible random seeds or financial model validation.

![Original convergence-speed comparison](velocidade_convergencia.png)

## Model interpretation

The implemented score is `mu.T @ x - lambda * (x.T @ covariance @ x) - penalties`, where `x` counts shares, `mu` contains annualized percentage returns, and penalties apply to budget/per-asset investment violations. This is the coursework objective. Multiplying percentage returns by share counts does not by itself produce currency profit or a normalized portfolio return; the corresponding risk term also needs consistent position units before financial interpretation.

The data loader computes returns before aligning different assets by their DataFrame row index. Those indices are not guaranteed to identify the same trading date, and the function overrides its base_path argument. These and other findings are recorded in [the source review](docs/REVIEW.md). Historical plot labels such as efficient frontier are not proof of an exact Pareto frontier or a validated investment strategy.

## Related work and attribution

The companion [Credit Risk Classification](https://github.com/jorge-barb-pereira/credit-risk-classification) project is maintained in its own repository, with separate data, dependencies and evaluation protocol.

The original presentation cites Ash Bellett's [Australian Historical Stock Prices](https://www.kaggle.com/datasets/ashbellett/australian-historical-stock-prices). The CSVs were already present in this repository; dataset redistribution terms must be verified at the original source before repackaging. No new blanket license is asserted over the coauthored work or dataset. See [provenance](docs/PROVENANCE.md).
