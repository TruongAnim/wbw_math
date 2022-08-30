import random
from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
SCENE_NAME = list_scene[2]
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

        self.play(LaggedStart(*[
            Write(i) for i in group_shape
        ], lag_ratio=0.2))

        self.play(
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

        self.play(DrawBorderThenFill(shape))
        self.play(Write(area))
        self.play(FadeIn(pi, shift=RIGHT * 2))
        bubble_kwargs = {
            "stroke_width": 3,
            "stroke_color": WHITE,
            "stretch_height": 2,
            "stretch_width": 3.5
        }
        self.play(
            NumberCreatureSays(pi,
                               Text(r"Hay là chia thành tam giác?",
                                    font_size=35)
                               , target_mode="wonder",
                               bubble_kwargs=bubble_kwargs)
        )
        self.play(FadeOut(area))
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
        self.play(LaggedStart(*[
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
        side = brace.get_tex("a=2m")
        num_point = 20
        list_point = [shape.point_from_proportion(i / num_point)
                      for i in range(num_point)]
        self.play(DrawBorderThenFill(shape))
        self.play(Write(square))
        self.play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_dot = 30
        dots = VGroup(
            *[
                Dot(self.get_random_position())
                for i in range(num_dot)
            ])
        for dot in dots:
            if is_in_shape(dot.get_center(), list_point):
                dot.set_color(GREEN)
        self.play(LaggedStart(*[
            FadeIn(dot)
            for dot in dots
        ], lag_ratio=0.1))
