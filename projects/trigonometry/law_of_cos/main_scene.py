from manim import *
import math

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3")
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


class Scene0(MyScene):
    def construct(self):
        A = Dot(LEFT * 2)
        B = Dot(UP * 3.464)
        C = Dot(RIGHT * 2.9)
        H = Dot(ORIGIN)
        group_point = VGroup(A, B, C, H)
        group_point.shift(RIGHT * 3 + DOWN).scale(1.3)
        AB = Line(A, B, color=RED)
        BC = Line(B, C, color=YELLOW)
        AC = Line(C, A, color=BLUE)
        A_angle = Angle(AC, AB, quadrant=(-1, 1))
        A_angle_t = MathTex("A").move_to(Angle(AC, AB, quadrant=(-1, 1), radius=1))
        B_angle = Angle(AB, BC, quadrant=(-1, 1))
        B_angle_t = MathTex("B").move_to(Angle(AB, BC, quadrant=(-1, 1), radius=0.8))
        C_angle = Angle(AC, BC, quadrant=(1, -1), other_angle=True)
        C_angle_t = MathTex("C").move_to(Angle(AC, BC, quadrant=(1, -1), other_angle=True, radius=1))

        c = MathTex("c", color=RED).next_to(AB.get_center(), UL)
        b = MathTex("b", color=BLUE).next_to(AC.get_center(), DOWN)
        a = MathTex("a", color=YELLOW).next_to(BC.get_center(), UR)
        fomular1 = MathTex("{sin(A)\over a} = {sin(B)\over b} = {sin(C) \over c}")
        fomular2 = MathTex("a^2 = b^2+c^2-2bc.cos(A)")
        fomular3 = MathTex("b^2 = a^2+c^2-2ac.cos(B)")
        fomular4 = MathTex("c^2 = a^2+b^2-2ab.cos(C)")
        fomular5 = MathTex(
            r"{a-b \over a+b} = {tan\left[ {1\over2}(A-B) \right] \over tan\left[{1\over2} (A+B) \right]}")
        los = Text("Định lý sin", font="Sans", font_size=27)
        loc = Text("Định lý cos", font="Sans", font_size=27)
        lot = Text("Định lý tan", font="Sans", font_size=27)
        group1 = VGroup(los, fomular1).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        group2 = VGroup(loc, fomular2, fomular3, fomular4).arrange(DOWN, aligned_edge=LEFT) \
            .next_to(group1, DOWN, aligned_edge=LEFT)
        group3 = VGroup(lot, fomular5).arrange(DOWN, aligned_edge=LEFT) \
            .next_to(group2, DOWN, aligned_edge=LEFT)
        group1[0].set_color(RED)
        group2[0].set_color(GREEN)
        group3[0].set_color(BLUE)
        source = [a, b, c, A_angle_t, B_angle_t, C_angle_t]
        letter = [i.copy() for i in source]
        question_mark = [MathTex("?").move_to(i) for i in source]
        case = [Text(i, font="Sans", font_size=30).next_to(b, DOWN) for i in
                ("(Góc - Góc - Cạnh)",
                 "(Góc - Cạnh - Góc)",
                 "(Cạnh - Góc - Cạnh)",
                 "(Cạnh - Cạnh - Góc)",
                 "(Cạnh - Cạnh - Cạnh)",
                 "(Góc - Góc - Góc)")]
        case_letter = [
            (0, 1, 0, 1, 1, 0),
            (0, 1, 0, 1, 0, 1),
            (0, 1, 1, 1, 0, 0),
            (0, 1, 1, 0, 0, 1),
            (1, 1, 1, 0, 0, 0),
            (0, 0, 0, 1, 1, 1)
        ]

        def get_plays(state):
            result = []
            for index, i in enumerate(state):
                if i == 1:
                    result.append(Transform(source[index], letter[index]))
                else:
                    result.append(Transform(source[index], question_mark[index]))
            return result

        triangle_group = VGroup(A, B, C, AB, BC, AC, A_angle, B_angle, C_angle, A_angle_t, B_angle_t, C_angle_t, a, b,
                                c)
        self.play(LaggedStart(*[
            Write(i)
            for i, j in zip((triangle_group),
                            (1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1))
        ], lag_ratio=0.2))
        self.play(Write(group1))
        self.wait()
        self.play(Write(group2))
        self.play(Write(group3))
        for i, j in enumerate(case):
            if i != 0:
                self.play(FadeOut(case[i - 1]))
            self.play(Write(j), *get_plays(case_letter[i]))
            self.play(*[Indicate(source[index]) for index, temp in enumerate(case_letter[i]) if temp == 1])
        self.play(Create(Cross(case[-1])))
        self.my_play(triangle_group.animate.scale(0.5), rate_func=linear)
        self.my_play(triangle_group.animate.scale(1.8), rate_func=linear)


class Scene1(MyScene):
    def construct(self):
        map = ImageMobject("map").rotate(PI).scale(1.2).shift(LEFT * 4)
        ship = SVGMobject("ship").scale(0.3)

        A = Dot(LEFT * 5 + DOWN * 2.5, color=RED)
        base = SVGMobject("base", color=GREEN).scale(0.3).move_to(A)

        B = Dot(LEFT * 2 + DOWN * 2.5, color=RED)
        C = Dot(LEFT * 5 + UP * 3.2, color=YELLOW)
        a = MathTex("A", color=RED).next_to(A, DOWN)
        b = MathTex("B", color=RED).next_to(B, DOWN)
        c = MathTex("C", color=YELLOW).next_to(C, UP)
        AC = DashedLine(A, C, color=YELLOW)
        BC = DashedLine(B, C)
        AB = Line(A, B, color=RED)
        right_angle = RightAngle(AC, AB, color=RED)
        AB_t = MathTex("1(km)", color=RED).scale(0.8).next_to(AB, DOWN, buff=SMALL_BUFF)
        AC_t = MathTex("1880(m)", color=YELLOW).scale(0.8).next_to(AC, LEFT, buff=SMALL_BUFF)

        def get_angle():
            return math.atan(AC.get_length() / AB.get_length()) * 57.29

        def create_angle():
            angle = Angle(AB, BC, quadrant=(-1, 1), other_angle=True, color=PINK)
            degree = get_angle()
            angle_t = MathTex("{0} ^\circ".format(int(degree)), color=PINK).scale(0.8).move_to(
                Angle(AB, BC, quadrant=(-1, 1), other_angle=True, radius=0.8))
            return VGroup(angle, angle_t)

        def create_fomular(text):
            fomular1 = MathTex(r"\Rightarrow ", "AC", " = ", "AB", r"\times ",
                               "tan({0}^\circ)".format(int(get_angle()))).next_to(text, DOWN, aligned_edge=LEFT)
            fomular2 = MathTex("AC", " = ", "{0}(m)".format(int(1000 * math.tan(int(get_angle()) * DEGREES)))).next_to(
                fomular1[1],
                DOWN,
                aligned_edge=LEFT)
            fomular1[5].set_color(PINK)
            fomular1[3].set_color(RED)
            fomular1[1].set_color(YELLOW)
            fomular2[0].set_color(YELLOW)
            fomular2[2].set_color(YELLOW)
            return VGroup(fomular1, fomular2)

        c_angle = create_angle()

        ship.move_to(C)
        text1 = Text("Tam giác ABC vuông:", font="Sans", font_size=30).shift(UP * 2 + RIGHT * 2)
        fomular = create_fomular(text1)

        # self.add(map, ship, A, B, C, a, b, c, AC, BC, AB, c_angle, text1, fomular, AB_t, right_angle)

        def move_ship(obj):
            c.next_to(C, UP, MED_SMALL_BUFF)
            AC.become(DashedLine(A, C, color=YELLOW))
            BC.become(DashedLine(B, C))
            obj.move_to(C)
            c_angle.become(create_angle())
            AC_t.become(
                MathTex("{0}(m)".format(int(1000 * math.tan(int(get_angle()) * DEGREES))), color=YELLOW)
                .scale(0.8).next_to(AC, LEFT, buff=SMALL_BUFF))
            fomular.become(create_fomular(text1))

        self.my_play(FadeIn(map), Write(base), Create(A), Create(a))
        self.my_play(Write(ship), Write(C), Write(c))
        self.my_play(Write(b), Create(B), Write(AB_t), Create(AB))
        self.my_play(Create(AC), Create(BC), Write(c_angle), Create(right_angle))
        self.my_play(Write(text1), Write(fomular))
        self.my_play(ReplacementTransform(fomular[1][2].copy(), AC_t))
        ship.add_updater(move_ship)
        self.play(C.animate.shift(DOWN * 5), rate_func=linear, run_time=5)
        self.wait()
        # self.play(C.animate.shift(UP*2), rate_func=linear, run_time=2)


class Scene2(MyScene):
    def construct(self):
        map = ImageMobject("map").rotate(PI).scale(1.2).shift(LEFT * 4)
        ship = SVGMobject("ship").scale(0.3)

        A = Dot(LEFT * 5 + DOWN * 2.5, color=RED)
        base = SVGMobject("base", color=GREEN).scale(0.3).move_to(A)

        B = Dot(LEFT * 2 + DOWN * 2.5, color=RED)
        C = Dot(LEFT * 5 + UP * 3.2, color=YELLOW)
        a = MathTex("A", color=RED).next_to(A, DOWN)
        b = MathTex("B", color=RED).next_to(B, DOWN)
        c = MathTex("C", color=YELLOW).next_to(C, UP)

        def create_path(init_point):
            p1 = init_point + DOWN + LEFT
            p2 = p1 + DOWN + RIGHT * 5
            p3 = p2 + DOWN * 2 + LEFT
            p4 = p3 + UP + LEFT * 2
            return VMobject().set_points_smoothly([init_point, p1, p2, p3, p4])

        path = create_path(C.get_center())
        AC = DashedLine(A, C, color=YELLOW)
        BC = DashedLine(B, C)
        AB = Line(A, B, color=RED)
        right_angle = RightAngle(AC, AB, color=RED)
        AB_t = MathTex("1(km)", color=RED).scale(0.8).next_to(AB, DOWN, buff=SMALL_BUFF)
        AC_t = MathTex("1950(m)", color=YELLOW).scale(0.8).next_to(AC, LEFT, buff=SMALL_BUFF)

        def get_angle():
            return math.atan(AC.get_length() / AB.get_length()) * 57.29

        def create_angle():
            angle = Angle(AB, BC, quadrant=(-1, 1), other_angle=True, color=PINK)
            degree = get_angle()
            angle_t = MathTex("{0} ^\circ".format(int(degree)), color=PINK).scale(0.8).move_to(
                Angle(AB, BC, quadrant=(-1, 1), other_angle=True, radius=0.8))
            return VGroup(angle, angle_t)

        def create_fomular(text):
            fomular1 = MathTex(r"\Rightarrow ", "AC", " = ", "AB", r"\times ",
                               "tan({0}^\circ)".format(int(get_angle()))).next_to(text, DOWN, aligned_edge=LEFT)
            fomular2 = MathTex("AC", " = ", "{0}(m)".format(int(1000 * math.tan(get_angle() * DEGREES)))).next_to(
                fomular1[1],
                DOWN,
                aligned_edge=LEFT)
            fomular1[5].set_color(PINK)
            fomular1[3].set_color(RED)
            fomular1[1].set_color(YELLOW)
            fomular2[0].set_color(YELLOW)
            fomular2[2].set_color(YELLOW)
            return VGroup(fomular1, fomular2)

        c_angle = create_angle()

        ship.move_to(C)
        text1 = Text("Tam giác ABC vuông:", font="Sans", font_size=30).shift(UP * 2 + RIGHT * 2)
        fomular = create_fomular(text1)

        # self.add(map, ship, A, B, C, a, b, c, AC, BC, AB, c_angle, text1, fomular, AB_t, right_angle)

        def move_ship(obj):
            c.next_to(C, UP, MED_SMALL_BUFF)
            AC.become(DashedLine(A, C, color=YELLOW))
            BC.become(DashedLine(B, C))
            obj.move_to(C)
            c_angle.become(create_angle())
            AC_t.become(
                MathTex("{0}(m)".format(int(1000 * math.tan(get_angle() * DEGREES))), color=YELLOW).next_to(AC, LEFT,
                                                                                                            buff=SMALL_BUFF))
            fomular.become(create_fomular(text1))

        self.play(FadeIn(map), Write(base), Create(A), Create(a))
        self.play(Write(ship), Write(C), Write(c))
        self.play(Write(b), Create(B), Write(AB_t), Create(AB))
        self.play(Create(AC), Create(BC), Write(c_angle))
        self.wait()
        ship.add_updater(move_ship)
        self.play(MoveAlongPath(C, path), rate_func=linear, run_time=5)
        self.wait()


class Scene3(MyScene):
    def construct(self):
        map = ImageMobject("map").rotate(PI).scale(1.2).shift(LEFT * 4)
        ship = SVGMobject("ship").scale(0.3)

        A = Dot(LEFT * 5 + DOWN * 2.5, color=RED)
        base = SVGMobject("base", color=GREEN).scale(0.3).move_to(A)

        B = Dot(LEFT * 2 + DOWN * 2.5, color=RED)
        C = Dot(LEFT * 5 + UP * 3.2, color=YELLOW)
        a = MathTex("A", color=RED).next_to(A, DOWN)
        b = MathTex("B", color=RED).next_to(B, DOWN)
        c = MathTex("C", color=YELLOW).next_to(C, UP)

        def create_path(init_point):
            p1 = init_point + DOWN + LEFT
            p2 = p1 + DOWN + RIGHT * 5
            p3 = p2 + DOWN * 2 + LEFT
            p4 = p3 + DOWN + LEFT * 2
            p5 = p4 + UP * 2 + LEFT * 3
            p6 = p5 + RIGHT * 4 + UP
            return VMobject().set_points_smoothly([init_point, p1, p2, p3, p4, p5, p6])

        path = create_path(C.get_center())
        AC = DashedLine(A, C, color=YELLOW)
        BC = DashedLine(B, C)
        AB = Line(A, B, color=RED)
        AB_t = MathTex("1(km)", color=RED).scale(0.8).next_to(AB, DOWN, buff=SMALL_BUFF)
        AC_t = MathTex("1880(m)", color=YELLOW).scale(0.8).next_to(AC, LEFT, buff=SMALL_BUFF)

        def get_angle():
            a = BC.get_length()
            b = AC.get_length() + 0.05
            c = AB.get_length()
            return math.acos((c * c + a * a - b * b) / (2 * a * c)) * 57.2957

        def get_angle2():
            a = BC.get_length()
            b = AC.get_length() + 0.05
            c = AB.get_length()
            return math.acos((c * c + b * b - a * a) / (2 * b * c)) * 57.2957

        def create_angle():
            angle = Angle(AB, BC, quadrant=(-1, 1), other_angle=True, color=PINK)
            degree = get_angle()
            angle_t = MathTex("{0} ^\circ".format(int(degree)), color=PINK).scale(0.8).move_to(
                Angle(AB, BC, quadrant=(-1, 1), other_angle=True, radius=0.8).point_from_proportion(0.5))
            return VGroup(angle, angle_t)

        def create_angle2():
            angle = Angle(AB, AC, color="#143264")
            degree = get_angle2()
            angle_t = MathTex("{0} ^\circ".format(int(degree)), color="#143264").scale(0.8).move_to(
                Angle(AB, AC, radius=0.8).point_from_proportion(0.5))
            return VGroup(angle, angle_t)

        def create_fomular1(text):
            angle1 = int(get_angle())
            angle2 = int(get_angle2())
            angle3 = 180 - angle1 - angle2
            fomular1 = MathTex(r"\Rightarrow ", r"\angle C", "=", "180^\circ", "-", "{0}^\circ".format(angle1), "-",
                               "{0}^\circ".format(angle2), "=", "{0}^\circ".format(angle3)) \
                .scale(0.9) \
                .next_to(text, DOWN, aligned_edge=LEFT)
            fomular1[5].set_color(PINK)
            fomular1[7].set_color("#143264")
            fomular1[1].set_color(YELLOW)
            fomular1[9].set_color(YELLOW)
            return fomular1

        def create_fomular(text):
            angle1 = int(get_angle())
            angle2 = int(get_angle2())
            angle3 = 180 - angle1 - angle2
            fomular1 = MathTex(r"\Rightarrow ", "{AC", "\over", "sin({0}^\circ)".format(angle1) + "}", "= ", "{AB",
                               r"\over", "sin({0}^\circ)".format(angle3), "}").scale(0.9).next_to(text, DOWN,
                                                                                                  aligned_edge=LEFT)
            result = int(1000 * math.sin(angle1 * DEGREES) / math.sin(angle3 * DEGREES))
            fomular2 = MathTex(r"\Rightarrow ", "AC", " = ", "{AB", r"\times", "sin({0}^\circ)".format(angle1), "\over",
                               " sin({0}^\circ)".format(angle3) + "}", "=", "{0}(m)".format(result)).scale(0.9).next_to(
                fomular1,
                DOWN,
                aligned_edge=LEFT)
            fomular1[1].set_color(YELLOW)
            fomular1[3].set_color(PINK)
            fomular1[5].set_color(RED)
            fomular1[7].set_color(YELLOW)

            fomular2[1].set_color(YELLOW)
            fomular2[3].set_color(RED)
            fomular2[5].set_color(PINK)
            fomular2[7].set_color(YELLOW)
            fomular2[9].set_color(YELLOW)
            return VGroup(fomular1, fomular2)

        c_angle = create_angle()
        a_angle = create_angle2()

        ship.move_to(C)
        text1 = Text("Tổng 3 góc tam giác = 180 độ:", font="Sans", font_size=30).shift(UP * 2 + RIGHT * 3)
        text2 = Text("Áp dụng định lý sin:", font="Sans", font_size=30).align_to(text1, LEFT)
        fomular = create_fomular(text2)
        fomular1 = create_fomular1(text1)

        # self.add(map, ship, A, B, C, a, b, c, AC, BC, AB, c_angle, text1, fomular, AB_t, a_angle, text2, fomular1)

        def move_ship(obj):
            c.next_to(C, UP, MED_SMALL_BUFF)
            AC.become(DashedLine(A, C, color=YELLOW))
            BC.become(DashedLine(B, C))
            obj.move_to(C)
            c_angle.become(create_angle())
            a_angle.become(create_angle2())
            angle1 = int(get_angle())
            angle2 = int(get_angle2())
            angle3 = 180 - angle1 - angle2
            result = int(1000 * math.sin(angle1 * DEGREES) / math.sin(angle3 * DEGREES))
            AC_t.become(
                MathTex("{0}(m)".format(result), color=YELLOW).scale(0.8).next_to(AC.get_center(), LEFT,
                                                                                  buff=SMALL_BUFF))
            fomular.become(create_fomular(text2))
            fomular1.become(create_fomular1(text1))

        # self.add(path)
        self.play(FadeIn(map), Write(base), Create(A), Create(a))
        self.play(Write(ship), Write(C), Write(c))
        self.play(Write(b), Create(B), Write(AB_t), Create(AB))
        self.play(Create(AC), Create(BC), Write(c_angle), Write(a_angle))
        self.play(Write(text1), Write(fomular1))
        self.play(Write(text2), Write(fomular[0]), Write(fomular[1]))
        self.play(ReplacementTransform(fomular[1][-1].copy(), AC_t))
        self.wait()
        ship.add_updater(move_ship)
        self.play(MoveAlongPath(C, path), rate_func=linear, run_time=20)
