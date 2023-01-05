from manim import *
from common.utils.color_utils import HSL

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Thumbnail")
SCENE_NAME = list_scene[4]
# SCENE_NAME = " ".join(list_scene[:])
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")

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


class Scene0(Scene):
    def construct(self):
        last_fermat_theory = Text("Định lý cuối cùng của Fermat", font_size=50, font="Sans", color=BLUE).to_edge(UP)
        condition = Text("Với a,b,c nguyên dương", font_size=40, font="Sans", color=YELLOW).next_to(last_fermat_theory,
                                                                                                    DOWN)
        f1 = MathTex("a^2+b^2=c^2", color=GREEN)
        f2 = MathTex("a^3+b^3=c^3", color=RED)
        f3 = MathTex("a^4+b^4=c^4", color=RED)
        f4 = MathTex("a^5+b^5=c^5", color=RED)
        f5 = MathTex("....................", color=RED)
        fn = MathTex("a^n+b^n=c^n", color=RED)
        group = VGroup(f1, f2, f3, f4, f5, fn).scale(1.5).arrange(DOWN).next_to(condition, DOWN)
        b1 = Brace(f1, RIGHT)
        bt1 = Text("OKê!", font_size=40, font="Sans", color=GREEN).next_to(b1, RIGHT)

        b2 = Brace(VGroup(f2, f3, f4, f5, fn), RIGHT)
        bt2 = Text("Impossible!", font_size=40, font="Sans", color=RED).next_to(b2, RIGHT)
        self.play(FadeIn(last_fermat_theory, shift=UP))
        self.play(FadeIn(condition, shift=UP))
        self.play(FadeIn(f1, shift=UP))
        self.play(FadeIn(b1, shift=LEFT), FadeIn(bt1, shift=LEFT))
        self.play(LaggedStart(*[FadeIn(i) for i in (f2, f3, f4, f5, fn)], lag_ratio=0.2))
        self.play(FadeIn(bt2, shift=LEFT), FadeIn(b2, shift=LEFT))
        self.wait(0.5)
        self.add(last_fermat_theory, group, condition, b1, bt1, b2, bt2)


class Scene1(Scene):
    def construct(self):
        f1 = MathTex("1782^{12}+1841^{12}", "=", "1922^{12}").scale(1.5).shift(UP*3+LEFT*0.5)
        f1[0].shift(LEFT*2)
        f1[1].shift(LEFT*1)
        f1[2].shift(RIGHT*1)
        self.play(FadeIn(f1[0], shift=UP), FadeIn(f1[2], shift=UP))
        self.wait()
        self.play(FadeIn(f1[1], shift=UP))
        self.play(Flash(f1[1]))
        self.play(Flash(f1[1]))
        self.play(Flash(f1[1]))


class Scene2(Scene):
    def construct(self):
        f1 = MathTex("1782^{12}+1841^{12}", "=", "2541210259314801410819278649643651567616")
        f2 = MathTex("1922^{12}", "=", "2541210258614589176288669958142428526657").next_to(f1, DOWN)
        f1[2].set_color(RED)
        f1[2][:10].set_color(GREEN)
        f2[2].set_color(RED)
        f2[2][:10].set_color(GREEN)
        f2[0].align_to(f1[0], LEFT)
        f2[1].align_to(f1[1], LEFT)
        f2[2].align_to(f1[2], LEFT)
        self.add(f1, f2)


class Scene3(Scene):
    def construct(self):
        f1 = MathTex("\sqrt[2]{","50}.", color=RED).scale(2.5).shift(LEFT*2)
        f4 = MathTex("=", "7.07", color=RED).scale(2.5).next_to(f1, DOWN)
        f3 = MathTex(r"\neq ").scale(2.5).next_to(f1, RIGHT, buff=LARGE_BUFF)
        f2 = MathTex("{50", " \over 2 }", "=", "25", color=GREEN).scale(2.5).next_to(f3, RIGHT, buff=MED_LARGE_BUFF)
        self.play(Write(f1[0]), Write(f1[1][0]), Write(f2[1]), FadeIn(f3, shift=UP))
        self.wait()
        self.play(Write(f1[1][1]), Write(f1[1][2]), Write(f2[0]))
        self.wait()
        self.play(Write(f2[2]), Write(f2[3]))
        self.wait()
        self.play(Write(f4))
        self.wait()


class Scene4(Scene):
    def construct(self):
        f = MathTex(r"\text{Anh }",r" \sqrt{\text{mời}} ",r"\text{ em}", tex_template=myTemplate).scale(3)
        f[0].set_color(GREEN)
        f[1].set_color(YELLOW)
        f[2].set_color(RED)
        self.play(Write(f))
        self.wait()