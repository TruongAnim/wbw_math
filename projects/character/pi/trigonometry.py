from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Trigonometry"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5")
SCENE_NAME = PROJECT_NAME+"_"+list_scene[1]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class MyScene(Scene):
    def setup(self):
        self.slice_stroke_color=RED
        self.slice_fill_color=TEAL,
        self.slice_fill_opacity=0.5

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


class Trigonometry_Scene0(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Paragraph("Cái cây kia cao\n bao nhiêu mét nhỉ?",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5)
        self.play(FadeIn(pi, shift=RIGHT*2))
        self.wait()
        self.my_play(NumberCreatureThinks(pi,
                                          wbw,
                                          target_mode="wonder",
                                          bubble_kwargs=bubble_kwargs
                                          )
                     )
        self.wait()

class Trigonometry_Scene1(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain"
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        sin = MathTex("sin(60^\circ)=\sqrt{3}/2", color=RED).scale(1.8)
        wbw = Paragraph("Sách giáo khoa bảo thế.",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5).next_to(sin, DOWN)
        group = VGroup(sin, wbw)
        self.play(FadeIn(pi, shift=RIGHT*2))
        self.wait()
        self.my_play(NumberCreatureSays(pi,
                                          group,
                                          target_mode="plain",
                                          bubble_kwargs=bubble_kwargs
                                          )
                     )
        self.wait()