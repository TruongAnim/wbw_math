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
