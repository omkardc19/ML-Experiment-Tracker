import json
from pathlib import Path


def save_run(run: dict, path: Path) -> None:
    """Append a run as a JSON line to the file at `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(run))
        file.write("\n")


def load_runs(path: Path) -> list[dict]:
    """Load all runs from a JSON-lines file."""
    if not path.exists():
        return []

    runs: list[dict] = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                runs.append(json.loads(line))
    return runs
