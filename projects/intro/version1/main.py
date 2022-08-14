from manim import *
from common.svg.character.number_creature import NumberCreature
from common.svg.character.number_creature_anim import *

list_scene = ("SpiralInExample", "TestPi", "Example")
SCENE_NAME = list_scene[1]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"
config.background_color = BLACK

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
        pi = NumberCreature(
            file_name_prefix='PiCreatures',
            flip_at_start=False,
            mode="wonder"
        ).shift(LEFT*3+DOWN)
        self.play(Create(pi))
        self.wait()
        self.play(Blink(pi),  run_time=1)
        self.wait()
        bubble_kwargs = {
            "fill_color":BLACK,
            "fill_opacity": 0.5,
            "stroke_width":3,
            "stroke_color":WHITE,
            "stretch_width": 7,
            "stretch_height":3
        }
        self.play(NumberCreatureSays(
            pi,
            Tex("hello!", color=BLUE),
            target_mode="wonder",
            bubble_kwargs=bubble_kwargs
        ))
        rec = Rectangle().surround(pi, stretch=True)
        self.wait()
