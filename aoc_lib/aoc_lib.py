import time
from collections.abc import Callable
import tracemalloc


def timed_call(func: Callable):
    def time_func(*args, **kwargs):
        start = time.time()
        rc = func(*args, **kwargs)
        return rc, time.time() - start

    return time_func


@timed_call
def _solve_problem(func: Callable, *args, **kwargs):
    return func(*args, **kwargs)


def solve_problem(func: Callable, part: int, test_data: tuple[int, int] | None, *args, **kwargs):
    result, run_time = _solve_problem(func, *args, *kwargs)
    test_string = ''
    if test_data:
        test, expected = test_data
        assert result == expected, f'Test {test} for part {part} failed: {expected=} {result=}'
        test_string = f' [test {test}]'
    print(f'Part {part}{test_string}: {result} [elapsed time: {run_time * 1000:.5f}ms]')


def tracer(func):
    """Tracer decorator"""

    def wrapper(*args, **kwargs):
        """Tracer Wrapper"""
        tracemalloc.start()
        rc = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f'Current memory usage for {func.__name__} is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB')
        tracemalloc.stop()
        return rc

    return wrapper

