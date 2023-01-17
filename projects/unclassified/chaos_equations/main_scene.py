from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4",
              "Scene5", "Scene6", "Scene7", "Scene8", "Scene9", "Thumbnail")
SCENE_NAME = list_scene[4]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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


class Scene0(Scene):
    def construct(self):
        arr = [i for i in range(16)]

        def factory(i, j):
            def create_point():
                return np.array([arr[i], arr[j], 0])

            return create_point

        tracker = ValueTracker(-2)
        a = TracedPath(factory(0, 1), stroke_color=RED)
        b = TracedPath(factory(2, 3), stroke_color=GREEN)
        c = TracedPath(factory(3, 4), stroke_color=BLUE)
        d = TracedPath(factory(4, 5), stroke_color=BLUE)
        e = TracedPath(factory(5, 6), stroke_color=BLUE)

        def parametric_equation(x, y, t):
            return x + y, x - y

        def update_array():
            arr[0] = arr[1] = tracker.get_value()
            for i in range(2, len(arr), 2):
                arr[i], arr[i + 1] = parametric_equation(arr[i - 2], arr[i - 1], tracker.get_value())
            print(arr)
            return VMobject()

        redraw = always_redraw(update_array)
        self.add(tracker, redraw, a, b, c, d, e)
        self.play(tracker.animate.increment_value(3), run_time=4, rate_func=linear)
        self.wait()


class Scene1(Scene):
    def construct(self):
        iterr = 100

        arr_x = [i for i in range(iterr)]
        arr_y = [i for i in range(iterr)]

        def create_point(index):
            # print("first",index, arr_x[index], arr_y[index])
            x = (arr_x[index] / 1600) * config.frame_width
            y = (arr_y[index] / 900) * config.frame_height
            # print("second",index, x, y)
            return np.array([x, y, 0])

        tracker = ValueTracker(-2)

        def parametric_equation(x, y, t):
            if x > 10 ** 10 or y > 10 ** 10:
                return 10 ** 10, 10 ** 10
            if x < -10 ** 10 or y < -10 ** 10:
                return -10 ** 10, -10 ** 10
            new_x = -(t * t) - x * y + y * t - x + y
            new_y = -(x * x) - x * t
            return new_x, new_y

        def update_array():
            arr_x[0] = arr_y[0] = tracker.get_value()
            for i in range(1, iterr):
                arr_x[i], arr_y[i] = parametric_equation(arr_x[i - 1], arr_y[i - 1], arr_x[0])
            # print(arr_x)
            # print(arr_y)
            # print(arr_x, arr_y)
            return VGroup(*[Dot(create_point(i)) for i in range(iterr)])

        redraw = always_redraw(update_array)
        self.add(tracker, redraw)
        self.play(tracker.animate.increment_value(4), run_time=4, rate_func=linear)
        self.wait()


class Scene2(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=PI / 4).shift(RIGHT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(RIGHT * 2))
        self.wait()


class Scene3(Scene):
    def construct(self):
        tracker = ValueTracker(-2)

        def get_point():
            x = tracker.get_value()
            y = x ** 2
            return np.array([x, y, 0])

        path = TracedPath(get_point, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(path, tracker)
        self.play(tracker.animate.increment_value(4), run_time=3)
        self.wait()


class Scene4(Scene):
    def construct(self):
        circ = Circle(color=RED).shift(4 * LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start, dissipating_time=1, stroke_opacity=[1, 0], stroke_width=5)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=4, rate_func=linear)