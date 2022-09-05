import math

from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *
from common.utils.mobject_utils import get_indexes

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
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


class Scene1(Scene):
    def construct(self):
        text = Text("Hello")
        self.wait()
        self.add(text)
        self.wait()
        for i in range(1000):
            text.set_color(RED)
            self.wait(0.1)
            text.set_color(YELLOW)
            self.wait(0.1)
