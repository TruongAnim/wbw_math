import math

from manim import *
import random

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9")
SCENE_NAME = list_scene[3]
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


class Scene0(MyScene):
    def construct(self):
        import random
        from common.utils.color_utils import interpolate_color_range
        ran = MathTex(r"\text{random}(", "0", ",", "1", ") \longrightarrow").scale(1.5).shift(UP + LEFT)
        ran[1].set_color(YELLOW)
        ran[3].set_color(RED)
        list_rand = [0.6404715302525753, 0.4542988583872273, 0.4161880799942135, 0.6337411245598525, 0.349581448236874,
                     0.8310301991771485, 0.8257280156247735, 0.024194002080686006, 0.23833225617200948,
                     0.7370351328115762,
                     0.7008278818280986, 0.4820941891462207, 0.29395250257861627, 0.40836605817292004,
                     0.9084620255657727, 0.17721597164415415, 0.0902734603242028, 0.6138566180452795, 0.592348573135173,
                     0.551363570531275]
        texts = [
            MathTex("{:4f}".format(i), color=interpolate_color_range(YELLOW, RED, i)).scale(1.2).next_to(ran, RIGHT) for
            i in list_rand]
        to_do = Text("Hãy tính sấp xỉ số Pi.", font_size=35, font="Sans", color=GREEN).shift(DOWN)
        first_value = texts[0]
        self.my_play(Write(ran))
        self.my_play(Write(first_value))
        count = 0
        for i in texts[1:]:
            self.play(Transform(first_value, i))
            count += 1
            if count == 3:
                self.play(Write(to_do))


class Scene1(MyScene):
    def construct(self):
        circle = Circle(radius=2, color=TEAL)
        diameter = Line(LEFT * 2, RIGHT * 2, color=RED)
        chuvi = Text("Chu vi", color=TEAL, font="Sans", font_size=25).next_to(circle, UP)
        dk = Text("Đường kính", color=RED, font="Sans", font_size=25).next_to(diameter, UP)
        pi = MathTex("\pi", "=", "{1234567", r"\over", "1234567}", "=3.141592...")
        pi[0].set_color(GREEN)
        pi.next_to(circle, DOWN, buff=MED_LARGE_BUFF)
        self.play(Create(circle), Write(chuvi))
        self.play(Create(diameter), Write(dk))
        self.play(Write(pi[0:2]), Write(pi[3]))
        self.play(chuvi.copy().animate.move_to(pi[2]), dk.copy().animate.move_to(pi[4]))
        self.play(Write(pi[5:]))
        # self.add(circle, diameter, chuvi, dk, pi)


class Scene2(MyScene):
    def construct(self):
        import random
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        P = Dot(RIGHT * 2.3 + UP * 1, color=YELLOW)
        random.seed(9)
        list_x = [random.uniform(0, 1) for _ in range(100)]
        random.seed(2)
        list_y = [random.uniform(0, 1) for _ in range(100)]
        list_point = [Dot(RIGHT * i *3 + UP * j * 3, color=YELLOW) if (i*i+j*j)<=1 else Dot(RIGHT * i *3 + UP * j * 3) for i, j in zip(list_x, list_y)]
        count = 0
        for i, j in zip(list_x, list_y):
            if i*i+j*j <=1:
                count+=1
        print(count)
        sub_circle = main_circle.get_subcurve(0, 0.25)
        sub_circle.add_points_as_corners([ORIGIN, RIGHT*3])
        sub_circle.set_stroke(color=YELLOW, width=2)
        sub_circle.set_fill(color=YELLOW, opacity=0.2)
        square = VMobject(stroke_width=2, stroke_color=WHITE, fill_color=WHITE, fill_opacity=0.2)\
            .set_points_as_corners([ORIGIN, RIGHT*3, UR*3, UP*3, ORIGIN])
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal.get_end(), DOWN)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        brace = Brace(Line(start=ORIGIN, end=RIGHT * 3), DOWN, buff=SMALL_BUFF, color=GREEN)
        brace_t = brace.get_tex("1")
        brace_t.set_color(GREEN)
        brace2 = Brace(Line(start=ORIGIN, end=UP * 3), LEFT, buff=SMALL_BUFF, color=GREEN)
        brace2_t = brace2.get_tex("1")
        brace2_t.set_color(GREEN)
        group = VGroup(main_circle, vertical, horizontal, O, O_t, x_t, y_t, brace, brace2, brace_t, brace2_t, P,
                       *list_point, sub_circle, square).shift(LEFT * 3.5)
        x = MathTex("x", "=", "random(0, 1)").shift(RIGHT * 3 + UP * 2)
        y = MathTex("y", "=", "random(0, 1)").next_to(x, DOWN, aligned_edge=LEFT)
        A = MathTex("A", "(", "x", ",", "y", ")").next_to(y, DOWN, aligned_edge=LEFT)
        color_map = {
            "x": ORANGE,
            "y": RED,
            "A": YELLOW
        }
        for i in (x, y, A):
            i.set_color_by_tex_to_color_map(color_map)
        formula1 = MathTex(r"{\text{Điểm màu vàng} \over \text{Tổng số điểm}} \approx", tex_template=myTemplate)
        formula2 = MathTex("{S_", "{a}", "\over", "S_", "{a}}").next_to(formula1, RIGHT)
        formula3 = MathTex(r"={1 ^{2} \times \pi \backslash 4", "\over", "1^{2}}=").next_to(formula2, RIGHT)
        formula4 = MathTex("\pi \over 4").next_to(formula3, RIGHT)
        formula5 = MathTex(r"\rightarrow \pi \approx", r"{\text{Điểm màu vàng} \over \text{Tổng số điểm}}", r"\approx {78\over 100} \times 4", r"\approx 3.12", tex_template=myTemplate).next_to(formula1, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        group_2 = VGroup(formula1, formula2, formula3, formula4, formula5).scale(0.75).shift(RIGHT*1+UP*2)
        small_circle = sub_circle.copy().scale(0.06).move_to(formula2[1])
        small_square = square.copy().scale(0.06).move_to(formula2[4])
        self.my_play(Create(horizontal), Create(vertical), Write(O_t), Create(O), Write(x_t), Write(y_t))
        self.my_play(Create(main_circle), FadeIn(brace, shift=UP), FadeIn(brace_t, shift=UP),
                  FadeIn(brace2_t, shift=RIGHT), FadeIn(brace2, shift=RIGHT))
        self.my_play(Write(x), Write(y))
        self.my_play(Write(A[0:2]), Write(A[3]), Write(A[5]))
        self.my_play(ReplacementTransform(x[0].copy(), A[2]), ReplacementTransform(y[0].copy(), A[4]))
        self.my_play(Transform(A.copy(), P))
        self.play(LaggedStart(*[Transform(A.copy(), i) for i in list_point], lag_ratio=0.05))
        self.my_play(FadeOut(x), FadeOut(y), FadeOut(A))
        self.my_play(Write(formula1))
        self.play(DrawBorderThenFill(sub_circle))
        self.my_play(Write(formula2[0]), Transform(sub_circle.copy(), small_circle))
        self.play(DrawBorderThenFill(square))
        self.my_play(Write(formula2[2:4]), Transform(square.copy(), small_square))
        self.play(Write(formula3))
        self.play(Write(formula4))
        self.wait(0.5)
        self.my_play(Write(formula5))
        self.my_play(Circumscribe(formula5[-1]))


class Scene3(MyScene):
    def construct(self):
        import random
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        a = Dot(RIGHT * 2.2 + UP * 1.3, color=YELLOW)
        a_t = MathTex("A", color=YELLOW).scale(0.7).next_to(a, RIGHT, buff=SMALL_BUFF)
        b = Dot(RIGHT * 1.9 + UP * 2.6, color=RED)
        b_t = MathTex("B", color=RED).scale(0.7).next_to(b, RIGHT, buff=SMALL_BUFF)
        A = VGroup(a, a_t)
        B = VGroup(b, b_t)
        sub_circle = main_circle.get_subcurve(0, 0.25)
        sub_circle.add_points_as_corners([ORIGIN, RIGHT*3])
        sub_circle.set_stroke(color=YELLOW, width=2)
        sub_circle.set_fill(color=YELLOW, opacity=0.2)
        square = VMobject(stroke_width=2, stroke_color=WHITE, fill_color=WHITE, fill_opacity=0.2)\
            .set_points_as_corners([ORIGIN, RIGHT*3, UR*3, UP*3, ORIGIN])
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal.get_end(), DOWN)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        brace = Brace(Line(start=ORIGIN, end=RIGHT * 3), DOWN, buff=SMALL_BUFF, color=GREEN)
        brace_t = brace.get_tex("1")
        brace_t.set_color(GREEN)
        brace2 = Brace(Line(start=ORIGIN, end=UP * 3), LEFT, buff=SMALL_BUFF, color=GREEN)
        brace2_t = brace2.get_tex("1")
        brace2_t.set_color(GREEN)
        group = VGroup(main_circle, vertical, horizontal, O, O_t, x_t, y_t, brace, brace2, brace_t, brace2_t, A, B,
                       sub_circle, square).shift(LEFT * 3.5)
        A_t = MathTex("A(0.73, 0.43)", color=YELLOW).shift(RIGHT*2+UP*2)
        OA = Line(O.get_center(), a.get_center(), color=YELLOW)
        OA_t = MathTex("OA = \sqrt{0.73^2+0.43^2}=", "0.85", color=YELLOW).next_to(A_t, DOWN, aligned_edge=LEFT)
        B_t = MathTex("B(0.63, 0.86)", color=RED).next_to(OA_t, DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)
        OB = Line(O.get_center(), b.get_center(), color=RED)
        OB_t = MathTex("OB = \sqrt{0.63^2+0.86^2}=", "1.07", color=RED).next_to(B_t, DOWN, aligned_edge=LEFT)
        self.play(Create(horizontal), Create(vertical), Write(O_t), Create(O), Write(x_t), Write(y_t))
        self.play(Create(main_circle), FadeIn(brace, shift=UP), FadeIn(brace_t, shift=UP),
                     FadeIn(brace2_t, shift=RIGHT), FadeIn(brace2, shift=RIGHT))
        self.my_play(Write(A_t), Write(B_t))
        self.my_play(LaggedStart(Transform(A_t.copy(), A), Transform(B_t.copy(), B), lag_ratio=0.5))
        self.my_play(Create(OA), Write(OA_t))
        self.my_play(Create(OB), Write(OB_t))
        self.my_play(Wiggle(OA_t[-1], scale_value=1.5))
        self.my_play(Wiggle(OB_t[-1], scale_value=1.5))
        # self.add(group, OA, OA_t, A_t, B_t, OB_t, OB)


rel_obj = 500000
rel_time = 20
test_obj = 100
test_time = 3


class Scene4(MyScene):
    def get_random_position(self):
        x = random.uniform(0, 5)
        y = random.uniform(0, 5)
        return np.array([x, y, 0])

    def construct(self):
        random.seed(1)
        shape = Circle(radius=5, stroke_width=3, stroke_color=YELLOW).shift(DOWN*2.5).get_subcurve(0, 0.25)
        square = Square(side_length=5, stroke_color=WHITE, stroke_width=3).shift(RIGHT*2.5)
        brace1 = Brace(square, DOWN)
        side1 = brace1.get_tex("1")
        brace2 = Brace(square, LEFT)
        side2 = brace2.get_tex("1")

        vertical = Arrow(start=square.point_from_proportion(0.5)+LEFT, end=square.point_from_proportion(0.75)+RIGHT, stroke_width=1)
        horizontal = Arrow(start=square.point_from_proportion(0.5)+DOWN, end=square.point_from_proportion(0.25)+UP, stroke_width=1)

        self.my_play(Create(vertical), Create(horizontal))
        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace1, shift=UP), FadeIn(side1, shift=UP), FadeIn(brace2, shift=RIGHT), FadeIn(side2, shift=RIGHT))

        formula = MathTex(
            r"\pi",  # 0
            r"\approx",  # 1
            r"{\text{aaaaaaaa}",  # 2
            r"\over",  # 3
            r"\text{aaaaaaaa}}",  # 4
            r"\times",  # 5
            r"4",  # 6
        ).scale(1.2).shift(LEFT * 4.7)
        for i in (2, 4):
            formula[i].set_color(BLACK)

        formula[0].set_color(RED)
        formula2 = formula[1].copy().shift(DOWN*1.5)

        real_pi = Text("{:.10f}...".format(math.pi),
                     color=GREEN,
                     font_size=35,
                     font="Arial") \
                .next_to(formula2, RIGHT, aligned_edge=LEFT, buff=MED_LARGE_BUFF)\
            .shift(DOWN)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(formula2),
            Write(real_pi)
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=YELLOW,
                             font_size=35,
                             font="Arial") \
                .move_to(formula[2])
            dot_total = Text(str(self.num_dot),
                             color=WHITE,
                             font_size=35,
                             font="Arial") \
                .move_to(formula[4])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(4 * self.num_green / self.num_dot)
            s = Text(result,
                     color=RED,
                     font_size=35,
                     font="Arial") \
                .next_to(formula2, RIGHT, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)
        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    p = self.get_random_position()
                    # dot = Square(side_length=0.01, stroke_width=2).move_to(p+DOWN*2.5)
                    if p[0]*p[0]+p[1]*p[1]<25:
                        # dot.set_color(YELLOW)
                        self.num_green += 1
                    else:
                        # dot.set_color(WHITE)
                        pass
                    # self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(rel_obj),
                  run_time=rel_time,
                  rate_func=linear)
        self.play(Circumscribe(group[2]))
