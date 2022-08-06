from manim import *


def parabola(t, amp=1):
    return (1 - (2 * t - 1) ** 2) * amp


def rate_func_from_bezier(handles, start_end=[0, 1], partitions=100):
    def simple_cubic_bezier(x1, y1, x2, y2):
        return bezier([
            np.array([0, start_end[0], 0]),
            np.array([x1, y1, 0]),
            np.array([x2, y2, 0]),
            np.array([1, start_end[1], 0]),
        ])

    def line_between_points(t, x1, x2, y1, y2):
        return (y2 - y1) * (t - x1) / (x2 - x1) + y1

    def closure_func(func, partitions=100):
        dt = 1 / partitions
        t_range = np.arange(0, 1 + dt, dt)
        x_range = [func(t)[0] for t in t_range]
        y_range = [func(t)[1] for t in t_range]

        x_steps = [
            (x_range[i], x_range[i + 1])
            for i in range(len(x_range) - 1)
        ]

        y_steps = [
            (y_range[i], y_range[i + 1])
            for i in range(len(y_range) - 1)
        ]

        def f(t):
            if t <= 0:
                return start_end[0]
            if t >= 1:
                return start_end[1]

            for i in range(len(x_range)):
                x1, x2 = x_steps[i]
                y1, y2 = y_steps[i]
                if x1 <= t <= x2:
                    return line_between_points(t, x1, x2, y1, y2)

        return f

    parametric_bezier = simple_cubic_bezier(*handles)
    cartesian_bezier = closure_func(parametric_bezier, partitions)
    return cartesian_bezier