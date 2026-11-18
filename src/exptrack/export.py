import csv
from collections.abc import Iterable
from pathlib import Path

from exptrack.models import Run


def export_csv(runs: Iterable[Run], path: Path) -> int:
    """Export runs to CSV and return the number of exported rows."""
    runs = list(runs)

    param_keys: set[str] = set()
    metric_keys: set[str] = set()

    for run in runs:
        param_keys.update(run.params.keys())
        metric_keys.update(run.metrics.keys())

    param_keys_sorted = sorted(param_keys)
    metric_keys_sorted = sorted(metric_keys)

    columns = (
        ["name", "created_at", "tags"]
        + [f"param.{key}" for key in param_keys_sorted]
        + [f"metric.{key}" for key in metric_keys_sorted]
    )

    rows = sorted(runs, key=lambda run: run.name)

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        for run in rows:
            row = {
                "name": run.name,
                "created_at": run.created_at.isoformat(),
                "tags": ";".join(run.tags),
            }

            for key in param_keys_sorted:
                row[f"param.{key}"] = run.params.get(key, "")

            for key in metric_keys_sorted:
                row[f"metric.{key}"] = run.metrics.get(key, "")

            writer.writerow(row)

    return len(rows)