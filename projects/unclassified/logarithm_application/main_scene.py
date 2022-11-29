from manim import *
from common.custom.custom_mobject import TextTranslation

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
SCENE_NAME = list_scene[2]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{vntex}")


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


class Scene0(MyScene):
    def construct(self):
        lt = TextTranslation("Lũy thừa", "(Exponentiation)", font_u="Sans",
                             color_u=YELLOW, color_d=RED).shift(DOWN * 2 + LEFT * 3)
        loga = TextTranslation("Logarit", "(Logarithm)", font_u="Sans",
                               color_u=YELLOW, color_d=GREEN).shift(DOWN * 2 + RIGHT * 3)

        ex_fomular = MathTex("a", "^b").scale(2).next_to(lt, UP, buff=1)
        ex_fomular[0].set_color(YELLOW)
        ex_fomular[1].set_color(TEAL)
        loga_fomular = MathTex("\log", "_a", "b").scale(2).next_to(loga, UP, buff=1)
        loga_fomular[1].set_color(YELLOW)
        loga_fomular[2].set_color(TEAL)
        # self.add(lt, loga, ex_fomular, loga_fomular)
        self.my_play(Write(lt), FadeIn(ex_fomular))
        self.my_play(Write(loga), FadeIn(loga_fomular))


class Scene1(MyScene):
    def construct(self):
        remind = Text("Nhắc lại kiến thức:", font="Sans", color=GREEN, font_size=40).to_corner(UL)
        ex = Text("Ví dụ:", font="Sans", color=GREEN, font_size=40).to_edge(LEFT)

        # self.add(remind, ex)

        def create_formular(a, x, b):
            formula1 = MathTex(a, "^" + x, "=", b)
            formula2 = MathTex(r"\rightarrow", "\log_{", a + "}", b, "=", x).next_to(formula1, DOWN)
            formula1[0].set_color(RED)
            formula1[1].set_color(YELLOW)
            formula1[3].set_color(BLUE)
            formula2[2].set_color(RED)
            formula2[3].set_color(BLUE)
            formula2[5].set_color(YELLOW)
            return VGroup(formula1, formula2)

        def create_transform(fomula):
            f1 = fomula[0]
            f2 = fomula[1]
            self.play(Write(f1))
            self.play(Write(f2[0:2]))
            self.play(FadeTransform(f1[0].copy(), f2[2]))
            self.play(Transform(f1[-1].copy(), f2[3]))
            self.play(FadeTransform(f1[1].copy(), f2[-1], path_arc=-PI), FadeIn(f2[-2]))

        formula1 = create_formular("a", "x", "b").scale(2).shift(UP * 2)
        formula2 = create_formular("3", "2", "9").scale(1.5).shift(LEFT * 3.5 + DOWN * 1.5)
        formula3 = create_formular("10", "4", "10,000").scale(1.5).shift(RIGHT * 3 + DOWN * 1.5)
        # self.add(formula1, formula2, formula3)
        self.play(Write(remind))
        create_transform(formula1)
        self.play(Write(ex))
        create_transform(formula2)
        create_transform(formula3)


class Scene2(MyScene):
    def construct(self):
        def text_factory(text):
            return Text(text, font_size=35, font="Sans", color=YELLOW)
        table = MathTable(
            [["\lg x", "\log x, \log_{10} x", r"\text{Toán học, kỹ thuật,...}"],
             [r"\text{lb } x", "\log_{2} x", r"\text{Toán học, tin học,...}"],
             ["\ln x", "\log_{e} x", r"\text{Toán học, vật lý,...}"]],
            row_labels=[text_factory("Cơ số 10"), text_factory("Cơ số 2"), text_factory("Cơ số e")],
            col_labels=[text_factory("Kí hiệu"), text_factory("Kí hiệu khác"), text_factory("Lĩnh vực ứng dụng")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            h_buff=0.5,
            element_to_mobject_config={"tex_template": my_template},
            line_config={"stroke_width": 1, "color": YELLOW})
        table.get_horizontal_lines()

        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        self.play(Write(table.get_rows()[0]))
        self.play(Write(table.get_rows()[1]))
        self.play(Write(table.get_rows()[2]))
        self.play(Write(table.get_rows()[3]))


class Scene3(MyScene):
    def construct(self):
        pass