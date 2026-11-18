import csv

from exptrack.export import export_csv
from exptrack.models import Run


def test_export_csv_with_different_metrics(tmp_path):
    path = tmp_path / "runs.csv"

    # baseline
    run1 = Run(
        name="baseline",
        params={"lr": 0.01},
        metrics={"rmse": 0.42},
        tags=["baseline", "cpu"],
    )

    # experiment_2 
    run2 = Run(
        name="experiment_2",
        params={"lr": 0.02, "batch_size": 32},
        metrics={"accuracy": 0.91},
    )

    count = export_csv([run1, run2], path)

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert count == 2
    assert len(rows) == 2

    assert "name" in reader.fieldnames
    assert "created_at" in reader.fieldnames
    assert "tags" in reader.fieldnames
    assert "param.lr" in reader.fieldnames
    assert "param.batch_size" in reader.fieldnames
    assert "metric.rmse" in reader.fieldnames
    assert "metric.accuracy" in reader.fieldnames

    baseline = next(row for row in rows if row["name"] == "baseline")  #first row is baseline
    experiment_2 = next(row for row in rows if row["name"] == "experiment_2")  #second row is experiment_2

    assert baseline["metric.rmse"] == "0.42"
    assert baseline["metric.accuracy"] == ""
    assert experiment_2["metric.accuracy"] == "0.91"
    assert experiment_2["metric.rmse"] == ""
    assert baseline["tags"] == "baseline;cpu"