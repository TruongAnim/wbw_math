from manim import *
from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
SCENE_NAME = list_scene[1]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

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
        say_location = Dot().scale(0.001)
        bubble_kwargs = {
            "stroke_color": WHITE,
            "stretch_width": 4,
            "stretch_height": 2
        }
        self.my_play(FadeIn(pi, shift=RIGHT*2))
        self.my_play(NumberCreatureSays(pi, say_location,
                                     target_mode="plain",
                                     bubble_kwargs=bubble_kwargs))
        say1.move_to(say_location)
        self.my_play(Write(say1))

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
        self.my_play(NumberCreatureSays(pi2, say_location,
                                     target_mode="wonder",
                                     bubble_kwargs=bubble_kwargs))
        say2.move_to(say_location)
        self.my_play(Write(say2))


class Scene2(MyScene):
    def generate_rec(self, height=0.3, width=3):
        line_up = VMobject().set_points_as_corners(
            [LEFT * (width / 2) + RIGHT * (width * (i) / 8) for i in range(9)])

        def add_width(point, height):
            return np.array([point[0], point[1] - height, point[2]])

        line_down = [add_width(i, height) for i in reversed(line_up.points)]
        rec = VMobject().append_points(line_up.points)
        rec.add_line_to(line_down[0])
        rec.append_points(line_down)
        rec.add_line_to(line_up.points[0])
        return rec

    def construct(self):
        main_circle = Circle(radius=1.5,
                             stroke_width=2,
                             fill_color=BLUE,
                             fill_opacity=0.5) \
            .shift(UP * 2)
        self.add(main_circle)
        num_arc = 5
        num_arc = 10
        # num_arc = 50
        num_arc = 500
        radius = 1.5
        arcs = VGroup(*[AnnularSector(
            inner_radius=i * (radius / num_arc),
            outer_radius=(i + 1) * (radius / num_arc),
            angle=2 * PI,
            start_angle=PI / 2,
            stroke_width=1,
            stroke_color=RED,
            fill_color=YELLOW,
            fill_opacity=0.7)
                      .move_to(main_circle) for i in range(num_arc)])
        stroke_arcs = arcs.copy().set_style(fill_opacity=0,
                                            stroke_color=YELLOW,
                                            stroke_opacity=0.7)
        self.my_play(*[
            DrawBorderThenFill(arc) for arc in arcs
        ])
        self.add(stroke_arcs)
        recs = VGroup(*[self.generate_rec(
            width=(i + 1) / num_arc * (radius * 2 * PI),
            height=(1 / num_arc) * radius).shift(DOWN * 2)
                        for i in range(num_arc)]).arrange(DOWN, buff=0)
        recs.set_style(
            stroke_width=1,
            stroke_color=RED,
            fill_color=YELLOW,
            fill_opacity=1)
        recs.shift(DOWN * 2)
        self.play(LaggedStart(*[
            Transform(i, j)
            for i, j in zip(reversed(arcs), reversed(recs))
        ], lag_ratio=0.01))
        self.wait()

        r_line = Line(start=main_circle.get_center(),
                      end=main_circle.get_bottom(),
                      color=BLUE)
        r = MathTex("r", color=BLUE) \
            .next_to(r_line, LEFT)

        perimeter = Circle(radius=radius,
                           color=GREEN,
                           stroke_width=6)
        perimeter.rotate(PI / 2)
        perimeter.move_to(main_circle)
        chuvi = MathTex(r"2r\pi") \
            .next_to(perimeter, DOWN)
        chuvi[0][1].set_color(BLUE)
        chuvi[0][2].set_color(RED)

        for i in (r_line, r, perimeter, chuvi):
            i.generate_target()

        r_line.target.align_to(recs, DOWN)
        r.target.next_to(r_line.target, LEFT)
        perimeter.target = Line(start=recs[-1].get_corner(DL),
                                end=recs[-1].get_corner(DR),
                                color=GREEN)
        chuvi.target.next_to(perimeter.target, DOWN)

        self.my_play(*[Write(i) for i in (r, r_line)])
        self.my_play(*[Transform(i.copy(), i.target) for i in (r_line, r)])

        self.my_play(*[Write(i) for i in (chuvi, perimeter)])
        self.my_play(*[Transform(i.copy(), i.target) for i in (perimeter, chuvi)])

        color_map = {
            "S": YELLOW,
            "r": BLUE,
            "p": RED,
            "over": WHITE
        }

        #               0     1         2         3       4       5    6   7        7
        area1 = MathTex("S", "=", "{1 \over 2}", "r", r"\times", "2", "r", r"\pi")
        area1.set_color_by_tex_to_color_map(color_map)

        #               0     1    2     3         4      5
        area2 = MathTex("S", "=", "r", r"\times", "r", r"\pi")
        area2.set_color_by_tex_to_color_map(color_map)

        #               0     1    2     3         4
        area3 = MathTex("S", "=", "r", "^{2}", r"\pi")
        area3.set_color_by_tex_to_color_map(color_map)

        for i in (area1, area2, area3):
            i.next_to(main_circle, RIGHT, LARGE_BUFF)
        self.my_play(*[Write(area1[i])
                    for i in (0, 1, 2, 4)])
        self.my_play(*[
            ReplacementTransform(i, j)
            for i, j in zip((r.target.copy(),
                             chuvi.target[0][0].copy(),
                             chuvi.target[0][1].copy(),
                             chuvi.target[0][2].copy()),
                            (area1[3],
                             area1[5],
                             area1[6],
                             area1[7]))
        ])

        self.my_play(*[
            ReplacementTransform(area1[i], area2[j])
            for i, j in zip((0, 1, 3, 4, 6, 7),
                            (0, 1, 2, 3, 4, 5))
        ],  FadeOut(area1[2]),
            FadeOut(area1[5]))
        self.my_play(*[
            Transform(area2[i], area3[j])
            for i, j in zip((0, 1, 2, 4, 5),
                            (0, 1, 2, 3, 4))
        ],  FadeOut(area2[3]))

        self.my_play(Circumscribe(area3))