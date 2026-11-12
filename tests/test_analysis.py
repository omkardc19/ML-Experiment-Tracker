from exptrack.analysis import best_run
from exptrack.models import Run


def test_best_run_min() -> None:
    runs = [
        Run(name="baseline", metrics={"rmse": 0.42}),
        Run(name="experiment_2", metrics={"rmse": 0.38}),
        Run(name="experiment_3", metrics={"rmse": 0.51}),
    ]

    result = best_run(runs, metric="rmse", mode="min")

    assert result is not None
    assert result.name == "experiment_2"


def test_best_run_max() -> None:
    runs = [
        Run(name="baseline", metrics={"accuracy": 0.85}),
        Run(name="experiment_2", metrics={"accuracy": 0.93}),
        Run(name="experiment_3", metrics={"accuracy": 0.89}),
    ]

    result = best_run(runs, metric="accuracy", mode="max")

    assert result is not None
    assert result.name == "experiment_2"


def test_missing_metric_is_skipped() -> None:
    runs = [
        Run(name="baseline", metrics={"rmse": 0.42}),
        Run(name="experiment_2", metrics={"accuracy": 0.95}),
        Run(name="experiment_3", metrics={"rmse": 0.38}),
    ]

    result = best_run(runs, metric="rmse", mode="min")

    assert result is not None
    assert result.name == "experiment_3"


def test_empty_input_returns_none() -> None:
    result = best_run([], metric="rmse")

    assert result is None
