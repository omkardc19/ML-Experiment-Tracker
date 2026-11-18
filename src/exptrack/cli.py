import sys
from pathlib import Path

from exptrack.analysis import best_run
from exptrack.config import get_runs_path
from exptrack.errors import ExptrackError
from exptrack.export import export_csv
from exptrack.models import Run
from exptrack.storage import load_runs, save_run
from exptrack.timing import timer


def main() -> int:
    """Run Exptrack and return an exit code."""
    path = get_runs_path()

    try:
        run = Run(
            name="baseline",
            params={"lr": 0.01},
            metrics={"rmse": 0.02},
            tags=["baseline", "v1"],
        )
        save_run(run, path)

        with timer("load runs"):
            runs = load_runs(path)

        print(f"Total experiment runs: {len(runs)}")

        best = best_run(runs, metric="rmse", mode="min")

        if best is None:
            print("No runs found with the rmse metric.")
        else:
            print(f"Best run: {best.name} (RMSE: {best.metrics['rmse']})")

        csv_path = path.parent / "runs.csv"
        export_csv(runs, csv_path)
        print(f"CSV exported to: {csv_path}")

        return 0

    except ExptrackError as err:
        print(f"Exptrack error: {err}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())