from manim import *
from common.utils.color_utils import interpolate_color_range

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4")
# SCENE_NAME = list_scene[1]
SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

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


class Scene0(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=3.9, stroke_color=YELLOW)
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center() - ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2, color=YELLOW)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN), out_circle)

        def fix_error(f):
            if f >= 1:
                return f % 1
            return f

        def make_points():
            diff = value.get_value() - self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                if p.my_radius > 3:
                    list_point.remove(p)
                else:
                    # p.set_color(interpolate_color_range(GREEN, YELLOW, p.my_radius/4.5))
                    p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle / (2 * PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        angle = 40
        # for i in range(1, 300):
        #     self.play(value.animate.increment_value(0.03), run_time=0.02, rate_func=linear)
        #     list_point.append(self.MyPoint(my_angle=i * (angle * DEGREES), my_radius=0.2, color=YELLOW))
        #     print(len(list_point))
        #     if i % 20 == 0:
        #         angle += 3
        # for i in range(1, 125):
        #     self.play(value.animate.increment_value(0.03), run_time=0.02, rate_func=linear)
        #     list_point.append(self.MyPoint(my_angle=i*(50*DEGREES), my_radius=0.2, color=YELLOW))
        #     print(len(list_point))


class Bullet(ArrowCircleFilledTip):
    def __init__(self, vector=RIGHT, **kwargs):
        super().__init__(**kwargs)
        self.scale(0.3)
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


color_list = [RED, GOLD, YELLOW, GREEN, TEAL, BLUE, PURPLE]
color_list = color_list[::-1]
v = 20


class Scene1(Scene):
    def construct(self):
        vg1 = VGroup()
        vg2 = VGroup()
        vg3 = VGroup()
        self.time = 0

        def update_one_trace(start_angle: float):
            def update(mob, dt):
                mob.add(Bullet(rotate_vector(RIGHT, start_angle+self.time**2)))
                mob.set_color_by_gradient(*color_list)
                for o in mob:
                    o.shift(v * dt * o.vector)
                    if o.is_off_screen():
                        mob.remove(o)

            return update
        def update_time(mob, dt):
            self.time = tracker.get_value()
            pass

        vg1.add_updater(update_time)
        vg1.add_updater(update_one_trace(0))
        vg2.add_updater(update_one_trace(120*DEGREES))
        vg3.add_updater(update_one_trace(240*DEGREES))
        self.add(vg1, vg2, vg3)
        tracker = ValueTracker(0)
        self.play(tracker.animate.increment_value(60), run_time=30, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)


class Scene2(Scene):
    def construct(self):
        vg1 = VGroup()
        vg2 = VGroup()
        vg3 = VGroup()
        self.time = 0

        def update_one_trace(start_angle: float):
            def update(mob, dt):
                mob.add(Bullet(rotate_vector(RIGHT, start_angle+self.time**2)))
                mob.set_color_by_gradient(*color_list)
                for o in mob:
                    o.shift(v * dt * o.vector)
                    if o.is_off_screen():
                        mob.remove(o)

            return update
        def update_time(mob, dt):
            self.time = tracker.get_value()
            pass

        vg1.add_updater(update_time)
        vg1.add_updater(update_one_trace(0))
        vg2.add_updater(update_one_trace(180*DEGREES))
        # vg3.add_updater(update_one_trace(240*DEGREES))
        self.add(vg1, vg2)
        tracker = ValueTracker(0)
        self.play(tracker.animate.increment_value(60), run_time=30, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)

class Scene3(Scene):
    def construct(self):
        vg1 = VGroup()
        vg2 = VGroup()
        vg3 = VGroup()
        self.time = 0

        def update_one_trace(start_angle: float):
            def update(mob, dt):
                mob.add(Bullet(rotate_vector(RIGHT, start_angle+self.time**2)))
                mob.set_color_by_gradient(*color_list)
                for o in mob:
                    o.shift(v * dt * o.vector)
                    if o.is_off_screen():
                        mob.remove(o)

            return update
        def update_time(mob, dt):
            self.time = tracker.get_value()
            pass

        vg1.add_updater(update_time)
        vg1.add_updater(update_one_trace(0))
        vg2.add_updater(update_one_trace(120*DEGREES))
        vg3.add_updater(update_one_trace(240*DEGREES))
        self.add(vg1, vg2)
        tracker = ValueTracker(0)
        self.play(tracker.animate.increment_value(120), run_time=60, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)

class Scene4(Scene):
    def construct(self):
        vg1 = VGroup()
        vg2 = VGroup()
        vg3 = VGroup()
        self.time = 0

        def update_one_trace(start_angle: float):
            def update(mob, dt):
                mob.add(Bullet(rotate_vector(RIGHT, start_angle+self.time**2)))
                mob.set_color_by_gradient(*color_list)
                for o in mob:
                    o.shift(v * dt * o.vector)
                    if o.is_off_screen():
                        mob.remove(o)

            return update
        def update_time(mob, dt):
            self.time = tracker.get_value()
            pass

        vg1.add_updater(update_time)
        vg1.add_updater(update_one_trace(0))
        vg2.add_updater(update_one_trace(180*DEGREES))
        # vg3.add_updater(update_one_trace(240*DEGREES))
        self.add(vg1, vg2)
        tracker = ValueTracker(0)
        self.play(tracker.animate.increment_value(120), run_time=60, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)
        # self.play(tracker.animate.increment_value(-20), run_time=5, rate_func=linear)


omega = 0.25
side_length = 10


class Scene5(Scene):
    def construct(self):
        vg = VGroup()
        self.count = 0
        self.time=0

        def update_danmaku(mob: VGroup, dt: float):
            if self.count % 15 == 0:
                vectors = np.array([
                    rotate_vector(v * RIGHT, self.time * omega),
                    rotate_vector(v * UP, self.time * omega),
                    rotate_vector(v * LEFT, self.time * omega),
                    rotate_vector(v * DOWN, self.time * omega),
                ])
                mob.add(*[
                    Bullet(interpolate(
                        vectors[j % 4], vectors[(j + 1) % 4], k / side_length))
                    for k in range(side_length)
                    for j in range(4)
                ])
            for o in mob:
                o.shift(dt * o._vector)
                if o.is_off_screen():
                    mob.remove(o)
            mob.set_color_by_gradient(*color_list)
            self.count += 1

        vg.add_updater(update_danmaku)
        self.add(vg)
        self.wait(3)

class Scene3(Scene):
    def construct(self):
        b = Bullet().shift(RIGHT)
        self.add(b, Dot(), ArrowCircleFilledTip())