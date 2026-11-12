import pytest
from pydantic import ValidationError

from exptrack.models import Run


def test_valid_run() -> None:
    run = Run(
        name="baseline",
        params={"lr": 0.01},
        metrics={"rmse": 0.42},
        tags=["v1"],
    )

    assert run.name == "baseline"
    assert run.metrics["rmse"] == 0.42
    assert run.created_at.tzinfo is not None


def test_empty_name_rejected() -> None: 
    with pytest.raises(ValidationError):
        Run(name="")


def test_nan_metric_rejected() -> None:
    with pytest.raises(ValidationError):
        Run(name="baseline", metrics={"rmse": float("nan")})


def test_unknown_field_rejected() -> None:
    with pytest.raises(ValidationError):
        Run.model_validate(
            {
                "name": "baseline",
                "unknown_field": 123,
            }
        )


def test_string_metric_converted_to_float() -> None:
    run = Run.model_validate(
        {
            "name": "baseline",
            "metrics": {"rmse": "0.5"},
        }
    )

    assert run.metrics["rmse"] == 0.5
    assert isinstance(run.metrics["rmse"], float)
