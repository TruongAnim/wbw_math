import math

from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10",
              "Scene11", "Scene12", "Scene13", "Scene14")
SCENE_NAME = list_scene[13]
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
        dash_line = DashedLine(start=UP * 3 + RIGHT * 0.001, end=DOWN)
        square = Square(side_length=3)
        line = Line(start=UP * 1.5, end=ORIGIN)
        group = VGroup(square, line)

        def create_angle():
            angle = Angle(dash_line, line, quadrant=(-1, -1), color=RED)
            value = DecimalNumber(angle.get_value(degrees=True),
                                  num_decimal_places=0,
                                  unit="^{\circ}",
                                  color=RED) \
                .scale(0.7) \
                .next_to(angle.get_top(), UL, buff=SMALL_BUFF)
            return VGroup(angle, value)

        angle_group = always_redraw(create_angle)
        pi_right = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True).to_corner(DR)
        pi_left = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 3,
            "stretch_height": 1.5
        }
        self.my_play(Create(square),
                     FadeIn(pi_right, shift=LEFT * 2),
                     FadeIn(pi_left, shift=RIGHT * 2))
        self.my_play(NumberCreatureSays(pi_right,
                                        MathTex(r"\text{Rotate }60^\circ"),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.my_play(NumberCreatureSays(pi_left,
                                        Text("Okay!"),
                                        target_mode="smile1",
                                        bubble_kwargs=bubble_kwargs))
        self.add(dash_line, angle_group)
        self.my_play(Rotate(group, PI / 3, about_point=ORIGIN))


class Scene2(MyScene):
    def construct(self):
        dash_line = DashedLine(start=UP * 3 + RIGHT * 0.001, end=DOWN)
        square = Square(side_length=3)
        line = Line(start=UP * 1.5, end=ORIGIN)
        group = VGroup(square, line)

        def create_angle():
            angle = Angle(dash_line, line, quadrant=(-1, -1), color=RED)
            value = DecimalNumber(angle.get_value(degrees=True),
                                  num_decimal_places=0,
                                  unit="^{\circ}",
                                  color=RED) \
                .scale(0.7) \
                .next_to(angle.get_top(), UL, buff=SMALL_BUFF)
            return VGroup(angle, value)

        angle_group = always_redraw(create_angle)
        pi_right = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True).to_corner(DR)
        pi_left = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 3,
            "stretch_height": 1.5
        }
        self.my_play(Create(square),
                     FadeIn(pi_right, shift=LEFT * 2),
                     FadeIn(pi_left, shift=RIGHT * 2))
        self.my_play(NumberCreatureSays(pi_right,
                                        MathTex(r"\text{Rotate }{\pi\over3} rad"),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.my_play(NumberCreatureSays(pi_left,
                                        Text("Wait... what?"),
                                        target_mode="wonder",
                                        bubble_kwargs=bubble_kwargs))
        self.wait()


class Scene3(MyScene):
    def construct(self):
        l1 = Line(start=ORIGIN, end=RIGHT * 3, color=GREEN)
        l2 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE).rotate(30 * DEGREES, about_point=ORIGIN)
        self.play(Create(l1), Create(l2))

        def create_angle():
            angle = Angle(l1, l2, quadrant=(1, 1), color=RED)
            angle2 = Angle(l1, l2, quadrant=(1, 1), radius=0.8)
            value = DecimalNumber(angle.get_value(degrees=True),
                                  num_decimal_places=0,
                                  unit="^{\circ}",
                                  color=RED) \
                .scale(0.7) \
                .move_to(angle2.point_from_proportion(0.5))
            return VGroup(angle, value)

        angle = always_redraw(create_angle)
        self.add(angle)

        self.play(Rotate(l2, PI / 2, about_point=ORIGIN))
        self.play(Rotate(l2, -PI / 4, about_point=ORIGIN))
        self.play(Rotate(l2, PI, about_point=ORIGIN))


class Scene4(MyScene):
    def construct(self):
        l1 = Line(start=ORIGIN, end=RIGHT * 3, color=GREEN)
        l2 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE).rotate(30 * DEGREES, about_point=ORIGIN)
        self.play(Create(l1), Create(l2))

        def create_angle():
            angle = Angle(l1, l2, quadrant=(1, 1), color=RED)
            angle2 = Angle(l1, l2, quadrant=(1, 1), radius=1)
            value = DecimalNumber(angle.get_value(degrees=False),
                                  num_decimal_places=2,
                                  unit="^{rad}",
                                  color=RED) \
                .scale(0.7) \
                .move_to(angle2.point_from_proportion(0.5))
            return VGroup(angle, value)

        angle = always_redraw(create_angle)
        self.add(angle)

        self.play(Rotate(l2, PI / 2, about_point=ORIGIN))
        self.play(Rotate(l2, -PI / 4, about_point=ORIGIN))
        self.play(Rotate(l2, PI, about_point=ORIGIN))


class Scene5(MyScene):
    def construct(self):
        proportion = 0.2
        circle = Circle(radius=3, color=WHITE)
        A = circle.point_from_proportion(proportion)
        line1 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE)
        line2 = Line(start=ORIGIN, end=A, color=BLUE)
        arc = circle.get_subcurve(0, proportion)
        arc.set_color(RED)
        angle = Angle(line1, line2, quadrant=(1, 1), color=YELLOW)
        phi = MathTex(r"\phi", color=YELLOW).next_to(angle, UR, buff=0.1)
        r = MathTex("r", color=BLUE).next_to(line1, UP)
        a = MathTex("a", color=RED) \
            .next_to(circle.point_from_proportion(proportion / 2), UR, buff=0.1)
        phi2 = MathTex(r"\phi", "=", "{a", r"\over", "r", "}{(rad)}") \
            .next_to(circle, RIGHT, buff=LARGE_BUFF)
        for i, j in zip((0, 2, 4),
                        (YELLOW, RED, BLUE)):
            phi2[i].set_color(j)

        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (circle, line1, r)
        ]))
        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (line2, angle, phi, arc, a)
        ]))
        self.play(*[
            Write(phi2[i])
            for i in (1, 3, 5)
        ])
        self.play(LaggedStart(*[
            Transform(i.copy(), phi2[j])
            for i, j in zip((r, a, phi),
                            (4, 2, 0))
        ]))
        self.add(circle, line1, line2, arc, angle, phi, r, a, phi2)


class Scene6(MyScene):
    def construct(self):
        proportion = 1 / (2 * PI)
        circle = Circle(radius=3, color=WHITE)
        A = circle.point_from_proportion(proportion)
        line1 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE)
        line2 = Line(start=ORIGIN, end=A, color=BLUE)
        arc = circle.get_subcurve(0, proportion)
        arc.set_color(RED)
        angle = Angle(line1, line2, quadrant=(1, 1), color=YELLOW)
        angle2 = Angle(line1, line2, quadrant=(1, 1), radius=1)
        phi = MathTex(r"\phi", color=YELLOW).move_to(angle2)
        r = MathTex("r", color=BLUE).next_to(line1, UP)
        a = MathTex("r", color=RED) \
            .next_to(circle.point_from_proportion(proportion / 2), UR, buff=0.1)
        phi2 = MathTex(r"\phi", "=", "{r", r"\over", "r", "}=1^{rad}") \
            .next_to(circle, RIGHT, buff=LARGE_BUFF)
        degree = MathTex(r"(\approx 57.29^\circ)").next_to(phi2, DOWN)
        for i, j in zip((0, 2, 4),
                        (YELLOW, RED, BLUE)):
            phi2[i].set_color(j)

        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (circle, line1, r, line2, angle, phi, arc, a)
        ]))
        self.play(*[
            Write(phi2[i])
            for i in (1, 3)
        ])
        self.play(LaggedStart(*[
            Transform(i.copy(), phi2[j])
            for i, j in zip((r, a, phi),
                            (4, 2, 0))
        ]))
        self.play(Write(phi2[5]), Write(degree))
        self.add(circle, line1, line2, arc, angle, phi, r, a, phi2)


class Scene7(MyScene):
    def construct(self):
        proportion = 2 / (2 * PI)
        circle = Circle(radius=3, color=WHITE)
        A = circle.point_from_proportion(proportion)
        line1 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE)
        line2 = Line(start=ORIGIN, end=A, color=BLUE)
        arc = circle.get_subcurve(0, proportion)
        arc.set_color(RED)
        angle = Angle(line1, line2, quadrant=(1, 1), color=YELLOW)
        angle2 = Angle(line1, line2, quadrant=(1, 1), radius=1)
        phi = MathTex(r"\phi", color=YELLOW).move_to(angle2.point_from_proportion(0.4))
        r = MathTex("r", color=BLUE).next_to(line1, UP)
        a = MathTex("2r", color=RED) \
            .next_to(circle.point_from_proportion(proportion / 2), UR, buff=0.1)
        phi2 = MathTex(r"\phi", "=", "{2r", r"\over", "r", "}=2^{rad}") \
            .next_to(circle, RIGHT, buff=MED_LARGE_BUFF)
        degree = MathTex(r"(\approx 114.59^\circ)").next_to(phi2, DOWN)
        for i, j in zip((0, 2, 4),
                        (YELLOW, RED, BLUE)):
            phi2[i].set_color(j)

        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (circle, line1, r, line2, angle, phi, arc, a)
        ]))
        self.play(*[
            Write(phi2[i])
            for i in (1, 3)
        ])
        self.play(LaggedStart(*[
            Transform(i.copy(), phi2[j])
            for i, j in zip((r, a, phi),
                            (4, 2, 0))
        ]))
        self.play(Write(phi2[5]), Write(degree))
        self.add(circle, line1, line2, arc, angle, phi, r, a, phi2)


class Scene8(MyScene):
    def construct(self):
        proportion = 1
        circle = Circle(radius=3, color=WHITE)
        A = circle.point_from_proportion(proportion)
        line1 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE)
        line2 = Line(start=ORIGIN, end=A, color=BLUE)
        arc = circle.get_subcurve(0, proportion)
        arc.set_color(RED)
        angle = Angle(line1, line2, quadrant=(1, 1), color=YELLOW)
        angle2 = Angle(line1, line2, quadrant=(1, 1), radius=1)
        phi = MathTex(r"\phi", color=YELLOW).move_to(angle2.point_from_proportion(0.4))
        r = MathTex("r", color=BLUE).next_to(line1, UP)
        a = MathTex("2 \pi r", color=RED) \
            .next_to(circle.point_from_proportion(proportion / 2), UR, buff=0.1)
        phi2 = MathTex(r"\phi", "=", "{2\pi r", r"\over", "r", "}=2\pi^{rad}") \
            .scale(1) \
            .next_to(circle, RIGHT, buff=MED_SMALL_BUFF)
        degree = MathTex(r"(= 360^\circ)").next_to(phi2, DOWN).align_to(phi2[1], LEFT)
        rad = MathTex(r"(\approx 6.2831^{rad})").next_to(degree, DOWN).align_to(phi2[1], LEFT)
        for i, j in zip((0, 2, 4),
                        (YELLOW, RED, BLUE)):
            phi2[i].set_color(j)

        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (circle, line1, r, line2, arc, a)
        ]))
        self.play(*[
            Write(phi2[i])
            for i in (1, 3)
        ], Write(phi), Write(angle))
        self.play(LaggedStart(*[
            Transform(i.copy(), phi2[j])
            for i, j in zip((r, a, phi),
                            (4, 2, 0))
        ]))
        self.play(Write(phi2[5]), Write(degree), Write(rad))
        self.add(circle, line1, line2, arc, angle, phi, r, a, phi2)


class Scene9(MyScene):
    def construct(self):
        proportion = 0.5
        circle = Circle(radius=3, color=WHITE)
        A = circle.point_from_proportion(proportion)
        line1 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE)
        line2 = Line(start=ORIGIN, end=A, color=BLUE)
        arc = circle.get_subcurve(0, proportion)
        arc.set_color(RED)
        angle = Angle(line1, line2, quadrant=(1, 1), color=YELLOW)
        angle2 = Angle(line1, line2, quadrant=(1, 1), radius=1)
        phi = MathTex(r"\phi", color=YELLOW).move_to(angle2.point_from_proportion(0.4))
        r = MathTex("r", color=BLUE).next_to(line1, UP)
        a = MathTex(" \pi r", color=RED) \
            .next_to(circle.point_from_proportion(proportion / 2), UP, buff=0.1)
        phi2 = MathTex(r"\phi", "=", "{\pi r", r"\over", "r", "}=\pi^{rad}") \
            .scale(1) \
            .next_to(circle, RIGHT, buff=MED_SMALL_BUFF)
        degree = MathTex(r"(= 180^\circ)").next_to(phi2, DOWN).align_to(phi2[1], LEFT)
        rad = MathTex(r"(\approx 3.14^{rad})").next_to(degree, DOWN).align_to(phi2[1], LEFT)
        for i, j in zip((0, 2, 4),
                        (YELLOW, RED, BLUE)):
            phi2[i].set_color(j)

        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (circle, line1, r, line2, arc, a)
        ]))
        self.play(*[
            Write(phi2[i])
            for i in (1, 3)
        ], Write(phi), Write(angle))
        self.play(LaggedStart(*[
            Transform(i.copy(), phi2[j])
            for i, j in zip((r, a, phi),
                            (4, 2, 0))
        ]))
        self.play(Write(phi2[5]), Write(degree), Write(rad))
        self.add(circle, line1, line2, arc, angle, phi, r, a, phi2)


class Scene10(MyScene):
    def construct(self):
        proportion = 0.25
        circle = Circle(radius=3, color=WHITE)
        A = circle.point_from_proportion(proportion)
        line1 = Line(start=ORIGIN, end=RIGHT * 3, color=BLUE)
        line2 = Line(start=ORIGIN, end=A, color=BLUE)
        arc = circle.get_subcurve(0, proportion)
        arc.set_color(RED)
        angle = Angle(line1, line2, quadrant=(1, 1), color=YELLOW)
        angle2 = Angle(line1, line2, quadrant=(1, 1), radius=1)
        phi = MathTex(r"\phi", color=YELLOW).move_to(angle2.point_from_proportion(0.4))
        r = MathTex("r", color=BLUE).next_to(line1, UP)
        a = MathTex(" {\pi \over 2} r", color=RED) \
            .next_to(circle.point_from_proportion(proportion / 2), UR, buff=0.1)
        phi2 = MathTex(r"\phi", "=", "{{\pi\over2} r", r"\over", "r", "}={\pi\over2}^{rad}") \
            .scale(1) \
            .next_to(circle, RIGHT, buff=MED_SMALL_BUFF)
        degree = MathTex(r"(= 90^\circ)").next_to(phi2, DOWN).align_to(phi2[1], LEFT)
        rad = MathTex(r"(\approx 1.57^{rad})").next_to(degree, DOWN).align_to(phi2[1], LEFT)
        for i, j in zip((0, 2, 4),
                        (YELLOW, RED, BLUE)):
            phi2[i].set_color(j)

        self.play(LaggedStart(*[
            FadeIn(i)
            if isinstance(i, MathTex)
            else Create(i)
            for i in (circle, line1, r, line2, arc, a)
        ]))
        self.play(*[
            Write(phi2[i])
            for i in (1, 3)
        ], Write(phi), Write(angle))
        self.play(LaggedStart(*[
            Transform(i.copy(), phi2[j])
            for i, j in zip((r, a, phi),
                            (4, 2, 0))
        ]))
        self.play(Write(phi2[5]), Write(degree), Write(rad))
        self.add(circle, line1, line2, arc, angle, phi, r, a, phi2)


class Scene11(MyScene):
    def construct(self):
        A = DOWN * 2 + LEFT * 2
        B = UP * 2 + LEFT * 2
        C = DOWN * 2 + RIGHT * 2
        tri = VMobject().set_points_as_corners([A, B, C, A]) \
            .set_color_by_gradient([TEAL, GREEN, BLUE])
        l1 = Line(A + DOWN, B + UP)
        l2 = Line(B, C)
        l3 = Line(C, A + LEFT)
        angle1 = Angle(l3, l1, quadrant=(-1, 1), color=RED)
        angle2 = Angle(l1, l2, quadrant=(-1, 1), color=YELLOW)
        angle3 = Angle(l2, l3, quadrant=(-1, 1), color=YELLOW)
        t1 = MathTex("90^\circ", color=RED).next_to(angle1, UR, buff=SMALL_BUFF).scale(0.7)
        t2 = MathTex("45^\circ", color=YELLOW).next_to(angle2.get_right(), DOWN).scale(0.7)
        t3 = MathTex("45^\circ", color=YELLOW).next_to(angle3.get_top(), LEFT).scale(0.7)

        r1 = MathTex("\pi\over 2", color=RED).next_to(angle1, UR, buff=SMALL_BUFF).scale(0.7)
        r2 = MathTex("\pi\over 4", color=YELLOW).next_to(angle2.get_right(), DOWN).scale(0.7)
        r3 = MathTex("\pi\over 4", color=YELLOW).next_to(angle3.get_top(), LEFT).scale(0.6)

        self.play(Create(tri))
        self.play(LaggedStart(*[
            Write(i)
            for i in (angle1, angle2, angle3, t1, t2, t3)
        ]))
        self.play(*[
            Transform(i, j)
            for i, j in zip((t1, t2, t3),
                            (r1, r2, r3))
        ])


class Scene12(MyScene):
    def construct(self):
        dash_line = DashedLine(start=LEFT * 2, end=RIGHT * 2).shift(UP * 2)
        line = Line(start=LEFT * 2, end=RIGHT * 2).shift(UP * 2)
        line.set_color_by_gradient([TEAL, BLUE, PINK])
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True).to_corner(DR)
        computer = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 4,
            "stretch_height": 1.5
        }

        self.my_play(Create(line),
                     FadeIn(pi, shift=LEFT * 2),
                     FadeIn(computer, shift=RIGHT * 2))
        self.my_play(NumberCreatureSays(pi,
                                        Text(r"self.play(Rotate(line, PI / 3))",
                                             t2c={"PI / 3":YELLOW}),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.add(dash_line)
        self.my_play(NumberCreatureSays(computer,
                                        Text("Okay!"),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs),
                     Rotate(line, PI / 3))
        self.wait()

class Scene13(MyScene):
    def construct(self):
        dash_line = DashedLine(start=LEFT * 2, end=RIGHT * 2).shift(UP * 2)
        line = Line(start=LEFT * 2, end=RIGHT * 2).shift(UP * 2)
        line.set_color_by_gradient([TEAL, BLUE, PINK])
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True).to_corner(DR)
        computer = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 4,
            "stretch_height": 1.5
        }

        self.my_play(Create(line),
                     FadeIn(pi, shift=LEFT * 2),
                     FadeIn(computer, shift=RIGHT * 2))
        self.my_play(NumberCreatureSays(pi,
                                        Text(r"self.play(Rotate(line, 60))",
                                             t2c={"60":YELLOW}),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.add(dash_line)
        self.my_play(NumberCreatureSays(computer,
                                        Text("60 rad...?",
                                             t2c={"60":YELLOW}),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs),
                     Rotate(line, 60), run_time=3)
        self.wait()


class Scene14(MyScene):
    def construct(self):
        dash_line = DashedLine(start=LEFT * 2, end=RIGHT * 2).shift(UP * 2)
        line = Line(start=LEFT * 2, end=RIGHT * 2).shift(UP * 2)
        line.set_color_by_gradient([TEAL, BLUE, PINK])
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True).to_corner(DR)
        computer = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 5,
            "stretch_height": 2.5
        }
        bubble_kwargs2 = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 2,
            "stretch_height": 2
        }

        self.my_play(Create(line),
                     FadeIn(pi, shift=LEFT * 2),
                     FadeIn(computer, shift=RIGHT * 2))
        a = Text("DEG = 2*PI/360", t2c={"DEG":GREEN,
                                        "2*PI/360":RED})
        b = Text("self.play(Rotate(line, 27*DEG))",
                 t2c={"27":YELLOW,
                      "DEG":GREEN
                    })\
            .next_to(a, DOWN, buff=MED_SMALL_BUFF)
        self.my_play(NumberCreatureSays(pi,
                                        VGroup(a, b),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.add(dash_line)
        self.my_play(NumberCreatureSays(computer,
                                        Text(r"Done!"),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs2),
                     Rotate(line, 27*DEGREES), run_time=2)
        self.wait()

