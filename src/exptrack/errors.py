# ExptrackError(Exception) as the base, and CorruptRunFileError(ExptrackError).



class ExptrackError(Exception):
    """Base class for all exceptions in the Exptrack package."""


class CorruptRunFileError(ExptrackError):
    """Exception raised when a run file is corrupt."""
