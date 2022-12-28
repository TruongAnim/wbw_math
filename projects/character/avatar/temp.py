import math

from manim import *

PROJECT_NAME = "Temp"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Scene12", "Scene13", "Scene14", "Scene15", "Scene16", "Scene17")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[2]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class MyScene(Scene):
    def setup(self):
        self.slice_stroke_color = RED
        self.slice_fill_color = TEAL,
        self.slice_fill_opacity = 0.5

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


class Temp_Scene0(Scene):
    def construct(self):
        rec = Rectangle(width=1, height=math.sqrt(2), fill_opacity=0.3, fill_color=WHITE).scale(4).to_corner(UL)
        brace_right = Brace(rec, RIGHT)
        brace_down = Brace(rec, DOWN)
        width = Text("21 cm", color=YELLOW, font_size=80).next_to(brace_down, DOWN)
        height = Text("29.7 cm", color=YELLOW, font_size=80).next_to(brace_right, RIGHT)
        text = Text("A4", color=GREEN, font_size=85).move_to(rec)
        odd = Text("Why not 30?", color=RED, font_size=80).to_corner(UR)
        arrow = Arrow(odd.get_left(), height.get_top())
        avt = ImageMobject("outfit1 (267)").scale(2).to_corner(DR, buff=0).shift(RIGHT*0.5)
        self.add(rec, brace_right, brace_down, width, height, text, odd, arrow, avt)


class Temp_Scene1(Scene):
    def construct(self):
        text1 = MathTex("\sqrt{2}=1.4142...", color=GREEN).scale(2.5).to_corner(UL).shift(DOWN*2)
        text2 = MathTex("\sqrt{3}=1.7320...", color=BLUE).scale(2.5).next_to(text1, DOWN, aligned_edge=LEFT)
        text3 = MathTex("\sqrt{e}=1.6487...", color=RED).scale(2.5).next_to(text2, DOWN, aligned_edge=LEFT)
        avt = ImageMobject("outfit1 (88)").scale(2).to_corner(DR, buff=0).shift(RIGHT*0.5)
        odd = Text("But how?", color=YELLOW, font_size=130).to_corner(UR)

        self.add(text1, text2, text3, avt, odd)


class Temp_Scene2(Scene):
    def construct(self):
        formula1 = MathTex(r"\left ( \prod_{i=1}^{n} a_{i} \right )^{ {1}\over{n} }").scale(2).shift(LEFT*3+UP)
        formula2 = MathTex(r"{1 \over n} \sum_{i=1}^{n}a_{i}").scale(2).shift(RIGHT*3+UP)
        line = Line(DOWN*3, UP*3)
        gm = Text("TB. Nhân", font_size=80, font="Sans", color=GREEN).next_to(formula1, DOWN, buff=LARGE_BUFF)
        am = Text("TB. Cộng", font_size=80, font="Sans", color=BLUE).next_to(formula2, DOWN).align_to(gm, UP)
        self.add(formula1, formula2, line, am, gm)