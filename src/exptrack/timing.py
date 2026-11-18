import time
from collections.abc import Iterator
from contextlib import contextmanager

@contextmanager
def timer(label: str) -> Iterator[None]:
    start = time.perf_counter()        # setup
    try:
        yield                          # the body of the `with` block runs here
    finally:
        elapsed = (time.perf_counter() - start) * 1000
        print(f"{label}: {elapsed:.1f} ms")   # cleanup, always runs

