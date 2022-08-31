import random
from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4")
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
        self.wait()


class Scene1(MyScene):
    def construct(self):
        square = Square(stroke_color=YELLOW, fill_color=YELLOW_A)
        circle = Circle(fill_color=RED_A)
        triangle = Triangle(fill_color=BLUE_A)
        group_shape = VGroup(square, circle, triangle) \
            .arrange(RIGHT, buff=LARGE_BUFF) \
            .scale(1.5)

        area_square = MathTex("S=a^2", color=YELLOW).next_to(square, DOWN)
        area_circle = MathTex("S=\pi r^2", color=RED).next_to(circle, DOWN)
        area_triangle = MathTex("S={1 \over 2}bh", color=BLUE).next_to(triangle, DOWN)

        group_formula = VGroup(area_square, area_circle, area_triangle)

        self.my_play(LaggedStart(*[
            Write(i) for i in group_shape
        ], lag_ratio=0.2))

        self.my_play(
            square.animate.set_fill(opacity=0.8),
            circle.animate.set_fill(opacity=0.8),
            triangle.animate.set_fill(opacity=0.8),
            Write(group_formula)
        )


class Scene2(MyScene):
    def construct(self):
        A = np.array([0, 0, 0])
        B = np.array([1, 1, 0])
        C = np.array([2, 0, 0])
        D = np.array([2, -1, 0])
        E = np.array([1, -1.5, 0])
        F = np.array([-0.5, -2.5, 0])
        G = np.array([-1.5, 0, 0])

        shape = VMobject(fill_color=YELLOW,
                         fill_opacity=0.8,
                         stroke_color=RED,
                         stroke_width=3) \
            .set_points_smoothly([A, B, C, D, E, F, G, A]).shift(UP)
        area = Text("Area?").move_to(shape)

        pi = NumberCreature(file_name_prefix="PiCreatures", mode="wonder") \
            .to_corner(DL)

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(area))
        self.my_play(FadeIn(pi, shift=RIGHT * 2))
        bubble_kwargs = {
            "stroke_width": 3,
            "stroke_color": WHITE,
            "stretch_height": 2,
            "stretch_width": 3.5
        }
        self.my_play(
            NumberCreatureSays(pi,
                               Text(r"Hay là chia thành tam giác?",
                                    font_size=35)
                               , target_mode="wonder",
                               bubble_kwargs=bubble_kwargs)
        )
        self.my_play(FadeOut(area))
        num_point = 20
        list_point = [shape.point_from_proportion(i / num_point)
                      for i in range(num_point)]
        list_tri = VGroup(
            *[VMobject().set_points_as_corners(
                [list_point[0],
                 list_point[i],
                 list_point[i + 1]]
            ) for i in range(1, num_point - 1)]
        )
        self.my_play(LaggedStart(*[
            Write(i)
            for i in list_tri
        ], lag_ratio=0.2))


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


def is_in_shape(point, P_list):
    n = closest_point(P_list, point)
    l = len(P_list)
    tangent_vector = P_list[(n + 1) % l] - P_list[(n - 1) % l]
    to_target_vector = point - P_list[n]
    cross_product_res = cross_product(tangent_vector, to_target_vector)
    return cross_product_res[2] <= 0


class Scene3(MyScene):
    def get_random_position(self):
        x = random.uniform(-1.75, 2.25)
        y = random.uniform(-1.75, 2.25)
        return np.array([x, y, 0])

    def construct(self):
        A = np.array([0, 0, 0])
        B = np.array([1, 1, 0])
        C = np.array([2, 0, 0])
        D = np.array([2, -1, 0])
        E = np.array([1, -1.5, 0])
        F = np.array([-0.5, -2.5, 0])
        G = np.array([-1.5, 0, 0])

        shape = VMobject(fill_color=YELLOW,
                         fill_opacity=0.8,
                         stroke_color=RED,
                         stroke_width=3) \
            .set_points_smoothly([A, B, C, D, E, F, G, A]).shift(UP)
        square = Square(side_length=4).move_to(shape)
        brace = Brace(square, UP)
        side = brace.get_tex("a=","4m")
        num_point = 30
        num_dot = 50
        num_green = 0
        list_point = [shape.point_from_proportion(i / num_point)
                      for i in range(num_point)]
        # points = VGroup(*[Dot(i) for i in list_point])
        # self.add(points)

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))

        dots = VGroup(
            *[
                Dot(self.get_random_position())
                for i in range(num_dot)
            ])

        for dot in dots:
            if is_in_shape(dot.get_center(), list_point):
                dot.set_color(GREEN)
                num_green+=1
        self.my_play(LaggedStart(*[
            FadeIn(dot)
            for dot in dots
        ], lag_ratio=0.1))

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")
        formula1 = MathTex(
            r"{\text{Số chấm xanh}",#0
            r"\over",               #1
            r"\text{Tổng số chấm}}",#2
            r"\approx",                   #3
            r"{S_",                 #4
            "{ab}",                 #5
            r"\over",               #6
            r"S_{\square }}",       #7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT*4.5)
        formula1[5].set_color(BLACK)
        s_shape1 = shape.copy()\
            .set_stroke(width=0)\
            .scale(0.07)\
            .move_to(formula1[5])
        formula2 = MathTex(
            r"S_",                  #0
            r"{ab}",                #1
            r"\approx",                   #2
            r"{\text{Số chấm xanh}",#3
            r"\over",               #4
            r"\text{Tổng số chấm}}",#5
            r"\times",              #6
            r"S_{\square}",         #7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT*4.5)
        formula2[1].set_color(BLACK)
        s_shape2 = shape.copy()\
            .set_stroke(width=0)\
            .scale(0.07)\
            .move_to(formula2[1])
        self.my_play(LaggedStart(*[Write(formula1), Write(s_shape1)], lag_ratio=0.7))
        self.my_play(
            ReplacementTransform(formula1[0], formula2[3]),
            ReplacementTransform(formula1[1], formula2[4]),
            ReplacementTransform(formula1[2], formula2[5]),
            ReplacementTransform(formula1[3], formula2[2], path_arc=PI),
            ReplacementTransform(formula1[4], formula2[0], path_arc=PI),
            ReplacementTransform(formula1[5], formula2[1]),
            ReplacementTransform(formula1[6], formula2[6]),
            ReplacementTransform(formula1[7], formula2[7]),
            ReplacementTransform(s_shape1, s_shape2, path_arc=PI),
        )
        dot_green = MathTex(str(num_green), color=GREEN)\
            .scale(0.8)\
            .move_to(formula2[3])
        dot_total = MathTex(str(num_dot), color=RED)\
            .scale(0.8)\
            .move_to(formula2[5])
        square_area = MathTex("16m^2")\
            .scale(0.7)\
            .next_to(formula2[6], RIGHT, buff=SMALL_BUFF)
        self.my_play(
            ReplacementTransform(formula2[3], dot_green),
            ReplacementTransform(formula2[5], dot_total),
            ReplacementTransform(formula2[7], square_area),
            Transform(side[1].copy(), square_area, path_arc=PI)
        )
        result = "{:.5}".format(16*num_green/num_dot)
        s = MathTex(r"\approx", result, "m^2")\
            .scale(0.7)\
            .next_to(formula2[2], DOWN, buff=LARGE_BUFF, aligned_edge=LEFT)
        self.my_play(Write(s))
        self.wait()

        for i in (100, 500, 1000):
            new_dot = i
            num_dot+=new_dot
            dots2 = VGroup(
                *[
                    Dot(self.get_random_position())
                    for i in range(new_dot)
                ])

            for dot in dots2:
                if is_in_shape(dot.get_center(), list_point):
                    dot.set_color(GREEN)
                    num_green += 1

            new_dot_green = MathTex(str(num_green), color=GREEN) \
                .scale(0.8) \
                .move_to(formula2[3])
            new_dot_total = MathTex(str(num_dot), color=RED) \
                .scale(0.8) \
                .move_to(formula2[5])
            result = "{:.5}".format(16 * num_green / num_dot)
            # \approx
            new_s = MathTex(r"\approx", result, "m^2") \
                .scale(0.7) \
                .next_to(formula2[2], DOWN, buff=LARGE_BUFF, aligned_edge=LEFT)

            self.my_play(
                LaggedStart(*[
                    FadeIn(dot)
                    for dot in dots2
                ], run_time=2),
                *[Transform(i, j)
                    for i,j in zip((dot_green, dot_total, s),
                    (new_dot_green, new_dot_total, new_s))
                ], run_time=2)


class Scene4(MyScene):
    def get_random_position(self):
        x = random.uniform(-1.75, 2.25)
        y = random.uniform(-1.75, 2.25)
        return np.array([x, y, 0])

    def construct(self):
        A = np.array([0, 0, 0])
        B = np.array([1, 1, 0])
        C = np.array([2, 0, 0])
        D = np.array([2, -1, 0])
        E = np.array([1, -1.5, 0])
        F = np.array([-0.5, -2.5, 0])
        G = np.array([-1.5, 0, 0])

        shape = VMobject(fill_color=YELLOW,
                         fill_opacity=0.8,
                         stroke_color=RED,
                         stroke_width=3) \
            .set_points_smoothly([A, B, C, D, E, F, G, A]).shift(UP)
        square = Square(side_length=4).move_to(shape)
        brace = Brace(square, UP)
        side = brace.get_tex("a=","4(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))

        num_point = 30
        list_point = [shape.point_from_proportion(i / num_point)
                      for i in range(num_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",                  #0
            r"{ab}",                #1
            r"\approx",                   #2
            r"{\text{Số chấm xanh}",#3
            r"\over",               #4
            r"\text{Tổng số chấm}}",#5
            r"\times",              #6
            r"16(m^2)",         #7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT*4.5)
        for i in (1,3,5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy()\
            .set_stroke(width=0)\
            .scale(0.07)\
            .move_to(formula[1])

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN+LEFT)

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
            if self.num_dot!=0:
                result = "{:.5f}".format(16 * self.num_green / self.num_dot)
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
                more_point = int(value)-self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point):
                        dot.set_color(GREEN)
                        self.num_green += 1
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(50000),
                  run_time=15,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))
