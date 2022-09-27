from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[3]
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
        kite = SVGMobject("kite").shift(UP * 2.5)
        # self.add(kite)

        C = Dot(kite.get_center())
        B = Dot(C.get_center() + DOWN * 5)
        A = Dot(B.get_center() + LEFT * 2.8)
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
        alpha = MathTex(r"60^\circ", color=GREEN).next_to(angle, UR, buff=0.1)
        formula = MathTex(r"AC", r"\times sin(60^\circ)").next_to(brace_tex, RIGHT)
        formula2 = MathTex(r"=", "300m", r"\times", "sin(60^\circ)") \
            .next_to(brace_tex, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        formula[0].set_color(RED)
        formula2[1].set_color(RED)
        string_len = MathTex("300m", color=RED).next_to(AC.get_center(), LEFT)
        self.play(LaggedStart(*[
            DrawBorderThenFill(kite),
            Create(ABC),
            *[Write(i)
              for i in (A, B, C, square1, *text)]
        ]))
        self.play(Write(string_len), Write(angle), Write(alpha))
        self.play(*[
            Write(i)
            for i in (brace, brace_tex, formula)
        ])
        self.play(Write(formula2))
        self.play(Circumscribe(formula2[3]))


class Scene1(MyScene):
    def construct(self):
        C = Dot(UP * 3)
        B = Dot(C.get_center() + DOWN * 4)
        A = Dot(B.get_center() + LEFT * 4)
        AC = Line(A, C, color=RED)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        a1 = MathTex("a", color=BLUE).next_to(AB, DOWN)
        a2 = MathTex("a", color=YELLOW).next_to(BC, RIGHT)
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha = MathTex(r"45^\circ", color=GREEN).move_to(Angle(AB, AC, radius=1.5))
        self.my_play(LaggedStart(*[
            Create(ABC),
            *[Write(i)
              for i in (square1, A, B, C, alpha, angle, a1)]
        ]))
        arrow = Arrow(start=A.get_center() + UP * 3, end=ABC.get_center())
        vc = Text("Vuông cân", font="Sans").next_to(arrow.get_start(), LEFT)
        huyen = MathTex("\sqrt{2}a", color=RED).move_to(ABC.get_center() + LEFT)
        self.play(GrowArrow(arrow), Write(vc))
        self.play(ReplacementTransform(a1.copy(), a2))
        tan = MathTex("tan(", "45^\circ", ")=", "{a", "\over", "a}", "=1") \
            .shift(RIGHT * 3 + UP * 3)
        sin = MathTex("sin(", "45^\circ", ")=", "{a", "\over", "\sqrt{2}a}", "={\sqrt{2} \over 2}") \
            .next_to(tan, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        cos = MathTex("cos(", "45^\circ", ")=", "{a", "\over", "\sqrt{2}a}", "={\sqrt{2} \over 2}") \
            .next_to(sin, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)

        for i, color in zip((tan, sin, cos),
                            ((YELLOW, BLUE), (YELLOW, RED), (BLUE, RED))):
            i[1].set_color(GREEN)
            i[3].set_color(color[0])
            i[5].set_color(color[1])

        self.play(Write(tan[:3]), Write(tan[4]))
        self.play(ReplacementTransform(a2.copy(), tan[3]), ReplacementTransform(a1.copy(), tan[5]))
        self.play(Write(tan[6]))
        self.play(FadeOut(arrow), FadeOut(vc))
        self.play(Transform(a1.copy(), huyen), Transform(a2.copy(), huyen))
        self.play(Write(sin[:3]), Write(sin[4]))
        self.play(Transform(a2.copy(), sin[3]), ReplacementTransform(huyen.copy(), sin[5]))
        self.play(Write(sin[6]))
        self.play(Write(cos[:3]), Write(cos[4]))
        self.play(Transform(a1.copy(), cos[3]), ReplacementTransform(huyen.copy(), cos[5]))
        self.play(Write(cos[6]))


class Scene2(MyScene):
    def construct(self):
        C = Dot(UP * 3 + LEFT * 3.5)
        B = Dot(C.get_center() + DOWN * 5)
        A = Dot(B.get_center() + LEFT * 2.886)
        D = Dot(B.get_center() + RIGHT * 2.886)
        AC = Line(A, C, color=RED)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=YELLOW)
        CD = Line(C, D, color=RED)
        BD = Line(D, B, color=BLUE)
        ABC = VGroup(AB, AC, BC)
        a1 = MathTex("a", color=BLUE).next_to(AB, DOWN)
        a2 = MathTex("a", color=BLUE).next_to(BD, DOWN)
        h = MathTex("\sqrt{3}a", color=YELLOW).next_to(BC, LEFT).shift(DOWN * 0.5)
        square1 = Square(side_length=0.2).move_to(B).shift(UP * 0.1 + LEFT * 0.1)
        angle1 = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha1 = MathTex(r"60^\circ", color=GREEN).move_to(Angle(AB, AC, radius=1.5))
        angle2 = Angle(CD, BD, quadrant=(-1, 1), radius=0.8, color=GREEN)
        alpha2 = MathTex(r"60^\circ", color=GREEN).move_to(Angle(CD, BD, quadrant=(-1, 1), radius=1.5))
        angle3 = Angle(AC, BC, radius=0.8, quadrant=(-1, -1), color=TEAL)
        alpha3 = MathTex(r"30^\circ", color=TEAL).scale(0.8).move_to(Angle(AC, BC, quadrant=(-1, -1), radius=1.5))
        angle4 = Angle(BC, CD, radius=0.8, quadrant=(-1, 1), color=TEAL)
        alpha4 = MathTex(r"30^\circ", color=TEAL).scale(0.8).move_to(Angle(BC, CD, radius=1.5, quadrant=(-1, 1), ))

        self.my_play(LaggedStart(*[
            Create(ABC),
            *[Write(i)
              for i in (square1, A, B, C, alpha1, angle1, alpha3, angle3, a1)]
        ]))
        BCD = VGroup(CD, D, BD)
        self.play(LaggedStart(*[
            Create(BCD),
            Write(angle2), Write(alpha2), Write(alpha4), Write(angle4), FadeIn(a2, shift=UP)
        ]))
        tgd = Text("Tam giác đều", font="Sans", font_size=28).to_corner(UL)
        arrow = Arrow(start=tgd.get_bottom(), end=ABC.get_center())
        huyen = MathTex("2a", color=RED).move_to(ABC.get_center() + UL * 0.5)
        self.play(GrowArrow(arrow), Write(tgd))
        self.play(FadeOut(arrow), FadeOut(tgd),
                  ReplacementTransform(a1.copy(), huyen),
                  ReplacementTransform(a2.copy(), huyen),
                  )

        #               0       1           2      3        4       5       6       7       8           9
        sin = MathTex("sin(", "30^\circ", ")=", "cos(", "60^\circ", ")=", "{a", "\over", "2a}", "={1 \over 2}") \
            .shift(RIGHT * 2.8 + UP * 3)
        cos = MathTex("cos(", "30^\circ", ")=", "sin(", "60^\circ", ")=", "{\sqrt{3}a", "\over", "2a}",
                      "={\sqrt{3} \over 2}") \
            .next_to(sin, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        tan = MathTex("tan(", "30^\circ", ")=", "cot(", "60^\circ", ")=", "{a", "\over", "\sqrt{3}a}",
                      "={1 \over \sqrt{3}}") \
            .next_to(cos, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        cot = MathTex("cot(", "30^\circ", ")=", "tan(", "60^\circ", ")=", "{\sqrt{3}a", "\over", "a}", "=\sqrt{3}") \
            .next_to(tan, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)

        sin_color = (TEAL, GREEN, BLUE, RED)
        cos_color = (TEAL, GREEN, YELLOW, RED)
        tan_color = (TEAL, GREEN, BLUE, YELLOW)
        cot_color = (TEAL, GREEN, YELLOW, BLUE)

        for i, color in zip((sin, cos, tan, cot),
                            (sin_color, cos_color, tan_color, cot_color)):
            i[1].set_color(color[0])
            i[4].set_color(color[1])
            i[6].set_color(color[2])
            i[8].set_color(color[3])

        self.play(Write(sin[:6]), Write(sin[7]))
        self.play(Transform(a1.copy(), sin[6]),
                  ReplacementTransform(huyen.copy(), sin[8]))
        self.play(Write(sin[-1]))

        self.play(ReplacementTransform(huyen.copy(), h),
                  ReplacementTransform(a1.copy(), h))

        self.play(Write(cos[:6]), Write(cos[7]))
        self.play(ReplacementTransform(h.copy(), cos[6]),
                  ReplacementTransform(huyen.copy(), cos[8]))
        self.play(Write(cos[-1]))

        self.play(Write(tan[:6]), Write(tan[7]))
        self.play(ReplacementTransform(a1.copy(), tan[6]),
                  ReplacementTransform(h.copy(), tan[8]))
        self.play(Write(tan[-1]))

        self.play(Write(cot[:6]), Write(cot[7]))
        self.play(ReplacementTransform(h.copy(), cot[6]),
                  ReplacementTransform(a1.copy(), cot[8]))
        self.play(Write(cot[-1]))


class Scene3(MyScene):
    def construct(self):
        sin = MathTex("sin(x) = x-{x^3\over3!}+{x^5\over5!}-{x^7\over7!}+{x^9\over9!}-...", color=RED)
        cos = MathTex("cos(x) = 1-{x^2\over2!}+{x^4\over4!}-{x^6\over6!}+{x^8\over8!}-...", color=YELLOW)
        tan = MathTex("tan(x) = ", "{sin(x)", "\over", " cos(x)}", color=BLUE)
        cot = MathTex("cot(x) = ", "{cos(x)", " \over ", "sin(x)}", color=GREEN)
        tan[1].set_color(RED)
        tan[3].set_color(YELLOW)
        cot[1].set_color(YELLOW)
        cot[3].set_color(RED)
        sin.shift(UP * 3)
        cos.next_to(sin, DOWN, aligned_edge=LEFT)
        tan.next_to(cos, DOWN, aligned_edge=LEFT)
        cot.next_to(tan, DOWN, aligned_edge=LEFT)
        self.play(LaggedStart(*[Write(i) for i in (sin, cos, tan, cot)]))
