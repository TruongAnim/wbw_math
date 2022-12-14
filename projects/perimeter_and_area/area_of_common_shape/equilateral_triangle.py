from manim import *

list_scene = ("Scene1",)
SCENE_NAME = list_scene[0]
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class ProofScene(Scene):
    def setup(self):
        pass

    def create_title(self, vn, en, edge=LEFT):
        self.title_vn = Text(vn, font="Times New Roman", font_size=30) \
            .to_edge(edge)
        self.title_en = Text(en, font_size=25, slant=ITALIC) \
            .next_to(self.title_vn, DOWN)

    def draw_title(self, other_obj):
        self.my_play(Write(self.title_en), Write(self.title_vn),
                     Write(other_obj), )

    def creat_formula(self, formula):
        self.formula = MathTex(formula).scale(1.5).shift(DOWN * 2.5)

    def draw_formula(self, indexs):
        self.my_play(LaggedStart(*[
            DrawBorderThenFill(self.formula[0][i]) for i in indexs
        ], lag_ratio=0.1))
        self.my_play(Circumscribe(self.formula))

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


# equilateral triangle
class Scene1(ProofScene):
    def setup(self):
        self.create_title(r"Tam giác đều", r"(Equilateral triangle)")

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

        self.my_play(*[
            FadeIn(i, shift=j) for i, j in zip(
                (brace_ab, text_ab, brace_ac, text_ac, brace_bc, text_bc),
                (DR, DR, DL, DL, UP, UP)
            )
        ])
        self.my_play(
            Create(line),
            Transform(brace_bc, brace_bh),
            ReplacementTransform(text_bc, text_bh[0][0]),
            Write(text_bh[0][1:]),
            Create(right_angle)
        )
        self.my_play(FadeIn(text_h), FadeOut(brace_ac), FadeOut(text_ac))

        text_using = Text("Using pythagoras theorem", font_size=25).to_corner(UR, buff=MED_LARGE_BUFF)
        pytago1 = MathTex(r"a^{2} = h^2 + ({a \over 2})^2").next_to(text_using, DOWN)
        pytago2 = MathTex(r"h^{2} = a^2 - ({a \over 2})^2").next_to(text_using, DOWN)
        pytago3 = MathTex(r"h^{2} = a^2 - {a^2 \over 4}").next_to(text_using, DOWN)
        pytago4 = MathTex(r"h^{2} = {{3a^2} \over 4}").next_to(text_using, DOWN)
        pytago5 = MathTex(r"h = {{\sqrt{3}a} \over 2}").next_to(text_using, DOWN)

        self.my_play(Write(text_using), *[
            Write(pytago1[0][i]) for i in set([i for i in range(12)]) - set([0, 3, 6, 7, 8, 9, 10])
        ])
        self.my_play(*[
            ReplacementTransform(i.copy(), pytago1[0][j])
            for i, j in zip([text_ab, text_h], [0, 3])
        ], FadeTransformPieces(text_bh.copy(), pytago1[0][7:10]),
                     FadeIn(pytago1[0][6]), FadeIn(pytago1[0][10]))

        self.my_play(*[
            ReplacementTransform(pytago1[0][i], pytago2[0][j])
            for i, j in zip([2, 5, 6, 7, 8, 9, 10, 11], [2, 5, 6, 7, 8, 9, 10, 11])
        ], *[ReplacementTransform(pytago1[0][i], pytago2[0][j], path_arc=PI)
             for i, j in zip([0, 1, 3, 4], [3, 4, 0, 1])])

        self.my_play(*[
            ReplacementTransform(pytago2[0][i], pytago3[0][j])
            for i, j in zip([0, 1, 2, 3, 4, 5, 7, 8, 9, 11], [0, 1, 2, 3, 4, 5, 6, 8, 9, 7])
        ], *[FadeOut(pytago2[0][i]) for i in (6, 10)])

        self.my_play(*[
            ReplacementTransform(pytago3[0][i], pytago4[0][j])
            for i, j in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 4, 5, 6, 7])
        ], FadeIn(pytago4[0][3]))

        self.my_play(*[
            ReplacementTransform(pytago4[0][i], pytago5[0][j])
            for i, j in zip([0, 1, 2, 3, 4, 5, 6, 7], [0, 2, 1, 4, 5, 3, 6, 7])
        ])

        self.my_play(*[
            Indicate(pytago5)
        ])

        self.creat_formula(r"S = {a \over 2} \times {{\sqrt{3}a} \over 2}")
        self.my_play(FadeTransform(text_bh.copy(), self.formula[0][2:5]),
                     FadeTransform(pytago5[0][2:].copy(), self.formula[0][6:]))
        self.my_play(*[Write(self.formula[0][i]) for i in (0, 1, 5)])
        result = MathTex(r"S = {{\sqrt{3}a^2} \over 4}").scale(1.5).align_to(self.formula, DL)
        self.my_play(*[Transform(self.formula[0][i], result[0][j])
                       for i, j in zip([0, 1, 3, 4, 6, 7, 8, 9, 10, 11],
                                       [0, 1, 7, 8, 2, 3, 4, 5, 7, 8])
                       ], FadeOut(self.formula[0][5]),
                     Transform(self.formula[0][2], result[0][6], path_arc=-PI))
        self.my_play(Circumscribe(result, run_time=2))
