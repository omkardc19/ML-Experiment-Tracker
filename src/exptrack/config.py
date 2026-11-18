import os
from pathlib import Path


def get_runs_path() -> Path:
    """Get the path to the runs.jsonl file, using EXPTRACK_HOME if set, otherwise defaulting to ~/.exptrack/runs.jsonl."""
    exptrack_home = os.getenv("EXPTRACK_HOME")

    if exptrack_home:
        folder = Path(exptrack_home)
    else:
        folder = Path.home() / ".exptrack"

    return folder / "runs.jsonl"