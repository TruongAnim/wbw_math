import numpy as np
from manim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[4]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class ProofScene(Scene):
    def setup(self):
        pass

    def create_title(self, en, vn, edge=LEFT):
        self.title_en = Text(en, font_size=30).to_edge(edge)
        self.title_vn = Text(vn, font="Times New Roman",
                             font_size=24, slant=ITALIC) \
            .next_to(self.title_en, DOWN)

    def draw_title(self, other_obj):
        self.play(Write(self.title_en), Write(self.title_vn),
                  Write(other_obj), )

    def creat_formula(self, formula):
        self.formula = MathTex(formula).scale(1.5).shift(DOWN * 2.5)

    def draw_formula(self, indexs):
        self.play(LaggedStart(*[
            DrawBorderThenFill(self.formula[0][i]) for i in indexs
        ], lag_ratio=0.1))
        self.play(Circumscribe(self.formula))


# acute triangle
class Scene1(ProofScene):
    def setup(self):
        import numpy as np
        self.create_title(r"Acute triangle", r"(Tam giác nhọn)")

    def construct(self):
        A = np.array([0, 3, 0])
        B = np.array([-1.5, 0, 0])
        C = np.array([2.5, 0, 0])
        H = ORIGIN
        K = np.array([0, 1.5, 0])
        E = (A + B) / 2
        F = (A + C) / 2
        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.7,
        }
        main_tri = VMobject().set_points_as_corners([A, B, C, A])
        line = Line(start=A, end=H, stroke_width=0.5)
        sub_left = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([A, B, H, A])
        sub_right = VMobject(fill_color=RED, **kwargs).set_points_as_corners([A, H, C, A])
        sub_left_1 = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([A, E, K, A])
        sub_left_2 = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([E, K, H, B, E])
        sub_right_1 = VMobject(fill_color=RED, **kwargs).set_points_as_corners([A, K, F, A])
        sub_right_2 = VMobject(fill_color=RED, **kwargs).set_points_as_corners([F, K, H, C, F])
        rectangle = Rectangle(width=4, height=1.5).align_to(main_tri, DL)

        brace_h = Brace(main_tri, LEFT)
        text_h = brace_h.get_text("h")
        brace_b = Brace(main_tri, DOWN)
        text_b = brace_b.get_text("b")
        brace_rec = Brace(rectangle, RIGHT)
        text_rec = brace_rec.get_text(r"$${h}\over{2}$$")

        self.draw_title(main_tri)

        self.play(*[
            Write(i) for i in (brace_b, brace_h, text_b, text_h)
        ])
        self.play(*[
            FadeIn(i) for i in (sub_left, sub_right)
        ], Create(line))
        self.remove(sub_left, sub_right)
        self.add(sub_left_1, sub_left_2, sub_right_1, sub_right_2)
        self.play(Create(rectangle), Write(brace_rec), Write(text_rec))
        self.play(Rotate(sub_left_1, PI, about_point=E),
                  Rotate(sub_right_1, -PI, about_point=F))

        self.creat_formula(r"S = {{h \times b} \over 2}")
        self.play(FadeTransform(text_h.copy(), self.formula[0][2]),
                  FadeTransform(text_b.copy(), self.formula[0][4]))
        self.draw_formula((0, 1, 3, 5, 6))


# Parallelogram
class Scene2(ProofScene):
    def setup(self):
        import numpy as np
        self.create_title(r"Parallelogram", r"(Hình bình hành)")

    def construct(self):
        A = np.array([0, 3, 0])
        B = np.array([-1.5, 0, 0])
        C = np.array([2.5, 0, 0])
        D = np.array([4, 3, 0])
        H = ORIGIN
        K = np.array([4, 0, 0])

        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.7,
        }
        main_para = VMobject().set_points_as_corners([A, B, C, D, A])
        line = Line(start=A, end=H, stroke_width=1)
        ABHA = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([A, B, H, A])
        AHCDA = VMobject(fill_color=RED, **kwargs).set_points_as_corners([A, H, C, D, A])
        sub_line = Line(start=H, end=K, stroke_width=1)

        brace_h = Brace(main_para, LEFT)
        text_h = brace_h.get_text("h")
        brace_b = Brace(Line(start=B, end=C), DOWN)
        text_b = brace_b.get_text("b")
        h = MathTex("h").next_to(line, RIGHT)

        right_angle = RightAngle(line, sub_line, quadrant=(-1, 1), stroke_width=2)

        self.draw_title(main_para)

        self.play(*[
            Write(i) for i in (brace_b, brace_h, text_b, text_h)
        ])
        self.play(*[
            FadeIn(i) for i in (ABHA, AHCDA)
        ], Create(line), Write(h), Create(right_angle))

        self.play(*[
            i.animate.shift(RIGHT * 1.5) for i in (brace_b, text_b)
        ], ABHA.animate.shift(RIGHT * 4), run_time=3, rate_func=linear)

        self.creat_formula(r"S = {h \times b}")
        self.play(FadeTransform(text_h.copy(), self.formula[0][2]),
                  FadeTransform(text_b.copy(), self.formula[0][4]))
        self.draw_formula((0, 1, 3))


# obtuse triangle
class Scene3(ProofScene):
    def setup(self):
        import numpy as np
        self.create_title(r"Obtuse triangle", r"(Tam giác tù)", edge=RIGHT)

    def construct(self):
        A = np.array([2, 3.8, 0])
        B = np.array([-3, 0, 0])
        C = ORIGIN
        D = (A + C) / 2
        K = (A + B) / 2
        E = np.array([-3, 1.9, 0])
        F = np.array([0, 1.9, 0])
        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.7,
        }
        main_tri = VMobject().set_points_as_corners([A, B, C, A])
        line = Line(start=D, end=F, stroke_width=0.5)
        KBCF = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([K, B, C, F, K])
        FCD = VMobject(fill_color=RED, **kwargs).set_points_as_corners([F, C, D, F])
        KDA = VMobject(fill_color=BLUE, **kwargs).set_points_as_corners([K, D, A, K])

        rectangle = Rectangle(width=3, height=1.9).align_to(main_tri, DL)

        brace_h = Brace(main_tri, RIGHT)
        text_h = brace_h.get_text("h")
        brace_b = Brace(rectangle, DOWN)
        text_b = brace_b.get_text("b")
        brace_rec = Brace(rectangle, LEFT)
        text_rec = brace_rec.get_text(r"$${h}\over{2}$$")

        self.draw_title(main_tri)

        self.play(*[
            Write(i) for i in (brace_b, brace_h, text_b, text_h)
        ])
        self.play(Create(rectangle), Write(brace_rec), Write(text_rec))
        self.play(*[
            FadeIn(i) for i in (KBCF, KDA, FCD)
        ], Create(line))
        self.play(Rotate(KDA, PI, about_point=K))
        FCD.generate_target()
        FCD.target.shift(LEFT * 3)
        self.play(MoveToTarget(FCD), path_arc=210 * DEGREES, run_time=3)

        self.creat_formula(r"S = {{h \times b} \over 2}")
        self.play(FadeTransform(text_h.copy(), self.formula[0][2]),
                  FadeTransform(text_b.copy(), self.formula[0][4]))
        self.draw_formula((0, 1, 3, 5, 6))


# Rhombus
class Scene4(ProofScene):
    def setup(self):
        import numpy as np
        self.create_title(r"Rhombus", r"(Hình thoi)")

    def construct(self):
        A = np.array([0, 3.8, 0])
        B = np.array([-2.5, 1.9, 0])
        C = ORIGIN
        D = np.array([2.5, 1.9, 0])
        K = np.array([0, 1.9, 0])

        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.7,
        }
        main_rhombus = VMobject().set_points_as_corners([A, B, C, D, A])
        AC = Line(start=A, end=C, stroke_width=1)
        BD = Line(start=B, end=D, stroke_width=1)
        AKB = VMobject(fill_color=RED, **kwargs).set_points_as_corners([A, K, B, A])
        AKD = VMobject(fill_color=BLUE, **kwargs).set_points_as_corners([A, K, D, A])
        CKB = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([C, K, B, C])
        CKD = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([C, K, D, C])

        brace_h = Brace(main_rhombus, LEFT)
        text_h = brace_h.get_text("h")
        brace_b = Brace(main_rhombus, DOWN)
        text_b = brace_b.get_text("b")
        brace_h2 = Brace(CKD, RIGHT)
        h = brace_h2.get_text(r"$$h \over 2$$")

        rec = Rectangle(width=5, height=1.9).align_to(main_rhombus, DR)

        right_angle = RightAngle(AC, BD, quadrant=(-1, 1), stroke_width=2)

        self.draw_title(main_rhombus)

        self.play(*[
            Write(i) for i in (brace_b, brace_h, text_b, text_h)
        ])
        self.play(*[
            FadeIn(i) for i in (AKB, AKD, CKB, CKD)
        ], Create(AC), Create(BD), Create(right_angle))

        self.play(AKB.animate.shift(RIGHT * 2.5 + DOWN * 1.9), run_time=2, rate_func=linear)
        self.play(AKD.animate.shift(LEFT * 2.5 + DOWN * 1.9), run_time=2, rate_func=linear)
        self.play(Create(rec), Write(brace_h2), Write(h))

        self.creat_formula(r"S = {{h \times b} \over 2}")
        self.play(FadeTransform(text_h.copy(), self.formula[0][2]),
                  FadeTransform(text_b.copy(), self.formula[0][4]))
        self.draw_formula((0, 1, 3, 5, 6))


# Trapezoid
class Scene5(ProofScene):
    def setup(self):
        import numpy as np
        self.create_title(r"Trapezoid", r"(Hình thang)")

    def construct(self):
        A = np.array([-1, 3, 0])
        B = np.array([-2.5, 0, 0])
        C = np.array([2, 0, 0])
        D = np.array([1, 3, 0])
        I = np.array([-1, 0, 0])
        K = np.array([1, 0, 0])
        E = (A + B) / 2
        H = (C + D) / 2
        F = (A + I) / 2
        G = (D + K) / 2

        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.7,
        }
        main_rhombus = VMobject().set_points_as_corners([A, B, C, D, A])
        horizontal_line1 = Line(start=E, end=H, stroke_width=1)
        horizontal_line2 = Line(start=B, end=C, stroke_width=1)
        vertical_line1 = Line(start=A, end=I, stroke_width=1)
        vertical_line2 = Line(start=D, end=K, stroke_width=1)
        EBCH = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([E, B, C, H, E])
        AEF = VMobject(fill_color=BLUE, **kwargs).set_points_as_corners([A, E, F, A])
        AFGD = VMobject(fill_color=TEAL, **kwargs).set_points_as_corners([A, F, G, D, A])
        DGH = VMobject(fill_color=RED, **kwargs).set_points_as_corners([D, G, H, D])

        brace_h = Brace(main_rhombus, LEFT)
        text_h = brace_h.get_text("h")
        brace_a = Brace(main_rhombus, DOWN)
        text_a = brace_a.get_text("a")
        brace_b = Brace(Line(start=A, end=D), UP)
        text_b = brace_b.get_text("b", buff=SMALL_BUFF)
        brace_h2 = Brace(EBCH, RIGHT)
        h = brace_h2.get_text(r"$$h \over 2$$")

        rec = Rectangle(width=6.5, height=1.5).align_to(main_rhombus, DL)

        right_angle_1 = RightAngle(vertical_line1, horizontal_line2, quadrant=(-1, 1), stroke_width=2)
        right_angle_2 = RightAngle(vertical_line2, horizontal_line2, quadrant=(-1, 1), stroke_width=2)

        self.draw_title(main_rhombus)

        self.play(*[
            Write(i) for i in (brace_b, brace_h, brace_a, text_b, text_h, text_a)
        ])
        self.play(*[
            Write(i) for i in (vertical_line1, vertical_line2,
                               horizontal_line1, h, brace_h2,
                               right_angle_1, right_angle_2)
        ])
        self.play(LaggedStart( *[
            FadeIn(i) for i in (AEF, AFGD, DGH, EBCH)
        ], lag_ratio=0.2))

        self.play(Rotate(AEF, PI, about_point=E),
                  Rotate(DGH, -PI, about_point=H))
        self.play(*[
            i.animate.shift(RIGHT * j)
            for i,j in zip(
                (brace_b, text_b, AFGD, brace_h2, h),
                (3,3,3,2,2)
            )
        ])
        self.play(*[
            i.animate.shift(DOWN * 1.5)
            for i in (brace_b, text_b, AFGD)
        ])
        self.play(Create(rec))

        self.creat_formula(r"S = {{(a+b) \times h} \over 2}")
        self.play(FadeTransform(text_a.copy(), self.formula[0][3]),
                  FadeTransform(text_b.copy(), self.formula[0][5]),
                  FadeTransform(text_h.copy(), self.formula[0][8]))
        self.draw_formula((0,1,2,4,6,7,9,10))
