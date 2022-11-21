from manim import *
from common.custom.custom_mobject import TextTranslation
from common.custom.custom_mobject import Explain

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Thumbnail")
SCENE_NAME = list_scene[-1]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -s -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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


class Thumbnail(MyScene):
    def construct(self):
        square = Square(side_length=6, color=GREEN, stroke_width=10)
        square_t1 = MathTex("1", color=GREEN).scale(2).next_to(square, DOWN)
        square_t2 = MathTex("1", color=GREEN).scale(2).next_to(square, LEFT)
        hypotenus = Line(square.point_from_proportion(0.25), square.point_from_proportion(0.75), color=YELLOW, stroke_width=10)
        root_of_2 = MathTex("\sqrt{2}", color=YELLOW).scale(2).next_to(hypotenus.get_center(), UP).shift(RIGHT * 0.3)
        square_group = VGroup(square.get_subcurve(0.25, 0.75), square_t1, square_t2, root_of_2, hypotenus).shift(LEFT * 3)
        root_of_20 = MathTex("\sqrt{2}", "=").to_edge(UP).shift(LEFT*3)
        root_of_20[0].set_color(YELLOW)
        root_of_22 = MathTex("=", "1.414213562373...").scale(2).next_to(root_of_2, RIGHT)
        brace = Brace(root_of_22[1], DOWN)
        text = Text("Dài vô tận", font='Sans', font_size=70, color=GREEN).next_to(brace, DOWN)
        self.add(square_group, root_of_22, text, brace)
        self.wait()


class Scene0(MyScene):
    def construct(self):
        title = TextTranslation(text_u="Số hữu tỉ", text_d="Rational number").to_corner(UP)
        content = MathTex(r"R={ a \over b}")
        condition = MathTex(r"(a,b)\in \mathbb{Z}").next_to(content, RIGHT)
        content_group = VGroup(content, condition).shift(UP).move_to(UP * 1.5)
        example_t = Text("Ví dụ:", font="Sans", color=GREEN, font_size=35).shift(LEFT * 3)
        example1 = MathTex(r"3={ 3 \over 1}")
        example2 = MathTex(r"1.25={ 5 \over 4}")
        example3 = MathTex(r"0.2468={ 617 \over 2500}")
        example4 = MathTex(r"...")
        example_group = VGroup(example1, example2, example3, example4).arrange(DOWN, aligned_edge=LEFT).shift(
            DOWN * 1.5)
        example_group.set_color_by_gradient(GREEN, TEAL)
        self.my_play(Write(title))
        self.my_play(Write(content_group))
        self.my_play(Write(example_t))
        for i in example_group:
            self.my_play(Write(i))
        self.add(title, content_group, example_t, example_group)


class Scene1(MyScene):
    def construct(self):
        title = TextTranslation(text_u="Số vô tỉ", text_d="Irrational number").to_corner(UP)
        content = MathTex(r"\pi", ",", r"\sqrt{2}", r"\neq ", r"{ a \over b}")
        content[0].set_color(TEAL)
        content[2].set_color(YELLOW)

        condition = MathTex(r"(a,b)\in \mathbb{Z}").next_to(content, RIGHT)
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
        root_of_2 = MathTex("\sqrt{2}", color=YELLOW).next_to(hypotenus.get_center(), DOWN).shift(LEFT * 0.2)
        square_group = VGroup(square, square_t1, square_t2, root_of_2, hypotenus).shift(DOWN + RIGHT * 4)

        pi = MathTex("\pi=").move_to(circle.get_corner(DR))
        pi[0][0].set_color(TEAL)
        line = Line(LEFT, RIGHT).next_to(pi, RIGHT)
        numerator = circle_t.copy().next_to(line, UP)
        dinominator = diameter_t.copy().next_to(line, DOWN)
        pi_group = VGroup(pi, line, numerator, dinominator)

        self.my_play(FadeIn(circle_group, shift=UP), FadeIn(pi_group, shift=UP))
        self.my_play(FadeIn(square_group, shift=UP))

        self.my_play(Transform(pi[0][0].copy(), content[0]),
                  Transform(root_of_2.copy(), content[2]))
        self.my_play(Write(content[1]), Write(content[3:]), Write(condition))
        self.my_play(Write(title))
        self.my_play(Indicate(content[3]))

        self.add(title, content_group, circle_group, square_group, pi_group)


class Scene2(MyScene):
    def construct(self):
        assumption1 = MathTex(r"\sqrt{2}", "=", "{ p", r"\over", "q }")
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
        self.my_play(FadeIn(rec_group[0], shift=LEFT*2))
        self.my_play(FadeIn(rec_group[1], shift=LEFT*2))

        formula1 = MathTex(r"\sqrt{2}", "=", "{ p", r"\over", "q }")
        formula2 = MathTex(r"\sqrt{2}", "q", "=", "p")
        formula3 = MathTex("2", "q", "^{2}", "=", "p", "^{2}")
        formula4 = MathTex("2", "q", "^{2}", "=", "(", "2", "a", ")", "^{2}")
        formula5 = MathTex("2", "q", "^{2}", "=", "4", "a", "^{2}")
        formula6 = MathTex("q", "^{2}", "=", "2", "a", "^{2}")
        formula_group = VGroup(formula1, formula2, formula3, formula4, formula5, formula6).scale(2.5).shift(LEFT * 2)

        def get_func(f, p1, p2):
            if f == 0:
                return ReplacementTransform(p1, p2)
            if f == 1:
                return FadeOut(p1)
            if f == 2:
                return FadeIn(p2)

        transform1 = [(0, 0, 0), (0, 1, 2), (0, 2, 3), (1, 3, -1), (0, 4, 1)]
        transform2 = [(0, 0, 0), (0, 1, 1), (0, 2, 3), (0, 3, 4), (2, -1, 2), (2, -1, 5)]
        transform3 = [(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 5, 8), (1, 4, -1), (2, -1, 4), (2, -1, 5),
                      (2, -1, 6), (2, -1, 7)]
        transform4 = [(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 4, -1), (0, 5, 4), (0, 6, 5), (1, 7, -1),
                      (0, 8, 6)]
        transform5 = [(1, 0, -1), (0, 1, 0), (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 5, 4), (0, 6, 5)]

        explain1 = Explain(formula3[:3], "Dạng 2c -> số chẵn", location=UP * 3 + LEFT * 5)
        explain2 = Explain(formula3[4:], "Số chẵn", location=DOWN * 3 + RIGHT * 2)
        explain3 = Explain(formula6[3:], "Dạng 2c -> số chẵn", location=UP * 3 + RIGHT*0.5)
        explain4 = Explain(formula6[:2], "Số chẵn", location=DOWN * 3 + LEFT * 5)
        curve_arrow1 = CurvedArrow(rec_group[2].get_left(), rec_group[4].get_left(), radius=1.5)
        curve_arrow2 = CurvedArrow(rec_group[3].get_left(), rec_group[4].get_left(), radius=1)

        self.my_play(ReplacementTransform(assumption1.copy(), formula1))
        self.my_play(*[get_func(f, formula1[p1], formula2[p2]) for f, p1, p2 in transform1])
        self.my_play(*[get_func(f, formula2[p1], formula3[p2]) for f, p1, p2 in transform2])
        self.my_play(Write(explain1))
        self.my_play(Write(explain2))
        self.my_play(FadeIn(rec_group[2], shift=LEFT*2))
        self.my_play(FadeOut(explain1), FadeOut(explain2))
        self.my_play(*[get_func(f, formula3[p1], formula4[p2]) for f, p1, p2 in transform3])
        self.my_play(*[get_func(f, formula4[p1], formula5[p2]) for f, p1, p2 in transform4])
        self.my_play(*[get_func(f, formula5[p1], formula6[p2]) for f, p1, p2 in transform5])
        self.my_play(Write(explain3))
        self.my_play(Write(explain4))
        self.my_play(FadeIn(rec_group[3], shift=LEFT*2))
        self.my_play(FadeOut(explain3), FadeOut(explain4))
        self.my_play(Create(curve_arrow1), Create(curve_arrow2))
        self.my_play(FadeIn(rec_group[4], shift=LEFT*2))
        self.my_play(rec5.animate.set_fill(color=RED), rec2.animate.set_fill(color=RED), rate_func=there_and_back)
        self.my_play(rec5.animate.set_fill(color=RED), rec2.animate.set_fill(color=RED), rate_func=there_and_back)
        self.my_play(rec5.animate.set_fill(color=RED), rec2.animate.set_fill(color=RED), rate_func=there_and_back)
        self.my_play(rec5.animate.set_fill(color=RED), rec2.animate.set_fill(color=RED), rate_func=there_and_back)
        self.my_play(rec5.animate.set_fill(color=RED), rec2.animate.set_fill(color=RED))
        # self.add(formula_group)


class Scene3(MyScene):
    def construct(self):
        square = Square(side_length=4, color=GREEN)
        square_t1 = MathTex("1", color=GREEN).next_to(square, DOWN)
        square_t2 = MathTex("1", color=GREEN).next_to(square, LEFT)
        hypotenus = Line(square.point_from_proportion(0.25), square.point_from_proportion(0.75), color=YELLOW)
        root_of_2 = MathTex("\sqrt{2}", color=YELLOW).next_to(hypotenus.get_center(), DOWN).shift(LEFT * 0.2)
        square_group = VGroup(square, square_t1, square_t2, root_of_2, hypotenus).shift(DOWN + LEFT * 4.5)
        root_of_20 = MathTex("\sqrt{2}", "=").to_edge(UP).shift(LEFT*3)
        root_of_20[0].set_color(YELLOW)
        root_of_22 = MathTex("1.41421356237309504880168872420969807856967")
        root_of_23 = MathTex("1875376948073176679737990732478462107038850")
        root_of_24 = MathTex("3875343276415727350138462309122970249248360")
        root_of_25 = MathTex("5585073721264412149709993583141322266592750")
        root_of_26 = MathTex("5592755799950501152782060571470109559971605")
        root_of_27 = MathTex("9702745345968620147285174186408891986095523")
        root_of_28 = MathTex("2923048430871432145083976260362799525140798")
        root_of_29 = MathTex("9687253396546331808829640620615258352395054")
        root_of_30 = MathTex("7457502877599617298355752203375318570113543")
        root_of_31 = MathTex("7460340849884716038689997069900481503054402")
        root_of_32 = MathTex("77903164542478230684929369186215805784.....")

        root_group = VGroup(root_of_22, root_of_23, root_of_24, root_of_25, root_of_26, root_of_27,
                            root_of_28, root_of_29, root_of_30, root_of_31, root_of_32).scale(0.8).arrange(DOWN, aligned_edge=LEFT)\
            .next_to(root_of_20[1], RIGHT, aligned_edge=UP).shift(UP*0.2)
        self.my_play(FadeIn(square, shift=UP), FadeIn(square_t1, shift=UP), FadeIn(square_t2, shift=RIGHT))
        self.my_play(Create(hypotenus), FadeIn(root_of_2, shift=UP))
        self.my_play(Transform(root_of_2.copy(), root_of_20[0]), Write(root_of_20[1]))
        for i in root_group:
            self.play(AddTextLetterByLetter(i[0]))
        self.wait()