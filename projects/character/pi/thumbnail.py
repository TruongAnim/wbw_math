from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Thumbnail"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Scene12", "Scene13", "Scene14", "Scene15")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[0]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class ThumbnailScene0(Scene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).scale(2).to_corner(DL)
        circle = Circle(color=GREEN, stroke_width=15).scale(3.5).shift(RIGHT*3)
        _360 = MathTex("360^\circ", color=YELLOW).scale(3).move_to(circle)
        text = Text("Sao không dùng", font="Sans", font_size=70, color=TEAL).to_corner(UL)
        _100 = MathTex("{100^\circ}?", color=ORANGE).scale(2.5).move_to(circle).next_to(text, DOWN)
        self.add(circle, _360, _100, text, pi)