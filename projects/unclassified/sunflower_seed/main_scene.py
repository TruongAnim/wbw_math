from manim import *
from common.utils.color_utils import interpolate_color_range

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4",
              "Scene5", "Scene6", "Scene7", "Scene8", "Scene9", "Thumbnail")
SCENE_NAME = list_scene[-1]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

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


class Scene0(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint())
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        for i in range(1, 20):
            self.play(value.animate.increment_value(0.01), run_time=0.02, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            list_point.append(self.MyPoint(my_angle=i*(137.5*DEGREES), my_radius=0.2))


class Scene1(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=3.9, stroke_color=YELLOW)
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2, color=YELLOW)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN), out_circle)
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.set_color(interpolate_color_range(GREEN, YELLOW, p.my_radius/4.5))
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        for i in range(1, 125):
            self.play(value.animate.increment_value(0.03), run_time=0.02, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            list_point.append(self.MyPoint(my_angle=i*(45*DEGREES), my_radius=0.2, color=YELLOW))


class Scene2(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=3.9, stroke_color=YELLOW)
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2, color=YELLOW)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN), out_circle)
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.set_color(interpolate_color_range(GREEN, YELLOW, p.my_radius/4.5))
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        for i in range(1, 185):
            self.play(value.animate.increment_value(0.02), run_time=0.02, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            list_point.append(self.MyPoint(my_angle=i*(65*DEGREES), my_radius=0.2, color=YELLOW))


class Scene3(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=1.5, stroke_color=YELLOW)
        circle = Circle(radius=1)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=1, color=GREEN)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN))
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        m = MathTex("65^\circ")
        for i in range(1, 10):
            self.play(value.animate.increment_value(0.5), run_time=1, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            new_point = self.MyPoint(my_angle=i * (65 * DEGREES), my_radius=1, color=GREEN).move_to(
                circle.point_from_proportion(fix_error(i * (65 * DEGREES)/(2*PI)))
            )
            l1 = Line(ORIGIN, out_circle.point_from_proportion(fix_error(list_point[-1].my_angle/(2*PI))))
            l2 = Line(ORIGIN, out_circle.point_from_proportion(fix_error(i * (65 * DEGREES)/(2*PI))))
            self.play(Create(l1), Create(l2),
                      Write(m.move_to(out_circle.point_from_proportion(fix_error((i-0.5) * (65 * DEGREES)/(2*PI))))),
                      FadeIn(new_point),
                      Flash(new_point))
            self.remove(l1, l2, m)
            list_point.append(new_point)
        self.wait()
        out_circle.set_fill(color=YELLOW, opacity=0.3)
        self.add(points)
        self.wait()


class Scene4(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=1.5, stroke_color=YELLOW)
        circle = Circle(radius=1)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=1, color=GREEN)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN))
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        m = MathTex("137.5^\circ")
        for i in range(1, 10):
            self.play(value.animate.increment_value(0.5), run_time=1, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            new_point = self.MyPoint(my_angle=i * (137.5 * DEGREES), my_radius=1, color=GREEN).move_to(
                circle.point_from_proportion(fix_error(i * (137.5 * DEGREES)/(2*PI)))
            )
            l1 = Line(ORIGIN, out_circle.point_from_proportion(fix_error(list_point[-1].my_angle/(2*PI))))
            l2 = Line(ORIGIN, out_circle.point_from_proportion(fix_error(i * (137.55 * DEGREES)/(2*PI))))
            self.play(Create(l1), Create(l2),
                      Write(m.move_to(out_circle.point_from_proportion(fix_error((i-0.5) * (137.55 * DEGREES)/(2*PI))))),
                      FadeIn(new_point),
                      Flash(new_point))
            self.remove(l1, l2, m)
            list_point.append(new_point)
        self.wait()
        out_circle.set_fill(color=YELLOW, opacity=0.3)
        self.add(points)
        self.wait()


class Scene5(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=3.9, stroke_color=YELLOW)
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2, color=YELLOW)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN), out_circle)
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.set_color(interpolate_color_range(GREEN, YELLOW, p.my_radius/4.5))
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        for i in range(1, 125):
            self.play(value.animate.increment_value(0.03), run_time=0.02, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            list_point.append(self.MyPoint(my_angle=i*(136*DEGREES), my_radius=0.2, color=YELLOW))


class Scene6(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=3.9, stroke_color=YELLOW)
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2, color=YELLOW)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN), out_circle)
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.set_color(interpolate_color_range(GREEN, YELLOW, p.my_radius/4.5))
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        for i in range(1, 183):
            self.play(value.animate.increment_value(0.02), run_time=0.02, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            list_point.append(self.MyPoint(my_angle=i*(140*DEGREES), my_radius=0.2, color=YELLOW))


class Scene7(MyScene):
    class MyPoint(Dot):
        def __init__(self, my_angle=0, my_radius=1, **kwargs):
            self.my_angle = my_angle
            self.my_radius = my_radius
            super().__init__(**kwargs)

    def construct(self):
        out_circle = Circle(radius=3.9, stroke_color=YELLOW)
        circle = Circle(radius=0.2)
        dot = Dot(circle.point_from_proportion(0))
        direction = dot.get_center()-ORIGIN
        list_point = [self.MyPoint(my_angle=0, my_radius=0.2, color=YELLOW)]

        value = ValueTracker(1)
        self.pevius_value = value.get_value()
        self.add(self.MyPoint(color=GREEN), out_circle)
        def fix_error(f):
            if f>=1:
                return f%1
            return f

        def make_points():
            diff = value.get_value()-self.pevius_value
            self.pevius_value = value.get_value()
            for p in list_point:
                p.my_radius += diff
                p.set_color(interpolate_color_range(GREEN, YELLOW, p.my_radius/4.5))
                p.move_to(Circle(radius=p.my_radius).point_from_proportion(fix_error(p.my_angle/(2*PI))))
            return VGroup(*list_point)

        points = always_redraw(make_points)
        self.add(value, points)
        self.add(circle)
        for i in range(1, 380):
            self.play(value.animate.increment_value(0.01), run_time=0.02, rate_func=linear)
            for j in list_point:
                j.scale(1.002)
            list_point.append(self.MyPoint(my_angle=i*(137.5*DEGREES), my_radius=0.2, color=YELLOW))

# 0.01 0.02
# 1.002

class Scene8(MyScene):
    def construct(self):
        t = Text("Tỉ lệ vàng", font_size=80, font="Sans", color=YELLOW).shift(UP)
        m = MathTex(r"\varphi", "=", "1.618033...").scale(2).next_to(t, DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(t, shift=UP))
        self.play(AddTextLetterByLetter(m[2]), FadeIn(m[0:2], shift=RIGHT))
        self.wait()


class Scene9(MyScene):
    def construct(self):
        circle = Circle(radius=2.5, color=GREEN, stroke_width=5).rotate(PI/2).shift(UP)
        out_circle = Circle(radius=3).shift(UP).rotate(PI/2)
        line1 = Line(circle.get_center(), circle.point_from_proportion(0.618))
        line2 = Line(circle.get_center(), circle.point_from_proportion(0))

        arc1 = circle.get_subcurve(0, 0.618).set_color(RED)
        arc2 = circle.get_subcurve(0.618, 1).set_color(BLUE)
        a = MathTex("a", color=RED).move_to(out_circle.point_from_proportion(0.3))
        b = MathTex("b", color=BLUE).move_to(out_circle.point_from_proportion(0.85))
        angle = Angle(line1, line2, radius=0.4, color=YELLOW)
        angle_t = MathTex("137.5^\circ", color=YELLOW).move_to(Angle(line1, line2, radius=2.2))
        m = MathTex("{a", "\over ", "b}",  "=",  "1.61803").next_to(circle, DOWN)
        m[0].set_color(RED)
        m[2].set_color(BLUE)
        m[4].set_color(YELLOW)
        text = Text("Góc vàng", font_size=40, font="Sans", color=YELLOW).to_corner(UR)
        arrow = Arrow(text.get_left(), angle_t.get_top())
        self.play(Create(circle), run_time=0.5)
        self.play(Create(arc1), Create(arc2), Create(line2), Create(line1))
        self.play(FadeIn(a, shift=RIGHT), FadeIn(b, shift=LEFT), Write(m))
        self.wait(0.5)
        self.play(Create(angle), Write(angle_t))
        self.play(Write(text), GrowArrow(arrow))
        self.wait()
        self.add(circle, line1, line2, arc1, arc2, a, b, angle, angle_t, m, text, arrow)


class Thumbnail(MyScene):
    def construct(self):
        a = ImageMobject("thumbnail").scale(0.8)
        d1 = MathTex("136^\circ", color=RED).scale(3).move_to(LEFT*5+DOWN*1.5)
        d2 = MathTex("???", color=YELLOW).scale(3).move_to(DOWN*1.5)
        d3 = MathTex("140^\circ", color=BLUE).scale(3).move_to(RIGHT*5+DOWN*1.5)
        self.add(a, d1, d2, d3)