from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

list_scene = ("Scene1", "Scene2", "Scene3", "Scene31", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[1]
# SCENE_NAME = " ".join(list_scene)
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class Scene1(Scene):
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
        self.play(Write(circle), Write(center))
        self.play(Write(r_line), Write(r))
        self.play(Write(area_text), Write(arrow))
        self.play(FadeIn(pi, shift=RIGHT * 2))
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Text("Wait... but why?")
        self.play(NumberCreatureThinks(pi,
                                       wbw,
                                       target_mode="wonder",
                                       bubble_kwargs=bubble_kwargs
                                       )
                  )

        self.play(*[
            FadeOut(i) for i in (area_text, arrow, pi, pi.bubble, wbw, r_line, r)
        ])
        self.play(*[
            i.animate.shift(LEFT * 4) for i in (circle, center)
        ])
        self.play(Create(rectangle))


class Scene2(Scene):
    def construct(self):
        circle = Circle(radius=2, fill_color=YELLOW,
                        stroke_width=2,
                        fill_opacity=0.7).shift(LEFT * 4)
        center = Dot(circle.get_center(), color=RED).scale(0.5)
        rectangle = Rectangle(width=2 * PI, height=2, stroke_width=1) \
            .shift(RIGHT * 3)
        self.add(circle, center, rectangle)

        sector_count = 6
        angle = 2*PI/sector_count
        start_angle = [i*angle for i in range(sector_count)]
        
        sector_kwargs = {
            "outer_radius":2,
            "inner_radius":0,
        }
        sectors = [Sector(angle=angle, start_angle = i, **sector_kwargs).shift(LEFT*4) for i in start_angle]
        line1 = VGroup(*sectors[:int(sector_count/2)])
        line2 = VGroup(*sectors[int(sector_count/2):])

        self.play(*[
            Write(i) for i in line1
        ])
        self.play(*[
            Write(i) for i in line2
        ])
        for i in line1:
            i.save_state()
        def clousure(index):
            print(line1[index].points[0])
            def update_angle(obj, dt):
                obj.restore()
                obj.shift(dt * 3 * RIGHT)
                obj.rotate(dt*(PI/2-(start_angle[index]+angle/2)), about_point=obj.get_center())
                
            return update_angle

        self.play(*[
            UpdateFromAlphaFunc(obj, clousure(index)) for index,obj in enumerate(line1)
        ])
        target_line1 = line1.copy()
        target_line1.arrange(LEFT, buff=0).move_to(rectangle)
        self.play(*[
            Write(target_line1)
        ])
