from pathlib import Path

from exptrack.config import get_runs_path


def test_get_runs_path_uses_env_variable(monkeypatch, tmp_path):
    monkeypatch.setenv("EXPTRACK_HOME", str(tmp_path))

    result = get_runs_path()

    assert result == tmp_path / "runs.jsonl"


def test_get_runs_path_uses_home_when_env_missing(monkeypatch):
    monkeypatch.delenv("EXPTRACK_HOME", raising=False)

    result = get_runs_path()

    assert result == Path.home() / ".exptrack" / "runs.jsonl"