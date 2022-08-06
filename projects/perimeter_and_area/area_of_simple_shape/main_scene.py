from manim import *

SCENE_NAME = "TestScene"
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command+"]")
    os.system(command)


class TestScene(Scene):
    def setup(self):
        pass

    def construct(self):
        square = Square().shift(LEFT * 2)
        circle = Circle()
        triangle = Triangle().shift(RIGHT * 2)
        anim = [square, circle, triangle]

        for i in range(10):
            self.play(
                ApplyFunction(lambda obj: obj.move_to(anim[1].get_center()), anim[0]),
                ApplyFunction(lambda obj: obj.move_to(anim[2].get_center()), anim[1]),
                ApplyFunction(lambda obj: obj.move_to(anim[0].get_center()), anim[2], path_arc=PI)
            )
            anim = anim[2:] + anim[0:2]
