import pytest

from exptrack.timing import timer


def test_timer_prints_label(capsys):
    with timer("my task"):
        pass

    output = capsys.readouterr().out

    assert "my task:" in output
    assert "ms" in output


def test_timer_prints_when_block_raises(capsys):
    with pytest.raises(ValueError):
        with timer("failing task"):
            raise ValueError("boom")

    output = capsys.readouterr().out

    assert "failing task:" in output
    assert "ms" in output