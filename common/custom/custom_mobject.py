import random

from manim import *


class TickDecimalNumber(VGroup):
    def __init__(self, number=0, tick_direction=DOWN, tick_color=RED, **kwargs):
        super().__init__(**kwargs)
        self.tick_direction = tick_direction
        self.tick_color = tick_color
        self.number = number
        self.add_number()
        self.add_tick()

    def add_number(self):
        self.decimal_number = DecimalNumber(number=self.number)
        self.add(self.decimal_number)

    def add_tick(self):
        kwargs = {
            "stroke_width": 0,
            "fill_color": self.tick_color,
            "fill_opacity": 1
        }
        self.tick = Triangle(**kwargs).scale(0.2)

        if (self.tick_direction == DOWN).all():
            self.tick.rotate(PI)
        elif (self.tick_direction == LEFT).all():
            self.tick.rotate(PI / 2)
        elif (self.tick_direction == RIGHT).all():
            self.tick.rotate(-PI / 2)

        self.tick.next_to(self.decimal_number, self.tick_direction)
        self.add(self.tick)

    def get_decimal_number(self):
        return self.decimal_number

    def get_tick(self):
        return self.tick


class TextTranslation(VGroup):
    def __init__(self,
                 text_u: str = "text1",
                 text_d: str = "(text2)",
                 font_u: str = "Sans",
                 font_d: str = "",
                 font_size_u: float = 40,
                 font_size_d: float = 30,
                 color_u: str = YELLOW,
                 color_d: str = ORANGE,
                 buff: float = MED_SMALL_BUFF,
                 **kwargs):
        super().__init__(**kwargs)
        self.add(Text(text_u, font=font_u, font_size=font_size_u, color=color_u))
        self.add(Text(text_d, font=font_d, font_size=font_size_d, color=color_d))
        self.arrange(DOWN, buff=buff)

    def align_points_with_larger(self, larger_mobject):
        pass


class Explain(VGroup):
    def __init__(self, target, text: str = "text", location=ORIGIN, shift=ORIGIN, font_size: float = 35, **kwargs):
        super().__init__(**kwargs)
        explain = Text(text, font="Sans", font_size=font_size).move_to(location).shift(shift)
        rec = Rectangle(color=YELLOW).surround(target, stretch=True, buff=SMALL_BUFF)
        arrow = Arrow(explain.get_bottom(), rec.get_top())
        if explain.get_center()[1] < target.get_center()[1]:
            arrow = Arrow(explain.get_top(), rec.get_bottom())
        self.add(rec)
        self.add(arrow)
        self.add(explain)

    def align_points_with_larger(self, larger_mobject):
        pass


class ImageAndText(Group):
    def __init__(self,
                 name: str = "file_name",
                 image_width: float = 2,
                 content: str = "hello",
                 text_font: str = "Sans",
                 text_size: float = 30,
                 text_color: str = RED,
                 text_buff: float = 0.2,
                 **kwargs):
        super().__init__(**kwargs)
        image = ImageMobject(name).scale_to_fit_width(image_width)
        text = Text(content, font_size=text_size, font=text_font, color=text_color).next_to(image, DOWN, buff=text_buff)
        self.add(image, text)


class ImageAndMathTex(Group):
    def __init__(self,
                 name: str = "file_name",
                 image_width: float = 2,
                 content: str = "abc",
                 tex_scale: float = 1,
                 tex_color: str = RED,
                 text_buff: float = 0.2,
                 **kwargs):
        super().__init__(**kwargs)
        image = ImageMobject(name).scale_to_fit_width(image_width)
        tex = MathTex(content, color=tex_color).scale(tex_scale).next_to(image, DOWN, buff=text_buff)
        self.add(image, tex)


class SetNumber(VGroup):
    def __init__(self,
                 elements,
                 name: str = "Số tự nhiên",
                 elip_width: float = 3,
                 elip_height: float = 5,
                 font_size: float = 35,
                 text_color: str = RED,
                 **kwargs):
        super().__init__(**kwargs)
        elip = Ellipse(width=elip_width, height=elip_height, color=text_color)
        text = Text(name, font_size=font_size, font="Sans", color=text_color).next_to(elip, DOWN)
        self.add(elements, elip, text)


class Beaker(VGroup):
    def __init__(self,
                 file_name: str = "beaker",
                 beaker_color: str = TEAL,
                 solution_color: str = BLUE,
                 solution_percent: float = 0.7,
                 ion_number: int = 10,
                 ion_color: str = RED,
                 random_seed: int = 1,
                 **kwargs):
        super().__init__(**kwargs)
        beaker = SVGMobject(file_name).set_color(beaker_color)
        solution = RoundedRectangle(
            corner_radius=0.05,
            width=beaker.width-0.2,
            height=beaker.height*solution_percent,
            stroke_width=0,
            fill_opacity=0.5,
            fill_color=solution_color)\
            .align_to(beaker, DR).shift(LEFT*0.05+UP*0.05)

        def ion_factory():
            circle = Circle(radius=0.07, stroke_width=2)
            text = MathTex(r"\text{H}^+").move_to(circle).scale(0.15)
            group = VGroup(circle, text).move_to(solution)
            w_range = solution.width/2-0.1
            h_range = solution.height/2-0.1
            group.shift(RIGHT*random.uniform(-w_range*RIGHT, w_range*RIGHT))
            group.shift(UP*random.uniform(-h_range*UP, h_range*UP))
            return group
        ions = VGroup(*[ion_factory() for i in range(ion_number)])
        self.add(solution, beaker, *ions)


class TestCustomMobject(Scene):
    def construct(self):
        a = Beaker("assets/beaker.svg", ion_number=50).scale(3)
        self.add(a)
