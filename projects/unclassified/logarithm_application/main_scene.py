from manim import *
from common.custom.custom_mobject import TextTranslation

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
SCENE_NAME = list_scene[0]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class MyScene(Scene):
    def my_play(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):
        if "run_time" not in kwargs:
            kwargs["run_time"] = 2
        super().play(*args,
                     subcaption=subcaption,
                     subcaption_duration=subcaption_duration,
                     subcaption_offset=subcaption_offset,
                     **kwargs)
        self.wait(0.5)


class Scene0(MyScene):
    def construct(self):
        lt = TextTranslation("Lũy thừa", "(Exponentiation)", font_u="Sans",
                             color_u=YELLOW, color_d=RED).shift(DOWN * 2 + LEFT * 3)
        loga = TextTranslation("Logarit", "(Logarithm)", font_u="Sans",
                               color_u=YELLOW, color_d=GREEN).shift(DOWN * 2 + RIGHT * 3)

        ex_fomular = MathTex("a", "^b").scale(2).next_to(lt, UP, buff=1)
        ex_fomular[0].set_color(YELLOW)
        ex_fomular[1].set_color(TEAL)
        loga_fomular = MathTex("\log", "_a", "b").scale(2).next_to(loga, UP, buff=1)
        loga_fomular[1].set_color(YELLOW)
        loga_fomular[2].set_color(TEAL)
        # self.add(lt, loga, ex_fomular, loga_fomular)
        self.my_play(Write(lt), FadeIn(ex_fomular))
        self.my_play(Write(loga), FadeIn(loga_fomular))
