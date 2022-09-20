from manim import *
from common.utils.manim_utils import line_intersection_
from common.utils.utils import lerp

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
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


class Scene1(MyScene):
    def construct(self):
        tree = SVGMobject("tree").stretch_to_fit_height(5).shift(RIGHT * 5)
        tree.set_color(GREEN)
        brace = Brace(tree, LEFT)
        brace_tex = brace.get_tex("?")

        B = Dot(tree.get_bottom())
        C = Dot(tree.get_top())
        A = Dot(B.get_center() + LEFT * 4)
        H = Dot(B.get_center() + LEFT * 2.5)
        AC = Line(A, C)
        K = Dot(line_intersection_(Line(H.get_center(), H.get_center() + UP), AC))
        AB = Line(A, B)
        BC = Line(B, C)
        HK = Line(H.get_center(), K.get_center())
        AH = Line(A, H)
        AK = Line(A, K)
        ABC = VGroup(AB, AC, BC)
        ABC.set_color(RED)
        AHK = VGroup(AH, AK, HK)
        AHK.set_color(YELLOW)
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C", "H", "K"),
                (TEAL, RED, RED, YELLOW, YELLOW),
                (A, B, C, H, K),
                (LEFT, DOWN, UP, DOWN, UP)
            )
        ]
        square1 = Square(side_length=0.2).move_to(H).shift(UP * 0.1 + RIGHT * 0.1)
        square2 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)

        simi_text = MathTex(r"\triangle{ABC}", r"\sim", r"\triangle{AHK}", r"\to").to_edge(UL)
        simi_text.shift(DOWN)
        simi_text[0].set_color(RED)
        simi_text[2].set_color(YELLOW)
        formula1 = MathTex("{BC", "\over", "AB}", "=", "{HK", "\over ", "AH}").next_to(simi_text, RIGHT)
        formula1[0].set_color(RED)
        formula1[2].set_color(RED)
        formula1[4].set_color(YELLOW)
        formula1[6].set_color(YELLOW)
        to = MathTex(r"\to").next_to(simi_text[3], DOWN * 4, aligned_edge=LEFT)
        formula2 = MathTex("BC", "=", "{HK", "\over", "AH}", r"\times", "AB").next_to(to, RIGHT)
        formula2[0].set_color(RED)
        formula2[2].set_color(YELLOW)
        formula2[4].set_color(YELLOW)
        formula2[6].set_color(RED)
        self.play(DrawBorderThenFill(tree))
        self.play(FadeIn(brace, shift=RIGHT), FadeIn(brace_tex, shift=RIGHT))
        self.play(FadeOut(brace, brace_tex))
        self.bring_to_back(square2)
        self.play(Create(ABC), *[
            Write(i) for i in text[0:3]
        ], *[
            Write(i) for i in (A, B, C)
        ])
        self.play(FadeIn(HK, shift=DOWN * 3))
        self.bring_to_back(square1)
        self.play(*[
            Write(i)
            for i in (H, K, text[3], text[4])
        ], Write(AK), Write(AH))
        self.play(Write(simi_text),
                  *[Write(formula1[i]) for i in (1, 3, 5)]
                  )
        self.play(LaggedStart(*[
            ReplacementTransform(i.copy(), formula1[j])
            for i, j in zip(
                (BC, AB, HK, AH),
                (0, 2, 4, 6)
            )
        ], lag_ratio=0.5))
        self.play(Wiggle(BC, scale_value=1.3),
                  Wiggle(formula1[0], scale_value=1.3),
                  Wiggle(AB, scale_value=1.3),
                  Wiggle(formula1[2], scale_value=1.3))
        self.play(Wiggle(HK, scale_value=1.3),
                  Wiggle(formula1[4], scale_value=1.3),
                  Wiggle(AH, scale_value=1.3),
                  Wiggle(formula1[6], scale_value=1.3))
        self.play(Write(to))
        self.play(LaggedStart(*[
            ReplacementTransform(formula1[i].copy(), formula2[j])
            for i, j in zip((0, 1, 2, 3, 4, 5, 6),
                            (0, 5, 6, 1, 2, 3, 4))
        ], lag_ratio=0))
        self.play(FadeOut(formula1), FadeOut(formula2), FadeOut(to), FadeOut(simi_text))


class Scene2(Scene):
    def construct(self):
        tree = SVGMobject("tree").stretch_to_fit_height(5).shift(RIGHT * 5)
        tree.set_color(GREEN)
        brace = Brace(tree, LEFT)
        brace_tex = brace.get_tex("?")

        B = Dot(tree.get_bottom())
        C = Dot(tree.get_top())
        A = Dot(B.get_center() + LEFT * 4)
        H = Dot(B.get_center() + LEFT * 2.5)
        AC = Line(A, C)
        K = Dot(line_intersection_(Line(H.get_center(), H.get_center() + UP), AC))
        AB = Line(A, B)
        BC = Line(B, C)
        HK = Line(H.get_center(), K.get_center())
        AH = Line(A, H)
        AK = Line(A, K)
        ABC = VGroup(AB, AC, BC)
        ABC.set_color(RED)
        AHK = VGroup(AH, AK, HK)
        AHK.set_color(YELLOW)
        text = [
            MathTex(content, color=color).next_to(target, direction)
            for content, color, target, direction in zip(
                ("A", "B", "C", "H", "K"),
                (TEAL, RED, RED, YELLOW, YELLOW),
                (A, B, C, H, K),
                (LEFT, DOWN, UP, DOWN, UP)
            )
        ]
        square1 = Square(side_length=0.2).move_to(H).shift(UP * 0.1 + RIGHT * 0.1)
        square2 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)

        group = VGroup(square1, square2, tree, A, B, C, H, AC, K, ABC, AHK, *text)
        tempA = text[0].get_center()
        width = group.width

        def update(obj, alpha):
            obj.width = lerp(width / 2, width, 1 - alpha)
            obj.next_to(tempA, RIGHT, aligned_edge=DOWN)

        self.play(UpdateFromAlphaFunc(group, update))
        angle = Angle(AH, AK, radius=0.4, color=GREEN)
        alpha = MathTex(r"\alpha", color=GREEN).scale(0.8).next_to(angle, UR, buff=0.05)

        E = Dot(B.get_center() + RIGHT * 2)
        F = Dot(line_intersection_(Line(E.get_center(), E.get_center() + UP), AC))
        building = SVGMobject("building") \
            .stretch_to_fit_height(F.get_center()[1] - E.get_center()[1]).align_to(E, DL)
        building.set_color(WHITE)
        E_text = MathTex("E", color=TEAL).next_to(E, DOWN)
        F_text = MathTex("F", color=TEAL).next_to(F, UP)
        BE = Line(B, E, color=TEAL)
        CF = Line(C, F, color=TEAL)
        EF = Line(E, F, color=TEAL)

        simi_text = MathTex(r"\triangle{AHK}", r"\sim", r"\triangle{ABC}", r"\sim", r"\triangle{AEF}").to_edge(UL)
        simi_text[0].set_color(RED)
        simi_text[2].set_color(YELLOW)
        simi_text[4].set_color(TEAL)
        formula1 = MathTex("{KH\over AH}", "=", "{BC\over AB}", "=", "{EF\over AE}", " =", r"f(\alpha)") \
            .next_to(simi_text, DOWN * 1.5, aligned_edge=LEFT)
        formula1[0].set_color(YELLOW)
        formula1[2].set_color(RED)
        formula1[4].set_color(TEAL)
        formula1[6].set_color(GREEN)

        formula2 = MathTex("BC", "=", "AB", r"\times", r"f(\alpha)") \
            .next_to(formula1, DOWN * 1.5, aligned_edge=LEFT)
        formula2[0].set_color(RED)
        formula2[2].set_color(RED)
        formula2[4].set_color(GREEN)
        formula3 = MathTex("EF", "=", "AE", r"\times", r"f(\alpha)") \
            .next_to(formula2, DOWN * 1.5, aligned_edge=LEFT)
        formula3[0].set_color(TEAL)
        formula3[2].set_color(TEAL)
        formula3[4].set_color(GREEN)

        self.play(DrawBorderThenFill(building))
        self.play(*[Write(i)
                    for i in (E_text, F_text, E, F, BE, CF, EF)])
        self.play(Write(angle), Write(alpha))
        self.play(Write(simi_text))
        self.play(Write(formula1[:5]))
        self.play(ReplacementTransform(alpha.copy(), formula1[6]), Write(formula1[5]))
        self.play(LaggedStart(*[
            FadeOut(i)
            for i in (H, K, square1, text[3], text[4], AH, AK, HK)
        ], lag_ratio=0.2))
        self.play(LaggedStart(*[
            Write(formula2),
            Write(formula3)
        ]))
        tan1 = MathTex(r"tan(\alpha)", color=GREEN).next_to(formula1[5], RIGHT)
        tan2 = MathTex(r"tan(\alpha)", color=GREEN).next_to(formula2[3], RIGHT)
        tan3 = MathTex(r"tan(\alpha)", color=GREEN).next_to(formula3[3], RIGHT)
        self.play(
            Transform(formula1[6], tan1),
            Transform(formula2[4], tan2),
            Transform(formula3[4], tan3),
        )
        self.wait()
