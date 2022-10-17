import math

from manim import *

list_scene = ("Scene0", "Scene1", "Scene2")
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


class Scene0(MyScene):
    def setup(self):
        from datetime import datetime
        # self.now = datetime.now()
        self.nowhour = 12
        self.nowminute = 0
        self.hour = self.nowhour + self.nowminute / 60
        self.minute = self.nowminute
        print(self.hour)
        print(self.minute)
        self.circle = Circle().scale(2).rotate(PI / 2).flip(UP)
        self.add(self.circle)
        self.list_min = [self.circle.point_from_proportion(i / 60) for i in range(60)]
        self.list_line = [Line(i, self.circle.get_center()) for i in self.list_min]
        self.hour_hand = Arrow(self.circle.get_center(), self.list_line[0].point_from_proportion(0.4),
                               buff=0).set_color(RED).rotate(-self.hour / 6 * PI, about_point=self.circle.get_center())
        self.minute_hand = Arrow(self.circle.get_center(), self.list_line[0].point_from_proportion(0.15),
                                 buff=0).set_color(BLUE).rotate(-self.minute / 30 * PI,
                                                                about_point=self.circle.get_center())
        self.add(*[line.get_subcurve(0, 0.1) if i % 5 == 0 else line.get_subcurve(0, 0.03) for i, line in
                   enumerate(self.list_line)])
        self.add(self.hour_hand)
        self.add(self.minute_hand)
        self.add(Dot(self.circle.get_center()))
        self.add(*[
            Text("{hour:.0f}".format(hour=12 if i == 0 else i / 5)).scale(0.7).move_to(line.point_from_proportion(0.2))
            for i, line in enumerate(self.list_line) if i % 5 == 0])

    def construct(self):
        self.target_hour = 15
        self.target_minute = 20
        self.target_hour += self.target_minute / 60
        value = ValueTracker(self.hour * 60)
        self.add(value)

        def update_hand_factory(arrow, f):
            def func(obj):
                new_hand = arrow.copy().rotate(f(value.get_value()), about_point=self.circle.get_center())
                obj.become(new_hand)

            return func

        self.hour_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), self.list_line[0].point_from_proportion(0.4), buff=0).set_color(RED),
            lambda x: -(x / 60) / 6 * PI))
        self.minute_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), self.list_line[0].point_from_proportion(0.15), buff=0).set_color(BLUE),
            lambda x: -(x % 60) / 30 * PI))

        # self.play(value.animate.set_value(self.target_hour * 60), run_time=3)
        self.wait()

class Scene1(MyScene):
    def create_number(self):
        hour = str(self.nowhour)
        if self.nowhour < 10:
            hour = "0" + str(self.nowhour)
        minute = str(self.nowminute)
        if self.nowminute < 10:
            minute = "0" + str(self.nowminute)
        number = Text(hour + ":" + minute)
        rec = Rectangle().surround(number, buff=0.5, stretch=True)
        return VGroup(rec, number)

    def create_number(self, hours, minutes):
        hours = int(hours)
        minutes = int(minutes)
        hour = str(hours)
        if hours < 10:
            hour = "0" + hour
        minute = str(minutes)
        if minutes < 10:
            minute = "0" + minute
        number = MarkupText(hour + ":" + '<span foreground="yellow">{0}</span>'.format(minute), font="Sans")
        rec = Rectangle().surround(number, buff=1, stretch=True)
        return VGroup(rec, number)

    def setup(self):
        from datetime import datetime
        # self.now = datetime.now()
        self.nowhour = 0
        self.nowminute = 0
        self.hour = self.nowhour + self.nowminute / 60
        self.minute = self.nowminute
        print(self.hour)
        print(self.minute)
        self.circle = Circle().scale(2).rotate(PI / 2).flip(UP)
        self.big_circle = Circle(stroke_opacity=0).scale(2.3).rotate(PI / 2).flip(UP)
        self.add(self.circle)
        self.list_min = [self.circle.point_from_proportion(i / 60) for i in range(60)]
        self.list_line = [Line(i, self.circle.get_center()) for i in self.list_min]
        self.hour_hand = Arrow(self.circle.get_center(), self.list_line[0].point_from_proportion(0.4),
                               buff=0).set_color(RED).rotate(-self.hour / 6 * PI, about_point=self.circle.get_center())
        self.minute_hand = Arrow(self.circle.get_center(), self.list_line[0].point_from_proportion(0.15),
                                 buff=0).set_color(BLUE).rotate(-self.minute / 30 * PI,
                                                                about_point=self.circle.get_center())
        self.dot = Dot(self.circle.get_center())
        self.number = [
            Text("{hour:.0f}".format(hour=12 if i == 0 else i / 5)).scale(0.7).move_to(
                line.point_from_proportion(0.2))
            for i, line in enumerate(self.list_line) if i % 5 == 0]
        self.tick = [line.get_subcurve(0, 0.1) if i % 5 == 0 else line.get_subcurve(0, 0.03) for i, line in
                     enumerate(self.list_line)]
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number, self.big_circle)
        self.hands = VGroup(self.hour_hand, self.minute_hand)

    def construct(self):
        self.add(self.minute_hand)
        self.clock.shift(LEFT*3).scale(1.5)
        number = self.create_number(0, 0).shift(RIGHT*3+UP*3)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        A_t = MathTex("A", color=YELLOW).move_to(self.big_circle.point_from_proportion(0))
        self.add(number, A, A_t)
        self.add(self.clock)
        self.remove(self.hour_hand)

        value = ValueTracker(self.hour * 60)
        self.add(value)
        some_way = MarkupText('Bằng cách nào đó???', font="Sans", font_size=30).next_to(number, DOWN, buff=LARGE_BUFF)
        A_coord = MarkupText('A ({:.2f}, {:.2f})'.format(0,1), color=YELLOW, font="Sans", font_size=27).next_to(some_way, DOWN, buff=LARGE_BUFF)
        self.add(some_way, A_coord,
                 Arrow(some_way.get_bottom(), A_coord.get_top()),
                 Arrow(number.get_bottom(), some_way.get_top()),
                 Arrow(A_coord.get_left(), self.circle.get_right()+DOWN*0.05))

        def update_hand_factory(arrow, f):
            def func(obj):
                new_hand = arrow.copy().rotate(f(value.get_value()), about_point=self.circle.get_center())
                obj.become(new_hand)
                A.move_to(self.circle.point_from_proportion(value.get_value()/60))
                A_t.move_to(self.big_circle.point_from_proportion(value.get_value()/60))
                number[1].become(self.create_number(0, value.get_value()).shift(RIGHT * 3 + UP * 3)[1])
                angle = (value.get_value()/60)*2*PI
                angle *= -1
                angle += PI/2
                A_coord.become(MarkupText('A ({:.2f}, {:.2f})'.format(math.cos(angle), math.sin(angle)), color=YELLOW, font="Sans", font_size=27).next_to(some_way, DOWN, buff=LARGE_BUFF))

            return func

        def update_number(obj):
            pass

        line = Line(self.circle.get_center(), self.circle.get_start())

        self.minute_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), line.point_from_proportion(0.8), buff=0).set_color(BLUE),
            lambda x: -(x % 60) / 30 * PI))

        number.add_updater(update_number)

        self.play(value.animate.set_value(60), run_time=2)
        # self.play(value.animate.set_value(10), run_time=2)
        self.wait()
