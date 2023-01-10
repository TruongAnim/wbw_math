import random

from manim import *
from common.custom.custom_mobject import TextTranslation

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9")
SCENE_NAME = list_scene[5]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

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
        self.wait()


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


def get_lines(dots):
    lines = VGroup()
    for i in range(len(dots)-1):
        temp = VGroup()
        for j in range(i + 1, len(dots)):
            temp.add(Line(dots[i].get_center(), dots[j].get_center()))
        lines.add(temp)
    return lines


def get_triangle(n=4):
    result = VGroup()
    for i in range(1, n + 1):
        group = VGroup(*[Dot(radius=0.15) for i in range(1, i + 1)]).arrange(RIGHT, buff=MED_SMALL_BUFF)
        result.add(group)
    result.arrange(DOWN, buff=MED_SMALL_BUFF)
    return result


def get_triangel_number(n=4):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


class Scene0(Scene):
    def construct(self):
        circle = Circle(radius=3)
        n = 6
        dots = VGroup(*[Dot(circle.point_from_proportion(i / n), color=YELLOW)
                        for i in range(n)])
        lines = get_lines(dots)
        flags = [ImageMobject(str(i + 1)).scale_to_fit_width(1) for i in range(n)]
        circle2 = Circle(radius=3.5)
        [flags[i].move_to(circle2.point_from_proportion(i / n))
         for i in range(n)]
        self.play(LaggedStart(*[LaggedStart(Create(i)) for i in dots], lag_ratio=0.1))
        self.play(LaggedStart(*[LaggedStart(FadeIn(i)) for i in flags], lag_ratio=0.1))
        self.play(LaggedStart(*[Create(i) for _ in lines for i in _], lag_ratio=0.1))
        self.add(dots, lines)
        self.add(*flags)


class Scene1(Scene):
    def construct(self):
        circle = Circle(radius=3)
        n = 15
        dots = VGroup(*[Dot(circle.point_from_proportion(i / n), color=YELLOW)
                        for i in range(n)])
        lines = get_lines(dots)
        flags = [ImageMobject("computer").scale_to_fit_width(1) for i in range(n)]
        circle2 = Circle(radius=3.5)
        [flags[i].move_to(circle2.point_from_proportion(i / n))
         for i in range(n)]
        self.play(LaggedStart(*[LaggedStart(Create(i)) for i in dots], lag_ratio=0.05))
        self.play(LaggedStart(*[LaggedStart(FadeIn(i)) for i in flags], lag_ratio=0.05))
        self.play(LaggedStart(*[Create(i) for _ in lines for i in _], lag_ratio=0.05))
        self.add(dots, lines)
        self.add(*flags)


class Scene2(Scene):
    def construct(self):
        title = TextTranslation(text_u="Số tam giác",
                                text_d="(Triangular number)",
                                font_size_u=50,
                                font_size_d=40,
                                color_u=GREEN).to_edge(UP)
        triangle = get_triangle(7).shift(DOWN * 0.5)
        brace = Brace(triangle, DOWN)
        bt = Text("28 chấm", font="Sans", font_size=40, color=YELLOW).next_to(brace, DOWN)
        arrow = CurvedArrow(title[0].get_left(), bt.get_left(), radius=3.5)
        self.play(FadeIn(title[0], shift=RIGHT), FadeIn(title[1], shift=LEFT))
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in triangle], lag_ratio=0.2))
        self.play(FadeIn(brace, shift=UP), FadeIn(bt, shift=UP))
        self.play(Create(arrow))
        self.wait(0.5)
        self.add(title)
        self.add(triangle, brace, bt, arrow)


class Scene3(Scene):
    def construct(self):
        def create_triange(n=3):
            dots = get_triangle(n)
            brace = Brace(dots, DOWN)
            numbers = get_triangel_number(n=n)
            bt = MathTex("T_{", str(n), "}=", str(numbers), color=YELLOW).next_to(brace, DOWN)
            return VGroup(dots, brace, bt)
        tri1 = create_triange(1).to_edge(LEFT)
        tri2 = create_triange(2).next_to(tri1, RIGHT, buff=LARGE_BUFF).align_to(tri1, DOWN)
        tri3 = create_triange(3).next_to(tri2, RIGHT, buff=LARGE_BUFF).align_to(tri1, DOWN)
        tri4 = create_triange(4).next_to(tri3, RIGHT, buff=LARGE_BUFF).align_to(tri1, DOWN)
        tri5 = create_triange(5).next_to(tri4, RIGHT, buff=LARGE_BUFF).align_to(tri1, DOWN)
        tri6 = create_triange(6).next_to(tri5, RIGHT, buff=LARGE_BUFF).align_to(tri1, DOWN)
        for i in (tri1, tri2, tri3, tri4, tri5):
            self.play(FadeIn(i[0], shift=UP))
            self.play(FadeIn(i[1:], shift=UP))
            self.wait(0.5)
        self.add(tri1, tri2, tri3, tri4, tri5)


class Scene4(Scene):
    def construct(self):
        dots = get_triangle(6).shift(LEFT*3+UP)
        dots2 = MathTex(".........................").next_to(dots, DOWN)
        brace = Brace(dots2, DOWN)
        text = MathTex("T_{n}=", "1+", "2+", "3+", ".", ".", ".", "+n", "=\sum_{k=1}^{n}k", "={n(n+1)\over 2}").next_to(brace, DOWN, buff=0).shift(RIGHT*4)
        numbers = VGroup(*[MathTex(str(i+1)).next_to(dots[i], RIGHT, buff=SMALL_BUFF) for i in range(6)])
        numbers.add(MathTex("n").next_to(dots2, RIGHT, buff=SMALL_BUFF))
        self.play(FadeIn(dots, shift=UP), FadeIn(dots2, shift=UP))
        self.play(FadeIn(brace, shift=UP), FadeIn(text[0], shift=UP))
        self.wait(0.5)
        for i in range(6):
            self.play(FadeIn(numbers[i], shift=LEFT),
                      FadeIn(text[1+i], shift=UP),
                      dots[i].animate.set_color(YELLOW))
        self.play(FadeIn(numbers[6], shift=LEFT),
                  FadeIn(text[7], shift=UP),
                  dots2.animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(Write(text[-2]))
        self.wait(0.5)
        self.play(Write(text[-1]))
        self.play(Circumscribe(text[0][:-1]),
                  Circumscribe(text[-1][1:]))
        self.play(Circumscribe(text[0][:-1]),
                  Circumscribe(text[-1][1:]))
        self.play(Circumscribe(text[0][:-1]),
                  Circumscribe(text[-1][1:]))
        self.add(dots, dots2, brace, text, numbers)


class Scene5(Scene):
    def construct(self):
        circle = Circle(radius=3).shift(LEFT*3)
        n = 6
        dots = VGroup(*[Dot(circle.point_from_proportion(i / n), color=YELLOW)
                        for i in range(n)])
        lines = get_lines(dots)
        flags = [ImageMobject(str(i + 1)).scale_to_fit_width(1) for i in range(n)]
        circle2 = Circle(radius=3.5).shift(LEFT*3)
        [flags[i].move_to(circle2.point_from_proportion(i / n))
         for i in range(n)]
        self.play(LaggedStart(*[LaggedStart(Create(i)) for i in dots], lag_ratio=0.05))
        self.play(LaggedStart(*[LaggedStart(FadeIn(i)) for i in flags], lag_ratio=0.05))
        # random.seed(7)
        teams = Text("6 đội bóng", font_size=50, font="Sans", color=GREEN).to_edge(UP).shift(RIGHT*4)
        f1 = MathTex("1+", "2+", "3+", "4+", "5").next_to(teams, DOWN)
        colors = [RED, GREEN, YELLOW, BLUE, ORANGE]
        self.play(FadeIn(teams, shift=UP))
        for index, i in enumerate(reversed(lines)):
            i.set_color(colors[index])
            self.play(*[Create(j) for j in i],
                      FadeIn(f1[index], shift=UP), run_time=0.5)

        f2 = MathTex("=T_{(6-1)}={5*6\over 2}").next_to(f1, DOWN, aligned_edge=LEFT)
        f3 = MathTex(r"=15 \text{ (trận đấu)}", tex_template=myTemplate, color=YELLOW).next_to(f2, DOWN, aligned_edge=LEFT)
        self.play(Write(f2))
        self.play(Write(f3))
        self.add(dots, lines)
        self.add(*flags)


class Scene6(Scene):
    def construct(self):
        circle = Circle(radius=3).shift(LEFT*3)
        n = 15
        dots = VGroup(*[Dot(circle.point_from_proportion(i / n), color=YELLOW)
                        for i in range(n)])
        lines = get_lines(dots)
        flags = [ImageMobject("computer").scale_to_fit_width(1) for i in range(n)]
        circle2 = Circle(radius=3.5).shift(LEFT*3)
        [flags[i].move_to(circle2.point_from_proportion(i / n))
         for i in range(n)]
        self.play(LaggedStart(*[LaggedStart(Create(i)) for i in dots], lag_ratio=0.05))
        self.play(LaggedStart(*[LaggedStart(FadeIn(i)) for i in flags], lag_ratio=0.05))
        # random.seed(7)
        teams = Text("15 máy tính", font_size=50, font="Sans", color=GREEN).to_edge(UP).shift(RIGHT*4)
        f1 = MathTex("1+", "2+", "3+", "...", "+14").next_to(teams, DOWN)
        colors = [RED, GREEN, YELLOW, BLUE, ORANGE]
        temp = [j.set_color(random_color()) for i in lines for j in i]
        self.play(FadeIn(teams, shift=UP))
        self.play(LaggedStart(*[Create(i) for i in temp], run_time=2),
                  Write(f1, run_time=2))

        f2 = MathTex("=T_{(15-1)}={14*15\over 2}").next_to(f1, DOWN, aligned_edge=LEFT)
        f3 = MathTex(r"=105 \text{ (kết nối)}", tex_template=myTemplate, color=YELLOW).next_to(f2, DOWN, aligned_edge=LEFT)
        self.play(Write(f2))
        self.play(Write(f3))
        self.add(dots, lines)
        self.add(*flags)
