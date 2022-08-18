import math

from manim import *
from decimal import *

getcontext().prec = 30

list_scene = ("Scene1", "Scene2", "Scene3", "Scene31", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[0]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class Scene1(Scene):
    def construct(self):
        h = Decimal(1000000000)
        b = Decimal(0.02)
        area = h*b/2
        print(area)


        b2 = Decimal(0.01)
        ab = Decimal(h*h+b2*b2).sqrt()

        a1 = Decimal(10000000.01)
        a2 = Decimal(10000000.02)
        a3 = Decimal(0.03)
        s = (a1+a2+a3)/2

        area2 = s*(s-a1)*(s-a2)*(s-a3)
        print(area2.sqrt())

        b1 = 10000.1
        b2 = 10000.2
        b3 = 300

        s = 0.5*(b1+b2+b3)
        print(s)
        print(math.sqrt(s*(s-b1)*(s-b2)*(s-b3)))
        s = 0.5 * (b1+b2+b3)
        print(math.sqrt(s*b1*b2*b3))