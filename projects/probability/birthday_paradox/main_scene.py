from manim import *

import datetime
import random
from common.custom.custom_mobject import ImageAndText

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6",
              "Scene7")
SCENE_NAME = list_scene[7]
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


class Scene0(MyScene):
    def construct(self):
        def create_birthday(id, day):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            return ImageAndText("chars/char (" + str(id) + ")",
                                content=date.strftime('%Y-%m-%d'),
                                text_buff=-0.1,
                                text_size=20)

        random.seed(2)
        list_id = [random.randint(1, 10) for _ in range(32)]
        list_day = random.sample(range(1, 366), 32)
        list_day[19] = list_day[9]

        group = Group(*[create_birthday(i, j) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 8).scale(
            0.75).shift(UP * 0.7)
        brace = Brace(group, DOWN)
        text = Text("32 học sinh", font_size=40, font="Sans").next_to(brace, DOWN, buff=SMALL_BUFF)
        self.my_play(LaggedStart(*[FadeIn(i, shift=UP) for i in group]))
        self.my_play(Wiggle(group[9]), Wiggle(group[19]))
        group[9][1].set_color(GREEN), group[19][1].set_color(GREEN)
        self.my_play(Circumscribe(group[9][1]), Circumscribe(group[19][1]))
        self.my_play(FadeIn(brace, shift=UP), FadeIn(text, shift=UP))


class Scene1(MyScene):
    def construct(self):
        def create_birthday(id, day):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            return ImageAndText("other_chars/other_char (" + str(id) + ")",
                                content=date.strftime('%Y-%m-%d'),
                                text_buff=-0.1,
                                text_size=20)

        random.seed(3)
        first = 4
        second = 21
        list_id = [random.randint(1, 45) for _ in range(32)]
        list_day = random.sample(range(1, 366), 32)
        list_day[second] = list_day[first]

        group = Group(*[create_birthday(i, j) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 8).scale(
            0.75).shift(UP * 0.7)
        brace = Brace(group, DOWN)
        text = Text("Lớp A", font_size=50, font="Sans").next_to(group, DOWN)
        self.add(group, text)
        self.wait()
        self.play(Wiggle(group[first]), Wiggle(group[second]))
        group[second][1].set_color(GREEN), group[first][1].set_color(GREEN)
        self.play(Circumscribe(group[second][1]), Circumscribe(group[first][1]),
                  Create(Rectangle(color=GREEN).surround(group[second], stretch=True)),
                  Create(Rectangle(color=GREEN).surround(group[first], stretch=True)))


class Scene2(MyScene):
    def construct(self):
        def create_birthday(id, day):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            return ImageAndText("other_chars/other_char (" + str(id) + ")",
                                content=date.strftime('%Y-%m-%d'),
                                text_buff=-0.1,
                                text_size=20)

        random.seed(4)
        first = 13
        second = 19
        list_id = [random.randint(1, 45) for _ in range(32)]
        list_day = random.sample(range(1, 366), 32)
        list_day[second] = list_day[first]

        group = Group(*[create_birthday(i, j) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 8).scale(
            0.75).shift(UP * 0.7)
        brace = Brace(group, DOWN)
        text = Text("Lớp B", font_size=50, font="Sans").next_to(group, DOWN)
        self.add(group, text)
        self.wait()
        self.play(Wiggle(group[first]), Wiggle(group[second]))
        group[second][1].set_color(GREEN), group[first][1].set_color(GREEN)
        self.play(Circumscribe(group[second][1]), Circumscribe(group[first][1]),
                  Create(Rectangle(color=GREEN).surround(group[second], stretch=True)),
                  Create(Rectangle(color=GREEN).surround(group[first], stretch=True)))


class Scene3(MyScene):
    def construct(self):
        def create_birthday(id, day):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            return ImageAndText("other_chars/other_char (" + str(id) + ")",
                                content=date.strftime('%Y-%m-%d'),
                                text_buff=-0.1,
                                text_size=20)

        random.seed(5)
        first = 4
        second = 21
        list_id = [random.randint(1, 45) for _ in range(32)]
        list_day = random.sample(range(1, 366), 32)

        group = Group(*[create_birthday(i, j) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 8).scale(
            0.75).shift(UP * 0.7)
        brace = Brace(group, DOWN)
        text = Text("Lớp C", font_size=50, font="Sans").next_to(group, DOWN)
        self.add(group, text)
        self.wait()


class Scene4(MyScene):
    def construct(self):
        def create_birthday(id, day):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            return ImageAndText("other_chars/other_char (" + str(id) + ")",
                                content=date.strftime('%Y-%m-%d'),
                                text_buff=-0.1,
                                text_size=20)

        random.seed(6)
        first = 8
        second = 28
        list_id = [random.randint(1, 45) for _ in range(32)]
        list_day = random.sample(range(1, 366), 32)
        list_day[second] = list_day[first]

        group = Group(*[create_birthday(i, j) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 8).scale(
            0.75).shift(UP * 0.7)
        brace = Brace(group, DOWN)
        text = Text("Lớp D", font_size=50, font="Sans").next_to(group, DOWN)
        self.add(group, text)
        self.wait()
        self.play(Wiggle(group[first]), Wiggle(group[second]))
        group[second][1].set_color(GREEN), group[first][1].set_color(GREEN)
        self.play(Circumscribe(group[second][1]), Circumscribe(group[first][1]),
                  Create(Rectangle(color=GREEN).surround(group[second], stretch=True)),
                  Create(Rectangle(color=GREEN).surround(group[first], stretch=True)))


class Scene5(MyScene):
    def construct(self):
        def create_birthday(id, day):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            return ImageAndText("other_chars/other_char (" + str(id) + ")",
                                content=date.strftime('%Y-%m-%d'),
                                text_buff=-0.1,
                                text_size=20)

        random.seed(7)
        first = 25
        second = 11
        list_id = [random.randint(1, 45) for _ in range(32)]
        list_day = random.sample(range(1, 366), 32)
        list_day[second] = list_day[first]

        group = Group(*[create_birthday(i, j) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 8).scale(
            0.75).shift(UP * 0.7)
        brace = Brace(group, DOWN)
        text = Text("Lớp E", font_size=50, font="Sans").next_to(group, DOWN)
        self.add(group, text)
        self.wait()
        self.play(Wiggle(group[first]), Wiggle(group[second]))
        group[second][1].set_color(GREEN), group[first][1].set_color(GREEN)
        self.play(Circumscribe(group[second][1]), Circumscribe(group[first][1]),
                  Create(Rectangle(color=GREEN).surround(group[second], stretch=True)),
                  Create(Rectangle(color=GREEN).surround(group[first], stretch=True)))


class Scene6(MyScene):
    def construct(self):
        problem1 = Text("Một lớp học có 35 bạn.", font="Sans", font_size=40, color=GREEN).shift(UP)
        problem2 = Text("Hãy tính xác xuất để ít nhất 2 bạn có cùng ngày sinh.", font="Sans", font_size=40,
                        color=YELLOW).shift(DOWN)
        self.my_play(Write(problem1))
        self.my_play(Write(problem2))


class Scene7(MyScene):
    def construct(self):
        khac = Text("Xác xuất\nkhác ngày sinh", font="Sans", font_size=48, color=RED)
        cung = Text("Xác xuất\ntrùng ngày sinh", font="Sans", font_size=48, color=GREEN)
        m1 = MathTex(r"100\%").scale(2).to_edge(LEFT)
        m2 = MathTex("-").scale(2).next_to(m1, RIGHT)
        khac.next_to(m2, RIGHT)
        m3 = MathTex("=").scale(2).next_to(khac, RIGHT)
        cung.next_to(m3, RIGHT)
        for i in (khac, VGroup(m1, m2), VGroup(m3, cung)):
            self.play(FadeIn(i, shift=UP))


