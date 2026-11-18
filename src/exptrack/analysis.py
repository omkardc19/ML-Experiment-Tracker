from collections.abc import Iterable
from typing import Literal

from exptrack.models import Run


def best_run(
    runs: Iterable[Run],  # iterable so we can pass in a list or a generator
    metric: str,
    mode: Literal["min", "max"] = "min",
) -> Run | None:
    """Return the best run based on a given metric and mode (min or max)."""

    best: Run | None = None

    for run in runs:
        if metric not in run.metrics:
            continue

        if best is None:
            best = run
            continue

        current_value = run.metrics[metric]
        best_value = best.metrics[metric]

        if mode == "min" and current_value < best_value  or mode == "max" and current_value > best_value:
            best = run

    return best
