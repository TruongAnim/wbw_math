import math
from manim import *
from common.utils.manim_utils import line_intersection_

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Thumbnail")
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
        self.wait(0.5)


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Thumbnail(MyScene):
    def construct(self):
        square = Square(side_length=6, color=GREEN)
        square_t1 = MathTex("1", color=GREEN).scale(2).next_to(square, DOWN)
        square_t2 = MathTex("1", color=GREEN).scale(2).next_to(square, LEFT)
        hypotenus = Line(square.point_from_proportion(0.25), square.point_from_proportion(0.75), color=YELLOW,
                         stroke_width=10)
        root_of_2 = MathTex("\sqrt{2}", color=YELLOW).scale(2).next_to(hypotenus.get_center(), UP).shift(RIGHT * 0.3)
        square_group = VGroup(square.get_subcurve(0.25, 0.75), square_t1, square_t2, root_of_2, hypotenus).shift(
            LEFT * 3)
        root_of_20 = MathTex("\sqrt{2}", "=").to_edge(UP).shift(LEFT * 3)
        root_of_20[0].set_color(YELLOW)
        root_of_22 = MathTex("=", "1.414213562373...").scale(2).next_to(root_of_2, RIGHT)
        brace = Brace(root_of_22[1], DOWN)
        text = Text("Dài vô tận", font='Sans', font_size=70, color=GREEN).next_to(brace, DOWN)
        self.add(square_group, root_of_22, text, brace)
        self.wait()


class Scene0(MyScene):
    def construct(self):
        colors = [RED, GREEN, YELLOW]
        text_color = "#ffd5c0"
        side_length = 7
        shift_down = 3
        radius = 1.5
        A = UP * math.sqrt(side_length ** 2 - (side_length / 2) ** 2) + DOWN * 3
        B = LEFT * side_length / 2 + DOWN * 3
        C = RIGHT * side_length / 2 + DOWN * 3
        A_dot = Dot(A)
        B_dot = Dot(B)
        C_dot = Dot(C)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=BLUE)
        AC = Line(C, A, color=BLUE)
        circle = Circle(radius=radius).shift(DOWN)
        D = Dot(circle.get_start())
        def create_perpendicular():
            line1 = Line(AB.get_projection(D.get_center()), D.get_center(), color=colors[0], stroke_width=8)
            line2 = Line(BC.get_projection(D.get_center()), D.get_center(), color=colors[1], stroke_width=8)
            line3 = Line(AC.get_projection(D.get_center()), D.get_center(), color=colors[2], stroke_width=8)
            angle1 = RightAngle(AB, line1, color=colors[0], length=0.25)
            angle2 = RightAngle(BC, line2, color=colors[1], length=0.25)
            angle3 = RightAngle(AC, line3, color=colors[2], length=0.25)
            return VGroup(line1, line2, line3, angle1, angle2, angle3)

        line = always_redraw(create_perpendicular)

        def create_sum():
            line1 = line[1].copy()
            line1.move_to(ORIGIN).align_to(BC, DOWN).shift(LEFT * 4)
            line2 = line[0].copy().rotate(120 * DEGREES).next_to(line1, UP, buff=0)
            line3 = line[2].copy().rotate(60 * DEGREES).next_to(line2, UP, buff=0)

            return VGroup(line1, line2, line3)

        sum = always_redraw(create_sum)
        dash_line1 = DashedLine(A, A + LEFT * 5, dashed_ratio=0.3, dash_length=0.07)
        dash_line2 = DashedLine(B, B + LEFT * 1.5, dashed_ratio=0.3, dash_length=0.07)
        tgd = Text("Tam giác đều", font="Sans", font_size=40, color=text_color).move_to(UP * 3 + RIGHT * 5)
        text1 = MarkupText("Chọn một điểm bất kì\nnằm trong tam giác", font_size=40,
                              font="Sans", color=text_color).move_to(UP * 3 + LEFT * 4)
        text2 = MarkupText("Từ điểm đó\nkẻ vuông góc xuống 3 cạnh", font_size=35,
                              font="Sans", color=text_color).move_to(UP * 3 + RIGHT * 4)
        text3 = MarkupText("Tổng độ dài 3 đường\nvuông góc luôn bằng \nchiều cao tam giác đều", font_size=40,
                           font="Sans", color=text_color).move_to(UP * 2 + RIGHT * 4)
        text4 = MarkupText("Viviani's Theorem:", font_size=45,
                           font="Sans", color=YELLOW).next_to(text3, UP)
        arrow = Arrow(tgd.get_left(), AC.point_from_proportion(0.7), color=text_color)
        self.play(Create(AB), Create(BC), Create(AC))
        self.play(Write(tgd), GrowArrow(arrow))
        self.wait()
        self.play(FadeOut(arrow), FadeOut(tgd))
        self.play(Create(text1),
                  MoveAlongPath(D, circle, run_time=3), rate_func=linear)
        self.play(FadeOut(text1), Write(text2), LaggedStart(*[
            Create(i) for i in line
        ], lag_ratio=0.3))
        self.add(line)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.add(sum, dash_line1, dash_line2)
        self.remove(text2)
        self.play(Write(text4), Write(text3),  MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)


class Scene1(MyScene):
    def construct(self):
        colors = [RED, GREEN, YELLOW]
        side_length = 7
        shift_down = 3
        radius = 1.5
        A = UP * math.sqrt(side_length ** 2 - (side_length / 2) ** 2) + DOWN * 3
        B = LEFT * side_length / 2 + DOWN * 3
        C = RIGHT * side_length / 2 + DOWN * 3
        A_dot = Dot(A)
        B_dot = Dot(B)
        C_dot = Dot(C)
        AB = Line(A, B)
        BC = Line(B, C)
        AC = Line(C, A)
        D = Dot(RIGHT * 1 + DOWN * 1.25)

        def create_perpendicular():
            line1 = Line(AB.get_projection(D.get_center()), D.get_center(), color=colors[0])
            angle1 = RightAngle(AB, line1, color=colors[0], length=0.25)
            line2 = Line(BC.get_projection(D.get_center()), D.get_center(), color=colors[1])
            angle2 = RightAngle(BC, line2, color=colors[1], length=0.25)
            line3 = Line(AC.get_projection(D.get_center()), D.get_center(), color=colors[2])
            angle3 = RightAngle(AC, line3, color=colors[2], length=0.25)
            return VGroup(line1, line2, line3, angle1, angle2, angle3)

        perpendicular = create_perpendicular()

        def create_ss(l1, l2, angle):
            l = Line(D.get_center(), D.get_center() + RIGHT).rotate(angle, about_point=D.get_center())
            p1 = line_intersection_(l, l1)
            p2 = line_intersection_(l, l2)
            return Line(p1, p2, stroke_width=2)

        line1 = create_ss(AB, AC, angle=0)
        line2 = create_ss(AC, BC, angle=60 * DEGREES)
        line3 = create_ss(AB, BC, angle=120 * DEGREES)
        polygon1 = Polygon(line1.get_start(), D.get_center(), line3.get_start(), fill_color=BLUE, fill_opacity=0.2)
        polygon2 = Polygon(line2.get_end(), D.get_center(), line3.get_end(), fill_color=BLUE, fill_opacity=0.2)
        polygon3 = Polygon(line2.get_start(), D.get_center(), line1.get_end(), fill_color=BLUE, fill_opacity=0.2)
        cm = MarkupText("Cách 1:", font_size=45,
                           font="Sans", color=YELLOW).to_corner(UL)
        self.play(Create(AB), Create(BC), Create(AC), Write(cm))

        self.my_play(Create(D), LaggedStart(*[Create(i) for i in perpendicular]))
        self.my_play(Create(line1), run_time=1)
        self.my_play(Create(line2), run_time=1)
        self.my_play(Create(line3), run_time=1)
        self.my_play(Create(polygon1), run_time=1)
        self.my_play(Create(polygon2), run_time=1)
        self.my_play(Create(polygon3), run_time=1)
        self.remove(line1, line2, line3)
        self.my_play(FadeOut(perpendicular[3:]), FadeOut(D), run_time=1)
        group1 = VGroup(perpendicular[0], polygon1)
        group2 = VGroup(perpendicular[1], polygon2)
        group3 = VGroup(perpendicular[2], polygon3)
        self.my_play(Rotate(group1, angle=120 * DEGREES, about_point=perpendicular[0].point_from_proportion(1 / 3)))
        self.my_play(Rotate(group3, angle=-120 * DEGREES, about_point=perpendicular[2].point_from_proportion(1 / 3)))
        self.my_play(group1.animate.shift(A - perpendicular[0].get_end()))
        self.my_play(group3.animate.move_to(ORIGIN).next_to(group1, DOWN, buff=0))
        self.my_play(group2.animate.move_to(ORIGIN).next_to(group3, DOWN, buff=0))
        self.my_play(LaggedStart(
            *[line.copy().animate.shift(LEFT * 4)
              for line in (perpendicular[1], perpendicular[2], perpendicular[0])
              ]
            , lag_ratio=0.5))
        dash_line1 = DashedLine(A, A + LEFT * 5, dashed_ratio=0.3, dash_length=0.07)
        dash_line2 = DashedLine(B, B + LEFT * 1.5, dashed_ratio=0.3, dash_length=0.07)
        self.my_play(Create(dash_line1), Create(dash_line2))
        self.play(Wiggle(VGroup(perpendicular[0].copy().shift(LEFT*4),
                                      perpendicular[1].copy().shift(LEFT*4),
                                      perpendicular[2].copy().shift(LEFT*4))),
                  Wiggle(VGroup(perpendicular[0], perpendicular[1], perpendicular[2])))
        self.wait()
        self.add(AB, BC, AC, D, perpendicular, line1, line2, line3, polygon1, polygon2, polygon3)


class Scene2(MyScene):
    def construct(self):
        h_color = "#31c2fc"
        colors = [RED, GREEN, YELLOW, h_color]
        side_length = 7
        shift_down = 3
        radius = 1.5
        A = UP * math.sqrt(side_length ** 2 - (side_length / 2) ** 2) + DOWN * 3 + LEFT * 2 + UP * 0.3
        B = LEFT * side_length / 2 + DOWN * 3 + LEFT * 2 + UP * 0.3
        C = RIGHT * side_length / 2 + DOWN * 3 + LEFT * 2 + UP * 0.3
        A_dot = Dot(A)
        B_dot = Dot(B)
        C_dot = Dot(C)
        AB = Line(A, B)
        BC = Line(B, C)
        AC = Line(C, A)
        P = Dot(RIGHT * 1 + DOWN * 1.25 + LEFT * 2)

        def create_perpendicular():
            line1 = Line(AB.get_projection(P.get_center()), P.get_center(), color=colors[0])
            angle1 = RightAngle(AB, line1, color=colors[0], length=0.25)
            line2 = Line(BC.get_projection(P.get_center()), P.get_center(), color=colors[1])
            angle2 = RightAngle(BC, line2, color=colors[1], length=0.25)
            line3 = Line(AC.get_projection(P.get_center()), P.get_center(), color=colors[2])
            angle3 = RightAngle(AC, line3, color=colors[2], length=0.25)
            a = MathTex("a", color=colors[0]).scale(1).next_to(line1.get_center(), UR, buff=0.2)
            b = MathTex("b", color=colors[1]).scale(1).next_to(line2.get_center(), LEFT, buff=0.1)
            c = MathTex("c", color=colors[2]).scale(1).next_to(line3.get_center(), UL, buff=0.2)
            return VGroup(line1, line2, line3, angle1, angle2, angle3, a, b, c)

        def create_edge():
            line1 = Line(P.get_center(), A)
            line2 = Line(P.get_center(), B)
            line3 = Line(P.get_center(), C)
            return VGroup(line1, line2, line3)

        edge = create_edge()
        dash_line1 = DashedLine(A, A + LEFT * 3.7, dashed_ratio=0.3, dash_length=0.07)
        dash_line2 = DashedLine(B, B + LEFT * 0.2, dashed_ratio=0.3, dash_length=0.07)
        brace1 = Brace(VGroup(dash_line1, dash_line2), LEFT)
        brace2 = Brace(BC, DOWN)

        def create_tri_group0():
            tri1 = Polygon(A, P.get_center(), B, color=colors[0], fill_opacity=0.3, fill_color=colors[0])
            tri2 = Polygon(B, P.get_center(), C, color=colors[1], fill_opacity=0.3, fill_color=colors[1])
            tri3 = Polygon(A, P.get_center(), C, color=colors[2], fill_opacity=0.3, fill_color=colors[2])
            group = VGroup(tri1, tri3, tri2)
            return group

        def create_tri_group():
            add = MathTex("+").scale(8)
            tri1 = Polygon(A, P.get_center(), B, color=colors[0], fill_opacity=0.3, fill_color=colors[0])
            tri2 = Polygon(B, P.get_center(), C, color=colors[1], fill_opacity=0.3, fill_color=colors[1])
            tri3 = Polygon(A, P.get_center(), C, color=colors[2], fill_opacity=0.3, fill_color=colors[2])
            group = VGroup(tri1, add.copy(), tri2, add.copy(), tri3).scale(0.22).arrange(RIGHT)
            return group

        group_tri = create_tri_group().shift(UP * 2.5 + RIGHT * 2)
        result = MathTex("=", "{x", ".", "h", "\over", "2}").scale(1.5).next_to(group_tri, RIGHT)
        result[3].set_color(h_color)

        def create_abc():
            a = MathTex("{x", ".", "a", "\over", "2}", color=colors[0]).scale(1.5)
            a.move_to(group_tri[0])
            b = MathTex("{x", ".", "b", "\over", "2}", color=colors[1]).scale(1.5)
            b.move_to(group_tri[2])
            c = MathTex("{x", ".", "c", "\over", "2}", color=colors[2]).scale(1.5)
            c.move_to(group_tri[4])
            return VGroup(a, b, c)

        abc = create_abc()

        perpendicular = create_perpendicular()
        x = MathTex("x").scale(1.5).next_to(brace2, DOWN)
        h = MathTex("h", color=h_color).scale(1.5).next_to(brace1, LEFT)
        result1 = MathTex(r"\rightarrow", "a", "+", "b", "+", "c", "=", "h").scale(1.5).shift(RIGHT * 3)
        for i, j in zip((1, 3, 5, 7), colors):
            result1[i].set_color([j])
        group0 = create_tri_group0()
        cm = MarkupText("Cách 2", font_size=45,
                           font="Sans", color=YELLOW).to_corner(DR).shift(UP)
        self.my_play(Create(AB), Create(BC), Create(AC), Write(cm), Create(P))
        self.my_play(FadeIn(P), LaggedStart(*[
            Create(i) for i in edge
        ]))
        self.my_play(LaggedStart(*[
            Create(i) for i in group0
        ]))

        self.my_play(LaggedStart(*[
            ReplacementTransform(group0[0].copy(), group_tri[0]),
            ReplacementTransform(group0[2].copy(), group_tri[2]),
            ReplacementTransform(group0[1].copy(), group_tri[4]),
        ], lag_ratio=0.5))
        self.my_play(FadeIn(brace2, shift=UP), FadeIn(x, shift=UP))
        self.my_play(FadeIn(brace1, shift=RIGHT), FadeIn(h, shift=RIGHT), Create(dash_line1), Create(dash_line2))
        self.my_play(LaggedStart(*[
            FadeIn(group_tri[1], shift=UP),
            FadeIn(group_tri[3], shift=UP),
            FadeIn(result[0], shift=UP)
        ], lag_ratio=0.3))
        self.my_play(LaggedStart(*[
            Transform(x.copy(), result[1]),
            Transform(h.copy(), result[3]),
            FadeIn(result[2]), FadeIn(result[4]), FadeIn(result[5])
        ], lag_ratio=0.5))
        self.my_play(*[FadeOut(i) for i in (group0)])
        self.my_play(LaggedStart(*[
            Create(i) for i in perpendicular
        ]))
        for i, j in zip((group_tri[0], group_tri[2], group_tri[4]), abc):
            self.play(Transform(i, j))
        self.my_play(Write(result1))
        self.my_play(Circumscribe(result1))
        self.wait()
