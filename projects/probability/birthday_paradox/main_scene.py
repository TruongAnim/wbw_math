from manim import *
from common.custom.custom_mobject import TextTranslation
from common.custom.custom_mobject import Explain

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3")
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


class Scene0(MyScene):
    def construct(self):
        names = ["chars/char (" + str(i) + ")" for i in range(1, 11)]
        group = Group(*[ImageMobject(i).scale_to_fit_height(1.7) for i in names]).arrange_in_grid(5, 5, buff=-0.2)
        self.add(group)
