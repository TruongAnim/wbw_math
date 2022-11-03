import math
from manim import *
import random

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9")
SCENE_NAME = list_scene[0]
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


rel_obj = 10000
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

        self.num_dot = 999990000
        self.num_green = 800000000

        tracker = ValueTracker(999990000)

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