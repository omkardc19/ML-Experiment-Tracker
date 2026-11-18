from collections.abc import Iterator
from pathlib import Path
from pydantic import ValidationError

from exptrack.errors import CorruptRunFileError
from exptrack.models import Run


def save_run(run: Run, path: Path) -> None:
    """Append a run as a JSON line to the file at `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        file.write(run.model_dump_json())
        file.write("\n")


def iter_runs(path: Path) -> Iterator[Run]:
    """Yield runs from a JSON-lines file, validating each line."""
    if not path.exists():
        return

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip():
                try:
                    yield Run.model_validate_json(line)
                except ValidationError as err:
                    raise CorruptRunFileError(
                        f"{path}, line {line_number}: invalid run"
                    ) from err


def load_runs(path: Path) -> list[Run]:
    """Load all runs from a JSON-lines file, eager evaluation."""
    if not path.exists():
        return []

    return list(iter_runs(path))
