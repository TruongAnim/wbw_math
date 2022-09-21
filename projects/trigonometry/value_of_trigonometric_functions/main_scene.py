from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[0]
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
        self.my_play(Write(formula2))
        self.my_play(Write(formula2))
        self.my_play(Circumscribe(formula2[3]))
