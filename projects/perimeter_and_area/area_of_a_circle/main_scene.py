from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5")
# SCENE_NAME = list_scene[1]
SCENE_NAME = "Thumbnail"
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class MyScene(Scene):
    def setup(self):
        self.slice_stroke_color=RED
        self.slice_fill_color=TEAL,
        self.slice_fill_opacity=0.5

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
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=0.7)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        area_text = MathTex("S = \pi r^2").to_corner(UR, buff=LARGE_BUFF)
        r_line = Line(start=circle.points[0], end=circle.get_center())
        r = MathTex("r").next_to(r_line, UP)
        arrow = Arrow(start=area_text.get_left(), end=r.get_center() + UP * 0.5)
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).to_corner(DL)
        rectangle = Rectangle(width=2 * PI, height=2, stroke_width=1) \
            .shift(RIGHT * 3)
        self.my_play(Write(circle), Write(center))
        self.my_play(Write(r_line), Write(r))
        self.my_play(Write(area_text), Write(arrow))
        self.my_play(FadeIn(pi, shift=RIGHT * 2))
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Text("Wait... but why?")
        self.my_play(NumberCreatureThinks(pi,
                                          wbw,
                                          target_mode="wonder",
                                          bubble_kwargs=bubble_kwargs
                                          )
                     )

        self.my_play(*[
            FadeOut(i) for i in (area_text, arrow, pi, pi.bubble, wbw, r_line, r)
        ])
        self.my_play(*[
            i.animate.shift(LEFT * 4) for i in (circle, center)
        ])
        self.my_play(Create(rectangle))


class Scene2(MyScene):
    def construct(self):
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=0.7).shift(LEFT * 4)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        rectangle = Rectangle(width=2 * PI, height=2, stroke_width=3) \
            .shift(RIGHT * 3)
        self.add(circle, center, rectangle)

        # sector_count = 10
        sector_count = 20
        # sector_count = 50
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "stroke_width": 2,
            "stroke_color": RED,
            "fill_color": self.slice_fill_color
        }
        sectors = [Sector(angle=angle, start_angle=i, **sector_kwargs)
                   .shift(LEFT * 4)
                   for i in start_angle]
        line1 = VGroup(*sectors[:int(sector_count / 2)])
        line2 = VGroup(*sectors[int(sector_count / 2):])
        target_sectors = [Sector(angle=angle, start_angle=PI / 2 - angle / 2, **sector_kwargs)
                          for i in range(sector_count)]
        target_line1 = VGroup(*target_sectors[:int(sector_count / 2)]).arrange(LEFT, buff=0) \
            .move_to(rectangle)
        target_line2 = VGroup(*target_sectors[int(sector_count / 2):]).arrange(RIGHT, buff=0) \
            .move_to(rectangle) \
            .shift(LEFT * (2 * PI / sector_count))

        shifts_line1 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line1, line1)]
        shifts_line2 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line2, line2)]

        self.my_play(LaggedStart(*[
            Write(i) for i in line1
        ],*[
            Write(i) for i in line2
        ], lag_ratio=0.1))

        for i in line1:
            i.save_state()
        for i in line2:
            i.save_state()

        def clousure(shift_line, index):
            def update_angle(obj, dt):
                obj.restore()
                obj.rotate(dt * (PI / 2 - (start_angle[index] + angle / 2)),
                           about_point=obj.get_center_of_mass())
                obj.shift(dt * (shift_line[index]))

            return update_angle

        self.my_play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line1, index)) for index, obj in enumerate(line1)
        ], rate_func=linear)
        self.my_play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line2, index)) for index, obj in enumerate(line2)
        ], rate_func=linear)


class Scene3(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.2,
            zoomed_display_height=5,
            zoomed_display_width=5,
            image_frame_stroke_width=0.2,
            zoomed_camera_frame_starting_position=UP + RIGHT * (PI / 2 / 15),
            zoomed_camera_config={
                "default_frame_stroke_width": 1,
            },
            **kwargs
        )

    def construct(self):
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=0.7).shift(LEFT * 4)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        rectangle = Rectangle(width=2 * PI,
                              height=2,
                              stroke_width=1,
                              stroke_color=YELLOW) \
            .shift(RIGHT * 3)
        self.add(circle, center, rectangle)

        sector_count = 50
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "fill_color": TEAL,
            "fill_opacity": 1,
            "stroke_width": 0.5,
            "stroke_color": RED
        }
        sectors = [Sector(angle=angle, start_angle=i, **sector_kwargs)
                   .shift(LEFT * 4)
                   for i in start_angle]
        line1 = VGroup(*sectors[:int(sector_count / 2)])
        line2 = VGroup(*sectors[int(sector_count / 2):])
        target_sectors = [Sector(angle=angle, start_angle=PI / 2 - angle / 2, **sector_kwargs)
                          for i in range(sector_count)]
        target_line1 = VGroup(*target_sectors[:int(sector_count / 2)]).arrange(LEFT, buff=0) \
            .move_to(rectangle)
        target_line2 = VGroup(*target_sectors[int(sector_count / 2):]).arrange(RIGHT, buff=0) \
            .move_to(rectangle) \
            .shift(LEFT * (2 * PI / sector_count))

        shifts_line1 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line1, line1)]
        shifts_line2 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line2, line2)]

        self.play(LaggedStart(*[
            Write(i) for i in line1
        ],*[
            Write(i) for i in line2
        ], lag_ratio=0.1))

        self.wait()

        for i in line1:
            i.save_state()
        for i in line2:
            i.save_state()

        def clousure(shift_line, index):
            def update_angle(obj, dt):
                obj.restore()
                obj.rotate(dt * (PI / 2 - (start_angle[index] + angle / 2)),
                           about_point=obj.get_center_of_mass())
                obj.shift(dt * (shift_line[index]))

            return update_angle

        self.play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line1, index)) for index, obj in enumerate(line1)
        ], rate_func=linear, run_time=2)
        self.wait()
        self.play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line2, index)) for index, obj in enumerate(line2)
        ], rate_func=linear, run_time=2)
        self.wait()

        self.activate_zooming(animate=True)
        self.wait()
        self.play(self.zoomed_camera.frame.animate.scale(0.1),
                     rectangle.animate.set_stroke(width=0.05),
                     line1.animate.set_stroke(width=0.05),
                     line2.animate.set_stroke(width=0.05),
                     run_time=3)
        self.wait()


class Scene4(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.2,
            zoomed_display_height=5,
            zoomed_display_width=5,
            image_frame_stroke_width=0.2,
            zoomed_camera_frame_starting_position=LEFT * 4 + DOWN * 2,
            zoomed_camera_config={
                "default_frame_stroke_width": 1,
            },
            **kwargs
        )

    def construct(self):
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=0.7).shift(LEFT * 4)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        rectangle = Rectangle(width=2 * PI,
                              height=2,
                              stroke_width=1,
                              stroke_color=YELLOW) \
            .shift(RIGHT * 3)
        self.add(circle, center, rectangle)

        sector_count = 2880
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "fill_color": TEAL,
            "fill_opacity": 1,
            "stroke_width": 0.5,
            "stroke_color": RED
        }
        sectors = [Sector(angle=angle, start_angle=i, **sector_kwargs)
                   .shift(LEFT * 4)
                   for i in start_angle]
        line1 = VGroup(*sectors[:int(sector_count / 2)])
        line2 = VGroup(*sectors[int(sector_count / 2):])
        target_sectors = [Sector(angle=angle, start_angle=PI / 2 - angle / 2, **sector_kwargs)
                          for i in range(sector_count)]
        target_line1 = VGroup(*target_sectors[:int(sector_count / 2)]).arrange(LEFT, buff=0) \
            .move_to(rectangle)
        target_line2 = VGroup(*target_sectors[int(sector_count / 2):]).arrange(RIGHT, buff=0) \
            .move_to(rectangle) \
            .shift(LEFT * (2 * PI / sector_count))

        shifts_line1 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line1, line1)]
        shifts_line2 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line2, line2)]

        for i in line1:
            i.save_state()
        for i in line2:
            i.save_state()

        def clousure(shift_line, index):
            def update_angle(obj, dt):
                obj.restore()
                obj.rotate(dt * (PI / 2 - (start_angle[index] + angle / 2)),
                           about_point=obj.get_center_of_mass())
                obj.shift(dt * (shift_line[index]))

            return update_angle

        total_line = 1440
        small_line = VGroup(*[Line(start=LEFT * 6,
                                   end=LEFT * 2,
                                   stroke_width=1).rotate(angle=i / total_line * PI)
                              for i in range(total_line)])

        self.play(*[
            FadeIn(small_line[i])
            for i in range(0, total_line, 4)
        ])
        self.wait()
        self.activate_zooming(animate=True)
        self.play(self.zoomed_camera.frame.animate.scale(0.2),
                     circle.animate.set_stroke(width=0.2),
                     *[small_line[i].animate.set_stroke(width=0.2)
                       for i in range(0, total_line, 4)],
                     run_time=3)
        self.wait()
        for i in range(0, total_line):
            small_line[i].set_stroke(width=0.2)

        self.play(*[
            FadeIn(small_line[i])
            for i in range(2, total_line, 4)
        ])
        self.wait()
        self.play(self.zoomed_camera.frame.animate.scale(0.3),
                     circle.animate.set_stroke(width=0.1),
                     run_time=3)
        self.wait()
        for i in range(0, total_line):
            small_line[i].set_stroke(width=0.1)

        self.play(*[
            FadeIn(small_line[i])
            for i in range(1, total_line, 2)
        ])
        self.wait()
        self.play(self.get_zoomed_display_pop_out_animation(),
                     rate_func=lambda t: smooth(1 - t))
        self.wait()
        self.play(FadeOut(self.zoomed_display), FadeOut(self.zoomed_camera.frame))
        self.wait()
        self.play(LaggedStart(*[
            FadeIn(i) for i in line1
        ],*[
            FadeIn(i) for i in line2
        ], lag_ratio=0.001))

        self.wait()

        self.play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line1, index)) for index, obj in enumerate(line1)
        ], rate_func=linear, run_time=2)
        self.wait()
        self.play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line2, index)) for index, obj in enumerate(line2)
        ], rate_func=linear, run_time=2)
        self.wait()


class Scene5(MyScene):
    def construct(self):
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=1).shift(LEFT * 4)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        rectangle = Rectangle(width=2 * PI, height=2, stroke_width=1) \
            .shift(RIGHT * 3)
        self.add(circle, center, rectangle)

        sector_count = 100
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "stroke_width": 2,
            "stroke_color": RED,
            "fill_color": WHITE
        }
        sectors = [Sector(angle=angle, start_angle=i, **sector_kwargs)
                   .shift(LEFT * 4)
                   for i in start_angle]
        line1 = VGroup(*sectors[:int(sector_count / 2)])
        line2 = VGroup(*sectors[int(sector_count / 2):])
        target_sectors = [Sector(angle=angle, start_angle=PI / 2 - angle / 2, **sector_kwargs)
                          for i in range(sector_count)]
        target_line1 = VGroup(*target_sectors[:int(sector_count / 2)]).arrange(LEFT, buff=0) \
            .move_to(rectangle)
        target_line2 = VGroup(*target_sectors[int(sector_count / 2):]).arrange(RIGHT, buff=0) \
            .move_to(rectangle) \
            .shift(LEFT * (2 * PI / sector_count))

        shifts_line1 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line1, line1)]
        shifts_line2 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line2, line2)]

        self.my_play(LaggedStart(*[
            FadeIn(i) for i in line1
        ],*[
            FadeIn(i) for i in line2
        ], lag_ratio=0.1))

        for i in line1:
            i.save_state()
        for i in line2:
            i.save_state()

        def clousure(shift_line, index):
            def update_angle(obj, dt):
                obj.restore()
                obj.rotate(dt * (PI / 2 - (start_angle[index] + angle / 2)),
                           about_point=obj.get_center_of_mass())
                obj.shift(dt * (shift_line[index]))

            return update_angle

        self.my_play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line1, index)) for index, obj in enumerate(line1)
        ], rate_func=linear)

        line = Line(start=center.get_center(),
                    end=center.get_center() + UP * 2,
                    color=BLUE)
        r = MathTex("r", color=BLUE).next_to(line, LEFT)

        h = VGroup(line, r)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        arc = circle.get_subcurve(0, 0.5).set_style(fill_opacity=0,
                                                    stroke_width=4,
                                                    stroke_color=GREEN)
        s = MathTex(r"\text{Nửa chu vi}", tex_template=myTemplate, color=GREEN).next_to(arc, UP)
        s_copy = s.copy().next_to(rectangle, UP, buff=MED_LARGE_BUFF)
        b = VGroup(arc, s)

        self.my_play(Write(h))
        self.my_play(h.copy().animate.next_to(rectangle, LEFT))
        self.my_play(Write(b))
        self.my_play(Transform(arc.copy(), rectangle.get_subcurve(0, 0.25)
                               .set_style(stroke_width=4,
                                          stroke_color=GREEN)
                               .next_to(rectangle, UP)),
                     Transform(s.copy(), s_copy))

        self.my_play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line1, index)) for index, obj in enumerate(line1)
        ], rate_func=lambda t: linear(1 - t))

        self.my_play(*[
            UpdateFromAlphaFunc(obj, clousure(shifts_line1, index)) for index, obj in enumerate(line1)
        ], rate_func=lambda t: linear(t))

        area = MathTex(r"S_{\text{hình tròn}} = S_{\text{hình chữ nhật}} = ",
                       "r", r" \times ", r"\text{Nửa chu vi}",
                       tex_template=myTemplate) \
            .to_edge(DOWN)

        area1 = MathTex(r"S_{\text{hình tròn}} = S_{\text{hình chữ nhật}} = ",
                        "r", r" \times ", r"r \times \pi",
                        tex_template=myTemplate) \
            .to_edge(DOWN)

        area2 = MathTex(r"S_{\text{hình tròn}} = S_{\text{hình chữ nhật}} = ",
                        "r^2", r" \times ", " \pi",
                        tex_template=myTemplate) \
            .to_edge(DOWN)

        map_color = ((area[1], area1[1], area1[3][0], area2[1][0]),
                     (area[3], area1[3]))
        color = (BLUE, GREEN)
        for i, j in zip(map_color, color):
            for tex in i:
                tex.set_color(j)

        self.my_play(*[Write(area[i])
                       for i in (0, 2)])

        self.my_play(ReplacementTransform(s[0].copy(), area[3]),
                     ReplacementTransform(r.copy(), area[1]))

        self.my_play(ReplacementTransform(area, area1))

        self.my_play(Transform(area1[3][0], area2[1][1]),
                     FadeOut(area1[2]),
                     Transform(area1[3][2], area2[3]),
                     Transform(area1[0], area2[0]),
                     Transform(area1[1], area2[1][0]),
                     Transform(area1[3][1], area2[2])
                     )

        self.my_play(Circumscribe(area2))

class Thumbnail(MyScene):
    def construct(self):
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=1)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        rectangle = Rectangle(width=2 * PI, height=2, stroke_width=1) \
            .shift(RIGHT * 3)
        # self.add(circle, center, rectangle)

        sector_count = 100
        angle = 2 * PI / sector_count
        start_angle = [i * angle for i in range(sector_count)]

        sector_kwargs = {
            "outer_radius": 2,
            "inner_radius": 0,
            "stroke_width": 2,
            "stroke_color": RED,
            "fill_color": WHITE
        }
        sectors = [Sector(angle=angle, start_angle=i, **sector_kwargs)
                   for i in start_angle]
        line1 = VGroup(*sectors[:int(sector_count / 2)])
        line2 = VGroup(*sectors[int(sector_count / 2):])
        target_sectors = [Sector(angle=angle, start_angle=PI / 2 - angle / 2, **sector_kwargs)
                          for i in range(sector_count)]
        target_line1 = VGroup(*target_sectors[:int(sector_count / 2)]).arrange(LEFT, buff=0) \
            .move_to(rectangle)
        target_line2 = VGroup(*target_sectors[int(sector_count / 2):]).arrange(RIGHT, buff=0) \
            .move_to(rectangle) \
            .shift(LEFT * (2 * PI / sector_count))

        shifts_line1 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line1, line1)]
        shifts_line2 = [i.get_center_of_mass() - j.get_center_of_mass()
                        for i, j in zip(target_line2, line2)]

        self.my_play(LaggedStart(*[
            FadeIn(i) for i in line1
        ],*[
            FadeIn(i) for i in line2
        ], lag_ratio=0.1))
        area_text = MathTex("S = \pi r^2", color=BLUE).scale(2).shift(RIGHT*4+UP*1.5)
        bw = Text("But \nwhy?", color=YELLOW, font_size=80).shift(RIGHT*4+DOWN/2)
        self.play(Write(area_text), Write(bw))