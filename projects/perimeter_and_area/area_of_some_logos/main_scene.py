import random
from manim import *

list_scene = ("Scene1", "Scene2", "Scene3",
              "Scene4", "Scene5", "Scene6",
              "Scene7")
# SCENE_NAME = list_scene[2]
SCENE_NAME = " ".join(list_scene)
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


def cross_product(u, v):
    return np.array([u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]])


def dist(u, v):
    return np.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)


def closest_point(list, target):
    best = 0
    best_dist = dist(list[best], target)
    for i in range(len(list)):
        if dist(list[i], target) < best_dist:
            best = i
            best_dist = dist(list[best], target)
    return best


def is_in_shape(point, P_list, greater_than_one):
    n = closest_point(P_list, point)
    l = len(P_list)
    tangent_vector = P_list[(n + 1) % l] - P_list[(n - 1) % l]
    to_target_vector = point - P_list[n]
    cross_product_res = cross_product(tangent_vector, to_target_vector)
    if greater_than_one:
        return cross_product_res[2] >= 0
    else:
        return cross_product_res[2] <= 0


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")
rel_obj = 50000
rel_time = 20
test_obj = 1000
test_time = 3

class Scene1(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):

        shape = Circle(radius=2.5, stroke_color=GREEN)
        square = Square(side_length=5).move_to(shape)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=2, color=GREEN) \
            .set_fill(color=YELLOW, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN)

        error = MathTex(r"\text{Sai số:}",
                        tex_template=myTemplate,
                        ).shift(DOWN * 2).align_to(formula, LEFT).scale(0.7)
        error_percent = MathTex(r"\%").next_to(error, RIGHT, buff=LARGE_BUFF * 1.7).scale(0.7)

        real_area = MathTex(r"S = 2.5^{2}*\pi = ",
                            "19.63495",
                            color=GREEN).scale(0.8)
        self.my_play(Write(real_area))
        real_area[1].generate_target()
        real_area[1].target.scale(0.85)
        real_area[1].target.next_to(formula2, RIGHT)
        real_area[1].target.shift(DOWN * 0.5)
        self.my_play(FadeOut(real_area[0]), MoveToTarget(real_area[1]))

        num_point = 30
        list_point = [shape.point_from_proportion(i / num_point)
                      for i in range(num_point)]

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:]),
            Write(error),
            Write(error_percent)
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=YELLOW,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT)
            if self.num_dot != 0:
                e = abs((25 * self.num_green / self.num_dot) - 19.63495)
                result = "{:.5f}".format(e * 100 / 19.63495)
            s2 = Text(result,
                      color=RED,
                      font_size=30,
                      font="Arial") \
                .scale(0.7) \
                .next_to(error, RIGHT)
            return VGroup(dot_green, dot_total, s, s2)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point, True):
                        dot.set_color(YELLOW)
                        self.num_green += 1
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(rel_obj),
                  run_time=rel_time,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))


class Scene2(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        shape = SVGMobject("batman2",
                           stroke_color=YELLOW,
                           stroke_width=2).scale(1.2)[0]
        square = Square(side_length=5, stroke_color=YELLOW).move_to(shape)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 100
        list_point = [shape.point_from_proportion(i / num_point)
                      for i in range(num_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=YELLOW, opacity=1) \
            .scale(0.07) \
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point, False):
                        dot.set_color(YELLOW)
                        self.num_green += 1
                    else:
                        dot.set_color(WHITE)
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(500),
                  run_time=1,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))


class Scene3(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        shape = SVGMobject("apple2",
                           stroke_color=GREEN,
                           stroke_width=2).scale(2)
        square = Square(side_length=5, stroke_color=GREEN)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 60
        list_point1 = [shape[0].point_from_proportion(i / num_point)
                       for i in range(num_point)]
        list_point2 = [shape[1].point_from_proportion(i / num_point)
                       for i in range(num_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=GREEN, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point1, True) or \
                            is_in_shape(dot.get_center(), list_point2, False):
                        dot.set_color(GREEN)
                        self.num_green += 1
                    else:
                        dot.set_color(WHITE)
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(1000),
                  run_time=1,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))


class Scene4(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        shape = SVGMobject("tiktok",
                           stroke_color=TEAL,
                           stroke_width=2).scale(2)
        square = Square(side_length=5, stroke_color=TEAL)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 100
        list_point = [shape[0].point_from_proportion(i / num_point)
                      for i in range(num_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=TEAL, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point, True):
                        dot.set_color(TEAL)
                        self.num_green += 1
                    else:
                        dot.set_color(WHITE)
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(1000),
                  run_time=1,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))


class Scene5(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        square = Square(side_length=5, stroke_color=WHITE)
        shape = SVGMobject("facebook",
                           stroke_color=WHITE,
                           stroke_width=2).scale(2).align_to(square,DOWN)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 100
        list_point = [shape[0].point_from_proportion(i / num_point)
                      for i in range(num_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=WHITE, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point, True):
                        dot.set_color(WHITE)
                        self.num_green += 1
                    else:
                        dot.set_color("#4267b2")
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(1000),
                  run_time=1,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))

class Scene6(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        square = Square(side_length=5, stroke_color=RED)
        shape = SVGMobject("pi",
                           stroke_color=RED,
                           stroke_width=2)[4].scale(2)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 200
        list_point = [shape[0].point_from_proportion(i / num_point)
                      for i in range(num_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=RED, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point, True):
                        dot.set_color(RED)
                        self.num_green += 1
                    else:
                        dot.set_color(WHITE)
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(1000),
                  run_time=1,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))

class Scene7(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        square = Square(side_length=5, stroke_color=ORANGE)
        shape = SVGMobject("bitcoin3",
                           stroke_color=ORANGE,
                           stroke_width=2).scale(2.2)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 200
        sub_point = 30
        list_point1 = [shape[0].point_from_proportion(i / num_point)
                      for i in range(num_point)]
        list_point2 = [shape[1].point_from_proportion(i / sub_point)
                      for i in range(sub_point)]
        list_point3 = [shape[2].point_from_proportion(i / sub_point)
                      for i in range(sub_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=ORANGE, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])
        s_shape[1].set_fill(color=WHITE)
        s_shape[2].set_fill(color=WHITE)

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point1, True) \
                            and is_in_shape(dot.get_center(), list_point2, True) \
                            and is_in_shape(dot.get_center(), list_point3, True):
                        dot.set_color(ORANGE)
                        self.num_green += 1
                    else:
                        dot.set_color(WHITE)
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(1000),
                  run_time=1,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))
