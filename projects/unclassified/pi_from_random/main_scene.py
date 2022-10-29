from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9")
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


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Scene0(MyScene):
    def construct(self):
        import random
        from common.utils.color_utils import interpolate_color_range
        ran = MathTex(r"\text{random}(", "0", ",",  "1", ") \longrightarrow").scale(1.5).shift(UP+LEFT)
        ran[1].set_color(YELLOW)
        ran[3].set_color(RED)
        list_rand = [0.6404715302525753, 0.4542988583872273, 0.4161880799942135, 0.6337411245598525, 0.349581448236874, 0.8310301991771485, 0.8257280156247735, 0.024194002080686006, 0.23833225617200948, 0.7370351328115762,
                     0.7008278818280986, 0.4820941891462207, 0.29395250257861627, 0.40836605817292004, 0.9084620255657727, 0.17721597164415415, 0.0902734603242028, 0.6138566180452795, 0.592348573135173, 0.551363570531275]
        texts = [MathTex("{:4f}".format(i), color=interpolate_color_range(YELLOW, RED, i)).scale(1.2).next_to(ran, RIGHT) for i in list_rand]
        to_do = Text("Hãy tính sấp xỉ số Pi.", font_size=35, font="Sans", color=GREEN).shift(DOWN)
        first_value = texts[0]
        self.play(Write(ran))
        self.play(Write(first_value))
        count = 0
        for i in texts[1:]:
            self.play(Transform(first_value, i))
            count+=1
            if count==3:
                self.play(Write(to_do))


class Scene1(MyScene):
    def construct(self):
        circle = Circle(radius=2, color=TEAL)
        diameter = Line(LEFT*2, RIGHT*2, color=RED)
        chuvi = Text("Chu vi", color=TEAL, font="Sans", font_size=25).next_to(circle, UP)
        dk = Text("Đường kính", color=RED, font="Sans", font_size=25).next_to(diameter, UP)
        pi = MathTex("\pi", "=", "{1234567", r"\over",  "1234567}", "=3.141592...")
        pi[0].set_color(GREEN)
        pi.next_to(circle, DOWN, buff=MED_LARGE_BUFF)
        self.play(Create(circle), Write(chuvi))
        self.play(Create(diameter), Write(dk))
        self.play(Write(pi[0:2]), Write(pi[3]))
        self.play(chuvi.copy().animate.move_to(pi[2]), dk.copy().animate.move_to(pi[4]))
        self.play(Write(pi[5:]))
        # self.add(circle, diameter, chuvi, dk, pi)