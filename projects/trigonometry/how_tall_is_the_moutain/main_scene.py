from manim import *
import math

list_scene = ("Scene0", "Scene1", "Scene2", "Thumbnail")
SCENE_NAME = "Thumbnail"
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
        moutain1 = SVGMobject("moutain1").stretch_to_fit_height(5).stretch_to_fit_width(4).to_edge(RIGHT)
        moutain2 = SVGMobject("moutain2").to_edge(RIGHT)
        K = Dot(moutain1.get_top(), color=RED)
        H = Dot(moutain1.get_bottom(), color=RED)
        HK = Line(H, K, color=RED)
        A = Dot(H.get_center() + HK.get_length() * math.tan(40 * DEGREES) * LEFT)
        B = Dot(H.get_center() + HK.get_length() * math.tan(50 * DEGREES) * LEFT)
        AH = Line(A, H, color=BLUE)
        AH_dash = DashedLine(A, H, color=BLUE)
        BA = Line(B, A, color=GREEN)
        BK = DashedLine(B, K, color=YELLOW_D)
        AK = DashedLine(A, K, color=YELLOW_B)
        cross = Cross(Square(side_length=0.4).move_to(H.get_center() + LEFT))
        hk_text = MathTex("?", color=RED).next_to(HK, RIGHT)
        alpha = Angle(AH, AK)
        beta = Angle(BA, BK)
        text = [MathTex(i, color=j).next_to(obj, direction=direction)
                if not isinstance(obj, Angle)
                else MathTex(i, color=j).move_to(obj)
                for i, j, obj, direction in zip(
                ("?", "A", "B", "H", "K", r"\alpha", r"\beta"),
                (RED, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE),
                (HK, A, B, H, K, Angle(AH, AK, radius=1), Angle(BA, BK, radius=1)),
                (RIGHT, DOWN, DOWN, DOWN, UP, RIGHT, RIGHT)
            )]
        formula1 = MathTex(r"HK", "=", "AH", r"\times", r"tan(\alpha)")
        formula1[0].set_color(RED)
        formula1[2].set_color(BLUE)
        formula1.to_edge(UL)
        self.my_play(DrawBorderThenFill(moutain1),
                  Create(HK),
                  Write(text[0]),
                  Create(K),
                  Create(H))
        self.my_play(Create(AK),
                  Create(AH),
                  Create(alpha),
                  Create(A))
        self.my_play(FadeIn(text[5], shift=LEFT),
                  FadeIn(text[1], shift=UP),
                  FadeIn(text[3], shift=UP),
                  FadeIn(text[4], shift=DOWN))
        self.my_play(Write(formula1))
        self.my_play(Transform(AH, AH_dash), Create(cross), Create(Cross(formula1[2])))
        self.add(moutain1, K, H, hk_text, HK,
                 A, B, AH, BA, BK, AK,
                 cross, alpha, beta, *text)


class Scene1(MyScene):
    def construct(self):
        moutain1 = SVGMobject("moutain1").stretch_to_fit_height(5).stretch_to_fit_width(4).to_edge(RIGHT)
        moutain2 = SVGMobject("moutain2").to_edge(RIGHT)
        K = Dot(moutain1.get_top(), color=RED)
        H = Dot(moutain1.get_bottom(), color=RED)
        HK = Line(H, K, color=RED)
        A = Dot(H.get_center() + HK.get_length() * math.tan(40 * DEGREES) * LEFT)
        B = Dot(H.get_center() + HK.get_length() * math.tan(50 * DEGREES) * LEFT)
        AH = Line(A, H, color=BLUE)
        AH_dash = DashedLine(A, H, color=BLUE)
        BA = Line(B, A, color=GREEN)
        BK = DashedLine(B, K, color=YELLOW_D)
        AK = DashedLine(A, K, color=YELLOW_B)
        cross = Cross(Square(side_length=0.4).move_to(H.get_center() + LEFT))
        hk_text = MathTex("?", color=RED).next_to(HK, RIGHT)
        alpha = Angle(AH, AK)
        beta = Angle(BA, BK)
        text = [MathTex(i, color=j).next_to(obj, direction=direction)
                if not isinstance(obj, Angle)
                else MathTex(i, color=j).move_to(obj)
                for i, j, obj, direction in zip(
                ("?", "A", "B", "H", "K", r"\alpha", r"\beta"),
                (RED, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE),
                (HK, A, B, H, K, Angle(AH, AK, radius=1), Angle(BA, BK, radius=1)),
                (RIGHT, DOWN, DOWN, DOWN, UP, RIGHT, RIGHT)
            )]
        formula1 = MathTex(r"AH", r"\times", r"tan(\alpha)", "=", "HK")
        formula2 = MathTex(r"(", "AH", "+", "AB", ")", r"\times", r"tan(\beta)", "=", "HK")
        formula1.to_edge(UL, LARGE_BUFF)
        formula2.next_to(formula1, DOWN, aligned_edge=LEFT)
        formula1[0].set_color(BLUE)
        formula1[4].set_color(RED)
        formula2[1].set_color(BLUE)
        formula2[3].set_color(GREEN)
        formula2[8].set_color(RED)
        brace = Brace(VGroup(formula1, formula2), LEFT)
        formula3 = MathTex("\Rightarrow ", "AH", "=", r"{tan(\beta)", r"\times", "AB", r"\over tan(\alpha)-tan(\beta)}")
        formula4 = MathTex("\Rightarrow ", "HK", "=", r"AH", r"\times", r"tan(\alpha)")
        formula3[1].set_color(BLUE)
        formula3[5].set_color(GREEN)
        formula4[1].set_color(RED)
        formula4[3].set_color(BLUE)
        formula3.next_to(formula2, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        formula4.next_to(formula3, DOWN, aligned_edge=LEFT)
        self.my_play(DrawBorderThenFill(moutain1),
                  Create(HK),
                  Write(text[0]),
                  Create(K),
                  Create(H))
        self.my_play(Create(AK),
                  Create(AH_dash),
                  Create(alpha),
                  Create(A))
        self.my_play(FadeIn(text[5], shift=LEFT),
                  FadeIn(text[1], shift=UP),
                  FadeIn(text[3], shift=UP),
                  FadeIn(text[4], shift=DOWN))
        self.my_play(Create(BK), Create(BA), Create(B))
        self.my_play(Create(beta), FadeIn(text[-1], shift=LEFT), FadeIn(text[2], shift=UP))

        self.my_play(Write(formula1), Write(formula2), FadeIn(brace, shift=RIGHT))
        self.my_play(Write(formula3))
        self.my_play(Write(formula4))


class Scene2(MyScene):
    def construct(self):
        moutain1 = SVGMobject("moutain1").stretch_to_fit_height(5).stretch_to_fit_width(4).to_edge(RIGHT)
        moutain2 = SVGMobject("moutain2").to_edge(RIGHT)
        K = Dot(moutain1.get_top(), color=RED)
        H = Dot(moutain1.get_bottom(), color=RED)
        HK = Line(H, K, color=RED)
        A = Dot(H.get_center() + HK.get_length() * math.tan(40 * DEGREES) * LEFT)
        B = Dot(H.get_center() + HK.get_length() * math.tan(50 * DEGREES) * LEFT)
        AH = Line(A, H, color=BLUE)
        AH_dash = DashedLine(A, H, color=BLUE)
        BA = Line(B, A, color=GREEN)
        BK = DashedLine(B, K, color=YELLOW_D)
        AK = DashedLine(A, K, color=YELLOW_B)
        cross = Cross(Square(side_length=0.4).move_to(H.get_center() + LEFT))
        hk_text = MathTex("?", color=RED).next_to(HK, RIGHT)
        alpha = Angle(AH, AK)
        beta = Angle(BA, BK)
        text = [MathTex(i, color=j).next_to(obj, direction=direction, buff=SMALL_BUFF)
                if not isinstance(obj, Angle)
                else MathTex(i, color=j).move_to(obj)
                for i, j, obj, direction in zip(
                ("?", "A", "B", "H", "K", r"50^\circ", r"40^\circ"),
                (RED, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE),
                (HK, A, B, H, K, Angle(AH, AK, radius=1), Angle(BA, BK, radius=1)),
                (RIGHT, DOWN, DOWN, DOWN, UP, RIGHT, RIGHT)
            )]
        formula1 = MathTex(r"AH", r"\times", r"tan(50^\circ)", "=", "HK")
        formula2 = MathTex(r"(", "AH", "+", "AB", ")", r"\times", r"tan(40^\circ)", "=", "HK")
        formula1.to_edge(UL, LARGE_BUFF)
        formula2.next_to(formula1, DOWN, aligned_edge=LEFT)
        formula1[0].set_color(BLUE)
        formula1[4].set_color(RED)
        formula2[1].set_color(BLUE)
        formula2[3].set_color(GREEN)
        formula2[8].set_color(RED)
        brace = Brace(BA, DOWN, buff=0.6)
        brace_tex = brace.get_tex("700m", buff=SMALL_BUFF).set_color(GREEN)
        formula3 = MathTex("\Rightarrow ", "AH", "=", r"{tan(40^\circ)", r"\times", "700",
                           r"\over tan(50^\circ)-tan(40^\circ)}", "=", "1665.6(m)")
        formula4 = MathTex("\Rightarrow ", "HK", "=", r"AH", r"\times", r"tan(50^\circ)", "=", "1984.9(m)")
        formula3[1].set_color(BLUE)
        formula3[5].set_color(GREEN)
        formula3[-1].set_color(BLUE)
        formula4[1].set_color(RED)
        formula4[3].set_color(BLUE)
        formula4[-1].set_color(RED)
        formula3.to_edge(UL, buff=MED_LARGE_BUFF)
        formula4.next_to(formula3, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        self.my_play(DrawBorderThenFill(moutain1),
                  Create(HK),
                  Write(text[0]),
                  Create(K),
                  Create(H))
        self.my_play(Create(AK),
                  Create(AH_dash),
                  Create(alpha),
                  Create(A))
        self.my_play(FadeIn(text[5], shift=LEFT),
                  FadeIn(text[1], shift=UP),
                  FadeIn(text[3], shift=UP),
                  FadeIn(text[4], shift=DOWN))
        self.my_play(Create(BK), Create(BA), Create(B))
        self.my_play(Create(beta),
                  FadeIn(text[-1], shift=LEFT),
                  FadeIn(text[2], shift=UP),
                  FadeIn(brace, shift=UP),
                  FadeIn(brace_tex, shift=UP))

        self.my_play(Write(formula3))
        self.my_play(Write(formula4))
        copy = formula4[-1].copy()
        self.my_play(copy.animate.next_to(HK, RIGHT), FadeOut(text[0]))
        self.my_play(Circumscribe(formula4[-1]), Circumscribe(copy))


class Thumbnail(Scene):
    def construct(self):
        moutain1 = SVGMobject("moutain1").stretch_to_fit_height(6).stretch_to_fit_width(5).to_edge(RIGHT)
        K = Dot(moutain1.get_top(), color=RED)
        H = Dot(moutain1.get_bottom(), color=RED)
        HK = Line(H, K, color=RED)
        hk_text = MathTex("?", color=RED).scale(2).next_to(HK, RIGHT)
        apply = Text("Ứng dụng", font="Sans", color=RED).scale(2).to_corner(UL)
        trinogometry = Text("Lượng giác", font="Sans", color=YELLOW).scale(2).next_to(apply, DOWN, aligned_edge=LEFT)
        in_real_life = Text("trong thực tế", font="Sans", color=GREEN).scale(1.5).next_to(trinogometry, DOWN, aligned_edge=LEFT)
        self.add(moutain1, H, K, HK, hk_text, apply, trinogometry, in_real_life)