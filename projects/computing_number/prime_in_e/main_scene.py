from manim import *
from manim.utils.rate_functions import ease_in_expo


list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Thumbnail")
SCENE_NAME = list_scene[3]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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


my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{vntex}")


class Scene0(MyScene):
    def construct(self):
        #                       01234567890123456789012345
        e = MathTex(r"e", "=", "2.718281828459045235360287...").scale(1.7)
        # 281
        rec1 = Rectangle(color=YELLOW).surround(VGroup(e[2][5:8]), stretch=True)
        # 4253
        rec2 = Rectangle(color=YELLOW).surround(VGroup(e[2][15:19]), stretch=True)
        # 360287
        rec3 = Rectangle(color=YELLOW).surround(VGroup(e[2][20:26]), stretch=True)
        # 904523
        rec4 = Rectangle(color=YELLOW).surround(VGroup(e[2][13:19]), stretch=True)

        text1 = Text("Số nguyên tố", font_size=60, font="Sans", color=GREEN).to_edge(UP)
        arrow1 = Arrow(text1.get_bottom(), rec1.get_top())
        arrow2 = Arrow(text1.get_bottom(), rec2.get_top())
        arrow3 = Arrow(text1.get_bottom(), rec3.get_top())
        arrow4 = Arrow(text1.get_bottom(), rec4.get_top())

        prime1 = Text("3 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec1, DOWN)
        prime2 = Text("4 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec2, DOWN)
        prime3 = Text("6 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec3, DOWN)
        prime4 = Text("6 digits", font_size=50, font="Sans", color=YELLOW).next_to(rec4, DOWN)

        # self.add(e, rec1, rec2, rec3, arrow1, arrow2, arrow3, prime1, prime2, prime3, text1)
        self.play(FadeIn(e[0:2]))
        self.my_play(AddTextLetterByLetter(e[2]))
        self.play(Write(text1), GrowArrow(arrow1), Create(rec1), FadeIn(prime1, shift=UP))
        self.play(Indicate(VGroup(e[2][5:8])))
        self.play(Transform(arrow1, arrow2), Transform(rec1, rec2), Transform(prime1, prime2))
        self.play(Indicate(VGroup(e[2][15:19])))
        self.play(Transform(arrow1, arrow3), Transform(rec1, rec3), Transform(prime1, prime3))
        self.play(Indicate(VGroup(e[2][20:26])))
        self.play(Transform(arrow1, arrow4), Transform(rec1, rec4), Transform(prime1, prime4))
        self.play(Indicate(VGroup(e[2][13:19])))


class Scene1(MyScene):
    def construct(self):
        s1 = MathTex(r"\to", r"e = \lim_{n \to \infty } \left( 1+ {1\over n} \right)^{n}").to_corner(UL)
        s2 = MathTex(r"\to").next_to(s1, DOWN, buff=LARGE_BUFF, aligned_edge=LEFT)
        s3 = MathTex(r"\to").next_to(s2, DOWN, buff=LARGE_BUFF, aligned_edge=LEFT)

        def create_tex(n):
            tex = MathTex(r"e = \left( 1+ {1\over 10^{"+str(n)+r"}} \right)^{10^{"+str(n)+"}}").next_to(s2, RIGHT)
            return tex

        def create_e(v, n):
            n = 48
            s = "{:."+str(n)+"f}........"
            value = s.format(v)
            e = MathTex(value, color=RED).next_to(s3, RIGHT)
            return e

        ee = create_e(1, 48)
        brace = Brace(ee[0][2:], DOWN)
        def create_number(n):
            if n>100:
                n -= (n//100)
            if n>990:
                n+=1
            return Text(str(n)+" chữ số", font_size=40, font="Sans", color=YELLOW).next_to(brace, DOWN)

        number = create_number(0)
        timee = Text('(0.5 giây)', font_size=40, font="Sans", color=GREEN).next_to(number, RIGHT, buff=MED_LARGE_BUFF)

        s22 = MathTex(r"e = \left( 1+ {1\over 1} \right)^{1}").next_to(s2, RIGHT)
        s33 = MathTex("2", color=RED).next_to(s3, RIGHT)

        self.play(FadeIn(s1))
        self.play(FadeIn(s2), FadeIn(s22))
        self.play(FadeIn(s3), FadeIn(s33), FadeIn(brace, shift=UP), FadeIn(number, shift=UP))

        import decimal
        decimal.getcontext().prec = 1050
        def computing_e(n):
            return (1 + decimal.Decimal(1) / n) ** n

        tracker = ValueTracker(1)
        def redraw():
            new_n = int(tracker.get_value())
            s22.become(create_tex(new_n))
            s33.become(create_e(computing_e(10**new_n), new_n))
            number.become((create_number(new_n-1)))

            return VGroup(s22, s33, number)
        temp = always_redraw(redraw)

        def update(obj):
            pass

        tracker.add_updater(update)
        self.add(tracker, temp)
        self.play(tracker.animate.increment_value(1009), run_time=10, rate_func=ease_in_expo)
        # self.remove(tracker, temp)
        self.play(Wait(0.5))
        self.play(FadeIn(timee, shift=UP))
        self.play(Wait(0.5))


class Scene2(MyScene):
    def construct(self):

        def text_factory(text):
            return Text(text, font_size=35, font="Sans", color=WHITE)

        title = Text("Tìm kiếm trong 1000 chữ số e", font_size=50, font="Sans", color=BLUE).to_edge(UP, buff=SMALL_BUFF)
        table = MathTable(
            [[r"1245778837", r"\text{Không xuất hiện}"],
             [r"1062458263", r"\text{Không xuất hiện}"],
             [r"1934580727", r"728"],
             [r"3564128719", r"\text{Không xuất hiện}"],
             [r"4564128743", r"\text{Không xuất hiện}"],
             [r"6062613313", r"313"],
             [r"1062458263", r"\text{Không xuất hiện}"],
             [r"..........", r"\text{.............}"],],
            col_labels=[text_factory("Số nguyên tố"), text_factory(r"Vị trí")],
            include_outer_lines=True,
            h_buff=0.5,
            v_buff=0.4,
            element_to_mobject_config={"tex_template": my_template},
            line_config={"stroke_width": 1, "color": YELLOW})
        table.scale(0.9).next_to(title, DOWN)
        labels = table.get_labels()
        entity = table.get_entries_without_labels()

        brace = Brace(entity, LEFT, buff=MED_LARGE_BUFF)
        brace_tex1 = Paragraph("Số nguyên tố\ncó 10 chữ số",
                               font="Sans",
                               color=YELLOW,
                               alignment="center",
                               line_spacing=0.5, font_size=30).next_to(brace, LEFT)
        brace_tex2 = MathTex(r"(\approx 400 \text{ triệu số})", color=RED, tex_template=my_template).scale(1).next_to(brace_tex1, DOWN)
        self.play(FadeIn(title, shift=UP))
        self.play(Create(table.get_horizontal_lines()),
                  Create(table.get_vertical_lines()))
        self.play(Write(labels), FadeIn(brace, shift=RIGHT), Write(brace_tex1))
        highlight1 = table.get_highlighted_cell((4, 1), color=GREEN)
        highlight2 = table.get_highlighted_cell((4, 2), color=GREEN)
        highlight3 = table.get_highlighted_cell((7, 1), color=GREEN)
        highlight4 = table.get_highlighted_cell((7, 2), color=GREEN)
        for i in range(0, 16, 2):
            self.play(FadeIn(entity[i]), run_time=0.5)
            self.play(FadeIn(entity[i+1]), run_time=0.5)
            if i == 4:
                self.add(highlight1)
                self.add(highlight2)
                self.add_foreground_mobjects(entity[i], entity[i+1])
            if i == 10:
                self.add(highlight3)
                self.add(highlight4)
                self.add_foreground_mobjects(entity[i], entity[i+1])

            self.wait(0.5)
        self.play(FadeIn(brace_tex2, shift=UP))
        self.wait(0.5)
        # self.add(table, title, brace_tex2, brace)


class Scene3(Scene):
    def construct(self):
        text = Text("2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639193200305992181741359",
                    font_size=50, font="Sans").align_to(LEFT*2, LEFT)
        brace = Brace(text[2:12], DOWN)
        text1 = Text("not prime", font_size=40, font="Sans", color=RED).next_to(brace, DOWN)
        text2 = Text("Prime (Vị trí 99)", font_size=40, font="Sans", color=GREEN).next_to(brace, DOWN)
        self.play(FadeIn(text, shift=UP))
        self.play(FadeIn(brace, shift=UP), text[2:12].animate.set_color(YELLOW))
        self.play(FadeIn(text1, shift=DOWN))

        for i in range(3, 101):
            text[i-1].set_color(WHITE)
            text[i+9].set_color(YELLOW)
            if i< 10:
                self.play(text.animate.shift(LEFT*(text[i].get_right()-text[i-1].get_right())),
                          FadeIn(text1, shift=DOWN), )
                # self.play(FadeIn(text1, shift=DOWN))
            elif i< 100:
                self.play(text.animate.shift(LEFT*(text[i].get_right()-text[i-1].get_right())),
                          FadeIn(text1, shift=DOWN), run_time=0.3, rate_func=linear)
                # self.play(FadeIn(text1, shift=DOWN), run_time=0.3)
            else:
                self.remove(text1)
                self.play(text.animate.shift(LEFT * (text[i].get_right() - text[i - 1].get_right())),
                          FadeIn(text2, shift=DOWN), run_time=0.3, rate_func=linear)
        self.wait(0.5)
        self.play(Wiggle(text[100:100+10]), ApplyWave(text2))
        self.play(Wiggle(text[100:100+10]), ApplyWave(text2))
        self.play(Wiggle(text[100:100+10]), ApplyWave(text2))
        self.wait(0.5)
