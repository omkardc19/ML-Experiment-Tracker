from pathlib import Path
import pytest

from exptrack.models import Run
from exptrack.storage import load_runs, save_run
from exptrack.errors import CorruptRunFileError
from exptrack.storage import iter_runs

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


def test_corrupt_line_raises_error_with_line_number(tmp_path):
    path = tmp_path / "runs.jsonl"

    path.write_text(
        '{"name": "valid-run", "params": {}, "metrics": {}}\n'
        'not-valid-json\n',
        encoding="utf-8",
    )

    with pytest.raises(
        CorruptRunFileError,
        match="line 2",
    ):
        list(iter_runs(path))