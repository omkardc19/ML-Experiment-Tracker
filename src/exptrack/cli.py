from pathlib import Path

from exptrack.storage import load_runs, save_run


def main() -> None:
    """A main() that builds a sample run such as {"name": "baseline", "params": {"lr": 0.01}, "metrics": {"rmse": 0.42}}, saves it to runs.jsonl, and prints how many runs exist."""
    run = {
        "name": "baseline",
        "params": {"lr": 0.01},
        "metrics": {"rmse": 0.42},
    }

    path = Path("runs.jsonl")
    save_run(run, path)
    runs = load_runs(path)
    print(f"Total experiment runs: {len(runs)}")


if __name__ == "__main__":
    main()
