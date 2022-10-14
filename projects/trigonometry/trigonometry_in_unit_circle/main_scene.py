import math

from manim import *

list_scene = ("Scene0", "Scene1", "Scene2")
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
        self.wait()


class Scene0(MyScene):
    def construct(self):
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        H = Dot(main_circle.point_from_proportion(1 / 6))
        H_t = MathTex("H").next_to(H, UR)
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal, RIGHT)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        A = Dot(RIGHT * 3)
        B = Dot(UP * 3)
        C = Dot(LEFT * 3)
        D = Dot(DOWN * 3)
        coord_A = MathTex("(1,0)").next_to(A, DR)
        coord_B = MathTex("(0,1)").next_to(B, UL)
        coord_C = MathTex("(-1,0)").next_to(C, DL)
        coord_D = MathTex("(0,-1)").next_to(D, DL)
        OH = Line(O, H, color=YELLOW)
        OH_t = MathTex("1", color=YELLOW).scale(0.7).next_to(OH.get_center(), DR, buff=SMALL_BUFF)
        X = Dot(RIGHT * math.cos(PI / 3) * 3)
        HX = Line(H, X.get_center(), color=GREEN)
        OX = Line(O, X.get_center(), color=RED)
        OHX = RightAngle(HX, OX, length=0.2, quadrant=(-1, -1))
        Y = Dot(UP * math.sin(PI / 3) * 3)
        HY = Line(H, Y.get_center(), color=RED)
        OY = Line(O, Y.get_center(), color=GREEN)
        OHY = RightAngle(HY, OY, length=0.2, quadrant=(-1, -1))
        alpha = Angle(OH, OX, other_angle=True, radius=0.3)
        a = MathTex("a", color=RED).next_to(OX, DOWN)
        b = MathTex("b", color=GREEN).next_to(OY, LEFT)
        alpha_t = MathTex(r"\alpha").scale(0.8).move_to(Angle(OH, OX, other_angle=True, radius=0.6))

        unit_circle = VGroup(main_circle, vertical, horizontal, O_t, x_t, y_t, O, A, B, C, D, coord_A, coord_B,
                             coord_C, coord_D, H, H_t, OH, OH_t, X, HX, OX, OHX, alpha, alpha_t, HY, Y, OY, OHY, a,
                             b).shift(LEFT * 2.5)

        fomular1 = MathTex(r"cos(\alpha)=", "{a", "\over", "1}", "=", "a").shift(UP * 3 + RIGHT * 4)
        fomular2 = MathTex(r"sin(\alpha)=", "{b", "\over", "1}", "=", "b").next_to(fomular1, DOWN, aligned_edge=LEFT)
        fomular3 = MathTex(r"sin^2(\alpha) + cos^2(\alpha) = ", "a", "^2", "+", "b", "^2", "=", "1")\
            .shift(DOWN * 3 + RIGHT * 3.5)
        color_map = {
            fomular1[1]: RED,
            fomular1[3]: YELLOW,
            fomular1[5]: RED,
            fomular2[1]: GREEN,
            fomular2[3]: YELLOW,
            fomular2[5]: GREEN,
            fomular3[1]: RED,
            fomular3[4]: GREEN,
            fomular3[-1]: YELLOW,
        }
        for item in color_map:
            item.set_color(color_map[item])
        # self.add(unit_circle, fomular1, fomular2)
        self.play(Create(O), Write(O_t), Create(main_circle))
        self.play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.play(Create(OH), Create(alpha), Create(H), Create(OH_t))
        self.play(Write(alpha_t), Create(H_t))
        self.play(Create(HX), Create(OHX), Create(X))
        self.play(Create(OX), Write(a))
        self.play(Write(fomular1[0]), Write(fomular1[2]), Write(fomular1[4]))
        self.play(ReplacementTransform(a.copy(), fomular1[1]),
                  ReplacementTransform(OH_t.copy(), fomular1[3]))
        self.play(Write(fomular1[-1]))
        self.play(Create(HY), Create(OHY), Create(Y))
        self.play(Create(OY), Write(b))
        self.play(Write(fomular2[0]), Write(fomular2[2]), Write(fomular2[4]))
        self.play(ReplacementTransform(b.copy(), fomular2[1]),
                  ReplacementTransform(OH_t.copy(), fomular2[3]))
        self.play(Write(fomular2[-1]))
        self.play(Transform(OH.copy(), OX), Wiggle(fomular1))
        self.play(Transform(OH.copy(), OY), Wiggle(fomular2))
        self.play(Write(fomular3[0]))
        self.play(Transform(a.copy(), fomular3[1]),
                  Transform(b.copy(), fomular3[4]))
        self.play(Write(fomular3[2]),
                  Write(fomular3[3]),
                  Write(fomular3[5]),
                  Write(fomular3[6]))
        self.play(Transform(OH_t.copy(), fomular3[-1]))
        self.play(Circumscribe(fomular3))


class Scene1(MyScene):
    def construct(self):
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        H = Dot(main_circle.point_from_proportion(1 / 6))
        H_t = MathTex("H").next_to(H, UR)
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal, RIGHT)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        A = Dot(RIGHT * 3)
        B = Dot(UP * 3)
        C = Dot(LEFT * 3)
        D = Dot(DOWN * 3)
        coord_A = MathTex("(1,0)").next_to(A, DR)
        coord_B = MathTex("(0,1)").next_to(B, UL)
        coord_C = MathTex("(-1,0)").next_to(C, DL)
        coord_D = MathTex("(0,-1)").next_to(D, DL)
        OH = Line(O, H, color=YELLOW)
        OH_t = MathTex("1", color=YELLOW).scale(0.7).next_to(OH.get_center(), DR, buff=SMALL_BUFF)
        X = Dot(RIGHT * math.cos(PI / 3) * 3)
        HX = Line(H, X.get_center(), color=GREEN)
        OX = Line(O, X.get_center(), color=RED)
        OHX = RightAngle(HX, OX, length=0.2, quadrant=(-1, -1))
        Y = Dot(UP * math.sin(PI / 3) * 3)
        HY = Line(H, Y.get_center(), color=RED)
        OY = Line(O, Y.get_center(), color=GREEN)
        OHY = RightAngle(HY, OY, length=0.2, quadrant=(-1, -1))
        alpha = Angle(OH, OX, other_angle=True, radius=0.3)
        a = MathTex("a", color=RED).next_to(OX, DOWN)
        b = MathTex("b", color=GREEN).next_to(OY, LEFT)
        alpha_t = MathTex(r"\alpha").scale(0.8).move_to(Angle(OH, OX, other_angle=True, radius=0.6))

        unit_circle = VGroup(main_circle, vertical, horizontal, O_t, x_t, y_t, O, A, B, C, D, coord_A, coord_B,
                             coord_C, coord_D, H, H_t, OH, OH_t, X, HX, OX, OHX, alpha, alpha_t, HY, Y, OY, OHY, a,
                             b).shift(LEFT * 2.5)

        fomular1 = MathTex(r"cos(\alpha)=", "{a", "\over", "1}", "=", "a").shift(UP * 3 + RIGHT * 4)
        fomular2 = MathTex(r"sin(\alpha)=", "{b", "\over", "1}", "=", "b").next_to(fomular1, DOWN, aligned_edge=LEFT)
        fomular3 = MathTex(r"sin^2(\alpha) + cos^2(\alpha) = ", "a", "^2", "+", "b", "^2", "=", "1") \
            .shift(DOWN * 3 + RIGHT * 3.5)
        color_map = {
            fomular1[1]: RED,
            fomular1[3]: YELLOW,
            fomular1[5]: RED,
            fomular2[1]: GREEN,
            fomular2[3]: YELLOW,
            fomular2[5]: GREEN,
            fomular3[1]: RED,
            fomular3[4]: GREEN,
            fomular3[-1]: YELLOW,
        }
        for item in color_map:
            item.set_color(color_map[item])
        # self.add(unit_circle, fomular1, fomular2)
        self.play(Create(O), Write(O_t), Create(main_circle))
        self.play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.play(Create(OH), Create(alpha), Create(H), Create(OH_t))
        self.play(Write(alpha_t), Create(H_t))
        self.play(Create(HX), Create(OHX), Create(X))
        self.play(Create(OX), Write(a))
        self.play(Write(fomular1[0]), Write(fomular1[2]), Write(fomular1[4]))
        self.play(ReplacementTransform(a.copy(), fomular1[1]),
                  ReplacementTransform(OH_t.copy(), fomular1[3]))
        self.play(Write(fomular1[-1]))
        self.play(Create(HY), Create(OHY), Create(Y))
        self.play(Create(OY), Write(b))
        self.play(Write(fomular2[0]), Write(fomular2[2]), Write(fomular2[4]))
        self.play(ReplacementTransform(b.copy(), fomular2[1]),
                  ReplacementTransform(OH_t.copy(), fomular2[3]))
        self.play(Write(fomular2[-1]))
        self.play(Transform(OH.copy(), OX), Wiggle(fomular1))
        self.play(Transform(OH.copy(), OY), Wiggle(fomular2))
        self.play(Write(fomular3[0]))
        self.play(Transform(a.copy(), fomular3[1]),
                  Transform(b.copy(), fomular3[4]))
        self.play(Write(fomular3[2]),
                  Write(fomular3[3]),
                  Write(fomular3[5]),
                  Write(fomular3[6]))
        self.play(Transform(OH_t.copy(), fomular3[-1]))


class Scene2(MyScene):
    def construct(self):
        main_circle = DashedVMobject(Circle(radius=3, color=BLUE), num_dashes=40)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal, RIGHT)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        brace = Brace(Line(start=ORIGIN, end=RIGHT * 3), DOWN, buff=SMALL_BUFF, color=GREEN)
        brace_t = brace.get_tex("1")
        brace_t.set_color(GREEN)
        A = Dot(RIGHT * 3)
        A_copy = Dot(RIGHT * 3)
        B = Dot(UP * 3)
        C = Dot(LEFT * 3)
        D = Dot(DOWN * 3)
        coord_A = MathTex("(1,0)").next_to(A, DR)
        coord_B = MathTex("(0,1)").next_to(B, UL)
        coord_C = MathTex("(-1,0)").next_to(C, DL)
        coord_D = MathTex("(0,-1)").next_to(D, DL)
        quadrant_dis = 3.2
        quadrant1 = Text("I").move_to(RIGHT * quadrant_dis + UP * quadrant_dis)
        quadrant2 = Text("II").move_to(LEFT * quadrant_dis + UP * quadrant_dis)
        quadrant3 = Text("III").move_to(LEFT * quadrant_dis + DOWN * quadrant_dis)
        quadrant4 = Text("IV").move_to(RIGHT * quadrant_dis + DOWN * quadrant_dis)
        sub_circle = Circle(radius=3, color=GREEN)
        A = Dot(RIGHT * 3 + UP * 0.01)
        self.color = PINK
        self.radius = 0.5

        def create_angle():
            OA = Line(O.get_center(), A.get_center(), color=YELLOW)
            angle = Angle(OA, Line(O.get_center(), RIGHT * 3), other_angle=False, color=RED)
            angle_value = angle.get_value() * -1
            angle_t = MathTex(r"\alpha", color=RED).move_to(
                Angle(OA, Line(O.get_center(), RIGHT * 3), other_angle=False, radius=1).point_from_proportion(0.5))

            return VGroup(OA, angle, angle_t)

        angle = create_angle()
        arc = TracedPath(A.get_center, dissipating_time=0.5, stroke_opacity=[0, 1], stroke_width=4)
        arc.set_color(PINK)

        # self.add(main_circle, vertical, horizontal, O_t, x_t, y_t, brace_t, brace, O, A, B, C, D, coord_A, coord_B,
        #          coord_C, coord_D, quadrant1, quadrant2, quadrant3, quadrant4, sub_circle, angle)

        def update_angle(obj):
            angle.become(create_angle())

        self.play(Create(O), Write(O_t), Create(main_circle))
        self.play(FadeIn(brace, shift=UP), FadeIn(brace_t, shift=UP))
        self.play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.play(LaggedStart(*[Write(i) for i in (quadrant1, quadrant2, quadrant3, quadrant4)]))
        self.play(FadeOut(brace), FadeOut(brace_t), Create(sub_circle), rate_func=linear)
        self.wait()
        self.add(A, angle, arc)
        A.add_updater(update_angle)
        angle_t2 = MathTex(r"\alpha={-\pi \backslash 4}", color=RED) \
            .next_to(x_t, UP, aligned_edge=LEFT)
        angle_t2.shift(UP * 2 + LEFT * 0.2)
        text1 = MathTex(r"\beta=", r"{7\pi \backslash 4}", color=RED) \
            .next_to(angle_t2, DOWN, aligned_edge=LEFT)

        text1.set_color(BLUE)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(7 / 8, 0.9999).reverse_points()), Write(angle_t2),
                  rate_func=linear,
                  run_time=1)
        self.wait(0.5)
        beta = Angle(angle[0], Line(O.get_center(), RIGHT * 3), other_angle=True, color=BLUE)
        beta_t = MathTex(r"\beta", color=BLUE).move_to(
            Angle(angle[0], Line(O.get_center(), RIGHT * 3), other_angle=True, radius=1).point_from_proportion(0.5))
        A_t = MathTex("A", color=YELLOW).next_to(ORIGIN + RIGHT * 3, UR)
        B_t = MathTex("B", color=YELLOW).next_to(A, RIGHT)
        self.play(Create(beta.reverse_points()), Write(beta_t), Write(text1), Write(A_copy), Write(A_t), Write(B_t))
        self.wait()
