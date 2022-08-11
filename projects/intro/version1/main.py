from manim import *

list_scene = ("SpiralInExample", "TestPi")
SCENE_NAME = list_scene[1]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"
config.background_color = YELLOW

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class Intro(Scene):
    def construct(self):
        pi = MathTex(r"\pi").scale(7)
        pi.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=GREEN_C, fill_opacity=1).shift(LEFT)
        square = Square(color=BLUE_D, fill_opacity=1).shift(UP)
        shapes = VGroup(pi, circle, square)
        self.play(SpiralIn(shapes))


class TestPi(Scene):
    def construct(self):
        svg = SVGMobject(file_name=r"PiCreatures_plain.svg")
        self.add(svg)