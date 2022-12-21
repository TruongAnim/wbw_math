import math

from manim import *
import random

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Thumbnail")
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


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Scene0(MyScene):
    def construct(self):
        #                       01234567890123456789012345
        e = MathTex(r"e", "=", "2.718281828459045235360287...").scale(1.7)
        # 281
        rec1 = Rectangle(color=YELLOW).surround(VGroup(e[2][5:8]), stretch=True)
        # 4253
        rec2 = Rectangle(color=YELLOW).surround(VGroup(e[2][15:19]), stretch=True)
        # 360287
        rec3 = Rectangle(color=YELLOW).surround(VGroup(e[2][20:26]), stretch=True)
        # 904523
        rec4 = Rectangle(color=YELLOW).surround(VGroup(e[2][13:19]), stretch=True)

        text1 = Text("Số nguyên tố", font_size=60, font="Sans", color=GREEN).to_edge(UP)
        arrow1 = Arrow(text1.get_bottom(), rec1.get_top())
        arrow2 = Arrow(text1.get_bottom(), rec2.get_top())
        arrow3 = Arrow(text1.get_bottom(), rec3.get_top())
        arrow4 = Arrow(text1.get_bottom(), rec4.get_top())

        prime1 = Text("3 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec1, DOWN)
        prime2 = Text("4 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec2, DOWN)
        prime3 = Text("6 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec3, DOWN)
        prime4 = Text("6 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec4, DOWN)

        # self.add(e, rec1, rec2, rec3, arrow1, arrow2, arrow3, prime1, prime2, prime3, text1)
        self.play(FadeIn(e[0:2]))
        self.my_play(AddTextLetterByLetter(e[2]))
        self.play(Write(text1), GrowArrow(arrow1), Create(rec1), FadeIn(prime1, shift=UP))
        self.play(Indicate(VGroup(e[2][5:8])))
        self.play(Transform(arrow1, arrow2), Transform(rec1, rec2), Transform(prime1, prime2))
        self.play(Indicate(VGroup(e[2][15:19])))
        self.play(Transform(arrow1, arrow3), Transform(rec1, rec3), Transform(prime1, prime3))
        self.play(Indicate(VGroup(e[2][20:26])))
        self.play(Transform(arrow1, arrow4), Transform(rec1, rec4), Transform(prime1, prime4))
        self.play(Indicate(VGroup(e[2][13:19])))
