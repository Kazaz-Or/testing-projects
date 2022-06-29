from datetime import datetime, timedelta
from typing import Callable

import pytest

from exceptions import PerformanceException


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"\n runtime: {diff.total_seconds()}")


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_func_and_validate_runtime(*args, **kwargs):
        tick = datetime.now()
        result = method(*args, **kwargs)
        tock = datetime.now()
        runtime = tock - tick
        print(f"\n runtime: {runtime.total_seconds()}")

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)
        return result

    return run_func_and_validate_runtime
