from manim import *

def get_indexes(mob, font_size=15, color_tex=True):
    from itertools import cycle
    ni = VGroup()
    colors = cycle([RED, TEAL, GREEN, BLUE, PURPLE])
    for i in range(len(mob)):
        c = next(colors)
        n = Text(f"{i}",  font_size=font_size, font="Times", color=c)
        n.next_to(mob[i], DOWN, buff=0.05)
        ni.add(n)
        if color_tex: mob[i].set_color(c)
    return ni