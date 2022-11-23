import random

from manim import *
from common.custom.custom_mobject import SetNumber
from common.custom.custom_mobject import TextTranslation

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8")
SCENE_NAME = list_scene[6]
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
        self.wait(0.5)


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Scene0(MyScene):
    def construct(self):
        def random_point(group, buff, seed):
            random.seed(seed)
            for i in group:
                shift = UP * random.uniform(0, buff) \
                        + DOWN * random.uniform(0, buff) \
                        + LEFT * random.uniform(0, buff) \
                        + RIGHT * random.uniform(0, buff)
                i.shift(shift)

        nature_color = GREEN
        even_color = RED
        list_nature = ["0", "1", "2", "3", "4", "..."]
        nature_group = VGroup(*[MathTex(i, color=nature_color).scale(1.5) for i in list_nature]) \
            .arrange_in_grid(5, 2, buff=1)
        random_point(nature_group, 0.4, 2)
        nature_set = SetNumber(nature_group, "Số tự nhiên", 4, 6, 40, nature_color).shift(LEFT * 2)

        list_even = ["0", "2", "4", "6", "8", "..."]
        even_group = VGroup(*[MathTex(i, color=even_color).scale(1.5) for i in list_even]) \
            .arrange_in_grid(5, 2, buff=1)
        random_point(even_group, 0.4, 2)
        even_set = SetNumber(even_group, "Số chẵn", 4, 6, 40, even_color).to_edge(RIGHT, buff=LARGE_BUFF)

        nature_set.scale(0.8).shift(UP)
        even_set.scale(0.8).shift(UP)

        infinity1 = Text("(Vô hạn)", font=("Sans"), font_size=32, color=YELLOW).next_to(nature_set[1], RIGHT)
        infinity2 = infinity1.copy().next_to(even_set[1], RIGHT)

        result1 = nature_set[1].copy().to_edge(DOWN)
        result2 = MathTex("=").scale(2).next_to(result1, RIGHT)
        result3 = even_set[1].copy().next_to(result2, RIGHT)
        result4 = MathTex("=").scale(2).next_to(result3, RIGHT)
        result5 = infinity1.copy().next_to(result4, RIGHT)
        # self.add(even_set, nature_set, infinity1, infinity12,
        #          result1, result2, result3, result4, result5)
        self.play(Write(nature_set))
        self.play(Write(infinity1))
        self.play(Write(even_set))
        self.play(Write(infinity2))

        self.play(Transform(nature_set[1].copy(), result1))
        self.play(Transform(even_set[1].copy(), result3))
        self.play(FadeIn(result2, shift=UP), FadeIn(result4, shift=UP))
        self.play(Transform(infinity1.copy(), result5), Transform(infinity2.copy(), result5))
        self.wait()


class Scene1(MyScene):
    def construct(self):
        def create_square(i):
            number = MathTex(str(i), color=GREEN).scale(1.5)
            square = Square(color=GREEN, side_length=0.7).move_to(number)
            return VGroup(number, square)

        nature_number = Text("Số tự nhiên", font_size=40, font="Sans", color=GREEN).to_edge(LEFT)
        even_number = Text("Số chẵn", font_size=40, font="Sans", color=RED)
        odd_number = Text("Số lẻ", font_size=40, font="Sans", color=BLUE)
        arrow = MathTex(r"\rightarrow").next_to(nature_number, RIGHT)
        nature_list = VGroup(*[create_square(i) for i in range(10)]).arrange(RIGHT, buff=0.1).next_to(arrow, RIGHT)
        dots = MathTex(r"\dots", color=GREEN).next_to(nature_list, RIGHT)

        even_number.to_edge(UP)
        even_arrow = VGroup(
            *[Arrow(even_number.get_corner(DL) + RIGHT * 0.2 * i, nature_list[i].get_top()) for i in range(0, 10, 2)])
        odd_number.to_edge(DOWN)
        odd_arrow = VGroup(
            *[Arrow(odd_number.get_corner(UL) + RIGHT * 0.2 * i, nature_list[i].get_bottom()) for i in range(1, 10, 2)])
        # self.add(nature_number, nature_list, dots, arrow,
        #          even_arrow, even_number, odd_arrow, odd_number)

        self.play(
            LaggedStart(*[FadeIn(i, shift=UP) for i in (nature_number, arrow, *nature_list, dots)], lag_ratio=0.1))
        self.play(FadeIn(even_number, shift=DOWN),
                  LaggedStart(*[GrowArrow(i) for i in even_arrow], lag_ratio=0.2),
                  LaggedStart(*[nature_list[i].animate.set_color(RED) for i in range(0, 10, 2)], lag_ratio=0.2))
        self.wait()
        self.play(FadeIn(odd_number, shift=UP),
                  LaggedStart(*[GrowArrow(i) for i in odd_arrow], lag_ratio=0.2),
                  LaggedStart(*[nature_list[i].animate.set_color(BLUE) for i in range(1, 10, 2)], lag_ratio=0.2))
        self.wait()


class Scene2(MyScene):
    def construct(self):
        nature_number = TextTranslation(text_u="Vô hạn", text_d="Số tự nhiên",
                                        font_u="Sans", font_d="Sans",
                                        font_size_u=35, font_size_d=35,
                                        color_u=YELLOW, color_d=GREEN).shift(LEFT * 3)
        even_number = TextTranslation(text_u="Vô hạn", text_d="Số chẵn",
                                      font_u="Sans", font_d="Sans",
                                      font_size_u=35, font_size_d=35,
                                      color_u=YELLOW, color_d=RED).shift(RIGHT * 3)

        nature_number[0].add_updater(lambda b: b.next_to(nature_number[1], UP))
        bigger = MathTex(">").scale(4).shift(UP * 0.5 + RIGHT)
        # self.add(nature_number, even_number)
        self.my_play(FadeIn(nature_number, shift=UP), FadeIn(even_number, shift=UP))
        self.my_play(nature_number[0].animate.scale(4), FadeIn(bigger, shift=UP))


class Scene3(MyScene):
    def construct(self):
        color = TEAL
        list_object = [Square(), Triangle(), Rectangle().scale(0.8), Star()]
        nature_group = VGroup(*[i.scale(0.5).set_color(color) for i in list_object]) \
            .arrange_in_grid(5, 2, buff=0.5)
        temp_set = SetNumber(nature_group, "Tập hợp A", 4, 5, 40, color).shift(LEFT * 2)

        card = TextTranslation(text_u="Lực lượng", text_d="(Cardinality)",
                               font_u="Sans", font_d="",
                               font_size_u=50, font_size_d=40,
                               color_u=YELLOW, color_d=RED).shift(RIGHT * 3 + UP * 1)
        denoted = Text("Kí hiệu", font="Sans", font_size=35, color=GREEN).next_to(card, DOWN, buff=1)
        denoted2 = MathTex(r"\left| A \right| = 4 \text{ hoặc } n(A) = 4", color=GREEN,
                           tex_template=myTemplate).next_to(denoted, DOWN)
        numbers = VGroup(*[MathTex(str(i + 1)).move_to(list_object[i].get_center()) for i in range(4)])
        # self.add(temp_set, card, denoted, denoted2, numbers)
        self.play(Write(temp_set))
        self.play(FadeIn(card[0], shift=RIGHT), FadeIn(card[1], shift=LEFT))
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in numbers]))
        self.play(Write(denoted), Write(denoted2))
        self.wait()


class Scene4(MyScene):
    def construct(self):
        chair = SVGMobject("chair").scale(0.5)
        student = SVGMobject("student").scale(0.5)

        def get_chair():
            return chair.copy()

        list_chair = VGroup(*[get_chair() for i in range(10)]).arrange_in_grid(2, 5)
        chairs = SetNumber(list_chair, "Tập hợp A", elip_width=5, elip_height=3, font_size=40, text_color=GREEN,
                           use_elip=False).shift(LEFT * 3 + UP)
        card_A = Text("10 chiếc ghế", font="Sans", font_size=35, color=GREEN).next_to(chairs, DOWN)

        def get_student():
            return student.copy()

        list_student = VGroup(*[get_student() for i in range(10)]).arrange_in_grid(2, 5)
        students = SetNumber(list_student, "Tập hợp B", elip_width=5, elip_height=3, font_size=40, text_color=RED,
                             use_elip=False).shift(RIGHT * 3 + UP)
        card_B = Text("10 học sinh", font="Sans", font_size=35, color=RED).next_to(students, DOWN)
        result = MathTex(r"\rightarrow ", "n(A)", "=", "n(B)", "=10").scale(1.5).to_edge(DOWN)
        result[1].set_color(GREEN)
        result[3].set_color(RED)
        self.my_play(FadeIn(chairs), Write(card_A))
        self.my_play(FadeIn(students), Write(card_B))
        self.my_play(Write(result))
        # self.add(chairs, students, card_B, card_A, result)


class Scene5(MyScene):
    def construct(self):
        chair = SVGMobject("chair").scale_to_fit_width(0.27).stretch_to_fit_height(0.45)
        student = SVGMobject("student").scale_to_fit_width(0.27).stretch_to_fit_height(0.45)

        def get_chair():
            return chair.copy()

        list_chair = VGroup(*[get_chair() for i in range(70)]).arrange_in_grid(7, 10)
        chairs = SetNumber(list_chair, "Tập hợp A", elip_width=5.7, elip_height=5.5, font_size=40, text_color=GREEN,
                           use_elip=False).shift(LEFT * 3 + UP)
        card_A = Text("10 chiếc ghế", font="Sans", font_size=35, color=GREEN).next_to(chairs, DOWN)

        def get_student():
            return student.copy()

        list_student = VGroup(*[get_student() for i in range(70)]).arrange_in_grid(7, 10)
        students = SetNumber(list_student, "Tập hợp B", elip_width=5.7, elip_height=5.5, font_size=40, text_color=RED,
                             use_elip=False).shift(RIGHT * 3 + UP)
        card_B = Text("10 học sinh", font="Sans", font_size=35, color=RED).next_to(students, DOWN)
        result = MathTex(r"\rightarrow ", "n(A)", "=", "n(B)").scale(1.5).to_edge(DOWN)
        result[1].set_color(GREEN)
        result[3].set_color(RED)
        # self.add(chairs, students, card_B, card_A, result)
        self.my_play(FadeIn(chairs, shift=UP), FadeIn(students, shift=UP))
        old_coord = list_student.get_center()
        self.play(list_student.animate.move_to(list_chair.get_center() + RIGHT * 0.1))
        self.play(LaggedStart(*[Wiggle(i, scale_value=1.3) for i in list_student], lag_ratio=0.01))
        self.play(list_student.animate.move_to(old_coord))
        self.my_play(Write(result))


class Scene6(MyScene):
    def construct(self):
        numbers = [i for i in range(1, 6)]
        chars = ["A", "B", "C", "D", "E"]
        list_numbers = VGroup(*[MathTex(str(i)) for i in numbers]).arrange(DOWN, buff=MED_LARGE_BUFF)
        set1 = SetNumber(list_numbers, "Tập hợp A", elip_width=3, elip_height=5, font_size=40, text_color=GREEN,
                         use_elip=True).shift(LEFT * 3 + UP)

        list_chars = VGroup(*[MathTex(i) for i in chars]).arrange(DOWN, buff=MED_LARGE_BUFF)
        set2 = SetNumber(list_chars, "Tập hợp B", elip_width=3, elip_height=5, font_size=40, text_color=RED,
                         use_elip=True).shift(RIGHT * 3 + UP)

        result = MathTex(r"\rightarrow ", "n(A)", "=", "n(B)").scale(1.5).to_edge(DOWN)
        result[1].set_color(GREEN)
        result[3].set_color(RED)
        arrows = [Arrow(i, j, stroke_width=4) for i, j in zip(list_numbers, list_chars)]
        self.my_play(FadeIn(set1, shift=RIGHT), FadeIn(set2, shift=LEFT))
        self.play(LaggedStart(*[GrowArrow(i) for i in arrows], lag_ratio=0.5))
        self.my_play(Write(result))
        # self.add(chairs, students, card_B, card_A, result)
