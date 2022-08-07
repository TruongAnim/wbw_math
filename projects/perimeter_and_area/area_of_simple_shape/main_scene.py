from manim import *

list_scene = ("Scene1", "Scene2", "Scene3")
SCENE_NAME = list_scene[2]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class Scene1(Scene):
    def setup(self):
        self.square = Square().scale(2)

        perimeter_en = Text("Perimeter").next_to(self.square, LEFT, buff=1)
        perimeter_vn = Text("Chu vi", font="Times New Roman").next_to(perimeter_en, DOWN, buff=0.3)

        area_en = Text("Area").next_to(self.square, RIGHT, buff=1)
        area_vn = Text("Diện tích", font="Times New Roman").next_to(area_en, DOWN, buff=0.3)

        self.perimeter = VGroup(perimeter_en, perimeter_vn)
        self.area = VGroup(area_en, area_vn)

    def construct(self):
        import numpy as np
        from common.custom.custom_animation import Indicate2
        self.play(*[
            Write(self.perimeter),
            Write(self.area)
        ])
        self.play(Create(self.square))
        self.remove(self.square)
        self.play(*[
            Indicate2(self.square.get_subcurve(i, i + 0.25), 0.5 * j)
            for i, j in zip(np.arange(0, 1, 0.25), [UP, LEFT, DOWN, RIGHT])
        ], Indicate(self.perimeter))
        self.square.set_style(
            fill_color=YELLOW,
            fill_opacity=0.7,
            stroke_width=0
        )
        self.play(Write(self.square))
        self.play(Indicate(self.square), Indicate(self.area))


class Scene2(Scene):
    def setup(self):
        A = np.array([0, 3, 0])
        B = np.array([-1.5, 0, 0])
        C = np.array([2.5, 0, 0])
        D = np.array([0, 0, 0])
        self.triangle = VMobject().set_points_as_corners(
            [A, B, C, A]
        )
        self.h_line = Line(A, D)
        self.group_tri = VGroup(self.triangle, self.h_line).shift(RIGHT * 4)

        self.h = MathTex("h=3").scale(0.8).next_to(self.h_line, RIGHT, buff=SMALL_BUFF)
        self.a = MathTex("a=4").scale(0.8).next_to(self.triangle, DOWN, buff=SMALL_BUFF)

        self.rectangle = Rectangle(width=3, height=2).shift(LEFT * 4).align_to(self.triangle, DOWN)
        self.d = MathTex("d=3").scale(0.8).next_to(self.rectangle, DOWN, buff=SMALL_BUFF)
        self.r = MathTex("r=2").scale(0.8).next_to(self.rectangle, LEFT, buff=SMALL_BUFF)

    def construct(self):
        from common.utils.mobject_utils import get_indexes
        self.play(Create(self.triangle), Create(self.rectangle))
        self.play(Create(self.h_line), Write(self.h), Write(self.r))
        self.play(Write(self.a), Write(self.d))

        formula1 = MathTex(r"s=r \times d=2 \times 3=6").next_to(self.rectangle, DOWN, buff=1.5)
        formula2 = MathTex(r"s={{h \times a}\over 2}={{3 \times 4} \over 2}=6").next_to(self.triangle, DOWN, buff=1)

        # self.add(get_indexes(formula1[0]), get_indexes(formula2[0]))

        init_index1 = [0, 1, 3, 5, 7, 9]
        init_index2 = [0, 1, 3, 5, 6, 7, 9, 11, 12, 13]
        self.play(*[
            Write(formula1[0][i]) for i in init_index1
        ], *[
            Write(formula2[0][i]) for i in init_index2
        ])
        scipts = (
            ((self.r[0][0], self.d[0][0], self.h[0][0], self.a[0][0]),
             (formula1[0][2], formula1[0][4], formula2[0][2], formula2[0][4])),
            ((self.r[0][2], self.d[0][2], self.h[0][2], self.a[0][2]),
             (formula1[0][6], formula1[0][8], formula2[0][8], formula2[0][10]))
        )
        for scipt in scipts:
            self.play(*[
                ReplacementTransform(i.copy(), j) for i, j in zip(*scipt)
            ])
            self.wait()

        self.play(Write(formula1[0][10]), Write(formula2[0][14]))

        copy_rec = self.rectangle.copy().set_style(
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.8
        )
        copy_tri = self.triangle.copy().set_style(
            stroke_width=0,
            fill_color=BLUE,
            fill_opacity=0.6
        )
        self.play(FadeIn(copy_rec), FadeIn(copy_tri))
        self.play(copy_rec.animate.shift(RIGHT * 3.8),
                  copy_tri.animate.shift(LEFT * 4.2))
        result = MathTex("S_{red}=S_{blue}=6").next_to(copy_tri, DOWN)
        self.play(Write(result),
                  *[
                      FadeOut(i) for i in (formula1, formula2)
                  ])


class Scene3(Scene):
    def construct(self):
        unit_square = Square(side_length=1, fill_color=YELLOW, fill_opacity=0.5).shift(LEFT * 3 + UP)
        b1 = Brace(unit_square, LEFT)
        t1 = b1.get_tex("1")
        b2 = Brace(unit_square, DOWN)
        t2 = b2.get_tex("1")

        arrow1 = Arrow(UP, DOWN).next_to(t2, DOWN, buff=MED_SMALL_BUFF)
        s1 = MathTex("S=1").next_to(arrow1, DOWN)

        self.play(*[
            Write(i) for i in [unit_square, b1, b2, t1, t2]
        ])
        self.play(Write(arrow1))
        self.play(Write(s1))

        triangle = VMobject().set_points_as_corners([ORIGIN, UP * 2, RIGHT * 2, ORIGIN]) \
            .shift(RIGHT * 3).align_to(unit_square, DOWN)
        b3 = Brace(triangle, LEFT)
        b4 = Brace(triangle, DOWN)
        t3 = b3.get_tex("2")
        t4 = b4.get_tex("2")

        self.play(*[
            Write(i) for i in [triangle, b3, b4, t3, t4]
        ])

        kwargs = {
            "fill_color":YELLOW,
            "fill_opacity": 0.5,
            "stroke_width": 0
        }
        copy1 = unit_square.copy().align_to(triangle, DL).set_style().set_style(**kwargs)
        copy2 = unit_square.copy().align_to(triangle, UL).set_style().set_style(**kwargs)

        self.play(ReplacementTransform(unit_square.copy().set_style().set_style(**kwargs), copy1),
                  ReplacementTransform(unit_square.copy().set_style().set_style(**kwargs), copy2))

        A = copy2.point_from_proportion(0)
        B = copy2.point_from_proportion(1/4)
        C = copy2.point_from_proportion(2/4)
        D = copy2.point_from_proportion(3/4)

        small_tri1 = VMobject().set_points_as_corners([A,B,D,A]).set_style(**kwargs)
        small_tri2 = VMobject().set_points_as_corners([B,C,D,B]).set_style(**kwargs)
        self.add(small_tri2)
        self.remove(copy2)
        self.play(Rotate(small_tri1, about_point=D, angle=-PI-0.005))
        arrow2 = Arrow(UP, DOWN).next_to(t4, DOWN, buff=MED_SMALL_BUFF)
        s2 = MathTex("S=2").next_to(arrow2, DOWN)
        self.play(Write(arrow2))
        self.play(Write(s2), *[Indicate(i) for i in (small_tri1, small_tri2, copy1)])
        self.wait()


class Scene4(Scene):
    def construct(self):
        square = Square(side_length=3)
        brace1 = Brace(square, LEFT)
        brace2 = Brace(square, UP)
        t = brace1.get_tex()