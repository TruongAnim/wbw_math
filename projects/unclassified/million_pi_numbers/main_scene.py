import math
from manim import *
from manim.utils.rate_functions import ease_in_expo
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

rel_obj = 1000000
rel_time = 5
test_obj = 100
test_time = 3


class Scene0(MyScene):
    def get_random_position(self):
        x = random.uniform(0, 5)
        y = random.uniform(0, 5)
        return np.array([x, y, 0])

    def construct(self):
        random.seed(1)
        shape = Circle(radius=5, stroke_width=3, stroke_color=YELLOW).shift(DOWN * 2.5).get_subcurve(0, 0.25)
        square = Square(side_length=5, stroke_color=WHITE, stroke_width=3).shift(RIGHT * 2.5)
        brace1 = Brace(square, DOWN)
        side1 = brace1.get_tex("1")
        brace2 = Brace(square, LEFT)
        side2 = brace2.get_tex("1")

        vertical = Arrow(start=square.point_from_proportion(0.5) + LEFT, end=square.point_from_proportion(0.75) + RIGHT,
                         stroke_width=1)
        horizontal = Arrow(start=square.point_from_proportion(0.5) + DOWN, end=square.point_from_proportion(0.25) + UP,
                           stroke_width=1)

        self.my_play(Create(vertical), Create(horizontal))
        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace1, shift=UP), FadeIn(side1, shift=UP), FadeIn(brace2, shift=RIGHT),
                     FadeIn(side2, shift=RIGHT))

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
        formula2 = formula[1].copy().shift(DOWN * 1.5)

        real_pi = Text("{:.10f}...".format(math.pi),
                       color=GREEN,
                       font_size=35,
                       font="Arial") \
            .next_to(formula2, RIGHT, aligned_edge=LEFT, buff=MED_LARGE_BUFF) \
            .shift(DOWN)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(formula2),
            Write(real_pi)
        ], lag_ratio=0.3))

        self.num_dot = 999000000
        self.num_green = 785382415
        self.num_green = 784609605

        tracker = ValueTracker(999000000)

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
                result = "{:.8f}".format(4 * self.num_green / self.num_dot)
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
                    if p[0] * p[0] + p[1] * p[1] < 25:
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


class Scene1(MyScene):
    def construct(self):
        s1 = MathTex("tan({\pi \over 4})=1")
        s2 = MathTex(r"\rightarrow {\pi \over 4}=", "arctan(1)")
        s3 = MathTex(r"\rightarrow \pi = 4 \times ", "arctan(1)")
        s4 = MathTex(r"\rightarrow \pi = 4 \times ", "\int_{0}^{1} {1\over 1+x^2}dx")
        s5 = MathTex(r"\rightarrow \pi = 4 \times ", "\int_{0}^{1} (1-x^2+x^4-...)dx")
        s6 = MathTex(r"\rightarrow \pi = 4 \times ", "1-{1 \over 3}+{1 \over 5}-{1\over 7}+...")

        for i in (s2, s3, s4, s5, s6):
            i[1].set_color(YELLOW)

        group = VGroup(s1, s2, s3, s4, s5, s6).arrange(DOWN, aligned_edge=LEFT)
        for i in group:
            self.my_play(Write(i))
        self.my_play(LaggedStart(*[FadeOut(i) for i in (s1, s2, s3, s3, s4, s5)], s6.animate.shift(UP*5), lag_ratio=0.15))
        text1 = Text("Số vô tỉ", font_size=40, font="Sans").next_to(s6[0][1], DOWN, buff=LARGE_BUFF)
        text2 = Text("Dài vô tận", font_size=40, font="Sans").next_to(s6[1], DOWN).align_to(text1, direction=UP)
        arrow = Arrow(text1.get_center(), s6[0][1])
        brace = Brace(s6[1], DOWN)
        self.my_play(FadeIn(text1, shift=UP), FadeIn(arrow, shift=UP))
        self.my_play(FadeIn(text2, shift=UP), FadeIn(brace, shift=UP))


class Scene2(MyScene):
    def construct(self):
        s = MathTex(r"\rightarrow \pi = 4 \times ", "1-{1 \over 3}+{1 \over 5}-{1\over 7}+...").shift(UP)
        s[1].set_color(YELLOW)
        brace = Brace(s[1], DOWN)
        brace_t = brace.get_text("5")
        s1 = MathTex(r"\rightarrow \pi \approx ").shift(DOWN).align_to(s, LEFT)
        pi = Text("{:.10f}".format(3.3396825396825403), font="Sans", font_size=35).next_to(s1, RIGHT)
        self.play(Write(s))
        self.play(FadeIn(brace, shift=UP), FadeIn(brace_t, shift=UP))
        self.play(Write(s1), Write(pi))
        self.pi_value = 3.3396825396825403
        self.last_frame = 5
        tracker = ValueTracker(5)

        def calculate(n):
            import time
            start_time = time.time()
            sum = self.pi_value/4
            for i in range(self.last_frame, n):
                if i % 2 == 0:
                    sum += (1 / (2 * i + 1))
                else:
                    sum -= (1 / (2 * i + 1))
            self.last_frame = n
            return 4 * sum
        def update(obj):
            value = int(tracker.get_value())
            self.pi_value = calculate(value)

        def redraw():
            pi.become(Text("{:.10f}".format(self.pi_value), font="Sans", font_size=35).next_to(s1, RIGHT))
            brace_t.become(Text(str(int(tracker.get_value())), font_size=30, font="Sans").move_to(brace_t))

            return VGroup(pi, brace_t)
        temp = always_redraw(redraw)

        tracker.add_updater(update)
        self.add(tracker, temp)
        self.play(tracker.animate.increment_value(1000000000-5), run_time=20, rate_func=ease_in_expo)
        self.play(Wait(0.5))


class Scene3(MyScene):
    def construct(self):
        f1 = MathTex("{\pi \over 4} = 4arctan({1 \over 5})-arctan({1 \over 239})", color=YELLOW)
        f2 = MathTex("{\pi \over 4} = 6arctan({1 \over 8})+2arctan({1 \over 57})+arctan({1 \over 239})", color=ORANGE)
        f3 = MathTex("{\pi \over 4} = 12arctan({1 \over 49})+32arctan({1 \over 57})-5arctan({1 \over 239})+12arctan({1 \over 110443})", color=RED).scale(0.8)
        group = VGroup(f1, f2, f3).arrange(DOWN, aligned_edge=LEFT)
        # self.add(group)
        self.play(Write(f1))
        self.play(Write(f2))
        self.play(Write(f3))
        self.wait()
        self.play(FadeOut(f2), FadeOut(f3), Circumscribe(f1))
        self.play(f1.animate.shift(UP))
        light_color = "#b26782"
        dark_color = "#80032f"
        text1 = Text("0.1 giây ", color=light_color, font_size=35, font="Sans").next_to(f1, DOWN, buff=1.5, aligned_edge=LEFT)
        pi1 = MathTex(r"\rightarrow \pi=", "3.1415926535897932...201989", color=light_color).next_to(text1, RIGHT)
        text2 = Text("19 phút ", color=dark_color, font_size=35, font="Sans").next_to(text1, DOWN, buff=1.5)
        brace1 = Brace(pi1[1], DOWN)
        milli = Text("10 ngàn chữ số",color=light_color, font_size=35, font="Sans").next_to(brace1, DOWN, buff=SMALL_BUFF)
        pi2 = MathTex(r"\rightarrow \pi=", "3.141592653589793238462643...779458151", color=dark_color).next_to(text2, RIGHT)
        brace2 = Brace(pi2[1], DOWN)
        billi = Text("1 triệu chữ số", color=dark_color, font_size=35, font="Sans").next_to(brace2, DOWN,
                                                                                            buff=SMALL_BUFF)
        self.play(Write(text1), Write(pi1))
        self.play(FadeIn(brace1, shift=UP), FadeIn(milli, shift=UP))
        self.wait()
        self.play(Write(text2), Write(pi2))
        self.play(FadeIn(brace2, shift=UP), FadeIn(billi, shift=UP))
        self.wait()


class Scene4(MyScene):
    def construct(self):
        line = Line(DOWN*3, UP*2)
        milli = Text("1 triệu số pi", font_size=40, font="Sans", color=YELLOW).next_to(line, UP)
        my_pi = Text("my_pi.txt", font_size=35).shift(UP+LEFT*3.5)
        my_md5 = Text("e87782d11eac8d992faca76ceb940433", font_size=25, font="Sans", color=TEAL).next_to(my_pi, DOWN, buff=2)
        arrow = Arrow(my_pi.get_center(), my_md5.get_center())
        md51 = Text("MD5 Checksum", font_size=20, font="Sans").next_to(arrow, LEFT)

        mit_pi = Text("MIT_pi.txt", font_size=35).shift(UP + RIGHT * 3.5)
        mit_md5 = Text("e87782d11eac8d992faca76ceb940433", font_size=25, font="Sans", color=TEAL).next_to(mit_pi, DOWN,
                                                                                                         buff=2)
        arrow2 = Arrow(mit_pi.get_center(), mit_md5.get_center())
        md52 = Text("MD5 Checksum", font_size=20, font="Sans").next_to(arrow2, RIGHT)
        # self.add(line, milli, my_md5, my_pi, md51, arrow,
        #          arrow2, mit_pi, mit_md5, md52)
        self.play(Create(line), Write(milli))
        self.play(Write(my_pi), Write(mit_pi))
        self.play(FadeIn(arrow, shift=DOWN), FadeIn(md51, shift=DOWN),
                  FadeIn(arrow2, shift=DOWN), FadeIn(md52, shift=DOWN))
        self.play(Write(my_md5), Write(mit_md5))
        self.play(Circumscribe(my_md5), Circumscribe(mit_md5))
        self.wait()


class Scene5(Scene):
    def construct(self):
        chitti = SVGMobject("alien").scale(2).to_corner(DL, buff=0)
        chat = SVGMobject("conversation", color=WHITE).scale(2).stretch_to_fit_width(6.5).next_to(chitti, UR, buff=-2).shift(UP*2)
        prime = MarkupText('Xin chào, chúng tôi đến từ\nmột nền văn minh tiên tiến\nĐã tính được tới <span foreground="yellow">1 triệu chữ số Pi</span>',
                           font_size=28, font="Sans")
        group = VGroup(prime).move_to(chat).shift(UP*0.5)
        joker = ImageMobject("politic").scale(1.3)
        pi = Text("Tưởng alien dư lào...", font_size=32, font="Sans", color=YELLOW).scale(1.3).next_to(joker, UP, buff=SMALL_BUFF)
        p2 = Text("100,000,000,000,000 chữ số", font_size=32, font="Sans", color=YELLOW).move_to(joker).shift(DOWN*1.5)
        group = Group(joker, pi, p2).to_corner(DR, buff=0)
        self.play(FadeIn(chitti, shift=RIGHT))
        self.play(FadeIn(chat), Write(prime))
        self.wait()
        self.play(FadeIn(group, shift=LEFT*3), rate_func=linear)
        self.wait()