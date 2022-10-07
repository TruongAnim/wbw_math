from manim import *
import math

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3")
SCENE_NAME = list_scene[2]
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
        A = Dot(LEFT * 2)
        B = Dot(UP * 3.464)
        C = Dot(RIGHT * 2.9)
        H = Dot(ORIGIN)
        group_point = VGroup(A, B, C, H)
        group_point.shift(RIGHT * 3 + DOWN).scale(1.3)
        AB = Line(A, B, color=RED)
        BC = Line(B, C, color=YELLOW)
        AC = Line(C, A, color=BLUE)
        BH = Line(B, H, color=GREEN)
        A_angle = Angle(AC, AB, quadrant=(-1, 1))
        A_angle_t = MathTex("60^\circ").move_to(Angle(AC, AB, quadrant=(-1, 1), radius=1))
        B_angle = Angle(AC, BC, quadrant=(1, -1), other_angle=True)
        B_angle_t = MathTex("50^\circ").move_to(Angle(AC, BC, quadrant=(1, -1), other_angle=True, radius=1))
        c = MathTex("4", color=RED).next_to(AB.get_center(), UL)
        a = MathTex("a=?", color=YELLOW).next_to(BC.get_center(), UR)
        self.play(Create(A), Create(B), Create(C))
        self.play(Create(AB), Create(BC), Create(AC))
        self.play(*[Write(i) for i in (c, A_angle_t, B_angle_t)],
                  *[Create(i) for i in (A_angle, B_angle)])
        self.play(Write(a))
        self.wait()


class Scene1(MyScene):
    def construct(self):
        A = Dot(LEFT * 2)
        B = Dot(UP * 3.464)
        C = Dot(RIGHT * 2.9)
        H = Dot(ORIGIN)
        group_point = VGroup(A, B, C, H)
        group_point.shift(RIGHT * 3 + DOWN).scale(1.3)
        AB = Line(A, B, color=RED)
        BC = Line(B, C, color=YELLOW)
        AC = Line(C, A, color=BLUE)
        BH = Line(B, H, color=GREEN)
        A_angle = Angle(AC, AB, quadrant=(-1, 1))
        A_angle_t = MathTex("A").move_to(Angle(AC, AB, quadrant=(-1, 1), radius=0.8))
        C_angle = Angle(AC, BC, quadrant=(1, -1), other_angle=True)
        C_angle_t = MathTex("C").move_to(Angle(AC, BC, quadrant=(1, -1), other_angle=True, radius=0.8))
        B_angle = Angle(AB, BC, quadrant=(-1, 1))
        B_angle_t = MathTex("B").move_to(Angle(AB, BC, quadrant=(-1, 1), radius=0.8)) \
            .shift(RIGHT * 0.15)
        H_angle_t = MathTex("H").next_to(H, DOWN)
        H_angle = RightAngle(BH, AC, quadrant=(-1, -1))
        c = MathTex("c", color=RED).next_to(AB.get_center(), UL)
        a = MathTex("a", color=YELLOW).next_to(BC.get_center(), UR)
        b = MathTex("b", color=BLUE).next_to(AC.get_center(), DOWN).shift(RIGHT * 0.5)
        h = MathTex("h", color=GREEN).next_to(BH.get_center(), RIGHT)
        equation1 = MathTex("sin(", "A", ")", "=", "{h", r"\over", "c}").to_corner(UL, buff=MED_LARGE_BUFF)
        equation2 = MathTex("sin(", "C", ")", "=", "{h", r"\over", "a}").next_to(equation1, DOWN, aligned_edge=LEFT,
                                                                                 buff=MED_LARGE_BUFF)
        equation3 = MathTex("\Rightarrow {sin(", "A", ")", "\over", "a}", "=", "{sin(", "C", ")", "\over", "c}", "=",
                            "{sin(", "B", ")", "\over", "b}").next_to(equation2, DOWN, aligned_edge=LEFT)
        color_map = {
            "a": YELLOW,
            "b": BLUE,
            "c": RED,
            "h": GREEN,
            "sin": WHITE
        }
        for i in (equation1, equation2, equation3):
            i.set_color_by_tex_to_color_map(color_map)
        brace = Brace(VGroup(equation2, equation1), LEFT)
        law_of_sin = Text("Định lý sin", font="Sans", color=YELLOW).next_to(equation3, DOWN)

        # self.add(equation1, equation2, equation3, brace)
        # self.add(BH, H, AB, BC, AC, A_angle, A_angle_t, C_angle, C_angle_t, B_angle_t, B_angle,
        #          a, b, c, A, B, C, H_angle, h, H_angle_t, law_of_sin)

        self.play(Create(A), Create(B), Create(C))
        self.play(Create(AB), Create(BC), Create(AC))
        self.play(
            LaggedStart(*[
                Write(i) for i in (a, b, c, A_angle_t, B_angle_t, C_angle_t)
            ]),
            *[Create(i) for i in (A_angle, B_angle, C_angle)])
        self.play(Create(BH), FadeIn(h, shift=LEFT),
                  Create(H_angle), Write(H_angle_t), FadeIn(H))
        self.wait()
        self.my_play(LaggedStart(*[
            Write(equation1[i]) for i in (0, 2, 3, 5)
        ]), LaggedStart(*[
            Write(equation2[i]) for i in (0, 2, 3, 5)
        ]), Write(brace))
        transform_map = (((A_angle_t, h, c),
                          (equation1[1], equation1[4], equation1[6])),
                         ((C_angle_t, h, a),
                          (equation2[1], equation2[4], equation2[6])))
        for transform in transform_map:
            self.my_play(LaggedStart(*[
                ReplacementTransform(i.copy(), j) for i, j in zip(transform[0], transform[1])
            ]))
        self.my_play(Write(equation3[:11]))
        self.my_play(Write(equation3[11:]), *[FadeOut(i) for i in (BH, H_angle, H_angle_t, h, H)])
        self.my_play(Write(law_of_sin))
        self.my_play(Circumscribe(VGroup(equation3[1:], law_of_sin)))


class Scene2(MyScene):
    def construct(self):
        A = Dot(LEFT * 2)
        B = Dot(UP * 3.464)
        C = Dot(RIGHT * 2.9)
        H = Dot(ORIGIN)
        group_point = VGroup(A, B, C, H)
        group_point.shift(RIGHT * 3 + DOWN).scale(1.3)
        AB = Line(A, B, color=RED)
        BC = Line(B, C, color=YELLOW)
        AC = Line(C, A, color=BLUE)
        BH = Line(B, H, color=GREEN)
        A_angle = Angle(AC, AB, quadrant=(-1, 1))
        A_angle_t = MathTex("60^\circ").move_to(Angle(AC, AB, quadrant=(-1, 1), radius=1))
        B_angle = Angle(AC, BC, quadrant=(1, -1), other_angle=True)
        B_angle_t = MathTex("50^\circ").move_to(Angle(AC, BC, quadrant=(1, -1), other_angle=True, radius=1))
        c = MathTex("4", color=RED).next_to(AB.get_center(), UL)
        a = MathTex("a=?", color=YELLOW).next_to(BC.get_center(), UR)
        self.play(Create(A), Create(B), Create(C))
        self.play(Create(AB), Create(BC), Create(AC))
        self.play(*[Write(i) for i in (c, A_angle_t, B_angle_t)],
                  *[Create(i) for i in (A_angle, B_angle)])
        self.play(Write(a))
        self.wait()
        equation1 = MathTex("{sin(", "60^\circ", ")", "\over", "a}", "=", "{sin(", "50^\circ", ")", "\over", "4}") \
            .to_corner(UL)
        equation2 = MathTex("\Rightarrow", "a", "=", "{sin(", "60^\circ", ")", r"\times", "4", "\over", "sin(",
                            "50^\circ", ")}") \
            .next_to(equation1, DOWN, aligned_edge=LEFT)
        equation3 = MathTex("\Rightarrow", "a", r"\approx", "4.52").next_to(equation2, DOWN, aligned_edge=LEFT)
        color_map = {
            "a": YELLOW,
            "b": BLUE,
            "4": RED,
            "h": GREEN,
            "sin": WHITE,
            "approx": WHITE,
            "4.52": WHITE
        }
        for i in (equation1, equation2, equation3):
            i.set_color_by_tex_to_color_map(color_map)
        self.play(LaggedStart(*[
            Write(equation1[i]) for i in (0, 2, 3, 5, 6, 8, 9)
        ]))
        self.my_play(LaggedStart(*[
            Transform(j.copy(), equation1[i]) for i, j in zip((10, 1, 4, 7),
                                                              (c, A_angle_t, a[0][0], B_angle_t))
        ]))
        self.my_play(Write(equation2))
        self.my_play(Write(equation3))
        self.my_play(equation3[-1].copy().animate.move_to(a).set_color(YELLOW), FadeOut(a))


class Scene3(MyScene):
    def construct(self):
        A = Dot(LEFT * 2)
        B = Dot(UP * 3.464)
        C = Dot(RIGHT * 2.9)
        H = Dot(ORIGIN)
        group_point = VGroup(A, B, C, H)
        group_point.shift(RIGHT * 3 + DOWN).scale(1.3)
        AB = Line(A, B, color=RED)
        BC = Line(B, C, color=YELLOW)
        AC = Line(C, A, color=BLUE)
        BH = Line(B, H, color=GREEN)
        H_angle = RightAngle(BH, AC, quadrant=(-1, -1))
        A_angle = Angle(AC, AB, quadrant=(-1, 1))
        A_angle_t = MathTex("60^\circ").move_to(Angle(AC, AB, quadrant=(-1, 1), radius=1))
        B_angle = Angle(AC, BC, quadrant=(1, -1), other_angle=True)
        B_angle_t = MathTex("50^\circ").move_to(Angle(AC, BC, quadrant=(1, -1), other_angle=True, radius=1))
        c = MathTex("a", color=RED).next_to(AB.get_center(), UL)
        a = MathTex("a", color=YELLOW).next_to(BC.get_center(), UR)
        b = MathTex("b", color=BLUE).next_to(AC.get_center(), DR)
        h = MathTex(r"a", "sin(", "60^\circ", ")").scale(0.8).next_to(BH.get_center(), RIGHT, buff=SMALL_BUFF)
        h.shift(DOWN*0.5)
        h[0].set_color(RED)
        self.play(Create(A), Create(B), Create(C))
        self.play(Create(AB), Create(BC), Create(AC))
        self.play(*[Write(i) for i in (c, A_angle_t, b)],
                  *[Create(i) for i in (A_angle)])
        self.wait()
        self.play(Create(BH), Create(H), Create(H_angle))
        self.wait()
        self.play(*[Write(h[i]) for i in (1, 3)],
                  Transform(c.copy(),h[0]),
                  Transform(A_angle_t.copy(), h[2]))

        equation1 = MathTex("\Rightarrow", r"\text{Area}=", "{1\over 2}", "a", "b", "sin(", "60^\circ", ")") \
            .shift(LEFT*3)
        color_map = {
            "a": RED,
            "b": BLUE,
            "sin": WHITE,
            "Area": WHITE,
            "Rightarrow": WHITE
        }
        equation1.set_color_by_tex_to_color_map(color_map)
        self.play(LaggedStart(*[
            Write(equation1[i]) for i in (0, 1, 2)
        ]))
        self.my_play(LaggedStart(*[
            Transform(j.copy(), equation1[i]) for i, j in zip((3, 4, 5, 6, 7),
                                                              (h[0], b, h[1], h[2], h[3]))
        ]))