import math

from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[1]
SCENE_NAME = " ".join(list_scene[1:5])
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

if __name__ == "__main__":
    command = f"manim --disable_caching -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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

        self.play(value.animate.set_value(self.target_hour * 60), run_time=3)
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
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number,
                            self.big_circle)
        self.hands = VGroup(self.hour_hand, self.minute_hand)

    def construct(self):
        self.add(self.minute_hand)
        self.clock.shift(LEFT * 3).scale(1.5)
        number = self.create_number(0, 0).shift(RIGHT * 3 + UP * 3)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        A_t = MathTex("A", color=YELLOW).move_to(self.big_circle.point_from_proportion(0))
        self.add(number, A, A_t)
        self.add(self.clock)
        self.remove(self.hour_hand)

        value = ValueTracker(self.hour * 60)
        self.add(value)
        some_way = MarkupText('Bằng cách nào đó???', font="Sans", font_size=30).next_to(number, DOWN, buff=LARGE_BUFF)
        A_coord = MarkupText('A ({:.2f}, {:.2f})'.format(0, 1), color=YELLOW, font="Sans", font_size=27).next_to(
            some_way, DOWN, buff=LARGE_BUFF)
        self.add(some_way, A_coord,
                 Arrow(some_way.get_bottom(), A_coord.get_top()),
                 Arrow(number.get_bottom(), some_way.get_top()),
                 Arrow(A_coord.get_left(), self.circle.get_right() + DOWN * 0.05))

        def update_hand_factory(arrow, f):
            def func(obj):
                new_hand = arrow.copy().rotate(f(value.get_value()), about_point=self.circle.get_center())
                obj.become(new_hand)
                A.move_to(self.circle.point_from_proportion(value.get_value() / 60))
                A_t.move_to(self.big_circle.point_from_proportion(value.get_value() / 60))
                number[1].become(self.create_number(0, value.get_value()).shift(RIGHT * 3 + UP * 3)[1])
                angle = (value.get_value() / 60) * 2 * PI
                angle *= -1
                angle += PI/2
                A_coord.become(
                    MarkupText('A ({:.2f}, {:.2f})'.format(math.cos(angle), math.sin(angle)), color=YELLOW, font="Sans",
                               font_size=27).next_to(some_way, DOWN, buff=LARGE_BUFF))

            return func

        def update_number(obj):
            pass

        line = Line(self.circle.get_center(), self.circle.get_start())

        self.minute_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), line.point_from_proportion(0.8), buff=0).set_color(BLUE),
            lambda x: -(x % 60) / 30 * PI))

        number.add_updater(update_number)

        self.play(value.animate.set_value(10), run_time=2)
        self.play(value.animate.set_value(25), run_time=2)
        self.play(value.animate.set_value(50), run_time=2)
        self.wait()


class Scene2(MyScene):
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
        if hours < 0 or minutes < 0:
            hour = "hh"
            minute = "mm"
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
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number,
                            self.big_circle)
        self.hands = VGroup(self.hour_hand, self.minute_hand)

    def construct(self):
        self.clock.shift(LEFT * 3).scale(1.5)
        self.clock.remove(self.hour_hand, self.minute_hand)
        number = self.create_number(-1, -1).shift(RIGHT * 3 + UP * 3)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        A_t = MathTex("A", color=YELLOW).move_to(self.big_circle.point_from_proportion(0))

        value = ValueTracker(self.hour * 60)
        some_way = MathTex(r'\alpha', "=", "mm", r"\times", "{\pi \over 30}", "=", "...") \
            .next_to(number, DOWN, buff=LARGE_BUFF)
        A_coord = MathTex(r'A', ' (cos(', r'\alpha', '), sin(', r"\alpha", '))') \
            .next_to(some_way, DOWN, buff=LARGE_BUFF)
        A_coord2 = MathTex(r'A', ' (', "x", ",", "y", ')').next_to(A_coord, DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)
        arrows = VGroup(
            Arrow(number.get_bottom(), some_way.get_top()),
            Arrow(some_way.get_bottom(), A_coord.get_top()),
            Arrow(A_coord2.get_left(), A_coord2.get_left() + LEFT * 1.2))

        def set_color(sw, A1, A2):
            sw[0].set_color(RED)
            sw[2].set_color(YELLOW)
            sw[-1].set_color(RED)
            A1[0].set_color(YELLOW)
            A1[2].set_color(RED)
            A1[4].set_color(RED)
            A2[0].set_color(YELLOW)
            A2[2].set_color(ORANGE)
            A2[4].set_color(ORANGE)

        set_color(some_way, A_coord, A_coord2)
        unit_circle = self.circle.copy().rotate(-PI / 2).flip(RIGHT)
        big_unit_circle = self.big_circle.copy().rotate(-PI / 2).flip(RIGHT)

        def update_hand_factory(arrow, f):
            def func(obj):
                int_minute = value.get_value()
                new_hand = arrow.copy().rotate(f(value.get_value()), about_point=self.circle.get_center())
                obj.become(new_hand)
                A.move_to(unit_circle.point_from_proportion(value.get_value() / 60))
                A_t.move_to(big_unit_circle.point_from_proportion(value.get_value() / 60))
                number[1].become(self.create_number(0, value.get_value()).shift(RIGHT * 3 + UP * 3)[1])
                angle = (value.get_value() / 60) * 2 * PI
                # angle *= -1
                # angle += PI / 2
                s = MathTex(r'\alpha', "=", "{:.0f}".format(int_minute), r"\times", "{\pi \over 30}", "=",
                            "{:.2f}".format(angle) + "^{rad}") \
                    .next_to(number, DOWN, buff=LARGE_BUFF)
                A1 = MathTex(r'A', ' (cos(', '{:.2f}'.format(angle), '), sin(', '{:.2f}'.format(angle), '))') \
                    .next_to(some_way, DOWN, buff=LARGE_BUFF).align_to(number, LEFT)
                A2 = MathTex(r'A', ' (', '{:.2f}'.format(math.cos(angle)), ",", '{:.2f}'.format(math.sin(angle)), ')') \
                    .next_to(A_coord, DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)

                set_color(s, A1, A2)
                some_way.become(s)
                A_coord.become(A1)
                A_coord2.become(A2)

            return func

        def update_number(obj):
            pass

        line = Line(unit_circle.get_center(), unit_circle.get_start())
        self.minute_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), line.point_from_proportion(0.8), buff=0).set_color(BLUE),
            lambda x: (x % 60) / 30 * PI))

        number.add_updater(update_number)
        self.my_play(Write(self.clock))
        self.my_play(Write(number), GrowArrow(arrows[0]))
        self.my_play(Write(some_way))
        self.my_play(Write(arrows[1]))
        self.my_play(Write(A_coord), Write(A_coord2))
        self.my_play(Write(arrows[2]))
        self.my_play(Create(self.minute_hand))
        self.add(value, A, A_t)
        self.my_play(value.animate.set_value(10), run_time=4)
        self.my_play(value.animate.set_value(25), run_time=4)
        self.my_play(value.animate.set_value(50), run_time=4)


class Scene3(MyScene):
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
        if hours < 0 or minutes < 0:
            hour = "hh"
            minute = "mm"
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
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number,
                            self.big_circle)
        self.hands = VGroup(self.hour_hand, self.minute_hand)

    def construct(self):
        self.clock.shift(LEFT * 3).scale(1.5)
        self.clock.remove(self.hour_hand, self.minute_hand)
        number = self.create_number(-1, -1).shift(RIGHT * 3 + UP * 3)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        A_t = MathTex("A", color=YELLOW).move_to(self.big_circle.point_from_proportion(0))

        value = ValueTracker(self.hour * 60)
        some_way = MathTex(r'\alpha', "=", "mm", r"\times", "{\pi \over 30}", "=", "...") \
            .next_to(number, DOWN, buff=LARGE_BUFF)
        some_way1 = MathTex(r"\alpha", "=", "-", r"\alpha").next_to(some_way, DOWN, buff=LARGE_BUFF)
        some_way1[0].set_color(RED)
        some_way1[-1].set_color(RED)
        some_way2 = MathTex(r"\alpha", "=", r"\alpha" + "{\pi \over 2}").next_to(some_way1, DOWN, aligned_edge=LEFT,
                                                                                 buff=SMALL_BUFF)
        some_way2[0].set_color(RED)
        some_way2[2].set_color(RED)
        A_coord = MathTex(r'A', ' (cos(', r'\alpha', '), sin(', r"\alpha", '))') \
            .next_to(some_way2, DOWN, buff=LARGE_BUFF)
        A_coord2 = MathTex(r'A', ' (', "x", ",", "y", ')').next_to(A_coord, DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)
        arrows = VGroup(
            Arrow(number.get_bottom(), some_way.get_top()),
            Arrow(some_way.get_bottom(), some_way1.get_top()),
            Arrow(some_way2.get_bottom(), A_coord.get_top()),
            Arrow(A_coord2.get_left(), A_coord2.get_left() + LEFT * 1.2 + UP))

        def set_color(sw, A1, A2):
            sw[0].set_color(RED)
            sw[2].set_color(YELLOW)
            sw[-1].set_color(RED)
            A1[0].set_color(YELLOW)
            A1[2].set_color(RED)
            A1[4].set_color(RED)
            A2[0].set_color(YELLOW)
            A2[2].set_color(ORANGE)
            A2[4].set_color(ORANGE)

        set_color(some_way, A_coord, A_coord2)
        unit_circle = self.circle.copy().rotate(-PI / 2)
        big_unit_circle = self.big_circle.copy().rotate(-PI / 2)

        def update_hand_factory(arrow, f):
            def func(obj):
                int_minute = value.get_value()
                new_hand = arrow.copy().rotate(f(value.get_value()), about_point=self.circle.get_center())
                obj.become(new_hand)
                A.move_to(unit_circle.point_from_proportion(value.get_value() / 60))
                A_t.move_to(big_unit_circle.point_from_proportion(value.get_value() / 60))
                number[1].become(self.create_number(0, value.get_value()).shift(RIGHT * 3 + UP * 3)[1])
                angle = (value.get_value() / 60) * 2 * PI

                s = MathTex(r'\alpha', "=", "{:.0f}".format(int_minute), r"\times", "{\pi \over 30}", "=",
                            "{:.2f}".format(angle) + "^{rad}") \
                    .next_to(number, DOWN, buff=LARGE_BUFF)
                angle *= -1
                # angle += PI / 2
                A1 = MathTex(r'A', ' (cos(', '{:.2f}'.format(angle), '), sin(', '{:.2f}'.format(angle), '))') \
                    .next_to(some_way2, DOWN, buff=LARGE_BUFF).align_to(number, LEFT)
                A2 = MathTex(r'A', ' (', '{:.2f}'.format(math.cos(angle)), ",", '{:.2f}'.format(math.sin(angle)), ')') \
                    .next_to(A_coord, DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)

                set_color(s, A1, A2)
                some_way.become(s)
                A_coord.become(A1)
                A_coord2.become(A2)

            return func

        def update_number(obj):
            pass

        line = Line(unit_circle.get_center(), unit_circle.get_start())
        self.minute_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), line.point_from_proportion(0.8), buff=0).set_color(BLUE),
            lambda x: -(x % 60) / 30 * PI))

        number.add_updater(update_number)
        self.my_play(Write(self.clock))
        self.my_play(Write(number), GrowArrow(arrows[0]))
        self.my_play(Write(some_way))
        self.my_play(GrowArrow(arrows[1]), Write(some_way1))
        self.my_play(Write(arrows[2]))
        self.my_play(Write(A_coord), Write(A_coord2))
        self.my_play(Write(arrows[3]))
        self.my_play(Create(self.minute_hand))
        self.add(value, A, A_t)
        self.my_play(value.animate.set_value(10), run_time=4)
        self.my_play(value.animate.set_value(25), run_time=4)
        self.my_play(value.animate.set_value(50), run_time=4)


class Scene4(MyScene):
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
        if hours < 0 or minutes < 0:
            hour = "hh"
            minute = "mm"
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
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number,
                            self.big_circle)
        self.hands = VGroup(self.hour_hand, self.minute_hand)

    def construct(self):
        self.clock.shift(LEFT * 3).scale(1.5)
        self.clock.remove(self.hour_hand, self.minute_hand)
        number = self.create_number(-1, -1).shift(RIGHT * 3 + UP * 3)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        A_t = MathTex("A", color=YELLOW).move_to(self.big_circle.point_from_proportion(0))

        value = ValueTracker(self.hour * 60)
        some_way = MathTex(r'\alpha', "=", "mm", r"\times", "{\pi \over 30}", "=", "...") \
            .next_to(number, DOWN, buff=LARGE_BUFF)
        some_way1 = MathTex(r"\alpha", "=", "-", r"\alpha").next_to(some_way, DOWN, buff=LARGE_BUFF)
        some_way1[0].set_color(RED)
        some_way1[-1].set_color(RED)
        some_way2 = MathTex(r"\alpha", "=", r"\alpha", "+", "{\pi \over 2}").next_to(some_way1, DOWN, aligned_edge=LEFT,
                                                                                     buff=SMALL_BUFF)
        some_way2[0].set_color(RED)
        some_way2[2].set_color(RED)
        A_coord = MathTex(r'A', ' (cos(', r'\alpha', '), sin(', r"\alpha", '))') \
            .next_to(some_way2, DOWN, buff=LARGE_BUFF)
        A_coord2 = MathTex(r'A', ' (', "x", ",", "y", ')').next_to(A_coord, DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)
        arrows = VGroup(
            Arrow(number.get_bottom(), some_way.get_top()),
            Arrow(some_way.get_bottom(), some_way1.get_top()),
            Arrow(some_way2.get_bottom(), A_coord.get_top()),
            Arrow(A_coord2.get_left(), A_coord2.get_left() + LEFT * 1.2 + UP))

        def set_color(sw, A1, A2):
            sw[0].set_color(RED)
            sw[2].set_color(YELLOW)
            sw[-1].set_color(RED)
            A1[0].set_color(YELLOW)
            A1[2].set_color(RED)
            A1[4].set_color(RED)
            A2[0].set_color(YELLOW)
            A2[2].set_color(ORANGE)
            A2[4].set_color(ORANGE)

        set_color(some_way, A_coord, A_coord2)
        unit_circle = self.circle.copy().rotate(-PI / 2).flip(RIGHT)
        big_unit_circle = self.big_circle.copy().rotate(-PI / 2).flip(RIGHT)

        def update_hand_factory(arrow, f):
            def func(obj):
                int_minute = value.get_value()
                new_hand = arrow.copy().rotate(f(value.get_value()), about_point=self.circle.get_center())
                obj.become(new_hand)
                A.move_to(self.circle.point_from_proportion(value.get_value() / 60))
                A_t.move_to(self.big_circle.point_from_proportion(value.get_value() / 60))
                number[1].become(self.create_number(0, value.get_value()).shift(RIGHT * 3 + UP * 3)[1])
                angle = (value.get_value() / 60) * 2 * PI

                s = MathTex(r'\alpha', "=", "{:.0f}".format(int_minute), r"\times", "{\pi \over 30}", "=",
                            "{:.2f}".format(angle) + "^{rad}") \
                    .next_to(number, DOWN, buff=LARGE_BUFF)
                angle *= -1
                angle += PI / 2
                A1 = MathTex(r'A', ' (cos(', '{:.2f}'.format(angle), '), sin(', '{:.2f}'.format(angle), '))') \
                    .next_to(some_way2, DOWN, buff=LARGE_BUFF).align_to(number, LEFT)
                A2 = MathTex(r'A', ' (', '{:.2f}'.format(math.cos(angle)), ",", '{:.2f}'.format(math.sin(angle)), ')') \
                    .next_to(A_coord, DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)

                set_color(s, A1, A2)
                some_way.become(s)
                A_coord.become(A1)
                A_coord2.become(A2)

            return func

        def update_number(obj):
            pass

        line = Line(self.circle.get_center(), self.circle.get_start())
        # self.play(Create(self.circle))
        self.minute_hand.add_updater(update_hand_factory(
            Arrow(self.circle.get_center(), line.point_from_proportion(0.8), buff=0).set_color(BLUE),
            lambda x: -(x % 60) / 30 * PI))

        number.add_updater(update_number)
        self.my_play(Write(self.clock))
        self.my_play(Write(number), GrowArrow(arrows[0]))
        self.my_play(Write(some_way))
        self.my_play(GrowArrow(arrows[1]), Write(some_way1))
        self.my_play(Write(some_way2))
        self.my_play(Write(arrows[2]))
        self.my_play(Write(A_coord), Write(A_coord2))
        self.my_play(Write(arrows[3]))
        self.my_play(Create(self.minute_hand))
        self.add(value, A, A_t)
        self.my_play(value.animate.set_value(10), run_time=4)
        self.my_play(value.animate.set_value(25), run_time=4)
        self.my_play(value.animate.set_value(50), run_time=4)


class Scene5(MyScene):
    def construct(self):
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        O = Dot(ORIGIN)
        H = Dot(main_circle.point_from_proportion(1 / 6))
        H_t = MathTex("A", "(", r"cos(\alpha)", ",", r"sin(\alpha)", ")").next_to(H, UR, buff=SMALL_BUFF)
        H_t[2].set_color(RED)
        H_t[4].set_color(GREEN)
        O_t = MathTex("O").next_to(O, DL)
        x_t = MathTex("x").next_to(horizontal, RIGHT)
        y_t = MathTex("y").next_to(vertical.get_end(), RIGHT)
        A = Dot(RIGHT * 3)
        B = Dot(UP * 3)
        C = Dot(LEFT * 3)
        D = Dot(DOWN * 3)
        coord_A = MathTex("(1,0)").next_to(A, DR)
        coord_B = MathTex("(0,1)").next_to(B, UL)
        coord_C = MathTex("(-1,0)").next_to(C, DL)
        coord_D = MathTex("(0,-1)").next_to(D, DL)
        OH = Line(O, H, color=YELLOW)
        OH_t = MathTex("1", color=YELLOW).scale(0.7).next_to(OH.get_center(), DR, buff=SMALL_BUFF)
        X = Dot(RIGHT * math.cos(PI / 3) * 3)
        HX = Line(H, X.get_center(), color=GREEN)
        OX = Line(O, X.get_center(), color=RED)
        OHX = RightAngle(HX, OX, length=0.2, quadrant=(-1, -1))
        Y = Dot(UP * math.sin(PI / 3) * 3)
        HY = Line(H, Y.get_center(), color=RED)
        OY = Line(O, Y.get_center(), color=GREEN)
        OHY = RightAngle(HY, OY, length=0.2, quadrant=(-1, -1))
        alpha = Angle(OH, OX, other_angle=True, radius=0.3)
        a = MathTex(r"cos(\alpha)", color=RED).next_to(OX, DOWN)
        b = MathTex(r"sin(\alpha)", color=GREEN).next_to(OY, LEFT)
        alpha_t = MathTex(r"\alpha").scale(0.8).move_to(Angle(OH, OX, other_angle=True, radius=0.6))

        unit_circle = VGroup(main_circle, vertical, horizontal, O_t, x_t, y_t, O, A, B, C, D, coord_A, coord_B,
                             coord_C, coord_D, H, H_t, OH, OH_t, X, HX, OX, OHX, alpha, alpha_t, HY, Y, OY, OHY, a,
                             b)
        # self.add(unit_circle, fomular1, fomular2)
        self.my_play(Create(O), Write(O_t), Create(main_circle))
        self.my_play(Create(vertical), Create(horizontal), Write(x_t), Write(y_t))
        self.my_play(Write(coord_A), Write(coord_B), Write(coord_C), Write(coord_D))
        self.my_play(Create(OH), Create(alpha), Create(H), Create(OH_t))
        self.my_play(Write(alpha_t), Write(H_t[0]))
        self.my_play(Create(HX), Create(OHX), Create(X), Create(HY), Create(OHY), Create(Y))
        self.my_play(Create(OX), Write(a), Create(OY), Write(b))
        self.my_play(Transform(a.copy(), H_t[2]), Transform(b.copy(), H_t[4]),
                  Write(H_t[1]), Write(H_t[3]), Write(H_t[5]))


class Scene6(MyScene):
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
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number,
                            self.big_circle)
        self.hands = VGroup(self.hour_hand, self.minute_hand)

    def construct(self):
        self.clock.shift(LEFT * 3)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        curve_arrow = CurvedArrow(self.big_circle.get_start(), self.big_circle.point_from_proportion(0.25), angle=-PI/2, color=GREEN)
        main_circle = Circle(radius=3, color=BLUE)
        vertical = Arrow(start=DOWN * 4, end=UP * 4, stroke_width=1)
        horizontal = Arrow(start=LEFT * 4, end=RIGHT * 4, stroke_width=1)
        unit_circle = VGroup(main_circle, vertical, horizontal).shift(RIGHT*3).scale(0.7)
        B = Dot(main_circle.point_from_proportion(0), color=YELLOW)
        curve_arrow2 = CurvedArrow(horizontal.point_from_proportion(0.99), vertical.point_from_proportion(0.99), angle=PI/2, color=GREEN)
        positive1 = Text("Chiều dương", font="Sans", font_size=30, color=GREEN).to_corner(UR)
        arrow1 = Arrow(positive1.get_bottom(), curve_arrow2.point_from_proportion(0.5))
        positive2 = Text("Chiều dương", font="Sans", font_size=30, color=GREEN).shift(UP*3.3+LEFT*0.5)
        arrow2 = Arrow(positive2.get_bottom(), curve_arrow.point_from_proportion(0.5))
        start_point = Text("Điểm bắt đầu", font="Sans", font_size=30, color=YELLOW).shift(DOWN*2+RIGHT*5.5)
        arrow3 = Arrow(start_point.get_top(), B)
        start_point2 = Text("Điểm bắt đầu", font="Sans", font_size=30, color=YELLOW).shift(UP*3.3+LEFT*5.5)
        arrow4 = Arrow(start_point2.get_bottom(), A)
        unit_circle_t = Text("Đường tròn đơn vị", font="Sans", font_size=30, color=BLUE).next_to(unit_circle, DOWN)
        clock_t = Text("Đồng hồ", font="Sans", font_size=30, color=RED).next_to(self.clock, DOWN).align_to(unit_circle_t, DOWN)
        self.my_play(Write(clock_t), Write(unit_circle_t), Write(self.clock), Write(unit_circle))
        self.my_play(Write(positive1), Write(positive2), GrowArrow(arrow1), GrowArrow(arrow2), Create(curve_arrow), Create(curve_arrow2))
        self.my_play(Create(A), Create(B), Write(start_point), Write(start_point2), GrowArrow(arrow3), GrowArrow(arrow4))