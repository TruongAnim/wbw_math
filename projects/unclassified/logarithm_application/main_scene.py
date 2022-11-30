from manim import *
from common.custom.custom_mobject import TextTranslation
from common.custom.custom_mobject import Beaker

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4",
              "Scene5", "Scene6", "Scene7", "Scene8", "Scene9")
# SCENE_NAME = list_scene[8]
SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

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
        self.wait()


class Scene3(MyScene):
    def construct(self):
        beaker = Beaker("assets/beaker2.svg", ion_number=20, random_seed=2).scale(3).shift(LEFT * 3)
        acid = TextTranslation(text_u="A-xít", text_d="(Acid)", color_u=RED, color_d=RED, font_size_u=45,
                               font_size_d=40).shift(RIGHT * 3 + UP * 2)
        acid_ion = MathTex(r"\text{Nhiều ion H}", "^+", tex_template=my_template, color=YELLOW).next_to(acid, DOWN)
        line = Line(LEFT * 2, RIGHT * 2).shift(RIGHT * 3)
        base = TextTranslation(text_u="Bazơ", text_d="(Base)", color_u=BLUE, color_d=BLUE, font_size_u=45,
                               font_size_d=40).shift(RIGHT * 3 + DOWN)
        base_ion = MathTex(r"\text{Ít ion H}", "^+", tex_template=my_template, color=YELLOW).next_to(base, DOWN)
        # self.add(beaker, acid, line, base, acid_ion, base_ion)
        self.play(FadeIn(beaker[0]), FadeIn(beaker[1]))
        self.my_play(Write(acid), Write(base), Create(line))
        self.play(LaggedStart(*[FadeIn(i) for i in beaker[2]]))
        self.my_play(Write(acid_ion), Write(base_ion))


class Scene4(MyScene):
    def construct(self):
        pure_water = Beaker("assets/beaker2.svg", ion_number=20, random_seed=3, solution_color=BLUE_B).scale(2.3).shift(
            UP)
        sea_water = Beaker("assets/beaker2.svg", ion_number=10, random_seed=2, solution_color=BLUE_E).scale(2.3).shift(
            RIGHT * 4.5 + UP)
        orange_juice = Beaker("assets/beaker2.svg", ion_number=40, random_seed=3, solution_color="#E3963E").scale(
            2.3).shift(LEFT * 4.5 + UP)

        def title_factory(text1, text2, text3, color):
            title = Text(text1, font_size=40, font="Sans")
            ion = MathTex(text2, color=YELLOW).next_to(title, DOWN)
            result = Text(text3, font_size=35, font="Sans", color=color).next_to(ion, DOWN)
            return VGroup(title, ion, result)

        pure_water_title = title_factory("Nước tinh khiết", r"\text{0.0000001 mol/l}", "Trung tính",
                                         color=BLUE_B).next_to(pure_water, DOWN, buff=MED_LARGE_BUFF)
        sea_water_title = title_factory("Nước biển", r"\text{0.00000001 mol/l}", "Tính bazơ", color=BLUE_E).next_to(
            pure_water_title, RIGHT, buff=1.3).shift(UP * 0.1)
        orange_juice_title = title_factory("Nước cam", r"\text{0.00031 mol/l}", "Tính a-xít", color="#E3963E").next_to(
            pure_water_title, LEFT, buff=1.3).shift(UP * 0.05)
        # self.add(pure_water, sea_water, orange_juice, sea_water_title, orange_juice_title, pure_water_title)
        bigger1 = MathTex(">", color=YELLOW).scale(1.5).next_to(pure_water_title[1], LEFT, buff=MED_LARGE_BUFF)
        bigger2 = MathTex(">", color=YELLOW).scale(1.5).next_to(pure_water_title[1], RIGHT, buff=MED_LARGE_BUFF)

        def animation_factory(beaker, title):
            self.play(FadeIn(beaker[0]), FadeIn(beaker[1]), Write(title[0]))
            self.play(LaggedStart(*[FadeIn(i) for i in beaker[2]]), Write(title[1]))
            self.play(Write(title[2]))
            self.wait(0.5)

        animation_factory(pure_water, pure_water_title)
        animation_factory(sea_water, sea_water_title)
        animation_factory(orange_juice, orange_juice_title)
        self.play(FadeIn(bigger1, shift=UP), FadeIn(bigger2, shift=UP))
        self.wait(0.5)


class Scene5(MyScene):
    def construct(self):
        def text_factory(text):
            return Text(text, font_size=35, font="Sans", color=YELLOW)

        table = MathTable(
            [[r"\text{A-xít ắc quy}", "0.316227", "-0.5", "0.5"],
             [r"\text{Nước cam}", "0.000316", "-3.5", "3.5"],
             [r"\text{Nước tinh khiết}", "0.0000001", "-7", "7"],
             [r"\text{Nước biển}", "0.00000001", "-8", "8"],
             [r"\text{Thuốc tẩy}", "0.0000000000001", "-13", "13"], ],
            # row_labels=[text_factory("Cơ số 10"), text_factory("Cơ số 2"), text_factory("Cơ số e")],
            col_labels=[text_factory("Chất"), MathTex(r"\text{H}^+ \text{ (mol/l)}"), MathTex(r"\log_{10}(\text{H}^+)"),
                        MathTex(r"-\log_{10}(\text{H}^+)")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            h_buff=0.5,
            element_to_mobject_config={"tex_template": my_template},
            line_config={"stroke_width": 1, "color": YELLOW})
        highlight = ["#bb0000", "#ffcc00", "#008000", "#006699", "#0000cc"]
        entries = table.get_entries_without_labels()
        column = table.get_col_labels()
        self.my_play(Create(table.get_horizontal_lines()),
                  Create(table.get_vertical_lines()),
                  Write(column[0]), Write(column[1]))
        self.my_play(Write(entries[4]), Write(entries[5]),
                  Write(entries[8]), Write(entries[9]),
                  Write(entries[12]), Write(entries[13]))

        self.play(Write(column[2]))
        self.my_play(Write(entries[6]), Write(entries[10]), Write(entries[14]))
        self.my_play(Write(column[3]), Write(entries[7]), Write(entries[11]), Write(entries[15]))
        self.my_play(LaggedStart(*[Write(entries[i]) for i in (0, 1, 2, 3, 16, 17, 18, 19)]))
        for index, color in enumerate(highlight):
            table.add_highlighted_cell((index + 2, 4), color=color)
        self.add(table)
        ph = MathTex(r"\text{pH}", color=YELLOW).scale(1.5).move_to(column[-1])
        self.play(Transform(column[-1], ph))


class Scene6(MyScene):
    def construct(self):
        A, B, C, D = LEFT*6, LEFT*3, RIGHT*3, RIGHT*6
        arrow1 = Arrow(B, A, stroke_width=5, buff=0)
        arrow1.set_color([BLUE, PINK])
        arrow1.get_tip().set_color(PINK)
        arrow2 = Arrow(C, D, stroke_width=5, buff=0)
        arrow2.set_color([RED, YELLOW])
        arrow2.get_tip().set_color(RED)
        line = Line(B, C, stroke_width=5)
        line.set_color([YELLOW, GREEN, BLUE])
        mark1 = Line(DOWN*0.3, UP*0.5).shift(LEFT*3)
        mark2 = mark1.copy().shift(RIGHT*6)
        min_sound = MathTex("0.000000000001w/m^2").scale(0.7).next_to(mark1, UP)
        max_sound = MathTex("1w/m^2").next_to(mark2, UP)
        brace1 = Brace(arrow1, DOWN)
        brace2 = Brace(line, DOWN).align_to(brace1, DOWN)
        brace3 = Brace(arrow2, DOWN)
        text1 = Text("Quá nhỏ", font_size=35, font="Sans", color=PINK).next_to(brace1, DOWN)
        text2 = Text("Ngưỡng nghe", font_size=35, font="Sans", color=GREEN).next_to(brace2, DOWN)
        text3 = Text("Bắt đầu đau tai", font_size=35, font="Sans", color=RED).next_to(brace3, DOWN)
        sound_intensity = TextTranslation(text_u="Cường độ âm thanh",
                                          text_d="(Sound intensity)").to_edge(UP)
        sub_arrow1 = Arrow(sound_intensity[1].get_left(), min_sound.get_top(), stroke_width=3)
        sub_arrow2 = Arrow(sound_intensity[1].get_right(), max_sound.get_top(), stroke_width=3)
        math1 = MathTex(r"{\text{Tối đa}", "\over", r"\text{Tối thiểu}}=", tex_template=my_template).shift(DOWN*3+LEFT*5)
        math2 = MathTex(r"{1w/m^2", "\over", r"{0.000000000001w/m^2}}", tex_template=my_template).next_to(math1)
        math3 = MathTex(r"=1,000,000,000,000", r"\text{ lần}", tex_template=my_template).next_to(math2)
        # self.add(math1, math2, math3)
        self.my_play(FadeIn(sound_intensity[0], shift=RIGHT),
                  FadeIn(sound_intensity[1], shift=LEFT))
        self.my_play(FadeIn(arrow1, shift=UP),
                  FadeIn(line, shift=UP),
                  FadeIn(arrow2, shift=UP))
        self.play(GrowArrow(sub_arrow1), FadeIn(mark1, shift=UP), Write(min_sound))
        self.play(GrowArrow(sub_arrow2), FadeIn(mark2, shift=UP), Write(max_sound))
        self.my_play(FadeIn(text1, shift=UP),
                  FadeIn(brace1, shift=UP))
        self.my_play(FadeIn(text2, shift=UP),
                  FadeIn(brace2, shift=UP))
        self.my_play(FadeIn(text3, shift=UP),
                  FadeIn(brace3, shift=UP))
        # self.add(arrow1, arrow2, line, mark1, mark2, min_sound, sound_intensity)
        # self.add(brace1, brace3, brace2, max_sound, text1, text2, text3, sub_arrow1, sub_arrow2)
        self.play(Write(math1))
        self.play(FadeTransform(min_sound.copy(), math2[2]),
                  FadeTransform(max_sound.copy(), math2[0]),
                  Create(math2[1]))
        self.play(Write(math3))
        self.wait(0.5)


class Scene7(MyScene):
    def construct(self):
        def text_factory(text):
            return Text(text, font_size=35, font="Sans", color=WHITE)

        table = MathTable(
            [[r"\text{Nói chuyện}", "0.000001w/m^2", "1000000", "6(B)", "60(dB)"],
             [r"\text{Nghe nhạc}", "0.00001w/m^2", "10000000", "7(B)", "70(dB)"],
             [r"\text{Vũ trường}", "0.1w/m^2", "100000000000", "11(B)", "110(dB)"]],
            # row_labels=[text_factory("Cơ số 10"), text_factory("Cơ số 2"), text_factory("Cơ số e")],
            col_labels=[text_factory("Âm thanh"), text_factory(r"Cường độ (I)"), MathTex(r"I \over I_{0}"),
                        MathTex(r"\log_{10}({I \over I_{0}})"), MathTex(r"10\log_{10}({I \over I_{0}})")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            h_buff=0.5,
            element_to_mobject_config={"tex_template": my_template},
            line_config={"stroke_width": 1, "color": YELLOW})
        table.scale(0.9).shift(UP)
        title = Paragraph("Cường độ âm thanh nhỏ nhất\n con người có thể nghe.",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5, font_size=30).to_corner(DL, buff=MED_SMALL_BUFF)
        i0 = MathTex("I_{0}=0.000000000001w/m^2", color=YELLOW).scale(0.7).next_to(title, RIGHT)
        entries = table.get_entries_without_labels()
        bel = Text("Bel", color=RED).next_to(entries[13], DOWN, buff=MED_LARGE_BUFF)
        decibel = Text("Decibel", color=ORANGE).next_to(entries[14], DOWN, buff=MED_LARGE_BUFF)
        column = table.get_col_labels()
        self.play(FadeIn(title, shift=UP), FadeIn(i0, shift=UP))
        self.play(Create(table.get_horizontal_lines()),
                  Create(table.get_vertical_lines()),
                  Write(column[0]), Write(column[1]), Write(column[2]))
        self.my_play(Write(entries[0]), Write(entries[1]), Write(entries[2]))
        self.my_play(Write(entries[5]), Write(entries[6]), Write(entries[7]))
        self.my_play(Write(entries[10]), Write(entries[11]), Write(entries[12]))
        self.play(Write(column[3]))
        self.play(Write(entries[3]))
        self.play(Write(entries[8]))
        self.play(Write(entries[13]))
        self.play(Write(bel))
        self.play(Write(column[4]))
        self.play(Write(entries[4]))
        self.play(Write(entries[9]))
        self.play(Write(entries[14]))
        self.play(Write(decibel))
        for index in range(4):
            table.add_highlighted_cell((index + 1, 4), color=RED)
        for index in range(4):
            table.add_highlighted_cell((index + 1, 5), color=ORANGE)
        self.add(table, title, i0)
        self.my_play(Wiggle(bel), Wiggle(decibel))


class Scene8(MyScene):
    def construct(self):
        A, B, C, D = LEFT*6, LEFT*3, RIGHT*3, RIGHT*6
        arrow1 = Arrow(B, A, stroke_width=5, buff=0)
        arrow1.set_color([BLUE, PINK])
        arrow1.get_tip().set_color(PINK)
        arrow2 = Arrow(C, D, stroke_width=5, buff=0)
        arrow2.set_color([RED, YELLOW])
        arrow2.get_tip().set_color(RED)
        line = Line(B, C, stroke_width=5)
        line.set_color([YELLOW, GREEN, BLUE])
        mark1 = Line(DOWN*0.3, UP*0.5).shift(LEFT*3)
        mark2 = mark1.copy().shift(RIGHT*6)
        min_sound = MathTex("0.000000000001w/m^2").scale(0.7).next_to(mark1, UP)
        max_sound = MathTex("1w/m^2").next_to(mark2, UP)
        min_sound2 = MathTex(r"\text{0 (dB)}").next_to(mark1, UP)
        max_sound2 = MathTex(r"\text{120 (dB)}").next_to(mark2, UP)
        brace1 = Brace(arrow1, DOWN)
        brace2 = Brace(line, DOWN).align_to(brace1, DOWN)
        brace3 = Brace(arrow2, DOWN)
        text1 = Text("Quá nhỏ", font_size=35, font="Sans", color=PINK).next_to(brace1, DOWN)
        text2 = Text("Ngưỡng nghe", font_size=35, font="Sans", color=GREEN).next_to(brace2, DOWN)
        text3 = Text("Bắt đầu đau tai", font_size=35, font="Sans", color=RED).next_to(brace3, DOWN)
        sound_intensity = TextTranslation(text_u="Cường độ âm thanh",
                                          text_d="(Sound intensity)").to_edge(UP)
        sound_intensity2 = TextTranslation(text_u="Thang đo decibel",
                                           text_d="(dB)").to_edge(UP)
        sub_arrow1 = Arrow(sound_intensity[1].get_left(), min_sound.get_top(), stroke_width=3)
        sub_arrow2 = Arrow(sound_intensity[1].get_right(), max_sound.get_top(), stroke_width=3)
        math1 = MathTex(r"{\text{Tối đa}", "\over", r"\text{Tối thiểu}}=", tex_template=my_template).shift(DOWN*3+LEFT*5)
        math2 = MathTex(r"{1w/m^2", "\over", r"{0.000000000001w/m^2}}", tex_template=my_template).next_to(math1)
        math3 = MathTex(r"=1,000,000,000,000", r"\text{ lần}", tex_template=my_template).next_to(math2)

        self.add(arrow1, arrow2, line, mark1, mark2, min_sound, sound_intensity)
        self.add(brace1, brace3, brace2, max_sound, text1, text2, text3, sub_arrow1, sub_arrow2)
        self.wait(0.5)
        self.my_play(Transform(sound_intensity, sound_intensity2),
                  Transform(min_sound, min_sound2),
                  Transform(max_sound, max_sound2))
