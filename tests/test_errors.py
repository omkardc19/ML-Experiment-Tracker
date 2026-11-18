from exptrack.errors import CorruptRunFileError, ExptrackError


def test_corrupt_run_file_error_is_exptrack_error():
    err = CorruptRunFileError("corrupt file")

    assert isinstance(err, ExptrackError)