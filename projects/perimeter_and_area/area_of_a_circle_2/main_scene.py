from manim import *
from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
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


class Scene1(MyScene):
    def construct(self):
        pi = NumberCreature(file_name_prefix="PiCreatures", mode="plain") \
            .to_corner(DL, buff=MED_SMALL_BUFF)

        circle = Circle()
        rec = Rectangle(width=2, height=1, color=YELLOW)
        area = Text("Area").scale(2)

        say1 = VGroup(circle, rec, area).arrange(RIGHT, buff=2)
        arrow1 = Arrow(start=circle.get_right(), end=rec.get_left())
        arrow2 = Arrow(start=rec.get_right(), end=area.get_left())
        say1.add(arrow1, arrow2)
        say1.scale(0.3)
        say_location = Dot().scale(0.01)
        bubble_kwargs = {
            "stroke_color": WHITE,
            "stretch_width": 4,
            "stretch_height": 2
        }
        self.play(NumberCreatureSays(pi, say_location,
                                     target_mode="plain",
                                     bubble_kwargs=bubble_kwargs))
        say1.move_to(say_location)
        self.play(Write(say1))

        pi2 = NumberCreature(file_name_prefix="PiCreatures",
                             mode="wonder", color=GREEN,
                             flip_at_start=True) \
            .to_corner(DR, buff=MED_SMALL_BUFF)

        circle2 = Circle()
        rec2 = Triangle()
        area2 = Text("Area?").scale(2)

        say2 = VGroup(circle2, rec2, area2).arrange(RIGHT, buff=2)
        arrow21 = Arrow(start=circle2.get_right(), end=rec2.get_left())
        arrow22 = Arrow(start=rec2.get_right(), end=area2.get_left())
        say2.add(arrow21, arrow22)
        say2.scale(0.3)
        self.play(NumberCreatureSays(pi2, say_location,
                                     target_mode="wonder",
                                     bubble_kwargs=bubble_kwargs))
        say2.move_to(say_location)
        self.play(Write(say2))


class Scene2(MyScene):
    def generate_rec_from_arc(self, arc, width=0.2):
        y = arc.points[0][1]
        print(arc.points)
        print(len(arc.points))
        line = VMobject().set_points_as_corners([LEFT, RIGHT, RIGHT*2])
        print("line", len(line.points))
        print(line.points)


        line_up = [np.array([index/2, y, p[2]]) for index,p in enumerate(arc.points)]

        def add_width(point, width):
            return np.array([point[0], point[1]-width, point[2]])

        line_down = [add_width(i, width) for i in reversed(line_up)]
        rec = VMobject().append_points(line_up)
        rec.add_line_to(line_down[0])
        rec.append_points(line_down)
        rec.add_line_to(line_up[0])
        return rec

    def construct(self):
        main_circle = Circle(radius=1.5,
                             stroke_width=2,
                             fill_color=BLUE,
                             fill_opacity=0.5) \
            .shift(UP * 2)
        self.add(main_circle)
        num_arc = 4
        arcs = [AnnularSector(
            inner_radius=i * (1.5 / num_arc),
            outer_radius=(i + 1) * (1.5 / num_arc),
            angle=2*PI,
            start_angle=PI/2,
            stroke_width=1,
            stroke_color=RED)
                .move_to(main_circle) for i in range(num_arc)]
        self.play(*[
            DrawBorderThenFill(arc) for arc in arcs
        ])
        # line = Line(stroke_width=10, start=RIGHT*2, end=LEFT*2).shift(DOWN*2)
        rec = self.generate_rec_from_arc(
            Arc(radius=2,
                start_angle=PI/2,
                angle=2*PI),
            width=0.5).shift(DOWN*2)
        num_point = 50
        dots = [Dot(arcs[3].point_from_proportion(i / num_point),
                    color=interpolate_color(YELLOW, GREEN, i / num_point))
                for i in range(num_point)]
        dots2 = [Dot(rec.point_from_proportion(i / num_point),
                     color=interpolate_color(YELLOW, GREEN, i / num_point))
                 for i in range(num_point)]
        self.add(*dots, *dots2)
        self.play(Transform(arcs[3], rec), run_time=3)
