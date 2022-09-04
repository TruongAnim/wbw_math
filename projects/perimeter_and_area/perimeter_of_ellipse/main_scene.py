import math

from manim import *
from common.utils.area import area_of_ellipse
from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3",
              "ErrorChart", "Scene5", "Scene6",
              "Scene7")
SCENE_NAME = list_scene[4]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c  {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")

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
        self.wait()


class Scene1(MyScene):
    def construct(self):
        ellipse = Ellipse(width=5.0, height=3.0, color=BLUE_B)
        circle = Circle(radius=1.5)
        ellipse.move_to(UP + RIGHT * 3)
        circle.move_to(UP + LEFT * 3)
        r = Line(circle.get_top(), circle.get_center())
        b = Line(ellipse.get_top(), ellipse.get_center())
        a = Line(ellipse.get_right(), ellipse.get_center())
        r_tex = MathTex("r").next_to(r, LEFT)
        a_tex = MathTex("a").next_to(a, DOWN)
        b_tex = MathTex("b").next_to(b, LEFT)
        g_tex = VGroup(*(r_tex, a_tex, b_tex))
        bound_circle = Rectangle().surround(circle, stretch=True, buff=0)
        bound_ellipse = Rectangle().surround(ellipse, stretch=True, buff=0)
        g_surround = VGroup(*(bound_ellipse, bound_circle))
        g_ellipse = VGroup(*(ellipse, a, b, a_tex, b_tex, bound_ellipse))
        area = Text("Diện tích:", font="Sans", font_size=30) \
            .to_edge(LEFT) \
            .shift(DOWN * 1.5)
        circle_area = MathTex(r"\pi \times r ^ 2") \
            .move_to(circle) \
            .align_to(area, DOWN).shift(UP * 0.1)
        ellipse_area = MathTex(r"\pi \times a \times b") \
            .move_to(ellipse) \
            .align_to(area, DOWN).shift(UP * 0.1)
        perimeter = Text("Chu vi:", font="Sans", font_size=30) \
            .to_edge(LEFT) \
            .shift(DOWN * 2.5)
        circle_peri = MathTex(r"\pi \times 2r") \
            .move_to(circle) \
            .align_to(perimeter, DOWN)
        ellipse_peri = MathTex(r"???") \
            .move_to(ellipse) \
            .align_to(perimeter, DOWN).shift(UP * 0.1)
        self.play(
            Write(a),
            Write(b),
            Write(a_tex),
            Write(b_tex)
        )
        self.play(Write(ellipse))
        self.play(
            Write(circle),
            Write(r),
            Write(r_tex)
        )
        self.play(Write(g_surround))
        self.play(
            g_ellipse.animate.stretch_to_fit_width(3),
            rate_func=there_and_back,
            run_time=3
        )
        self.play(Unwrite(g_surround))
        self.play(
            Write(area),
            *[Write(circle_area[0][i])
              for i in (0, 1)],
            *[Write(ellipse_area[0][i])
              for i in (0, 1, 3)],
        )
        self.play(
            *[Transform(r_tex.copy(), circle_area[0][i])
              for i in (2, 3)],
            *[Transform(i.copy(), ellipse_area[0][j])
              for i, j in zip((a_tex, b_tex), (2, 4))],
        )
        self.play(Write(perimeter))
        self.play(Write(circle_peri))
        # self.play(Write(ellipse_peri))

        ellipse_peri = MathTex(r"\pi \times (a+b )") \
            .move_to(ellipse) \
            .align_to(perimeter, DOWN).shift(UP * 0.1)
        circle_peri[0][2].set_color(YELLOW)
        circle_peri[0][3].set_color(YELLOW)
        ellipse_peri[0][3].set_color(YELLOW)
        ellipse_peri[0][4].set_color(YELLOW)
        ellipse_peri[0][5].set_color(YELLOW)
        self.play(
            *[Write(ellipse_peri[0][i])
              for i in (0, 1, 2, 4, 6)],
        )
        self.play(
            *[Transform(i.copy(), ellipse_peri[0][j])
              for i, j in zip((a_tex, b_tex), (3, 5))],
        )


class Scene2(MyScene):
    def construct(self):
        ellipse = Ellipse(width=6, height=2, color=BLUE).shift(UP * 2)
        b = Line(ellipse.get_top(), ellipse.get_center(), color=GREEN)
        a = Line(ellipse.get_right(), ellipse.get_center(), color=RED)
        a_tex = MathTex("a", color=RED).next_to(a, DOWN)
        b_tex = MathTex("b", color=GREEN).next_to(b, LEFT)
        ellipse_peri = MathTex(r"C=\pi \times (a+b )").shift(DOWN)
        ellipse_peri[0][5].set_color(RED)
        ellipse_peri[0][7].set_color(GREEN)
        self.play(
            *[Write(i)
              for i in (ellipse, a, b, a_tex, b_tex)]
        )
        self.play(
            *[Write(ellipse_peri[0][i])
              for i in (0, 1, 2, 3, 4, 6, 8)],
        )
        self.play(
            *[Transform(i.copy(), ellipse_peri[0][j])
              for i, j in zip((a_tex, b_tex), (5, 7))],
        )


class Scene3(MyScene):
    def construct(self):
        ellipse = Ellipse(width=4, height=2, color=BLUE).shift(UP * 2)
        b = Line(ellipse.get_top(), ellipse.get_center(), color=GREEN)
        a = Line(ellipse.get_right(), ellipse.get_center(), color=RED)
        a_tex = MathTex("a", color=RED).next_to(a, DOWN)
        b_tex = MathTex("b", color=GREEN).next_to(b, LEFT)
        graph = MathTex(r"{x^2\over a^2} + {y^2 \over b^2} = 1").shift(UP * 3 + RIGHT * 5)
        arrow = Arrow(graph.get_left(), ellipse.point_from_proportion(0.07),
                      buff=0.1, stroke_width=3)
        perimeter = MathTex(
            r"\text{Chu vi} = 4a\int_{0}^{\pi \over 2} \sqrt{1-e^2\sin^2\theta}d\theta") \
            .shift(DOWN + RIGHT * 2)
        e = MathTex(r"\left(e = {\sqrt{a^2-b^2} \over a}\right)").next_to(perimeter, DOWN)
        self.play(
            *[Write(i)
              for i in (ellipse, a, b, a_tex, b_tex)]
        )
        self.play(Write(graph), GrowArrow(arrow))
        self.play(Write(perimeter), Write(e))
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            color=RED,
        ).to_corner(DL)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.play(NumberCreatureThinks(
            pi, Text("Giải tiếp kiểu gì nhỉ?",
                     font_size=25,
                     font="Sans"),
            target_mode="wonder",
            bubble_kwargs={
                "stroke_width": 3,
                "stroke_color": WHITE,
                "stroke_opacity": 1,
                "stretch_width": 3
            }
        ))
        self.add(ellipse, a, b, a_tex, b_tex, graph, arrow, perimeter, e)


class ErrorChart(MyScene):
    def construct(self):
        axes = Axes(
            axis_config={
                "include_numbers": True,
            },
            x_range=(1, 6, 1),
            y_range=(0, 15, 3)
        )
        x_min, x_max, x_res = axes.x_range
        y_min, y_max, y_res = axes.y_range

        h_lines = VGroup(*[
            DashedLine(
                axes.c2p(x_min, y),
                axes.c2p(x_max, y),
                stroke_opacity=0.5,
                stroke_width=1,
            )
            for y in np.arange(y_min, y_max + y_res, y_res)
        ])
        v_lines = VGroup(*[
            DashedLine(
                axes.c2p(x, y_min),
                axes.c2p(x, y_max),
                stroke_opacity=0.5,
                stroke_width=1,
            )
            for x in np.arange(x_min, x_max + x_res, x_res)
        ])
        percent = MathTex(r"\%") \
            .next_to(axes.get_axes()[1].get_top(), UP)
        ba = MathTex(r"b \over a") \
            .next_to(axes.get_axes()[0].get_right(), RIGHT)
        center = [i.get_center() + DOWN / 2.5 for i in axes[0].get_tick_marks()]
        ellipse = VGroup(*[
            Ellipse(
                height=0.5,
                width=i / 2,
                color=BLUE,
                stroke_width=DEFAULT_STROKE_WIDTH / 2
            ).move_to(center[i - 1])
            for i in range(1, 6)
        ])

        def approximate_1(a, b):
            return PI * (a + b)

        def approximate_2(a, b):
            return PI * math.sqrt(2 * (a * a + b * b))

        def approximate_3(a, b):
            return PI * (1.5 * (a + b) - math.sqrt(a * b))

        def approximate_4(a, b):
            return PI * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

        def approximate_5(a, b):
            h = pow(a - b, 2) / pow(a + b, 2)
            return PI * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

        def clousure(func):
            def get_error(b):
                approximate = func(1, b)
                real = area_of_ellipse(1, b, accurate=15)
                return (math.fabs(approximate - real) / real) * 100

            return get_error

        plot1 = axes.plot(clousure(approximate_1), x_range=[1, 6, 0.005], color=RED)
        plot2 = axes.plot(clousure(approximate_2), x_range=[1, 6, 0.005], color=YELLOW)
        plot3 = axes.plot(clousure(approximate_3), x_range=[1, 6, 0.005], color=TEAL)

        point1 = Dot(axes.i2gp(5, plot1))
        error1 = MathTex(
            "{:.2f}".format(clousure(approximate_1)(5)) + r"\%",
            color=RED) \
            .next_to(point1, UP)
        point2 = Dot(axes.i2gp(5, plot2))
        error2 = MathTex(
            "{:.2f}".format(clousure(approximate_2)(5)) + r"\%",
            color=YELLOW) \
            .next_to(point2, DOWN)
        point3 = Dot(axes.i2gp(5, plot3))
        error3 = MathTex(
            "{:.2f}".format(clousure(approximate_3)(5)) + r"\%",
            color=TEAL) \
            .next_to(point3, UP)
        formula1 = MathTex(r"\pi(a+b)", color=RED) \
            .to_edge(UP) \
            .shift(LEFT * 4)
        formula2 = MathTex(
            r"\pi\sqrt{2(a^2+b^2)}",
            color=YELLOW) \
            .next_to(formula1, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        formula3 = MathTex(
            r"\pi\left[ {3 \over 2}(a+b)-\sqrt{ab} \right]",
            color=TEAL) \
            .next_to(formula2, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)

        group1 = VGroup(plot1, point1, error1, formula1)
        group2 = VGroup(plot2, point2, error2, formula2)
        group3 = VGroup(plot3, point3, error3, formula3)

        axes2 = Axes(
            axis_config={
                "include_numbers": True,
            },
            x_range=(1, 6, 1),
            y_range=(0, 0.015, 0.003)
        )
        plot4 = axes2.plot(clousure(approximate_3), x_range=[1, 2, 0.01], color=YELLOW)
        plot5 = axes2.plot(clousure(approximate_4), x_range=[1, 6, 0.01], color=GREEN)
        plot6 = axes2.plot(clousure(approximate_5), x_range=[1, 6, 0.01], color=PINK)
        point5 = Dot(axes2.i2gp(5, plot5))
        error5 = MathTex(
            "{:.6f}".format(clousure(approximate_4)(5)) + r"\%",
            color=GREEN) \
            .next_to(point5, DOWN * 5.6)
        point6 = Dot(axes2.i2gp(5, plot6))
        error6 = MathTex(
            "{:.6f}".format(clousure(approximate_5)(5)) + r"\%",
            color=PINK) \
            .next_to(point6, UP)
        formula4 = formula3.copy().scale(0.7).shift(UP * 2.5)
        formula5 = MathTex(
            r"\pi\left[ 3(a+b)-\sqrt{(3a+b)(a+3b)} \right]",
            color=GREEN) \
            .scale(0.7) \
            .next_to(formula4, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        formula6 = MathTex(
            r"\pi(a+b)\left[ 1+{3h \over 10+\sqrt{4-3h}} \right]",
            color=PINK) \
            .scale(0.7) \
            .next_to(formula5, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        formula7 = MathTex(
            r"\left(h={{(a-b)^2}\over(a+b)^2}  \right)",
            color=PINK) \
            .scale(0.7) \
            .next_to(formula6, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        group5 = VGroup(plot5, point5, error5, formula5)
        group6 = VGroup(plot6, point6, error6, formula6, formula7)
        self.play(
            *[Write(i)
              for i in (axes, h_lines, v_lines, percent, ba, ellipse)]
        )
        self.play(Write(group1))
        self.play(Write(group2))
        self.play(Write(group3))

        self.play(
            *[FadeOut(i)
              for i in (group1, group2, point3, error3)]
        )
        self.play(
            Transform(axes, axes2),
            Transform(plot3, plot4),
            Transform(formula3, formula4),
            run_time=3
        )
        self.play(Write(group5))
        self.play(Write(group6))
        self.add(axes, ellipse, percent,
                 ba, h_lines, v_lines, plot1, plot2,
                 plot3, point1, error1,
                 point2, error2, point3, error3,
                 formula1, formula2, formula3)


class Scene5(Scene):
    def construct(self):
        perimeter = MathTex(
            r"\text{Chu vi}=\pi (a+b)\left[ 1+{h\over4}+ \sum_{2}^{\infty }\left( {(2n-3)!!}\over 2^2n! \right)^2h^n\right]") \
            .shift(UP * 2)
        approximate = MathTex(r"\text{Chu vi}=",
                              r"\pi (a+b)\left[ 1+{h\over4}+",
                              "{h^2\over64}",
                              "+{h^3\over256}",
                              "+{h^4\over 16384}",
                              r"+.",
                              ".",
                              ".",
                              ".",
                              ".",
                              ".",
                              r"\right]").align_to(perimeter, LEFT)
        list_error = [20.943951023931955,
                      21.0021286656651,
                      21.008592848079896,
                      21.009715101971352,
                      21.009959503929934,
                      21.010020604419584,
                      21.01003736895302,
                      21.010042287713702,
                      21.010043805849715,
                      21.01004429334006,
                      21.010044538271753]
        real_p = 21.010044538271753
        list_error_percent = [(math.fabs(i-real_p)*100)/real_p for i in list_error]
        approximate[1].set_color(RED)
        brace = Brace(approximate[1], DOWN)
        error = brace.get_tex("{:.4f}\%".format(list_error_percent[0]))
        error_text = Text("Sai số:", font="Sans", font_size=25)\
            .next_to(error, LEFT)
        self.play(Write(perimeter))
        self.play(*[Write(i)
                  for i in (approximate, brace, error, error_text)])

        for i in range(2,12):
            new_brace = Brace(approximate[1:i+1], DOWN)
            new_error = new_brace.get_tex("{:.8f}\%".format(list_error_percent[i-1]))
            self.play(*[Transform(brace, new_brace),
                        Transform(error, new_error),
                        error_text.animate.next_to(new_error, LEFT)],
                        approximate[1:i+1].animate.set_color(RED))

        self.add(perimeter, approximate, brace)
