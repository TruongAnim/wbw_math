import math
import random

from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4",
              "Scene5", "Scene6", "Scene7", "Scene8", "Scene9",
              "Scene10", "Scene11", "Scene12", "Scene13", "Scene14",
              "Scene15", "Scene16", "Scene17", "Scene18", "Scene19",
              "Scene20", "Scene21", "Scene22", "Scene23", "Scene24", "Thumbnail")
# SCENE_NAME = list_scene[1]
SCENE_NAME = " ".join(list_scene[:20])
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


color_list = [RED, GOLD, YELLOW, GREEN, TEAL, BLUE, PURPLE]
color_list = color_list[::-1]
my_list = ["#C0392B", "#E74C3C", "#9B59B6", "#8E44AD", "#2980B9",
           "#3498DB", "#1ABC9C", "#16A085", "#27AE60", "#2ECC71",
           "#F1C40F", "#F39C12", "#E67E22", "#D35400", "#ECF0F1",
           "#BDC3C7", "#DFFF00", "#FFBF00", "#FF7F50", "#DE3163",
           "#9FE2BF", "#40E0D0", "#6495ED", "#CCCCFF"]


def random_color():
    return random.choice(my_list)


def random_color_list():
    return [random_color() for i in range(10)]


class MyGraph(VGroup):
    def __init__(self, source, x_range, n, **kwargs):
        super(MyGraph, self).__init__(**kwargs)
        func = FunctionGraph(source, x_range=x_range)
        func.set_color_by_gradient(random_color_list())
        list_func = [func.copy().rotate((360 / n) * i * DEGREES, about_point=ORIGIN) for i in range(1, n + 1)]
        self.add(*list_func)


class MultiGraph(VGroup):
    def __init__(self, graph1, graph2, **kwargs):
        super(MultiGraph, self).__init__(**kwargs)
        self.add(*graph1, *graph2.flip(RIGHT))


class Bullet(ArrowCircleFilledTip):
    def __init__(self, vector=RIGHT, **kwargs):
        super().__init__(**kwargs)
        self.scale(0.5)
        self.rotate(angle_of_vector(vector) + PI)
        self._vector = vector

    def get_angle(self):
        return angle_of_vector(self._vector)

    def get_vector(self):
        return self._vector

    def set_vector(self, vector: np.ndarray):
        previous_angle = self.get_angle()
        self._vector = vector
        self.rotate(angle_of_vector(vector) - previous_angle + PI)
        return self

    def set_angle(self, angle: float):
        previous_vector = self.get_vector()
        self.rotate(angle - self.get_angle())
        self._vector = rotate_vector(previous_vector, angle)
        return self


class PointCloud(VGroup):
    def __init__(self, n, angle, distance, **kwargs):
        super(PointCloud, self).__init__(**kwargs)
        d = 0
        a = 0
        start_angle = 0
        for i in range(n):
            obj = Bullet(rotate_vector(RIGHT, start_angle + a))
            obj.shift(d * obj.vector)
            d += distance
            a += angle
            self.add(obj)
        self.set_color_by_gradient(*random_color_list())

    def custom_rate(self, f):
        if f < 0.5:
            return rate_functions.ease_out_cubic(f * 2)
        elif f < 0.95:
            return 1
        else:
            return 0.001


class Firework():
    def __init__(self, start, h, graph):
        self.dot = Dot(start, color=RED)
        self.end = start + UP * h
        self.path = TracedPath(self.dot.get_center, dissipating_time=0.5, stroke_opacity=[0, 1], stroke_width=5,
                               stroke_color=[RED, YELLOW])
        self.graph = graph.move_to(self.end)

    def create_animation(self):
        shoot = self.dot.animate(rate_func=linear).move_to(self.end)
        fire = LaggedStart(FadeOut(self.dot),
                           Create(self.graph, lag_ratio=0, run_time=1,
                                  rate_func=rate_functions.ease_out_cubic), lag_ratio=0)
        fade = FadeOut(self.graph)
        if isinstance(self.graph, PointCloud):
            fire = LaggedStart(FadeOut(self.dot),
                               Create(self.graph, run_time=1, rate_func=rate_functions.ease_out_cubic)
                               , lag_ratio=0)
        return shoot, fire, fade

    def create_fade_out(self):
        return FadeOut(VGroup(self.dot, self.graph))


class Scene0(Scene):
    def construct(self):
        def create_laggedStart(firework):
            anim = firework.create_animation()
            self.add(firework.path)
            return LaggedStart(anim[0], anim[1], lag_ratio=1)

        def remove_firework(firework):
            self.remove(firework.path)
            return firework.create_fade_out()

        g = MyGraph(lambda t: t * t, x_range=[0, 2], n=20)
        g2 = MyGraph(lambda t: t * t * t, x_range=[0, 2], n=20)
        group = MultiGraph(g, g2)

        firework = Firework(DOWN * 3, 5, group)
        firework2 = Firework(DOWN * 3 + LEFT * 2, 5, g2.copy().scale(0.5))

        # self.play(LaggedStart(
        #     create_laggedStart(firework),
        #     create_laggedStart(firework2),
        #     lag_ratio=0.5
        # ))
        # self.wait()
        p = PointCloud(100, 1, 0.1).scale(1)
        self.play(Create(p), run_time=1, rate_func=rate_functions.ease_out_cubic)
        self.wait()
        # self.play(LaggedStart(
        #     remove_firework(firework),
        #     remove_firework(firework2),
        #     lag_ratio=0.5
        # ))


class Scene1(Scene):
    def construct(self):
        g = MyGraph(lambda t: t * t, x_range=[0, 2], n=20)
        g2 = MyGraph(lambda t: t * t, x_range=[0, 2], n=20)
        group = MultiGraph(g, g2).scale(0.4)
        firework = Firework(DOWN * 4, 5, group)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene2(Scene):
    def construct(self):
        g = MyGraph(lambda t: t * t * t, x_range=[0, 2], n=20)
        g2 = MyGraph(lambda t: t * t * t, x_range=[0, 2], n=20)
        group = MultiGraph(g, g2).scale(0.2)
        firework = Firework(DOWN * 4, 5, group)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene3(Scene):
    def construct(self):
        g = MyGraph(lambda t: t, x_range=[0, 2], n=30)
        g2 = MyGraph(lambda t: t, x_range=[0, 2], n=30)
        group = MultiGraph(g, g2).scale(0.6)
        firework = Firework(DOWN * 4, 5, group)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene4(Scene):
    def construct(self):
        g = MyGraph(lambda t: t * t, x_range=[0, 2], n=30).scale(0.6)
        firework = Firework(DOWN * 4, 5, g)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene5(Scene):
    def construct(self):
        g = MyGraph(lambda t: 0.1 * (t * t * t), x_range=[0, 3], n=30).scale(0.5)
        firework = Firework(DOWN * 4, 5, g)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene6(Scene):
    def construct(self):
        g = MyGraph(lambda t: 0.5 * math.sin(t), x_range=[0, 10], n=30).scale(0.2)
        firework = Firework(DOWN * 4, 5, g)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene7(Scene):
    def construct(self):
        g = MyGraph(lambda t: 0.5 * math.cos(t), x_range=[0, 10], n=30).scale(0.2)
        firework = Firework(DOWN * 4, 5, g)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene8(Scene):
    def construct(self):
        g = MyGraph(lambda t: math.sqrt(t ** 2 - t ** 4), x_range=[0, 1], n=15)
        g2 = MyGraph(lambda t: -math.sqrt(t ** 2 - t ** 4), x_range=[-1, 0], n=15)
        group = MultiGraph(g, g2).scale(2)
        firework = Firework(DOWN * 4, 5, group)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene9(Scene):
    def construct(self):
        g = MyGraph(lambda t: math.sqrt(t ** 2 - t ** 7), x_range=[-1, 1], n=15)
        g2 = MyGraph(lambda t: -math.sqrt(t ** 2 - t ** 7), x_range=[-1, 1], n=0)
        group = MultiGraph(g, g2).scale(1)
        firework = Firework(DOWN * 4, 5, group)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene10(Scene):
    def construct(self):
        g = MyGraph(lambda t: 1 / (10 * t), x_range=[0.1, 1], n=20).scale(2)
        firework = Firework(DOWN * 4, 5, g)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene11(Scene):
    def construct(self):
        g = MyGraph(lambda t: math.sqrt(t), x_range=[0, 1.5], n=20).scale(1.2)
        firework = Firework(DOWN * 4, 5, g)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene12(Scene):
    def construct(self):
        p = PointCloud(200, 1, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene13(Scene):
    def construct(self):
        p = PointCloud(200, 2, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene14(Scene):
    def construct(self):
        p = PointCloud(200, 3, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene15(Scene):
    def construct(self):
        p = PointCloud(200, 4, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene16(Scene):
    def construct(self):
        p = PointCloud(200, 5, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene17(Scene):
    def construct(self):
        p = PointCloud(200, 6, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene18(Scene):
    def construct(self):
        p = PointCloud(200, 7, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene19(Scene):
    def construct(self):
        p = PointCloud(200, 8, 0.1).scale(0.7)
        firework = Firework(DOWN * 4, 5, p)
        self.add(firework.path)
        anim1, anim2, anim3 = firework.create_animation()
        self.add_sound("5")
        self.play(anim1)
        self.remove(firework.path)
        self.play(anim2)
        self.play(anim3)


class Scene20(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            tips=False,
            x_length=7.5,
            y_length=7.5,
            axis_config={"include_numbers": True},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: 0.1 * (x ** 3), x_range=[-3.2, 3.2], use_smoothing=False, color=YELLOW)
        pt = MathTex("y=0.1x^3", color=YELLOW).scale(1.5).to_corner(UL, buff=SMALL_BUFF)
        graphs = VGroup(*[graph.copy().rotate(i * 18 * DEGREES) for i in range(10)])
        self.play(Create(ax))
        self.play(Create(graph), Write(pt))
        self.wait()
        self.play(Create(graphs), Rotate(graph, PI), rate_func=linear)
        self.wait()
        self.play(graphs.animate.set_color_by_gradient(random_color_list()))
        self.wait()


class Scene21(Scene):
    def construct(self):
        math1 = MathTex("y=x^2", color=YELLOW).scale(1).shift(DOWN * 3 + LEFT * 4)
        math2 = MathTex("y=0.1x^3", color=YELLOW).scale(1).shift(DOWN * 3)
        math3 = MathTex("y=0.5\sin(x)", color=YELLOW).scale(1).shift(DOWN * 3 + RIGHT * 4)
        self.add(math1, math2, math3)
