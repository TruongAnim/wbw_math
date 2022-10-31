from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9")
SCENE_NAME = list_scene[2]
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
        self.play(Write(ran))
        self.play(Write(first_value))
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

