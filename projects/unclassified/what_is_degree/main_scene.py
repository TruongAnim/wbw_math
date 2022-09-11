from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[4]
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


class Scene1(Scene):
    def construct(self):
        degree = Text("Độ", font="Sans", font_size=30, color=RED).shift(LEFT*3)
        en_degree = Text("(degree)", color=RED, font_size=27, slant=ITALIC) \
            .next_to(degree, RIGHT)
        sign = MathTex(r"\text{Kí hiệu: }^\circ", color=YELLOW, tex_template=myTemplate) \
            .next_to(degree, DOWN, aligned_edge=LEFT)

        table = MathTable(
            [
                ["degree", "360"],
                ["radian", "2\pi"],
                ["quadrant", "4"],
                ["turn", "1"],
                ["sextant", "6"],
                ["grad", "400"],
                ["arcmunute", "21600"],
                ["...", "..."],
            ],
            col_labels=[Text("Tên"), Text("1 vòng")],
            include_outer_lines=True).scale(0.7).to_edge(RIGHT)
        highlight1 = table.get_highlighted_cell((1, 1), color=GREEN)
        highlight2 = table.get_highlighted_cell((1, 2), color=GREEN)
        table.add_to_back(highlight1)
        table.add_to_back(highlight2)
        self.play(Write(degree), Write(en_degree))
        self.play(Write(sign))
        self.play(Write(table), run_time=3)


class Scene2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6.5, 1],
            x_length=10,
            y_length=6.5,
            axis_config={"include_numbers": True},
        )
        def func1(x):
            return -0.15*(x**2) +1.5*x -0
        def func2(x):
            return -0.4*(x**2) +3*x -0
        def func3(x):
            return -0.1*(x**2) +0.7*x -0
        graph1 = ax.plot(func1, x_range=[0, 10], color=RED)
        graph2 = ax.plot(func2, x_range=[0, 7.5], color=GREEN)
        graph3 = ax.plot(func3, x_range=[0, 7], color=YELLOW)
        line1 = Line(start=LEFT, end=ORIGIN, color=GREEN).shift(UP*3+RIGHT*4)
        line2 = line1.copy().next_to(line1, DOWN, buff=0.7).set_color(RED)
        line3 = line2.copy().next_to(line2, DOWN, buff=0.7).set_color(YELLOW)
        degree1 = MathTex("70^\circ", color=GREEN).next_to(line1)
        degree2 = MathTex("45^\circ", color=RED).next_to(line2)
        degree3 = MathTex("25^\circ", color=YELLOW).next_to(line3)
        self.play(*[
            Write(ax)
        ])
        self.play(LaggedStart(*[
            Create(i)
            for i in (graph1, graph2, graph3)
        ]))
        self.play(LaggedStart(*[
            Write(i)
            for i in (line1, degree1, line2, degree2, line3, degree3)
        ]))
        self.add(ax, graph1, graph2, graph3, line1, line2, line3, degree1, degree2, degree3)


class Scene3(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.1,
            zoomed_display_height=3,
            zoomed_display_width=3,
            image_frame_stroke_width=0.5,
            zoomed_camera_frame_starting_position=RIGHT*3,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )


    def construct(self):
        circle = Circle(radius=3,
                        stroke_width=1)
        center = Dot(circle.get_center(), color=RED).scale(0.5)

        sector_count = 360
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 3,
            "inner_radius": 0,
            "stroke_width": 1,
            "stroke_color": RED,
            "fill_color": GREEN,
            "fill_opacity":0
        }
        sectors = VGroup(*[Sector(angle=angle, start_angle=i, **sector_kwargs)
                   for i in start_angle])
        sec90 = VGroup(*sectors[:int(sector_count / 4)])
        sec180 = VGroup(*sectors[:int(sector_count / 2)])
        text1 = MathTex("1^\circ", color=YELLOW).scale(0.2)
        text1.next_to(sectors[0], RIGHT, buff=0.05)
        text90 = MathTex("90^\circ", color=YELLOW).move_to(sec90)
        text180 = MathTex("180^\circ", color=YELLOW).move_to(sec180)
        text360 = MathTex("360^\circ", color=YELLOW).move_to(sectors)
        self.play(Create(circle))
        self.play(LaggedStart(*[
            FadeIn(i)
            for i in sectors
        ], lag_ratio=0.005))
        self.add(sec90, sec180, sectors)
        self.activate_zooming(animate=True)
        self.play(sectors[0].animate
                  .set_style(fill_color=GREEN,
                             fill_opacity=1,
                             stroke_color=GREEN),
                  FadeIn(text1))
        self.wait()

        self.play(self.get_zoomed_display_pop_out_animation(),
                     rate_func=lambda t: smooth(1 - t))
        self.play(FadeOut(self.zoomed_display), FadeOut(self.zoomed_camera.frame))
        self.play(sec90.animate
                  .set_style(fill_color=GREEN,
                             fill_opacity=1,
                             stroke_color=GREEN),
                  Transform(text1, text90), run_time=2)
        self.play(sec180.animate
                  .set_style(fill_color=GREEN,
                             fill_opacity=1,
                             stroke_color=GREEN),
                  Transform(text1, text180), run_time=2)
        self.play(sectors.animate
                  .set_style(fill_color=GREEN,
                             fill_opacity=1,
                             stroke_color=GREEN),
                  Transform(text1, text360), run_time=2)

        self.wait()

class Scene4(Scene):
    def construct(self):
        circle = Circle(radius=2,
                        stroke_width=1)

        sector_count = 360
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "stroke_width": 1,
            "stroke_color": RED,
            "fill_color": GREEN,
            "fill_opacity": 0
        }
        sectors = VGroup(*[Sector(angle=angle, start_angle=i, **sector_kwargs)
                           for i in start_angle])
        text360 = MathTex("360^\circ", color=YELLOW).next_to(circle, UP)
        text1 = MathTex("1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24").next_to(circle, DOWN)
        text2 = MathTex("30, 36, 40, 45, 60, 72, 90, 120, 180, 360").next_to(text1, DOWN)
        self.play(Create(circle), Write(text360))
        self.play(LaggedStart(*[
            FadeIn(i)
            for i in sectors
        ], lag_ratio=0.005))
        self.play(Write(text1), Write(text2))
        self.wait()


class Scene5(Scene):
    def construct(self):
        circle = Circle(radius=2,
                        stroke_width=1)

        sector_count = 100
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "stroke_width": 1,
            "stroke_color": RED,
            "fill_color": GREEN,
            "fill_opacity": 0
        }
        sectors = VGroup(*[Sector(angle=angle, start_angle=i, **sector_kwargs)
                           for i in start_angle])
        text100 = MathTex("100^\circ", color=YELLOW).next_to(circle, UP)
        text1 = MathTex("1, 2, 4, 5, 10, 20, 25, 50, 100").next_to(circle, DOWN)
        self.play(Create(circle), Write(text100))
        self.play(LaggedStart(*[
            FadeIn(i)
            for i in sectors
        ], lag_ratio=0.005))
        self.play(Write(text1))
        self.wait()