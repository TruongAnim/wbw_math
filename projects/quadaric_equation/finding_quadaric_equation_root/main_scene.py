import math
import random

from manim import *
from common.custom.custom_mobject import SetNumber
from common.custom.custom_mobject import TextTranslation

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Thumbnail")
SCENE_NAME = list_scene[4]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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
        class MyText(Text):
            def __init__(self,
                         text: str):
                super().__init__(text=text, font="Sans")

        chart = BarChart(values=[100, 50, 25, 12.5, 6.25], y_range=[0, 120, 25],
                         bar_names=["Khi học", "Sau 1 năm", "Sau 2 năm", "Sau 3 năm", "Sau 4 năm"],
                         x_length=12,
                         tips=True,
                         x_axis_config={
                             "label_constructor": MyText
                         },
                         y_axis_config={
                             "label_constructor": MathTex
                         }).shift(UP)
        c_bar_lbls = chart.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )
        equation = MathTex("a", "x", "^2", "+", "b", "x", "+", "c", "=", "0").scale(2).to_edge(RIGHT).shift(UP * 2)
        equation.set_color("#ffa600")
        bars = chart.bars
        chart.remove(chart.bars)

        self.play(Create(chart))
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in bars], lag_ratio=0.5),
                  LaggedStart(*[FadeIn(i) for i in c_bar_lbls], lag_ratio=0.5))
        self.wait(0.5)
        self.my_play(Transform(bars[4].copy(), equation))


class Scene1(MyScene):
    def construct(self):
        ax = Axes(x_range=[-6, 6, 1],
                  y_range=[-4, 4, 1],
                  x_length=12,
                  y_length=8,
                  tips=True)

        def get_func(a, b, c):
            def temp(x):
                return a * x * x + b * x + c

            return temp

        graph1 = ax.plot(get_func(1, 0, -3), x_range=[-2.5, 2.5], use_smoothing=False, color=RED)
        graph2 = ax.plot(get_func(-1, 2, 1), x_range=[-1.24, 3.2], use_smoothing=False, color=GREEN)
        graph3 = ax.plot(get_func(0.5, 2, -1), x_range=[-5.45, 1.5], use_smoothing=False, color=BLUE)
        A = Dot(ax.coords_to_point(-1.732, 0), color=YELLOW)
        A_t = MathTex("x_1", color=YELLOW).next_to(A, DL)
        B = Dot(ax.coords_to_point(1.732, 0), color=YELLOW)
        B_t = MathTex("x_2", color=YELLOW).next_to(B, DR)
        formula1 = MathTex("x^2-3", color=RED).move_to(ax.c2p(3.5, 3.3))
        formula2 = MathTex("-x^2+2x+1", color=GREEN).move_to(ax.c2p(4.2, -3))
        formula3 = MathTex("0.5x^2+2x-1", color=BLUE).move_to(ax.c2p(-5.5, 3.3))
        equation = MathTex("a", "x", "^2", "+", "b", "x", "+", "c", "=", "0").scale(1.5).to_corner(DL,
                                                                                                   buff=MED_SMALL_BUFF)
        equation.set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": BLUE
        })
        # self.add(ax, graph1, graph2, graph3, A, B, A_t, B_t, formula1, formula3, formula2, equation)
        self.my_play(Write(equation), Create(ax))
        self.my_play(Write(graph1), Write(formula1))
        self.my_play(FadeIn(A), FadeIn(B), FadeIn(A_t, shift=UP), FadeIn(B_t, shift=UP))
        self.my_play(Write(graph2), Write(formula2))
        self.my_play(Write(graph3), Write(formula3))
        self.my_play(Circumscribe(equation[0]),
                     Circumscribe(equation[4]),
                     Circumscribe(equation[7]))


class Scene2(MyScene):
    def construct(self):
        ax = Axes(x_range=[-4, 3, 1],
                  y_range=[-3, 4, 1],
                  x_length=7,
                  y_length=7,
                  tips=True).to_edge(RIGHT)

        def get_func1(x):
            return math.sqrt(4 - x ** 2)

        def get_func2(x):
            return -math.sqrt(4 - x ** 2)

        def get_func3(x):
            return x + 1

        graph1 = ax.plot(get_func1, x_range=[-2, 2, 0.01], use_smoothing=True, color=RED)
        graph2 = ax.plot(get_func2, x_range=[-2, 2, 0.01], use_smoothing=True, color=RED)
        graph3 = ax.plot(get_func3, x_range=[-4, 3, 0.1], use_smoothing=True, color=BLUE)
        A = Dot(ax.coords_to_point(-1.823, -0.823), color=YELLOW)
        A_t = MathTex("x_1", color=YELLOW).next_to(A, LEFT)
        B = Dot(ax.coords_to_point(0.823, 1.823), color=YELLOW)
        B_t = MathTex("x_2", color=YELLOW).next_to(B, DOWN)
        line = Line(A, B).get_angle()
        formula1 = MathTex("x^2+y^2=4", color=RED).move_to(ax.c2p(2, -2.2))
        formula3 = MathTex("y=x+1", color=BLUE)
        equation = MathTex("a", "x", "^2", "+", "b", "x", "+", "c", "=", "0") \
            .scale(1.5).to_corner(DL, buff=MED_SMALL_BUFF)
        equation.set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": BLUE
        })
        f1 = formula1.copy().to_corner(UL).shift(RIGHT*0.5)
        f2 = formula3.copy().next_to(f1, DOWN, aligned_edge=LEFT)
        formula3.scale(0.75).next_to(graph3.point_from_proportion(0.92), UP, buff=SMALL_BUFF).rotate(line)
        brace = Brace(VGroup(f1, f2), LEFT)
        f3 = MathTex(r"\rightarrow x^2+(x+1)^2-4=0", color=GREEN).next_to(brace, DOWN, aligned_edge=LEFT)
        f4 = MathTex(r"\rightarrow x^2+(x+1)^2-4=0", color=GREEN).next_to(f3, DOWN, aligned_edge=LEFT)
        f5 = MathTex(r"\rightarrow 2x^2+2x-3=0", color=GREEN).next_to(f4, DOWN, aligned_edge=LEFT)
        computer = SVGMobject("computer_plain", color=BLUE).next_to(f5, DOWN)
        apply = Text("Áp dụng công thức nghiệm:", font="Sans", font_size=35, color=YELLOW).next_to(f5, DOWN,
                                                                                                   aligned_edge=LEFT)
        x1 = MathTex("x_1", "=", "{-2-\sqrt{28}\over{4}}", color=YELLOW).next_to(apply, DOWN)
        x2 = MathTex("x_2", "=", "{-2+\sqrt{28}\over{4}}", color=YELLOW).next_to(x1, DOWN)
        brace2 = Brace(VGroup(x1, x2), LEFT)
        self.play(Create(ax), Create(graph1), Create(graph2), Create(graph3), Write(formula3), Write(formula1))
        self.play(LaggedStart(*[Transform(formula1.copy(), f1), Transform(formula3.copy(), f2)], lag_ratio=0.5),
                  FadeIn(brace, shift=LEFT))
        self.wait(0.5)
        self.play(Write(f3))
        self.play(Write(f4))
        self.play(Write(f5))
        self.wait(0.5)
        self.play(Write(apply))
        self.play(FadeIn(brace2, shift=RIGHT), Write(x1), Write(x2))
        self.wait(0.5)
        self.play(LaggedStart(*[Transform(x1[2].copy(), A), Transform(x1[0].copy(), A_t)]))
        self.play(LaggedStart(*[Transform(x2[2].copy(), B), Transform(x2[0].copy(), B_t)]))
        self.wait()
        self.add(ax, graph1, graph2, graph3, A, B, A_t, B_t, formula1, formula3)
        self.add(f1, f2, f3, f4, f5, brace, apply, x1, x2, brace2)


class Scene3(MyScene):
    def construct(self):
        ax = Axes(x_range=[-4, 3, 1],
                  y_range=[-3, 4, 1],
                  x_length=7,
                  y_length=7,
                  tips=True).to_edge(RIGHT)

        def get_func1(x):
            return math.sqrt(4 - x ** 2)

        def get_func2(x):
            return -math.sqrt(4 - x ** 2)

        def get_func3(x):
            return 2

        graph1 = ax.plot(get_func1, x_range=[-2, 2, 0.01], use_smoothing=True, color=RED)
        graph2 = ax.plot(get_func2, x_range=[-2, 2, 0.01], use_smoothing=True, color=RED)
        graph3 = ax.plot(get_func3, x_range=[-4, 3, 0.1], use_smoothing=True, color=BLUE)
        A = Dot(ax.coords_to_point(0, 2), color=YELLOW)
        A_t = MathTex("x_1 = x_2", color=YELLOW).next_to(A, UL)
        B = Dot(ax.coords_to_point(0.823, 1.823), color=YELLOW)
        B_t = MathTex("x_2", color=YELLOW).next_to(B, DOWN)
        line = Line(A, B).get_angle()
        formula1 = MathTex("x^2+y^2=4", color=RED).move_to(ax.c2p(2, -2.2))
        formula3 = MathTex("y=2", color=BLUE)

        f1 = formula1.copy().to_corner(UL).shift(RIGHT*0.5)
        f2 = formula3.copy().next_to(f1, DOWN, aligned_edge=LEFT)
        formula3.next_to(graph3.point_from_proportion(0.92), UP, buff=SMALL_BUFF)
        brace = Brace(VGroup(f1, f2), LEFT)

        apply = Text("=>Có nghiệm kép", font="Sans", font_size=35, color=YELLOW)\
            .next_to(brace, DOWN, aligned_edge=LEFT)

        self.play(Create(ax), Create(graph1), Create(graph2), Create(graph3), Write(formula3), Write(formula1))
        self.play(LaggedStart(*[Transform(formula1.copy(), f1), Transform(formula3.copy(), f2)], lag_ratio=0.5),
                  FadeIn(brace, shift=LEFT))
        self.play(Write(apply))
        self.play(FadeIn(A), Write(A_t))
        self.wait(0.5)
        self.add(ax, graph1, graph2, graph3, A, B, A_t, B_t, formula1, formula3)
        self.add(f1, f2, brace, apply)


class Scene4(MyScene):
    def construct(self):
        ax = Axes(x_range=[-4, 3, 1],
                  y_range=[-3, 4, 1],
                  x_length=7,
                  y_length=7,
                  tips=True).to_edge(RIGHT)

        def get_func1(x):
            return math.sqrt(4 - x ** 2)

        def get_func2(x):
            return -math.sqrt(4 - x ** 2)

        def get_func3(x):
            return 0.5*x+3

        graph1 = ax.plot(get_func1, x_range=[-2, 2, 0.01], use_smoothing=True, color=RED)
        graph2 = ax.plot(get_func2, x_range=[-2, 2, 0.01], use_smoothing=True, color=RED)
        graph3 = ax.plot(get_func3, x_range=[-4, 3, 0.1], use_smoothing=True, color=BLUE)
        A = Dot(ax.coords_to_point(-4, 1), color=YELLOW)
        A_t = MathTex("x_1 = x_2", color=YELLOW).next_to(A, UL)
        B = Dot(ax.coords_to_point(2, 4), color=YELLOW)
        B_t = MathTex("x_2", color=YELLOW).next_to(B, DOWN)
        line = Line(A, B).get_angle()
        formula1 = MathTex("x^2+y^2=4", color=RED).move_to(ax.c2p(2, -2.2))
        formula3 = MathTex("y=0.5x+3", color=BLUE)

        f1 = formula1.copy().to_corner(UL).shift(RIGHT*0.5)
        f2 = formula3.copy().next_to(f1, DOWN, aligned_edge=LEFT)
        formula3.next_to(graph3.point_from_proportion(0.2), UP, buff=SMALL_BUFF).rotate(line)
        brace = Brace(VGroup(f1, f2), LEFT)

        apply = Text("=>Vô nghiệm", font="Sans", font_size=35, color=YELLOW)\
            .next_to(brace, DOWN, aligned_edge=LEFT)

        self.play(Create(ax), Create(graph1), Create(graph2), Create(graph3), Write(formula3), Write(formula1))
        self.play(LaggedStart(*[Transform(formula1.copy(), f1), Transform(formula3.copy(), f2)], lag_ratio=0.5),
                  FadeIn(brace, shift=LEFT))
        self.play(Write(apply))
        # self.play(FadeIn(A), Write(A_t))
        self.add(ax, graph1, graph2, graph3, A, B, A_t, B_t, formula1, formula3)
        self.add(f1, f2, brace, apply)