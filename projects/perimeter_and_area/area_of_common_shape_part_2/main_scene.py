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


# equilateral triangle
class Scene1(ProofScene):
    def setup(self):
        import numpy as np
        self.create_title(r"Equilateral triangle", r"(Tam giác đều)")

    def construct(self):
        A = np.array([0, 3.464, 0])
        B = np.array([-2, 0, 0])
        C = np.array([2, 0, 0])
        H = ORIGIN

        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.7,
        }
        main_tri = VMobject().set_points_as_corners([A, B, C, A])
        line = Line(start=A, end=H, stroke_width=2)
        sub_left = VMobject(fill_color=YELLOW, **kwargs).set_points_as_corners([A, B, H, A])
        sub_right = VMobject(fill_color=RED, **kwargs).set_points_as_corners([A, H, C, A])

        rectangle = Rectangle(width=2, height=3.464).align_to(main_tri, DL)

        brace_ab = BraceBetweenPoints(A, B)
        text_ab = brace_ab.get_text("$$a$$")
        brace_ac = BraceBetweenPoints(C, A)
        text_ac = brace_ac.get_text("$$a$$")
        brace_bc = BraceBetweenPoints(B, C)
        text_bc = brace_bc.get_text("$$a$$")
        brace_bh = BraceBetweenPoints(B, H)
        text_bh = brace_bh.get_text(r"$${a}\over{2}$$")
        text_h = MathTex("h").next_to(line, RIGHT, buff=SMALL_BUFF)

        right_angle = RightAngle(line, Line(B, C), stroke_width=2, quadrant=(-1, 1))

        self.draw_title(main_tri)

        self.play(*[
            Write(i) for i in (brace_ab, brace_ac, brace_bc, text_ab, text_ac, text_bc)
        ])
        self.play(
            Create(line),
            Transform(brace_bc, brace_bh),
            ReplacementTransform(text_bc, text_bh[0][0]),
            Write(text_bh[0][1:]),
            Create(right_angle)
        )
        self.play(FadeIn(text_h), FadeOut(brace_ac), FadeOut(text_ac))

        text_using = Text("Using pythagoras theorem", font_size=25).to_corner(UR, buff=MED_LARGE_BUFF)
        pytago1 = MathTex(r"a^{2} = h^2 + ({a \over 2})^2").next_to(text_using, DOWN)
        pytago2 = MathTex(r"h^{2} = a^2 - ({a \over 2})^2").next_to(text_using, DOWN)
        pytago3 = MathTex(r"h^{2} = a^2 - {a^2 \over 4}").next_to(text_using, DOWN)
        pytago4 = MathTex(r"h^{2} = {{3a^2} \over 4}").next_to(text_using, DOWN)
        pytago5 = MathTex(r"h = {{\sqrt{3}a} \over 2}").next_to(text_using, DOWN)

        self.play(Write(text_using), *[
            Write(pytago1[0][i]) for i in set([i for i in range(12)]) - set([0, 3, 6,7,8,9,10])
        ])
        self.play(*[
            ReplacementTransform(i.copy(),pytago1[0][j])
            for i, j in zip([text_ab, text_h],[0,3])
        ], FadeTransformPieces(text_bh.copy(), pytago1[0][7:10]),
        FadeIn(pytago1[0][6]), FadeIn(pytago1[0][10]))

        # self.remove(sub_left, sub_right)
        # self.add(sub_left_1, sub_left_2, sub_right_1, sub_right_2)
        # self.play(Create(rectangle), Write(brace_rec), Write(text_rec))
        # self.play(Rotate(sub_left_1, PI, about_point=E),
        #           Rotate(sub_right_1, -PI, about_point=F))
        #
        # self.creat_formula(r"S = {{h \times b} \over 2}")
        # self.play(FadeTransform(text_h.copy(), self.formula[0][2]),
        #           FadeTransform(text_b.copy(), self.formula[0][4]))
        # self.draw_formula((0, 1, 3, 5, 6))
