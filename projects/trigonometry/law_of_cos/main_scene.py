from manim import *
import math

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3")
SCENE_NAME = list_scene[1]
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
        self.play(triangle_group.animate.scale(0.5), rate_func=linear)
        self.play(triangle_group.animate.scale(1.8), rate_func=linear)


class Scene1(MyScene):
    def construct(self):
        map = ImageMobject("map").rotate(PI).scale(1.2).shift(LEFT * 4)
        ship = SVGMobject("ship").scale(0.3)

        A = Dot(LEFT * 5 + DOWN * 2.5, color=RED)
        B = Dot(LEFT * 2 + DOWN * 2.5, color=RED)
        C = Dot(LEFT * 5 + UP * 3, color=YELLOW)
        a = MathTex("A", color=RED).next_to(A, DOWN)
        b = MathTex("B", color=RED).next_to(B, DOWN)
        c = MathTex("C", color=YELLOW).next_to(C, UP, MED_LARGE_BUFF)
        path = Line(C, A)
        AC = DashedLine(A, C)
        BC = DashedLine(B, C)
        AB = Line(A, B, color=RED)
        c_angle =
        def create_angle():
            angle = Angle(AB, BC, quadrant=(-1, 1), other_angle=True)
            degree = math.atan(AC.get_length()/AB.get_length()) * 57.29
            angle_t = MathTex({})

        ship.next_to(C)

        obj = VMobject()
        self.add(map, ship, A, B, C, a, b, c, obj, AC, BC, AB, c_angle)

        def move_ship(obj):
            c.next_to(C, UP, MED_SMALL_BUFF)
            AC.become(DashedLine(A, C))
            BC.become(DashedLine(B, C))
            obj.move_to(C)
            c_angle.become(Angle(AB, BC, quadrant=(-1, 1), other_angle=True))
        ship.add_updater(move_ship)

        self.play(MoveAlongPath(C, path))


class Scene2(MyScene):
    def construct(self):
        map = ImageMobject("map")
        self.add(map)


class Scene3(MyScene):
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
        BH = Line(B, H, color=GREEN)
        H_angle = RightAngle(BH, AC, quadrant=(-1, -1))
        A_angle = Angle(AC, AB, quadrant=(-1, 1))
        A_angle_t = MathTex("60^\circ").move_to(Angle(AC, AB, quadrant=(-1, 1), radius=1))
        B_angle = Angle(AC, BC, quadrant=(1, -1), other_angle=True)
        B_angle_t = MathTex("50^\circ").move_to(Angle(AC, BC, quadrant=(1, -1), other_angle=True, radius=1))
        c = MathTex("a", color=RED).next_to(AB.get_center(), UL)
        a = MathTex("a", color=YELLOW).next_to(BC.get_center(), UR)
        b = MathTex("b", color=BLUE).next_to(AC.get_center(), DR)
        h = MathTex(r"a", "sin(", "60^\circ", ")").scale(0.8).next_to(BH.get_center(), RIGHT, buff=SMALL_BUFF)
        h.shift(DOWN * 0.5)
        h[0].set_color(RED)
        self.play(Create(A), Create(B), Create(C))
        self.play(Create(AB), Create(BC), Create(AC))
        self.play(*[Write(i) for i in (c, A_angle_t, b)],
                  *[Create(i) for i in (A_angle)])
        self.wait()
        self.play(Create(BH), Create(H), Create(H_angle))
        self.wait()
        self.play(*[Write(h[i]) for i in (1, 3)],
                  Transform(c.copy(), h[0]),
                  Transform(A_angle_t.copy(), h[2]))

        equation1 = MathTex("\Rightarrow", r"\text{Area}=", "{1\over 2}", "a", "b", "sin(", "60^\circ", ")") \
            .shift(LEFT * 3)
        color_map = {
            "a": RED,
            "b": BLUE,
            "sin": WHITE,
            "Area": WHITE,
            "Rightarrow": WHITE
        }
        equation1.set_color_by_tex_to_color_map(color_map)
        self.play(LaggedStart(*[
            Write(equation1[i]) for i in (0, 1, 2)
        ]))
        self.my_play(LaggedStart(*[
            Transform(j.copy(), equation1[i]) for i, j in zip((3, 4, 5, 6, 7),
                                                              (h[0], b, h[1], h[2], h[3]))
        ]))
