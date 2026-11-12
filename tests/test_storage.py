from pathlib import Path

from exptrack.models import Run
from exptrack.storage import load_runs, save_run


def test_save_and_load_runs(tmp_path: Path) -> None:
    path = (
        tmp_path / "runs.jsonl"
    )  # tmp_path is a pytest fixture that provides a temporary directory for the test to use. We create a Path object for the runs.jsonl file within that temporary directory.

    run1 = Run(
        name="baseline",
        params={"lr": 0.01},
        metrics={"rmse": 0.42},
    )

    run2 = Run(
        name="experiment_2",
        params={"lr": 0.02},
        metrics={"rmse": 0.38},
    )

    save_run(run1, path)
    save_run(run2, path)

    loaded_runs = load_runs(path)

    assert loaded_runs == [run1, run2]
    assert loaded_runs[0].created_at == run1.created_at
    assert loaded_runs[1].created_at == run2.created_at
