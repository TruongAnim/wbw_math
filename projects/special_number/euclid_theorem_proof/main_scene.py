from manim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
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


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Scene1(MyScene):
    def construct(self):
        day = Text("Dãy hữu hạn số nguyên tố:", font_size=40, font="Sans").to_corner(UL)
        goi = Text("Gọi", font_size=40, font="Sans").next_to(day, DOWN, aligned_edge=LEFT, buff=2)
        M = MathTex("M=", r"(P_{1} \times P_{2} \times P_{3} \times ... \times P_{n})", "+1").next_to(goi, RIGHT)
        p = MathTex("P=[P_{1}, P_{2}, P_{3}, ..., P_{n}]").next_to(M, UP, aligned_edge=LEFT, buff=1)
        M1 = MathTex("M", ":", "P_{1}", r"\text{ dư 1}", tex_template=myTemplate)
        M2 = MathTex("M", ":", "P_{2}", r"\text{ dư 1}", tex_template=myTemplate)
        M3 = MathTex("M", ":", "P_{3}", r"\text{ dư 1}", tex_template=myTemplate)
        M4 = MathTex("M", ":", "P_{n}", r"\text{ dư 1}", tex_template=myTemplate)
        VGroup(M1[2], M2[2], M3[2], M4[2]).set_color_by_gradient(BLUE, GREEN)
        math1 = MathTex(r"\rightarrow M")
        group = VGroup(M1, M2, M3, M4, math1).arrange(DOWN, aligned_edge=LEFT).next_to(M, DOWN, aligned_edge=LEFT)
        text1 = Text("không chia hết cho bất cứ số nào trong dãy P", font_size=35, font="Sans").next_to(math1, RIGHT, buff=MED_LARGE_BUFF)
        p.set_color_by_gradient(BLUE, GREEN)
        M[1].set_color_by_gradient(BLUE, GREEN)
        self.play(Write(day))
        self.play(Write(p))
        self.play(Write(goi), Write(M))
        self.play(Write(M1))
        self.play(Write(M2))
        self.play(Write(M3))
        self.play(Write(M4))
        self.play(Write(math1), Write(text1))
        self.play(p[0][-1].animate.shift(RIGHT))
        x = MathTex(", X", color=RED).next_to(p[0][-3], RIGHT)
        self.play(Write(x))
        text2 = Text("(Không bao giờ đầy đủ)", font_size=35, font="Sans", color=RED).next_to(p, RIGHT)
        self.play(Write(text2))
        # self.add(p, M, day, goi, group, text1)
