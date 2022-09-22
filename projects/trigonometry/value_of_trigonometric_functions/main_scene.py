from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
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
        formula2 = MathTex(r"=", "300m", r"\times", "sin(60^\circ)")\
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
        C = Dot(UP*3)
        B = Dot(C.get_center() + DOWN*4)
        A = Dot(B.get_center() + LEFT * 4)
        AC = Line(A, C, color=RED)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=YELLOW)
        ABC = VGroup(AB, AC, BC)
        a1 = MathTex("a", color=BLUE).next_to(AB, DOWN)
        a2 = MathTex("a", color=YELLOW).next_to(BC, RIGHT)
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
        angle = Angle(AB, AC, radius=0.8, color=GREEN)
        alpha = MathTex(r"45^\circ", color=GREEN).move_to(Angle(AB, AC, radius=1.5))
        self.my_play(LaggedStart(*[
            Create(ABC),
            *[Write(i)
              for i in (square1, A, B, C, alpha, angle, a1)]
        ]))
        arrow = Arrow(start=A.get_center()+UP*3, end=ABC.get_center())
        vc = Text("Vuông cân", font="Sans").next_to(arrow.get_start(), LEFT)
        self.play(GrowArrow(arrow), Write(vc))
        self.play(ReplacementTransform(a1.copy(), a2))
        tan = MathTex("tan(", "45^\circ", ")=", "{a", "\over", "a}", "=1")

