from manim import *

list_scene = ("Scene0", "Scene1", "Scene2")
SCENE_NAME = list_scene[0]
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


class Scene0(MyScene):
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

        def create_angle():
            OA = Line(O.get_center(), A.get_center(), color=YELLOW)
            angle = Angle(OA, Line(O.get_center(), RIGHT * 3), other_angle=True, color=RED)
            angle_value = angle.get_value() * -1
            angle_t = MathTex(r"\alpha", color=RED).move_to(
                Angle(OA, Line(O.get_center(), RIGHT * 3), other_angle=True, radius=1).point_from_proportion(0.5))
            angle_t2 = MathTex(r"\alpha={:.2f}".format(angle_value), "^{rad}", color=RED).next_to(x_t, UP,
                                                                                                  aligned_edge=LEFT)
            angle_t2.shift(UP * 2)
            arc = sub_circle.get_subcurve(0.001, angle_value / (2 * PI))
            arc.set_color(PINK)
            return VGroup(OA, angle, angle_t, angle_t2, arc)

        angle = create_angle()

        # self.add(main_circle, vertical, horizontal, O_t, x_t, y_t, brace_t, brace, O, A, B, C, D, coord_A, coord_B,
        #          coord_C, coord_D, quadrant1, quadrant2, quadrant3, quadrant4, sub_circle, angle)

        def update_angle(obj):
            angle.become(create_angle())

        self.my_play(Create(O), Write(O_t), Create(main_circle))
        self.my_play(FadeIn(brace, shift=UP), FadeIn(brace_t, shift=UP))
        self.my_play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.my_play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.my_play(LaggedStart(*[Write(i) for i in (quadrant1, quadrant2, quadrant3, quadrant4)]))
        self.my_play(FadeOut(brace), FadeOut(brace_t), Create(sub_circle), rate_func=linear)
        self.add(A, angle)
        A.add_updater(update_angle)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.001, 0.15)))
        self.wait(0.5)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.15, 0.5)))
        self.wait(0.5)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.5, 0.9999)))
        text = MathTex(r"\alpha=2\pi", color=RED).next_to(angle[3], DOWN, aligned_edge=LEFT)
        self.play(Write(text))
        self.wait()


class Scene1(MyScene):
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
            angle = Angle(OA, Line(O.get_center(), RIGHT * 3), other_angle=True, color=RED)
            angle_value = angle.get_value() * -1
            angle_t = MathTex(r"\alpha", color=RED).move_to(
                Angle(OA, Line(O.get_center(), RIGHT * 3), other_angle=True, radius=1).point_from_proportion(0.5))

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
        angle_t2 = MathTex(r"\alpha={\pi \backslash 4}", color=RED) \
            .next_to(x_t, UP, aligned_edge=LEFT)
        angle_t2.shift(UP * 3 + LEFT * 0.2)
        text1 = MathTex(r"\alpha=", r"2\pi", "+", r"{\pi \backslash 4}", color=RED) \
            .next_to(angle_t2, DOWN, aligned_edge=LEFT)
        text2 = MathTex(r"\alpha=", r"4\pi", "+", r"{\pi \backslash 4}", color=RED)\
            .next_to(text1, DOWN, aligned_edge=LEFT)
        text3 = MathTex(r"\alpha=", r"6\pi", "+", r"{\pi \backslash 4}", color=RED)\
            .next_to(text2, DOWN, aligned_edge=LEFT)
        text4 = MathTex(r"\alpha=", r"k2\pi", "+", r"{\pi \backslash 4}", color=RED)\
            .next_to(text3, DOWN, aligned_edge=LEFT)
        for i in (text1, text2, text3, text4):
            i[1].set_color(GREEN)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.001, 1 / 8)), Write(angle_t2), rate_func=linear,
                  run_time=1)
        A_t = MathTex("A", color=YELLOW).next_to(ORIGIN+RIGHT*3, UR)
        B_t = MathTex("B", color=YELLOW).next_to(A, RIGHT)
        self.play(Write(A_copy), Write(A_t), Write(B_t))
        self.wait(0.5)
        sub_circle.rotate(PI / 4)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.001, 0.9999)), Write(text1), rate_func=linear, run_time=2)
        self.wait(0.5)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.001, 0.9999)), Write(text2), rate_func=linear, run_time=2)
        self.wait(0.5)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.001, 0.9999)), Write(text3), rate_func=linear, run_time=2)
        self.wait(0.5)
        self.play(Write(text4))
        self.wait()

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
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(7 / 8, 0.9999).reverse_points()), Write(angle_t2), rate_func=linear,
                  run_time=1)
        self.wait(0.5)
        beta = Angle(angle[0], Line(O.get_center(), RIGHT * 3), other_angle=True, color=BLUE)
        beta_t = MathTex(r"\beta", color=BLUE).move_to(
            Angle(angle[0], Line(O.get_center(), RIGHT * 3), other_angle=True, radius=1).point_from_proportion(0.5))
        A_t = MathTex("A", color=YELLOW).next_to(ORIGIN+RIGHT*3, UR)
        B_t = MathTex("B", color=YELLOW).next_to(A, RIGHT)
        self.play(Create(beta.reverse_points()), Write(beta_t), Write(text1), Write(A_copy), Write(A_t), Write(B_t))
        self.wait()
