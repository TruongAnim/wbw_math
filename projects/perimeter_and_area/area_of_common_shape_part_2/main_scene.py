from manim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[0]
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