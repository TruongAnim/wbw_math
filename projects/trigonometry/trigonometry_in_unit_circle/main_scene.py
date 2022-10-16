import math

from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5")
SCENE_NAME = list_scene[5]
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
        self.play(Circumscribe(fomular3))


class Scene1(MyScene):
    def construct(self):
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        H = Dot(main_circle.point_from_proportion(1 / 6))
        K = Dot(main_circle.point_from_proportion(2 / 6))
        H_t = MathTex("H").next_to(H, UR)
        K_t = MathTex("K").next_to(K, UL)
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
        OK = Line(O, K, color=YELLOW)
        OK_t = MathTex("1", color=YELLOW).scale(0.7).next_to(OK.get_center(), DL, buff=SMALL_BUFF)

        Y = Dot(UP * math.sin(PI / 3) * 3)
        HY = Line(H, Y.get_center(), color=RED)
        OY = Line(O, Y.get_center(), color=GREEN)
        OHY = RightAngle(HY, OY, length=0.2, quadrant=(-1, -1))
        KY = Line(K, Y.get_center(), color=RED)

        alpha = Angle(OH, Line(O, RIGHT * 3), other_angle=True, radius=0.3, color=PINK)
        beta = Angle(OK, Line(O, RIGHT * 3), other_angle=True, radius=0.7, color=PURPLE)
        b = MathTex("b", color=GREEN).next_to(OY, LEFT)
        alpha_t = MathTex(r"\alpha", color=PINK).scale(0.8).move_to(
            Angle(OH, Line(O, RIGHT * 3), other_angle=True, radius=0.6))
        beta_t = MathTex(r"\beta", color=PURPLE).scale(0.8).move_to(
            Angle(OH, Line(O, RIGHT * 3), other_angle=True, radius=1))

        unit_circle = VGroup(main_circle, vertical, horizontal, O_t, x_t, y_t, O, A, B, C, D, coord_A, coord_B,
                             coord_C, coord_D, H, H_t, OH, OH_t, KY, OK, OK_t, K, alpha, alpha_t, HY, Y, OY, OHY,
                             b, beta, beta_t, K_t).shift(LEFT * 2.5)

        fomular1 = MathTex(r"\beta", "=", r"\pi", "-", r"\alpha").shift(UP * 3 + RIGHT * 2)
        fomular2 = MathTex("sin(", r"\alpha", ") = sin(", r"\pi", "-", r"\alpha", ")=", "b") \
            .next_to(fomular1, DOWN, aligned_edge=LEFT)
        color_map = {
            fomular1[0]: PURPLE,
            fomular1[4]: PINK,
            fomular2[1]: PINK,
            fomular2[5]: PINK,
            fomular2[-1]: GREEN
        }
        for item in color_map:
            item.set_color(color_map[item])
        # self.add(unit_circle, fomular1, fomular2)
        self.play(Create(O), Write(O_t), Create(main_circle))
        self.play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.play(Create(OH), Create(alpha), Create(H))
        self.play(Write(H_t), Write(alpha_t), Write(OH_t))
        self.play(Create(OK), Create(beta), Create(K))
        self.play(Write(K_t), Write(beta_t), Write(fomular1), Write(OK_t))
        self.play(Create(HY), Create(KY), Create(OY), Create(OHY), Create(Y), Write(b))
        self.play(Write(fomular2[:-1]))
        self.play(Transform(b.copy(), fomular2[-1]))


class Scene2(MyScene):
    def construct(self):
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        H = Dot(main_circle.point_from_proportion(1 / 6))
        K = Dot(main_circle.point_from_proportion(5 / 6))
        H_t = MathTex("H").next_to(H, UR)
        K_t = MathTex("K").next_to(K, DR)
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
        OH_t = MathTex("1", color=YELLOW).scale(0.7).next_to(OH.get_center(), UL, buff=SMALL_BUFF)
        OK = Line(O, K, color=YELLOW)
        OK_t = MathTex("1", color=YELLOW).scale(0.7).next_to(OK.get_center(), DL, buff=SMALL_BUFF)

        X = Dot(RIGHT * math.cos(PI / 3) * 3)
        HX = Line(H, X.get_center(), color=GREEN)
        OX = Line(O, X.get_center(), color=RED)
        OHY = RightAngle(HX, OX, length=0.2, quadrant=(-1, -1))
        KX = Line(K, X.get_center(), color=GREEN)

        alpha = Angle(OH, Line(O, RIGHT * 3), other_angle=True, radius=0.3, color=PINK)
        beta = Angle(OK, Line(O, RIGHT * 3), other_angle=False, radius=0.3, color=PURPLE)
        a = MathTex("a", color=RED).next_to(OX, UR)
        alpha_t = MathTex(r"\alpha", color=PINK).scale(0.8).move_to(
            Angle(OH, Line(O, RIGHT * 3), other_angle=True, radius=0.6))
        beta_t = MathTex(r"\beta", color=PURPLE).scale(0.8).move_to(
            Angle(OK, Line(O, RIGHT * 3), other_angle=False, radius=0.6))

        unit_circle = VGroup(main_circle, vertical, horizontal, O_t, x_t, y_t, O, A, B, C, D, coord_A, coord_B,
                             coord_C, coord_D, H, H_t, OH, OH_t, KX, OK, OK_t, K, alpha, alpha_t, HX, X, OX, OHY,
                             a, beta, beta_t, K_t).shift(LEFT * 2.5)

        fomular1 = MathTex(r"\beta", "=", "-", r"\alpha").shift(UP * 3 + RIGHT * 2)
        fomular2 = MathTex("cos(", r"\alpha", ") = cos(", "-", r"\alpha", ")=", "a") \
            .next_to(fomular1, DOWN, aligned_edge=LEFT)
        color_map = {
            fomular1[0]: PURPLE,
            fomular1[3]: PINK,
            fomular2[1]: PINK,
            fomular2[4]: PINK,
            fomular2[-1]: RED
        }
        for item in color_map:
            item.set_color(color_map[item])
        # self.add(unit_circle, fomular1, fomular2)
        self.play(Create(O), Write(O_t), Create(main_circle))
        self.play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.play(Create(OH), Create(alpha), Create(H))
        self.play(Write(H_t), Write(alpha_t), Write(OH_t))
        self.play(Create(OK), Create(beta), Create(K))
        self.play(Write(K_t), Write(beta_t), Write(fomular1), Write(OK_t))
        self.play(Create(HX), Create(KX), Create(OX), Create(OHY), Create(X), Write(a))
        self.play(Write(fomular2[:-1]))
        self.play(Transform(a.copy(), fomular2[-1]))


class Scene3(MyScene):
    def construct(self):
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        self.O = Dot(ORIGIN)
        O_t = MathTex("O").next_to(self.O, DL)
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

        H = Dot(RIGHT*3)
        turn = 0
        def create_angle():
            OH = Line(self.O.get_center(), H.get_center(), color=YELLOW)
            try:
                alpha = Angle(OH, Line(self.O.get_center(), self.O.get_center()+RIGHT * 3), other_angle=True, radius=0.3, color=PINK)
                alpha2 = Angle(OH, Line(self.O.get_center(), self.O.get_center()+RIGHT * 3), other_angle=True, radius=0.6, color=PINK)
            except:
                alpha = Angle(OH, Line(self.O.get_center(), self.O.get_center()+RIGHT * 3+UP*0.001), other_angle=True, radius=0.3, color=PINK)
                alpha2 = Angle(OH, Line(self.O.get_center(), self.O.get_center()+RIGHT * 3+UP*0.001), other_angle=True, radius=0.6, color=PINK)



            alpha_value = alpha.get_value()*-1 + turn*2*PI
            alpha_t = MathTex(r"x", color=PINK).scale(0.8).move_to(
                alpha2.point_from_proportion(0.5))
            Y = Dot(self.O.get_center()+UP*3*math.sin(alpha_value))
            OY = Line(self.O, Y, color=GREEN)
            b = MathTex("sin(x)", color=GREEN).next_to(OY, LEFT)
            HY = DashedLine(H, Y)
            fomular1 = MathTex(r"x", "=", "{:.2f}".format(alpha_value), "^{rad}").shift(UP * 3 + RIGHT * 3)
            fomular2 = MathTex("sin(", "x)", "=", "{:.2f}".format(math.sin(alpha_value)))\
                .next_to(fomular1, DOWN, aligned_edge=LEFT)
            color_map = {
                fomular1[0]: PINK,
                fomular2[0:2]: GREEN
            }
            for item in color_map:
                item.set_color(color_map[item])
            return VGroup(OH, OY, alpha, alpha_t, b, Y, HY, fomular1, fomular2)

        angle = create_angle()
        def updater(obj):
            angle.become(create_angle())
        angle.add_updater(updater)
        unit_circle = VGroup(main_circle, vertical, horizontal, O_t, x_t, y_t, self.O, A, B, C, D, coord_A, coord_B,
                             coord_C, coord_D, H, angle).shift(LEFT * 2.5)


        # fomular2 = MathTex("cos(", r"\alpha", ") = cos(", "-", r"\alpha", ")=", "a") \
        #     .next_to(fomular1, DOWN, aligned_edge=LEFT)


        self.add(unit_circle, angle)
        self.play(Rotate(H, PI/4, about_point=self.O.get_center()), run_time=1)
        self.wait(0.5)
        self.play(Rotate(H, 1, about_point=self.O.get_center()), run_time=1)
        self.wait(0.5)
        self.play(Rotate(H, 1, about_point=self.O.get_center()), run_time=1)
        self.wait(0.5)
        H.move_to(self.O.get_center()+RIGHT*3)
        def creat_anim(rotate_angle):
            self.play(Rotate(H, rotate_angle, about_point=self.O.get_center()), run_time=rotate_angle, rate_func=linear)

        creat_anim(PI/6)
        self.play(Circumscribe(VGroup(angle[-1], angle[-2])))
        self.wait()
        creat_anim(2*PI/3)
        self.play(Circumscribe(VGroup(angle[-1], angle[-2])))
        self.wait()
        creat_anim(PI+PI/6)
        turn+=1
        creat_anim(PI/6)
        self.play(Circumscribe(VGroup(angle[-1], angle[-2])))
        self.wait()
        creat_anim(2*PI/3)
        self.play(Circumscribe(VGroup(angle[-1], angle[-2])))
        self.wait()
        creat_anim(PI+PI/6)
        turn+=1
        creat_anim(PI/6)
        self.play(Circumscribe(VGroup(angle[-1], angle[-2])))
        self.wait()
        creat_anim(2*PI/3)
        self.play(Circumscribe(VGroup(angle[-1], angle[-2])))
        self.wait()


class Scene4(MyScene):
    def construct(self):
        fomular = MathTex("sin(x)={1 \over 2}", color=RED).scale(1.5).shift(UP*3+LEFT*2)

        source1 = ["...",
                   "{\pi \over 6} + 2\pi",
                  "{\pi \over 6} + 4\pi",
                  "{\pi \over 6} + 6\pi",
                  "{\pi \over 6} + 8\pi",
                  "..."]
        result1 = MathTex("x={\pi \over 6} + k2\pi", color=GREEN)
        source2 = ["...",
                   "{5\pi \over 6} + 2\pi",
                   "{5\pi \over 6} + 4\pi",
                   "{5\pi \over 6} + 6\pi",
                   "{5\pi \over 6} + 8\pi",
                   "..."]
        result2 = MathTex("x={5\pi \over 6} + k2\pi", color=GREEN)

        group1 = VGroup(*[MathTex(i, color=YELLOW) for i in source1]).arrange(DOWN, aligned_edge=LEFT)
        brace1 = Brace(group1, RIGHT)
        result1.next_to(brace1, RIGHT)
        condition1 = MathTex("k\in \mathbb{Z}", color=GREEN).next_to(result1, DOWN, aligned_edge=LEFT)

        group2 = VGroup(*[MathTex(i, color=YELLOW) for i in source2]).arrange(DOWN, aligned_edge=LEFT)
        brace2 = Brace(group1, RIGHT)
        result2.next_to(brace1, RIGHT)
        condition2 = MathTex("k\in \mathbb{Z}", color=GREEN).next_to(result2, DOWN, aligned_edge=LEFT)

        part1 = VGroup(group1, brace1, result1, condition1).shift(LEFT*5+DOWN)
        part2 = VGroup(group2, brace2, result2, condition2).shift(RIGHT*2+DOWN)

        self.play(Write(fomular),
                  LaggedStart(*[FadeIn(i, shift=RIGHT) for i in group1], lag_ratio=0.2),
                  LaggedStart(*[FadeIn(i, shift=RIGHT) for i in group2], lag_ratio=0.2))
        self.wait()
        self.play(FadeIn(brace1, shift=LEFT),
                  FadeIn(brace2, shift=LEFT),
                  FadeIn(result1, shift=LEFT),
                  FadeIn(result2, shift=LEFT),
                  FadeIn(condition1, shift=LEFT),
                  FadeIn(condition2, shift=LEFT))
        self.wait()


class Scene5(MyScene):
    def construct(self):
        group = Group(*[ImageMobject(str(i)).scale(1.1) for i in range(1,7)]).arrange(DOWN, buff=0)
        # group.shift(LEFT*1.4)
        self.play(LaggedStart(*[FadeIn(i, shift=RIGHT) for i in group], lag_ratio=0.2))