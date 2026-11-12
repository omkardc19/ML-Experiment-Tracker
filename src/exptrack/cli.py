from pathlib import Path

from exptrack.analysis import best_run
from exptrack.models import Run
from exptrack.storage import load_runs, save_run


def main() -> None:
    """A main() that builds a sample run, saves it to runs.jsonl, and prints how many runs exist."""

    run = Run(
        name="baseline",
        params={"lr": 0.01},
        metrics={"rmse": 0.02},
        tags=["baseline", "v1"],
    )

    path = Path("runs.jsonl")
    save_run(run, path)

    runs = load_runs(path)
    print(f"Total experiment runs: {len(runs)}")
    best = best_run(runs, metric="rmse", mode="min")

    if best is None:
        print("No runs found with the rmse metric.")
    else:
        print(f"Best run: {best.name} (RMSE: {best.metrics['rmse']})")


if __name__ == "__main__":
    main()
