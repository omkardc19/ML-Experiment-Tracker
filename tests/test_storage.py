from pathlib import Path

from exptrack.storage import load_runs, save_run


def test_save_and_load_runs(tmp_path: Path) -> None:
    path = tmp_path / "runs.jsonl"

    run1 = {
        "name": "baseline",
        "params": {"lr": 0.01},
        "metrics": {"rmse": 0.42},
    }

    run2 = {
        "name": "experiment_2",
        "params": {"lr": 0.02},
        "metrics": {"rmse": 0.38},
    }

    save_run(run1, path)
    save_run(run2, path)

    loaded_runs = load_runs(path)

    assert loaded_runs == [run1, run2]
