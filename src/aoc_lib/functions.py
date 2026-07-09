def quadratic_sequence(seq: list[int], x: int) -> int:
    diff1 = seq[1] - seq[0]
    diff2 = seq[2] - seq[1] - diff1

    a = diff2 // 2
    b = diff1 - (3 * a)
    c = seq[0] - a - b

    return (a * (x**2)) + (b * x) + c


def calculate_polygon_area(coordinates: list[tuple[int, int]]) -> int:
    """
    Calculate the area of a polygon. This does not fully include the perimeter. To include the perimeter in the
    value add 1 + perimeter // 2 to the result.

    I'm not including the perimeter part of the calculation here for added flexibility in implementations.

    :param coordinates: List of x, y coordinates that define the perimeter of the polygon.
    :return: The area of the polygon excluding the perimeter.
    """
    x, y = zip(*coordinates)
    return abs(sum((x[i - 1] + x[i]) * (y[i - 1] - y[i]) for i in range(len(coordinates))) // 2)
