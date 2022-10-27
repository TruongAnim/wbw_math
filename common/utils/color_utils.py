from manim import interpolate_color
from colour import Color

def interpolate_color_range(*colors):
    alpha = colors[-1]
    colors = colors[:-1]
    partition = len(colors)
    dx = 1 / (partition - 1)

    colors_steps = [
        (colors[i], colors[i + 1])
        for i in range(partition - 1)
    ]

    alpha_steps = [
        (dx * i, dx * (i + 1))
        for i in range(partition - 1)
    ]

    i_count = 0

    for c_s, a_s in zip(colors_steps, alpha_steps):
        if a_s[0] <= alpha <= a_s[1]:
            d_alpha = alpha - dx * i_count
            c_alpha = d_alpha / dx
            return interpolate_color(c_s[0], c_s[1], c_alpha)
        i_count += 1


def HSL(hue, saturation=1, lightness=0.5):
    return Color(hsl=(hue, saturation, lightness))