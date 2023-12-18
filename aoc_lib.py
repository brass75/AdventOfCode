from collections.abc import Callable
import time


def timed_call(func: Callable):
    def time_func(*args, **kwargs):
        start = time.time()
        rc = func(*args, **kwargs)
        return rc, time.time() - start
    return time_func


@timed_call
def _solve_problem(func: Callable, *args, **kwargs):
    return func(*args, **kwargs)


def calculate_polygon_area(coordinates: list[tuple[int, int]]) -> int:
    """
    Calculate the area of a polygon. This does not fully include the perimeter. To include the perimeter in the
    value add 1 + perimeter // 2 to the result.

    I'm not including the perimeter part of the calculation here for added flexibility in implementations.

    :param coordinates: List of x, y coordinates that define the perimeter of the polygon.
    :return: The area of the polygon excluding the perimeter.
    """
    x, y = zip(*coordinates)
    return abs(sum((x[i-1] + x[i]) * (y[i-1] - y[i]) for i in range(len(coordinates)))//2)


def solve_problem(func: Callable, part: int, test_data: tuple[int, int] | None, *args, **kwargs):
    result, run_time = _solve_problem(func, *args, *kwargs)
    test_string = ''
    if test_data:
        test, expected = test_data
        assert result == expected, f'Test {test} for part {part} failed: {expected=} {result=}'
        test_string = f' [test {test}]'
    print(f'Part 1{test_string}: {result} [elapsed time: {run_time * 1000:.5f}ms]')
