import math
from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Run(BaseModel):
    """A single run of an experiment, with a name, parameters, metrics, tags, and a timestamp."""

    model_config = ConfigDict(extra="forbid")  # NO EXTRA_FIELDS

    name: str = Field(min_length=1)
    params: dict[str, float | int | str | bool] = Field(default_factory=dict)
    metrics: dict[str, float] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("metrics")  # Make sure all metrics are finite numbers
    @classmethod
    def validate_metrics(cls, value: dict[str, float]) -> dict[str, float]:
        for metric_name, metric_value in value.items():
            if not math.isfinite(metric_value):
                raise ValueError(f"Metric '{metric_name}' must be finite")

        return value
