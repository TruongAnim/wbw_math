from manim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
# SCENE_NAME = list_scene[4]
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


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Scene1(MyScene):
    def construct(self):
        kite = SVGMobject("kite")
        # self.add(kite)
        tree = SVGMobject("tree").stretch_to_fit_height(5).shift(RIGHT)
        tree.set_color(GREEN)
        brace = Brace(tree, RIGHT)
        brace_tex = brace.get_tex("=")

        B = Dot(tree.get_bottom())
        C = Dot(tree.get_top())
        A = Dot(B.get_center() + LEFT * 4)
        AC = DashedLine(A, C)
        AB = Line(A, B, color=RED)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C"),
                (WHITE, WHITE, WHITE),
                (A, B, C,),
                (LEFT, DOWN, UP)
            )
        ]
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle = Angle(AB, AC, radius=0.5, color=GREEN)
        alpha = MathTex(r"\alpha", color=GREEN).next_to(angle, UR, buff=0.1)
        formula = MathTex(r"AB\times tan(\alpha)").next_to(brace_tex, RIGHT)
        self.my_play(LaggedStart(*[
            DrawBorderThenFill(tree),
            Create(ABC),
            *[Write(i)
              for i in (A, B, C, alpha, angle, square1, *text)]
        ]))
        self.my_play(*[
            Write(i)
            for i in (brace, brace_tex, formula)
        ])


class Scene2(MyScene):
    def construct(self):
        kite = SVGMobject("kite").shift(UP * 2.5)
        # self.add(kite)

        C = Dot(kite.get_center())
        B = Dot(C.get_center() + DOWN * 5)
        A = Dot(B.get_center() + LEFT * 4)
        AC = Line(A, C, color=RED)
        AB = DashedLine(A, B)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        brace = Brace(BC, RIGHT)
        brace_tex = brace.get_tex("=")
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C"),
                (WHITE, WHITE, WHITE),
                (A, B, C,),
                (LEFT, DOWN, RIGHT)
            )
        ]
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha = MathTex(r"\alpha", color=GREEN).next_to(angle, UR, buff=0.1)
        formula = MathTex(r"AB", r"\times tan(\alpha)").next_to(brace_tex, RIGHT)
        string_len = MathTex("300m", color=RED).next_to(AC.get_center(), LEFT)
        self.my_play(LaggedStart(*[
            DrawBorderThenFill(kite),
            Create(ABC),
            *[Write(i)
              for i in (A, B, C, square1, *text)]
        ]))
        self.my_play(Write(string_len), Write(angle), Write(alpha))
        self.my_play(*[
            Write(i)
            for i in (brace, brace_tex, formula)
        ])
        cross1 = Cross(formula[0])
        cross2 = Cross(Square(side_length=0.5).move_to(AB))
        self.my_play(Create(cross1), Create(cross2))


class Scene3(MyScene):
    def construct(self):
        C = Dot(ORIGIN + UP * 2.5 + LEFT * 2)
        B = Dot(C.get_center() + DOWN * 5)
        A = Dot(B.get_center() + LEFT * 4)
        AC = Line(A, C, color=RED)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        brace = Brace(BC, RIGHT)
        brace_tex = brace.get_tex("=")
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C"),
                (WHITE, WHITE, WHITE),
                (A, B, C,),
                (LEFT, DOWN, RIGHT)
            )
        ]
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha = MathTex(r"\alpha", color=GREEN).scale(1.5).move_to(Angle(AB, AC, radius=1.5))
        self.my_play(LaggedStart(*[
            Create(ABC),
            *[Write(i)
              for i in (A, B, C, square1, angle, alpha)]
        ]))
        huyen = MathTex(r"\text{Huyền}", tex_template=myTemplate, color=RED).rotate(AC.get_angle()).next_to(
            AC.get_center(), LEFT)
        doi = MathTex(r"\text{Đối}", tex_template=myTemplate, color=YELLOW).rotate(-PI / 2).next_to(BC, RIGHT)
        ke = MathTex(r"\text{Kề}", tex_template=myTemplate, color=BLUE).next_to(AB, DOWN)
        color_map = {
            r"\alpha": GREEN,
            r"{\text{Đối}": YELLOW,
            r"\text{Đối}}": YELLOW,
            r"{\text{Kề}": BLUE,
            r"\text{Kề}}": BLUE,
            r"\text{Huyền}}": RED,
            r"{\text{Huyền}": RED
        }
        cot = MathTex(r"cot(\alpha)", "=", r"{\text{Kề}", "\over", r"\text{Đối}}",
                      tex_template=myTemplate, tex_to_color_map=color_map) \
            .to_corner(UR, buff=LARGE_BUFF).shift(UP * 0.5)
        tan = MathTex(r"tan(\alpha)", "=", r"{\text{Đối}", "\over", r"\text{Kề}}",
                      tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cot, LEFT, buff=1.1)
        sin = MathTex(r"sin(\alpha)", "=", r"{\text{Đối}", "\over", r"\text{Huyền}}",
                      tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(tan, DOWN, buff=1.5, aligned_edge=LEFT)
        cos = MathTex(r"cos(\alpha)", "=", r"{\text{Kề}", "\over", r"\text{Huyền}}",
                      tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(sin, DOWN, buff=1.5, aligned_edge=LEFT)

        cose = MathTex(r"cose(\alpha)", "=", r"{\text{Huyền}", "\over", r"\text{Đối}}",
                       tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cot, DOWN, buff=1.5, aligned_edge=LEFT)

        sec = MathTex(r"sec(\alpha)", "=", r"{\text{Huyền}", "\over", r"\text{Kề}}",
                      tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cose, DOWN, buff=1.5, aligned_edge=LEFT)

        sin1 = MathTex(r"{1\over{sin(\alpha)}}", "=", r"{\text{Huyền}", "\over", r"\text{Đối}}",
                       tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cot, DOWN, buff=1.5, aligned_edge=LEFT)

        cos1 = MathTex(r"{1\over{cos(\alpha)}}", "=", r"{\text{Huyền}", "\over", r"\text{Kề}}",
                       tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cose, DOWN, buff=1.5, aligned_edge=LEFT)

        self.my_play(*[
            Write(i)
            for i in (huyen, doi, ke)
        ])

        def create_anim(obj, t1, t2):
            self.my_play(*[
                Write(i)
                for i in (obj[0:4], obj[5])
            ])
            self.my_play(LaggedStart(*[
                ReplacementTransform(t1.copy(), obj[4]),
                ReplacementTransform(t2.copy(), obj[6])
            ]))

        for i, j in zip((tan, sin, cos, cot, cose, sec),
                        ((doi, ke), (doi, huyen), (ke, huyen), (ke, doi), (huyen, doi), (huyen, ke))):
            create_anim(i, *j)
        self.my_play(Transform(cose, sin1), Transform(sec, cos1))


class Scene4(MyScene):
    def construct(self):
        C = Dot(ORIGIN + UP * 2.5 + LEFT * 2)
        B = Dot(C.get_center() + DOWN * 5)
        A = Dot(B.get_center() + LEFT * 4)
        AC = Line(A, C, color=RED)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        brace = Brace(BC, RIGHT)
        brace_tex = brace.get_tex("=")
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C"),
                (WHITE, WHITE, WHITE),
                (A, B, C,),
                (LEFT, DOWN, RIGHT)
            )
        ]
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha = MathTex(r"\alpha", color=GREEN).scale(1.5).move_to(Angle(AB, AC, radius=1.5))
        self.my_play(LaggedStart(*[
            Create(ABC),
            *[Write(i)
              for i in (A, B, C, square1, angle, alpha)]
        ]))
        huyen = MathTex(r"\text{Huyền}", tex_template=myTemplate, color=RED).rotate(AC.get_angle()).next_to(
            AC.get_center(), LEFT)
        doi = MathTex(r"\text{Đối}", tex_template=myTemplate, color=YELLOW).rotate(-PI / 2).next_to(BC, RIGHT)
        ke = MathTex(r"\text{Kề}", tex_template=myTemplate, color=BLUE).next_to(AB, DOWN)
        color_map = {
            r"\alpha": GREEN,
            r"{\text{Đối}": YELLOW,
            r"\text{Đối}}": YELLOW,
            r"\text{Đối}": YELLOW,
            r"{\text{Kề}": BLUE,
            r"\text{Kề}}": BLUE,
            r"\text{Kề}": BLUE,
            r"\text{Huyền}}": RED,
            r"{\text{Huyền}": RED,
            r"\text{Huyền}": RED
        }
        scale = 0.9
        cot = MathTex(r"arctan\left(", r"\text{Đối}", "\over", r"\text{Kề}", r" \right)=", r"\alpha",
                      tex_template=myTemplate, tex_to_color_map=color_map).scale(scale) \
            .to_corner(UR, buff=0.9).shift(UP * 0.5)
        tan = MathTex(r"tan(\alpha)", "=", r"{\text{Đối}", "\over", r"\text{Kề}}",
                      tex_template=myTemplate, tex_to_color_map=color_map).scale(scale) \
            .next_to(cot, LEFT, buff=1.1)
        sin = MathTex(r"sin(\alpha)", "=", r"{\text{Đối}", "\over", r"\text{Huyền}}",
                      tex_template=myTemplate, tex_to_color_map=color_map).scale(scale) \
            .next_to(tan, DOWN, buff=1.5, aligned_edge=LEFT)
        cos = MathTex(r"cos(\alpha)", "=", r"{\text{Kề}", "\over", r"\text{Huyền}}",
                      tex_template=myTemplate, tex_to_color_map=color_map).scale(scale) \
            .next_to(sin, DOWN, buff=1.5, aligned_edge=LEFT)

        cose = MathTex(r"arcsin\left(", r"\text{Đối}", "\over", r"\text{Huyền}", r" \right)=", r"\alpha",
                       tex_template=myTemplate, tex_to_color_map=color_map).scale(scale) \
            .next_to(cot, DOWN, buff=1.5, aligned_edge=LEFT)

        sec = MathTex(r"arccos\left(", r"\text{Kề}", "\over", r"\text{Huyền}", r" \right)=", r"\alpha",
                      tex_template=myTemplate, tex_to_color_map=color_map).scale(scale) \
            .next_to(cose, DOWN, buff=1.5, aligned_edge=LEFT)

        sin1 = MathTex(r"{1\over{sin(\alpha)}}", "=", r"{\text{Huyền}", "\over", r"\text{Đối}}",
                       tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cot, DOWN, buff=1.5, aligned_edge=LEFT)

        cos1 = MathTex(r"{1\over{cos(\alpha)}}", "=", r"{\text{Huyền}", "\over", r"\text{Kề}}",
                       tex_template=myTemplate, tex_to_color_map=color_map) \
            .next_to(cose, DOWN, buff=1.5, aligned_edge=LEFT)

        self.my_play(*[
            Write(i)
            for i in (huyen, doi, ke)
        ])
        self.my_play(*[
            Write(i)
            for i in (sin)
        ])
        self.my_play(*[
            Write(cose[0]),
            Write(cose[4]),
        ])
        self.my_play(Transform(sin[4:].copy(), cose[1:4], path_arc=PI))
        self.my_play(Transform(sin[1].copy(), cose[-1], path_arc=PI))
        self.my_play(*[
            Write(i)
            for i in (tan, cos, cot, sec)
        ])


class Scene5(MyScene):
    def construct(self):
        vertical_line = Line(UP * 3, DOWN * 3)
        vertical_line2 = Line(UP * 3 + LEFT * 5, DOWN * 3 + LEFT * 5)
        horizontal_line = Line(UP * 2 + LEFT * 4, UP * 2 + RIGHT * 4)
        cotang = MathTex("Cotan").next_to(horizontal_line, UP).shift(LEFT * 3)
        arctang = MathTex("Arctan").next_to(horizontal_line, UP).shift(RIGHT * 3)
        fraction = MathTex(r"{3 \over 5 }\to {5 \over 3}")
        fraction2 = MathTex(r"tan = {\text{Đối}\over \text{Kề}} \to cot = {\text{Kề} \over \text{Đối}}",
                            tex_template=myTemplate).scale(0.8)
        fraction.next_to(cotang, DOWN, buff=1, aligned_edge=LEFT)
        fraction2.next_to(fraction, DOWN, buff=0.5)
        inverse = MathTex(r"tan({60^\circ})=\sqrt{3}").next_to(arctang, DOWN, buff=1, aligned_edge=RIGHT)
        inverse2 = MathTex(r"arctan(\sqrt{3})=60^\circ").next_to(inverse, DOWN, buff=0.5)
        cotan_en = Text("Multiplicative inverse", font_size=30, color=RED).next_to(fraction2, DOWN)
        cotan_vn = Text("Nghịch đảo phép nhân", font="Sans", font_size=30, color=YELLOW).next_to(cotan_en, DOWN)
        arctan_en = Text("Inverse", font_size=30, color=RED).next_to(cotan_en, RIGHT, buff=2.5)
        arctan_vn = Text("Nghịch đảo (Hàm ngược)", font="Sans", font_size=30, color=YELLOW)\
            .next_to(arctan_en, DOWN)\
            .shift(RIGHT)

        self.my_play(*[
            Write(i)
            for i in (vertical_line, horizontal_line, cotang, arctang)
        ])
        self.my_play(Write(fraction))
        self.my_play(Write(fraction2), Write(cotan_vn), Write(cotan_en))
        self.my_play(Write(inverse))
        self.my_play(Write(inverse2))
        self.my_play(Write(arctan_vn), Write(arctan_en))


class Scene6(MyScene):
    def construct(self):
        kite = SVGMobject("kite").shift(UP * 2.5)
        # self.add(kite)

        C = Dot(kite.get_center())
        B = Dot(C.get_center() + DOWN * 5)
        A = Dot(B.get_center() + LEFT * 4)
        AC = Line(A, C, color=RED)
        AB = DashedLine(A, B)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        brace = Brace(BC, RIGHT)
        brace_tex = brace.get_tex("=")
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C"),
                (WHITE, WHITE, WHITE),
                (A, B, C,),
                (LEFT, DOWN, RIGHT)
            )
        ]
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha = MathTex(r"\alpha", color=GREEN).next_to(angle, UR, buff=0.1)
        formula = MathTex(r"AC", r"\times sin(\alpha)").next_to(brace_tex, RIGHT)
        formula[0].set_color(RED)
        string_len = MathTex("300m", color=RED).next_to(AC.get_center(), LEFT)
        self.my_play(LaggedStart(*[
            DrawBorderThenFill(kite),
            Create(ABC),
            *[Write(i)
              for i in (A, B, C, square1, *text)]
        ]))
        self.my_play(Write(string_len), Write(angle), Write(alpha))
        self.my_play(*[
            Write(i)
            for i in (brace, brace_tex, formula)
        ])
