from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4")
SCENE_NAME = list_scene[4]
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
        sqrt1 = MathTex("\sqrt{2}", r"\times", "\sqrt{2}", "=", "2")
        sqrt2 = MathTex("x", r"\times", "x", "=", "2")
        sqrt3 = MathTex("x", "=", "{2", "\over", "x}")
        group = VGroup(sqrt1, sqrt2, sqrt3).set_color(YELLOW).scale(3)

        table = MathTable(
            [[r"\text{Lần 1}", "1.5", "1.333333"],
             [r"\text{Lần 2}", "1.416667", "1.411764"],
             [r"\text{Lần 3}", "1.414216", "1.414211"],
             [r"\text{Lần 4}", "1.414214", "1.414213"],
             [r"\text{Lần 5}", "1.4142135", "1.4142135"]],
            col_labels=[Text("Thử", font="Sans", font_size=35), MathTex("x"), MathTex("2", "\over", "x")],
            include_outer_lines=True,
            element_to_mobject_config={"tex_template": myTemplate}).to_corner(UL).shift(UP * 0.4)
        # self.add(sqrt1, sqrt2, sqrt3)
        self.my_play(Write(sqrt1))
        self.my_play(ReplacementTransform(sqrt1, sqrt2))
        self.my_play(ReplacementTransform(sqrt2[0], sqrt3[0]),
                     ReplacementTransform(sqrt2[1], sqrt3[3]),
                     ReplacementTransform(sqrt2[2], sqrt3[4]),
                     ReplacementTransform(sqrt2[3], sqrt3[1]),
                     ReplacementTransform(sqrt2[4], sqrt3[2]))
        labels = table.get_col_labels()
        labels.set_color(YELLOW)
        entries = table.get_entries_without_labels()
        self.play(Transform(sqrt3[0], labels[1]),
                  Transform(sqrt3[2:], labels[2]),
                  FadeOut(sqrt3[1]))
        self.play(Create(table.get_vertical_lines()),
                  Create(table.get_horizontal_lines()),
                  Write(labels[0]))

        self.play(FadeIn(entries[0], shift=UP), run_time=0.5)
        self.play(FadeIn(entries[1], shift=UP), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(entries[2], shift=UP), run_time=0.5)
        tb = MathTex("{(", "1.5", "+", "1.333333", ")", "\over", "2}").next_to(entries[2], RIGHT, buff=1.5)
        tb2 = MathTex("=", "1.416667").next_to(entries[5], RIGHT, buff=1.5)
        self.play(ReplacementTransform(entries[1].copy(), tb[1]),
                  ReplacementTransform(entries[2].copy(), tb[3]))
        self.play(LaggedStart(*[FadeIn(tb[i]) for i in (0, 2, 4, 5, 6)]))
        self.play(Write(tb2))
        self.play(FadeIn(entries[3], shift=UP))
        self.play(Transform(tb2[-1], entries[4]), FadeOut(tb), FadeOut(tb2[0]))
        self.play(FadeIn(entries[5], shift=UP))

        self.play(FadeIn(entries[6], shift=UP))
        self.play(Transform(entries[4].copy(), entries[7]),
                  Transform(entries[5].copy(), entries[7]))
        self.play(FadeIn(entries[8], shift=UP))

        self.play(FadeIn(entries[9], shift=UP))
        self.play(Transform(entries[7].copy(), entries[10]),
                  Transform(entries[8].copy(), entries[10]))
        self.play(FadeIn(entries[11], shift=UP))

        self.play(FadeIn(entries[12], shift=UP))
        self.play(Transform(entries[10].copy(), entries[13]),
                  Transform(entries[11].copy(), entries[13]))
        self.play(FadeIn(entries[14], shift=UP))
        table.add_highlighted_cell((6, 2), color=GREEN)
        table.add_highlighted_cell((6, 3), color=GREEN)
        self.add(table)
        sqrt4 = MathTex("\Leftarrow \sqrt{2}", color=YELLOW).scale(1.5).next_to(entries[14], RIGHT, buff=1)
        self.play(FadeIn(sqrt4, shift=LEFT))


class Scene1(MyScene):
    def construct(self):
        sqrt1 = MathTex("\sqrt{127}", r"\times", "\sqrt{127}", "=", "127")
        sqrt2 = MathTex("x", r"\times", "x", "=", "127")
        sqrt3 = MathTex("x", "=", "{127", "\over", "x}")
        group = VGroup(sqrt1, sqrt2, sqrt3).set_color(YELLOW).scale(3)

        table = MathTable(
            [[r"\text{Lần 1}", "15", "8.466667"],
             [r"\text{Lần 2}", "11.73334", "10.82386"],
             [r"\text{Lần 3}", "11.27860", "11.26026"],
             [r"\text{Lần 4}", "11.26026", "11.26943"],
             [r"\text{Lần 5}", "11.26943", "11.26943"]],
            col_labels=[Text("Thử", font="Sans", font_size=35), MathTex("x"), MathTex("127", "\over", "x")],
            include_outer_lines=True,
            element_to_mobject_config={"tex_template": myTemplate}).to_corner(UL).shift(UP * 0.4)
        # self.add(sqrt1, sqrt2, sqrt3)
        self.my_play(Write(sqrt1))
        self.my_play(ReplacementTransform(sqrt1, sqrt2))
        self.my_play(ReplacementTransform(sqrt2[0], sqrt3[0]),
                     ReplacementTransform(sqrt2[1], sqrt3[3]),
                     ReplacementTransform(sqrt2[2], sqrt3[4]),
                     ReplacementTransform(sqrt2[3], sqrt3[1]),
                     ReplacementTransform(sqrt2[4], sqrt3[2]))
        labels = table.get_col_labels()
        labels.set_color(YELLOW)
        entries = table.get_entries_without_labels()
        self.play(Transform(sqrt3[0], labels[1]),
                  Transform(sqrt3[2:], labels[2]),
                  FadeOut(sqrt3[1]))
        self.play(Create(table.get_vertical_lines()),
                  Create(table.get_horizontal_lines()),
                  Write(labels[0]))

        self.play(FadeIn(entries[0], shift=UP))
        self.play(FadeIn(entries[1], shift=UP))
        self.play(FadeIn(entries[2], shift=UP))

        self.play(FadeIn(entries[3], shift=UP))
        self.play(Transform(entries[1].copy(), entries[4]),
                  Transform(entries[2].copy(), entries[4]))
        self.play(FadeIn(entries[5], shift=UP))

        self.play(FadeIn(entries[6], shift=UP))
        self.play(Transform(entries[4].copy(), entries[7]),
                  Transform(entries[5].copy(), entries[7]))
        self.play(FadeIn(entries[8], shift=UP))

        self.play(FadeIn(entries[9], shift=UP))
        self.play(Transform(entries[7].copy(), entries[10]),
                  Transform(entries[8].copy(), entries[10]))
        self.play(FadeIn(entries[11], shift=UP))

        self.play(FadeIn(entries[12], shift=UP))
        self.play(Transform(entries[10].copy(), entries[13]),
                  Transform(entries[11].copy(), entries[13]))
        self.play(FadeIn(entries[14], shift=UP))
        table.add_highlighted_cell((6, 2), color=GREEN)
        table.add_highlighted_cell((6, 3), color=GREEN)
        self.add(table)
        sqrt4 = MathTex("\Leftarrow \sqrt{127}", color=YELLOW).scale(1.5).next_to(entries[14], RIGHT, buff=1)
        self.play(FadeIn(sqrt4, shift=LEFT))


class Scene2(MyScene):
    def construct(self):
        light_color = "#FFC300"
        dark_color = "#FF5733"
        more_dark = "#C70039"
        text1 = Text("10 lần thử:", color=light_color, font_size=35, font="Sans").to_edge(LEFT).shift(UP*2)
        sqrt1 = MathTex(r"\rightarrow \sqrt{2}=", "1.4142135623...2804957", color=light_color).next_to(text1, RIGHT)
        text2 = Text("15 lần thử", color=dark_color, font_size=35, font="Sans").next_to(text1, DOWN, buff=1.5)
        sqrt2 = MathTex(r"\rightarrow \sqrt{2}=", "1.4142135623730950...834941229", color=dark_color).next_to(text2, RIGHT)
        text3 = Text("20 lần thử", color=more_dark, font_size=35, font="Sans").next_to(text2, DOWN, buff=1.5)
        sqrt3 = MathTex(r"\rightarrow \sqrt{2}=", "1.41421356237309504880...596377733289", color=more_dark).next_to(text3, RIGHT)

        time1 = Text("(0.01 giây)", font="Sans", font_size=30, color=light_color).next_to(text1, DOWN)
        time2 = Text("(0.5 giây)", font="Sans", font_size=30, color=dark_color).next_to(text2, DOWN)
        time3 = Text("(9.0 giây)", font="Sans", font_size=30, color=more_dark).next_to(text3, DOWN)

        brace1 = Brace(sqrt1[1], DOWN)
        brace2 = Brace(sqrt2[1], DOWN)
        brace3 = Brace(sqrt3[1], DOWN)

        number1 = Text("783 chữ số",color=light_color, font_size=35, font="Sans").next_to(brace1, DOWN, buff=SMALL_BUFF)
        number2 = Text("25.085 chữ số", color=dark_color, font_size=35, font="Sans").next_to(brace2, DOWN,buff=SMALL_BUFF)
        number3 = Text("802.739 chữ số", color=more_dark, font_size=35, font="Sans").next_to(brace3, DOWN,buff=SMALL_BUFF)

        # self.add(text1, text2, text3, sqrt1, sqrt2, sqrt3,
        #          brace1, brace2, brace3, number1, number2, number3,
        #          time1, time2, time3)
        self.play(Write(text1), Write(sqrt1))
        self.play(FadeIn(time1, shift=UP), FadeIn(brace1, shift=UP), FadeIn(number1, shift=UP))
        self.wait()

        self.play(Write(text2), Write(sqrt2))
        self.play(FadeIn(time2, shift=UP), FadeIn(brace2, shift=UP), FadeIn(number2, shift=UP))
        self.wait()

        self.play(Write(text3), Write(sqrt3))
        self.play(FadeIn(time3, shift=UP), FadeIn(brace3, shift=UP), FadeIn(number3, shift=UP))
        self.wait()

        self.play(Circumscribe(time3), Circumscribe(number3))
        self.wait()


class Scene3(MyScene):
    def construct(self):
        text1 = Paragraph("Không sử dụng\nnút căn",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        font_size=80,
                        line_spacing=0.5)
        text2 = MathTex(r"\text{Hãy tính }\sqrt{3}", color=GREEN, tex_template=myTemplate).scale(3).next_to(text1, DOWN)
        # self.add(text1, text2)
        self.play(Write(text1))
        self.my_play(Write(text2))


class Scene4(MyScene):
    def construct(self):
        text1 = MathTex(r"\text{Tính } \sqrt{N}:", tex_template=myTemplate, color=YELLOW)
        text2 = MathTex(r"\text{B1: Đoán 1 giá trị } x (\approx \sqrt{N})", tex_template=myTemplate, color=GREEN)
        text3 = MathTex(r"\text{B2: Nếu } x \neq {N \over x} \rightarrow \text{Thử } x={1 \over 2} ({x+ {N\over x}})", tex_template=myTemplate, color=GREEN)
        text4 = MathTex(r"\text{B3: Lặp lại B2 một vài lần}", tex_template=myTemplate, color=GREEN)
        text1.to_corner(UL)
        text2.next_to(text1, DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)
        text3.next_to(text2, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        text4.next_to(text3, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        # self.add(text1, text2, text3, text4)
        self.play(LaggedStart(*[FadeIn(i, shift=RIGHT) for i in (text1, text2, text3, text4)], lag_ratio=0.5))
        self.wait()