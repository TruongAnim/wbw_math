from manim import *
from common.custom.custom_mobject import TextTranslation

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3")
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
        title = TextTranslation(text_u="Số hữu tỉ", text_d="Rational number").to_corner(UP)
        content = MathTex(r"R={ a \over b}")
        condition = MathTex(r"(a,b)\in N^{*}").next_to(content, RIGHT)
        content_group = VGroup(content, condition).shift(UP).move_to(UP * 1.5)
        example_t = Text("Ví dụ:", font="Sans", color=GREEN, font_size=35).shift(LEFT * 3)
        example1 = MathTex(r"3={ 3 \over 1}")
        example2 = MathTex(r"1.25={ 5 \over 4}")
        example3 = MathTex(r"0.2468={ 617 \over 2500}")
        example4 = MathTex(r"...")
        example_group = VGroup(example1, example2, example3, example4).arrange(DOWN, aligned_edge=LEFT).shift(
            DOWN * 1.5)
        example_group.set_color_by_gradient(GREEN, TEAL)
        self.play(Write(title))
        self.play(Write(content_group))
        self.play(Write(example_t))
        self.play(Write(example_group))
        self.add(title, content_group, example_t, example_group)


class Scene1(MyScene):
    def construct(self):
        title = TextTranslation(text_u="Số vô tỉ", text_d="Irrational number").to_corner(UP)
        content = MathTex(r"\pi", ",", r"\sqrt{2}", r"\neq ", r"{ a \over b}")
        content[0].set_color(TEAL)
        content[2].set_color(YELLOW)

        condition = MathTex(r"(a,b)\in N^{*}").next_to(content, RIGHT)
        content_group = VGroup(content, condition).shift(UP).move_to(UP * 1.5)

        circle = Circle(radius=2, color=RED)
        diameter = Line(LEFT * 2, RIGHT * 2, color=BLUE)
        circle_t = Text("Chu vi", font_size=30, font="Sans", color=RED).next_to(circle, DOWN)
        diameter_t = Text("Đường kính", font_size=30, font="Sans", color=BLUE).next_to(diameter, UP)
        circle_group = VGroup(circle, circle_t, diameter, diameter_t).shift(DOWN + LEFT * 4)

        square = Square(side_length=4, color=GREEN)
        square_t1 = MathTex("1", color=GREEN).next_to(square, DOWN)
        square_t2 = MathTex("1", color=GREEN).next_to(square, LEFT)
        hypotenus = Line(square.point_from_proportion(0.25), square.point_from_proportion(0.75), color=YELLOW)
        root_of_2 = MathTex("\sqrt{2}", color=YELLOW).next_to(hypotenus.get_center(), DOWN).shift(LEFT*0.2)
        square_group = VGroup(square, square_t1, square_t2, root_of_2, hypotenus).shift(DOWN + RIGHT * 4)

        pi = MathTex("\pi=").move_to(circle.get_corner(DR))
        pi[0][0].set_color(TEAL)
        line = Line(LEFT, RIGHT).next_to(pi, RIGHT)
        numerator = circle_t.copy().next_to(line, UP)
        dinominator = diameter_t.copy().next_to(line, DOWN)
        pi_group = VGroup(pi, line, numerator, dinominator)

        self.play(FadeIn(circle_group, shift=UP), FadeIn(pi_group, shift=UP))
        self.play(FadeIn(square_group, shift=UP))

        self.play(Transform(pi[0][0].copy(), content[0]),
                  Transform(root_of_2.copy(), content[2]))
        self.play(Write(content[1]), Write(content[3:]), Write(condition))
        self.play(Write(title))
        self.play(Indicate(content[3]))

        self.add(title, content_group, circle_group, square_group, pi_group)


class Scene2(MyScene):
    def construct(self):
        assumption1 = MathTex("\sqrt{2}={ p \over q }")
        assumption2 = VGroup(
            MathTex(r"p, q \text{ không có}", tex_template=myTemplate),
            MathTex(r"\text{ước chung}", tex_template=myTemplate)
        ).arrange(DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)
        assumption3 = MathTex(r"p \text{ là số chẵn}", tex_template=myTemplate)
        assumption4 = MathTex(r"q \text{ là số chẵn}", tex_template=myTemplate)
        assumption5 = VGroup(
            MathTex(r"p, q \text{ có}", tex_template=myTemplate),
            MathTex(r"\text{ước chung là 2}", tex_template=myTemplate)
        ).arrange(DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)
        assumption_group = VGroup(assumption1, assumption2, assumption3, assumption4, assumption5)
        rec1 = Rectangle(width=3.5, height=1.3, fill_color=GREEN_D, fill_opacity=1).move_to(assumption1)
        rec2 = Rectangle(width=3.5, height=1.3, fill_color=GREEN_D, fill_opacity=1).move_to(assumption2)
        rec3 = Rectangle(width=3.5, height=1.3, fill_color=GREEN_D, fill_opacity=1).move_to(assumption3)
        rec4 = Rectangle(width=3.5, height=1.3, fill_color=GREEN_D, fill_opacity=1).move_to(assumption4)
        rec5 = Rectangle(width=3.5, height=1.3, fill_color=GREEN_D, fill_opacity=1).move_to(assumption5)
        rec_group = VGroup(VGroup(rec1, assumption1),
                           VGroup(rec2, assumption2),
                           VGroup(rec3, assumption3),
                           VGroup(rec4, assumption4),
                           VGroup(rec5, assumption5)
                           ).arrange(DOWN, aligned_edge=LEFT, buff=SMALL_BUFF).to_edge(RIGHT)
        self.add(rec_group)