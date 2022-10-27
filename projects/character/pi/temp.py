from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Temp"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Scene12", "Scene13", "Scene14", "Scene15")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[0]
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class Temp_Scene0(Scene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).scale(1.5).to_corner(DL, buff=0)
        bubble_kwargs = {
            "stretch_width": 5,
            "stretch_height": 4,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Paragraph("Khi nào thì tìm được\nsố lớn nhất?",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.play(NumberCreatureSays(pi,
                                     wbw,
                                     target_mode="wonder",
                                     bubble_kwargs=bubble_kwargs
                                     )
                  )
        euclid = ImageMobject("euclid").to_corner(DR, buff=0)
        bubble = SVGMobject("Bubbles_speech", stroke_color=WHITE).flip(UP).scale(1.5).next_to(euclid, UL, buff=-0.5)
        never = Text("Không bao giờ", font_size=35, font="Sans", color=YELLOW).move_to(bubble).shift(UP * 0.3)

        self.play(FadeIn(euclid, shift=LEFT))
        self.play(FadeIn(bubble), Write(never))

        self.wait()


class Temp_Scene1(Scene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile2"
        ).scale(1.5).to_corner(DL)
        question = MarkupText("Số nguyên tố nào lớn nhất bạn biết\nmà đồng thời là số fibonacci?", font_size=40,
                        font="Sans").shift(UP*2)
        example = Text("Ví dụ: 5, 13, 89, v.v...", color=GREEN, font="Sans").next_to(question, DOWN)
        self.play(FadeIn(pi, shift=RIGHT))
        self.play(Write(question))
        self.play(Write(example))
        self.wait()
