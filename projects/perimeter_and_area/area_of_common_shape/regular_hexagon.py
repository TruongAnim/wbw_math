from manim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[0]
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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


# regular hexagon
class Scene1(ProofScene):
    def setup(self):
        super().setup()
        self.create_title(r"Lục giác đều", r"(Regular hexagon)")

    def construct(self):
        circle = Circle(radius=2).shift(UP * 1.5)
        points = [circle.point_from_proportion(i / 6) for i in range(6)]
        hexagon = Polygon(*points)
        center = circle.get_center()

        lines = [Line(start=points[i], end=points[j], stroke_width=2)
                 for i, j in zip([0, 1, 2], [3, 4, 5])]

        brace_a = BraceBetweenPoints(points[4], points[5], buff=MED_SMALL_BUFF)
        text_a = brace_a.get_text("$$a$$", buff=SMALL_BUFF)

        angle_init = ((0, 1), (1, 2), (2, 0), (0, 1), (1, 2), (2, 0),)
        angle_quadrent = ((-1, -1), (-1, -1), (-1, 1), (1, 1), (1, 1), (1, -1))

        kwargs = {
            "stroke_width": 0,
            "fill_opacity": 0.6,
            "fill_color": YELLOW
        }

        sub_tri = Polygon(points[4], points[5], center, **kwargs)
        angles = [Angle(lines[i[0]], lines[i[1]], quadrant=(j[0], j[1]),
                        stroke_width=3, stroke_color=RED)
                  for i, j in zip(angle_init, angle_quadrent)]

        text_angle = MathTex("60^{\circ}").scale(0.7).next_to(angles[4], DOWN, SMALL_BUFF)
        text_equil_tri_vn = Text("Tam giác đều", font="Times New Roman", font_size=25) \
            .to_corner(UR, buff=LARGE_BUFF)
        text_equil_tri_en = Text("(Equilateral triangle)",
                                 font_size=20, slant=ITALIC) \
            .next_to(text_equil_tri_vn, DOWN)

        text_s = MathTex("\implies S = {{\sqrt{3}a^2} \over 4}") \
            .next_to(text_equil_tri_en, DOWN)
        text_remember = Text(r"remember  that?", font_size=20).next_to(text_s, DOWN)

        mark_location = [j.point_from_proportion(i) for i in (1 / 4, 3 / 4)
                         for j in lines]
        mark_rotation = [PI / 2, -PI / 4, PI / 4, PI / 2, -PI / 4, PI / 4]
        marks = [MathTex("=").move_to(i).rotate(j)
                 for i, j in zip(mark_location, mark_rotation)]

        arrow = Arrow(start=text_equil_tri_en.get_left(),
                      end=lines[2].point_from_proportion(0.75))

        self.draw_title(hexagon)
        self.my_play(*[FadeIn(i, shift=UP) for i in (brace_a, text_a)])
        self.my_play(Create(circle))
        self.my_play(LaggedStart(*[
            Create(line) for line in lines
        ], lag_ratio=0.2))
        self.my_play(LaggedStart(*[
            Create(angle) for angle in angles
        ], *[
            Create(mark) for mark in marks
        ], lag_ratio=0), Write(text_angle))
        self.my_play(Write(sub_tri), *[
            FadeOut(i) for i in (circle, *angles[0:4], *marks[0:4],
                                 angles[5])
        ])
        self.my_play(*[
            Write(i) for i in ( text_equil_tri_en, text_equil_tri_vn,
                               text_s, text_remember)
        ], GrowArrow(arrow))

        #
        self.creat_formula(r"S = 6 \times {{\sqrt{3}a^2} \over 4}")
        copy_tri = sub_tri.copy().scale(0.4).move_to(self.formula[0][9])
        self.my_play(ReplacementTransform(sub_tri.copy(), copy_tri), Write(self.formula[0][:4]))
        self.my_play(FadeOut(copy_tri),
                     FadeTransformPieces(text_s[0][4:].copy(), self.formula[0][4:]))
        result = MathTex(r"S = {3 \over 2}{\sqrt{3}a^2}") \
            .scale(1.5).align_to(self.formula, DL)
        self.my_play(*[Transform(self.formula[0][i], result[0][j])
                       for i, j in zip([0, 1, 2, 4, 5, 6, 7, 8, 9, 10],
                                       [0, 1, 2, 5, 6, 7, 8, 9, 3, 4])
                       ], FadeOut(self.formula[0][3]))
        self.my_play(Circumscribe(result, run_time=2))
