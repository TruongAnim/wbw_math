from manim import *
from common.characters.symbols.pi_symbol import *
from common.utils.mobject_utils import get_indexes

list_scene = ("SpiralInExample", "TestPi", "Example")
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
        pi = NumberCreature(file_name_prefix='PiCreatures', color=BLUE,
                            flip_at_start=False,
                            height=3).look(RIGHT)
        self.play(Create(pi))
        indexes = get_indexes(pi, font_size=20, color_obj=False)
        self.add(indexes)
        square = Square().set(height=1).shift(LEFT*3)
        self.add(square)
        self.wait()
        pi.generate_target()
        pi.target.change("thinking").look_at(square)
        self.play(MoveToTarget(pi))
        self.wait()