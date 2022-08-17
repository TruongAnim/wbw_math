from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene31", "Scene4", "Scene5", "Scene6")
# SCENE_NAME = list_scene[6]
SCENE_NAME = " ".join(list_scene)
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

class Scene1(MyScene):
    def setup(self):
        self.square = Square().scale(2)

        perimeter_vn = Text("Chu vi", font="Times New Roman").next_to(self.square, LEFT, buff=1)
        perimeter_en = Text("(Perimeter)").next_to(perimeter_vn, DOWN, buff=0.3)

        area_vn = Text("Diện tích", font="Times New Roman").next_to(self.square, RIGHT, buff=1)
        area_en = Text("(Area)").next_to(area_vn, DOWN, buff=0.3)

        self.perimeter = VGroup(perimeter_en, perimeter_vn)
        self.area = VGroup(area_en, area_vn)



    def construct(self):
        import numpy as np
        from common.custom.custom_animation import Indicate2
        self.my_play(*[
            Write(self.perimeter),
            Write(self.area)
        ])
        self.my_play(Create(self.square))
        self.remove(self.square)
        self.my_play(*[
            Indicate2(self.square.get_subcurve(i, i + 0.25), 0.5 * j)
            for i, j in zip(np.arange(0, 1, 0.25), [UP, LEFT, DOWN, RIGHT])
        ], Indicate(self.perimeter))
        self.square.set_style(
            fill_color=YELLOW,
            fill_opacity=0.7,
            stroke_width=0
        )
        self.my_play(Write(self.square))
        self.my_play(Indicate(self.square), Indicate(self.area))


class Scene2(MyScene):
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
        self.my_play(Create(self.triangle), Create(self.rectangle))
        self.my_play(Create(self.h_line), Write(self.h), Write(self.r))
        self.my_play(Write(self.a), Write(self.d))

        formula1 = MathTex(r"S=r \times d=2 \times 3=6").next_to(self.rectangle, DOWN, buff=1.5)
        formula2 = MathTex(r"S={{h \times a}\over 2}={{3 \times 4} \over 2}=6").next_to(self.triangle, DOWN, buff=1)

        # self.add(get_indexes(formula1[0]), get_indexes(formula2[0]))

        init_index1 = [0, 1, 3, 5, 7, 9]
        init_index2 = [0, 1, 3, 5, 6, 7, 9, 11, 12, 13]

        scipts = (
            ((self.r[0][0], self.d[0][0], self.h[0][0], self.a[0][0]),
             (formula1[0][2], formula1[0][4], formula2[0][2], formula2[0][4])),
            ((self.r[0][2], self.d[0][2], self.h[0][2], self.a[0][2]),
             (formula1[0][6], formula1[0][8], formula2[0][8], formula2[0][10]))
        )

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

        pi = NumberCreature(file_name_prefix="PiCreatures", mode="wonder")\
        .shift(DOWN*3 + LEFT*5)
        pi_say = Text("Diện tích bằng nhau thật á?", font="Times New Roman")

        self.my_play(*[
            Write(formula1[0][i]) for i in init_index1
        ], *[
            Write(formula2[0][i]) for i in init_index2
        ])

        for scipt in scipts:
            self.my_play(*[
                ReplacementTransform(i.copy(), j) for i, j in zip(*scipt)
            ])
            self.wait()

        self.my_play(Write(formula1[0][10]), Write(formula2[0][14]))


        self.my_play(FadeIn(copy_rec), FadeIn(copy_tri))
        self.my_play(copy_rec.animate.shift(RIGHT * 3.8),
                  copy_tri.animate.shift(LEFT * 4.2))

        result = MathTex("S_{red}", "=", "S_{blue}", "=6").next_to(copy_tri, DOWN)
        result[0].set_color(RED)
        result[2].set_color(BLUE)

        self.my_play(Write(result),
                  *[
                      FadeOut(i) for i in (formula1, formula2)
                  ])
        self.my_play(FadeIn(pi, shift=UP*3))
        bubble_kwargs = {
            "stretch_width":3.2,
            "stretch_height":2,
            "stroke_color":WHITE,
            "stroke_width":1
        }
        self.my_play(NumberCreatureSays(pi, pi_say, bubble_kwargs=bubble_kwargs, target_mode="wonder"))

class Scene3(MyScene):
    def construct(self):
        unit_square = Square(side_length=1, fill_color=YELLOW, fill_opacity=0.5).shift(LEFT * 3 + UP)
        b1 = Brace(unit_square, LEFT)
        t1 = b1.get_tex("1")
        b2 = Brace(unit_square, DOWN)
        t2 = b2.get_tex("1")

        arrow1 = Arrow(UP, DOWN).next_to(t2, DOWN, buff=MED_SMALL_BUFF)
        s1 = MathTex("S=1").next_to(arrow1, DOWN)

        self.my_play(*[
            Write(i) for i in [unit_square, b1, b2, t1, t2]
        ])
        self.my_play(Write(arrow1))
        self.my_play(Write(s1))

        triangle = VMobject().set_points_as_corners([ORIGIN, UP * 2, RIGHT * 2, ORIGIN]) \
            .shift(RIGHT * 3).align_to(unit_square, DOWN)
        b3 = Brace(triangle, LEFT)
        b4 = Brace(triangle, DOWN)
        t3 = b3.get_tex("2")
        t4 = b4.get_tex("2")

        self.my_play(*[
            Write(i) for i in [triangle, b3, b4, t3, t4]
        ])

        kwargs = {
            "fill_color":YELLOW,
            "fill_opacity": 0.5,
            "stroke_width": 0
        }
        copy1 = unit_square.copy().align_to(triangle, DL).set_style().set_style(**kwargs)
        copy2 = unit_square.copy().align_to(triangle, UL).set_style().set_style(**kwargs)

        self.my_play(ReplacementTransform(unit_square.copy().set_style().set_style(**kwargs), copy1),
                  ReplacementTransform(unit_square.copy().set_style().set_style(**kwargs), copy2))

        A = copy2.point_from_proportion(0)
        B = copy2.point_from_proportion(1/4)
        C = copy2.point_from_proportion(2/4)
        D = copy2.point_from_proportion(3/4)

        small_tri1 = VMobject().set_points_as_corners([A,B,D,A]).set_style(**kwargs)
        small_tri2 = VMobject().set_points_as_corners([B,C,D,B]).set_style(**kwargs)
        self.add(small_tri2)
        self.remove(copy2)
        self.my_play(Rotate(small_tri1, about_point=D, angle=-PI))
        arrow2 = Arrow(UP, DOWN).next_to(t4, DOWN, buff=MED_SMALL_BUFF)
        s2 = MathTex("S=2").next_to(arrow2, DOWN)

        self.my_play(Write(arrow2), *[
            FadeToColor(obj, color) for obj, color in zip(
                (small_tri1, small_tri2),
                (RED, BLUE)
            )
        ])
        self.my_play(Write(s2), *[Wiggle(i, scale_value=1.3) for i in (small_tri1, small_tri2, copy1)], run_time=2)
        self.wait()

class Scene31(MyScene):
    def construct(self):
        A = np.array([0,0,0])
        B = np.array([1,1,0])
        C = np.array([2,0,0])
        D = np.array([2,-1,0])
        E = np.array([-0.3,-2,0])
        F = np.array([-1.5,0,0])
        ground = VMobject(fill_color=YELLOW, fill_opacity=0.5)\
            .set_points_smoothly([A,B,C,D,E,F,A])\
            .shift(LEFT*4+UP*0.5)
        text_ground = MathTex("S = 10m^{2}").next_to(ground, DOWN)

        squares = VGroup(*[
            Square(side_length=0.8,
                   fill_color=YELLOW,
                   fill_opacity=0.5)
            for _ in range(10)
        ]).arrange_in_grid(2,5, buff=0.1).shift(RIGHT*4)
        text_square = text_ground.copy().next_to(squares, DOWN, LARGE_BUFF)

        b1 = Brace(squares[5], LEFT)
        t1 = b1.get_tex("1m")
        b2 = Brace(squares[5], DOWN)
        t2 = b2.get_tex("1m")
        text_equal = MathTex("=").scale(3).shift(LEFT*0.5)
        self.my_play(DrawBorderThenFill(ground), Write(text_ground))
        self.my_play(LaggedStart(*[
            Write(i) for i in squares
        ]))
        self.my_play(*[Write(i) for i in (text_square, b1, t1, b2, t2)])
        self.my_play(Write(text_equal), Indicate(text_square), Indicate(text_ground))


class Scene4(MyScene ):
    def construct(self):
        square = Square(side_length=3)
        brace1 = Brace(square, LEFT)
        brace2 = Brace(square, UP)
        t1 = brace1.get_tex("3")
        t2 = brace2.get_tex("3")

        self.my_play(*[
            Write(i) for i in (square, brace1, brace2, t1, t2)
        ])

        unit_square = VGroup(*[
            Square(side_length=1, fill_color=YELLOW, fill_opacity=0.5, stroke_width=0.5) for i in range(9)
        ]).arrange_in_grid(3,3, buff=0)
        self.my_play(LaggedStart(*[FadeIn(i) for i in unit_square]
                              , lag_ratio=0.5), run_time=3)
        self.wait()

        result = MathTex(r"3 \times 3 = 9", r" ({m^{2}, cm^2,...})").next_to(square, DOWN, buff=MED_LARGE_BUFF)
        self.my_play((Write(result)))

class Scene5(MyScene):
    def construct(self):
        rec = Rectangle(width=3, height=2)
        brace1 = Brace(rec, LEFT)
        brace2 = Brace(rec, UP)
        t1 = brace1.get_tex("2")
        t2 = brace2.get_tex("3")

        self.my_play(*[
            Write(i) for i in (rec, brace1, brace2, t1, t2)
        ])

        unit_square = VGroup(*[
            Square(side_length=1, fill_color=YELLOW, fill_opacity=0.5, stroke_width=0.5) for i in range(6)
        ]).arrange_in_grid(cols=3,rows=2, buff=0)
        self.my_play(LaggedStart(*[FadeIn(i) for i in unit_square]
                              , lag_ratio=0.5), run_time=3)
        self.wait()

        result = MathTex(r"3 \times 2 = 6", r"({m^{2}, cm^2,...})").next_to(rec, DOWN, buff=MED_LARGE_BUFF)
        self.my_play((Write(result)))


class Scene6(MyScene):
    def setup(self):
        import numpy as np
    def construct(self):
        A = np.array([0, 3, 0])
        B = np.array([-1.5, 0, 0])
        C = np.array([2.5, 0, 0])
        D = np.array([0, 0, 0])
        E = np.array([-1.5,3,0])
        F = np.array([2.5,3,0])
        triangle = VMobject().set_points_as_corners(
            [A, B, C, A]
        )
        h_line = Line(A, D)

        h = MathTex("h=3").scale(0.8).next_to(h_line, RIGHT, buff=SMALL_BUFF)
        a = MathTex("a=4").scale(0.8).next_to(triangle, DOWN, buff=SMALL_BUFF)

        self.my_play(Create(triangle))
        self.my_play(Create(h_line), Write(h))
        self.my_play(Write(a))

        rectangle = VMobject().set_points_as_corners([E, F, C, B, E])
        self.my_play(Create(rectangle))
        tri1 = VMobject(fill_color=YELLOW, fill_opacity=0.5, stroke_width=0).set_points_as_corners([A,D,B,A])
        tri2 = VMobject(fill_color=RED, fill_opacity=0.5, stroke_width=0).set_points_as_corners([A,D,C,A])
        self.my_play(Create(tri1), Create(tri2))

        self.my_play(Rotate(tri1.copy(), PI, about_point=(A+B)/2))
        self.my_play(Rotate(tri2.copy(), PI, about_point=(A+C)/2))

        rectangle.generate_target()
        self.my_play(rectangle.target.animate.shift(LEFT*5))
        unit_squares = VGroup(*[Square(
            side_length=1, stroke_width=0.5, fill_color=YELLOW, fill_opacity=0.5
        ) for i in range(12)]).arrange_in_grid(cols=4, rows=3, buff=0).move_to(rectangle.target)
        self.my_play(LaggedStart(*[Write(i) for i in unit_squares]))

        order = (0,1,4,5,8,9)

        self.my_play(*[
            unit_squares[i].animate.shift(DOWN*3.5) for i in order
        ],*[
            i.animate.shift(DOWN*3.5) for i in (tri1, tri2)
        ])
        equal = MathTex("=").scale(2).next_to(tri1, LEFT *3)
        result = MathTex(r"= \text{ 6 }", r"({m^{2}, cm^2,...})").next_to(tri2, RIGHT)
        self.my_play(Write(equal), Write(result))


        red_rec =  VGroup(*[Square(
            side_length=1, stroke_width=0.5, fill_color=RED, fill_opacity=0.7
        ) for i in range(6)]).arrange_in_grid(cols=3, rows=2, buff=0).align_to(tri1, DL)

        order2 = (0,1,3,2,4,5)

        self.my_play(*[
            Transform(unit_squares[i].copy(), red_rec[j])
            for i, j in zip(order, order2)
        ],*[
            i.animate.set_fill(BLUE)
            for i in (tri1, tri2)
        ], run_time=3)
