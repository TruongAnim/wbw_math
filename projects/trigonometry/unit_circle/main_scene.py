from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5")
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


class Scene0(MyScene):
    def construct(self):
        main_circle = DashedVMobject(Circle(radius=3, color=BLUE), num_dashes=40)
        vertical = Arrow(start=DOWN * 4, end=UP * 4)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4)
        O = Dot(ORIGIN)
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal, RIGHT)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        brace = Brace(Line(start=ORIGIN, end=RIGHT * 3), DOWN, buff=SMALL_BUFF)
        brace_t = brace.get_tex("1")
        A = Dot(RIGHT * 3)
        B = Dot(UP * 3)
        C = Dot(LEFT * 3)
        D = Dot(DOWN * 3)
        coord_A = MathTex("(1,0)").next_to(A, DR)
        coord_B = MathTex("(0,1)").next_to(B, UL)
        coord_C = MathTex("(-1,0)").next_to(C, UL)
        coord_D = MathTex("(0,-1)").next_to(D, DL)
        quadrant_dis = 3.2
        quadrant1 = Text("I").move_to(RIGHT * quadrant_dis + UP * quadrant_dis)
        quadrant2 = Text("II").move_to(LEFT * quadrant_dis + UP * quadrant_dis)
        quadrant3 = Text("III").move_to(LEFT * quadrant_dis + DOWN * quadrant_dis)
        quadrant4 = Text("IV").move_to(RIGHT * quadrant_dis + DOWN * quadrant_dis)
        sub_circle = Circle(radius=3, color=GREEN)
        A = Dot(RIGHT*3+UP*0.01)
        def create_angle():
            OA = Line(O.get_center(), A.get_center())
            angle = Angle(OA, Line(O.get_center(), RIGHT*3), other_angle=True)
            return VGroup(OA, angle)
        angle = create_angle()
        self.add(main_circle, vertical, horizontal, O_t, x_t, y_t, brace_t, brace, O, A, B, C, D, coord_A, coord_B,
                 coord_C, coord_D, quadrant1, quadrant2, quadrant3, quadrant4, sub_circle, angle)
        def update_angle(obj):
            angle.become(create_angle())
        A.add_updater(update_angle)
        self.play(MoveAlongPath(A, sub_circle.get_subcurve(0.01,0.9999)))


class Scene2(MyScene):
    def construct(self):
        pass
