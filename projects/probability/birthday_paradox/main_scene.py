from manim import *

import datetime
import random
from common.custom.custom_mobject import ImageAndText
from common.custom.custom_mobject import ImageAndMathTex

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6",
              "Scene7", "Scene8", "Scene9", "Scene10", "Scene11", "Scene12", "Thumbnail")
SCENE_NAME = list_scene[-1]
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


class Thumbnail(MyScene):
    def construct(self):
        char1 = ImageMobject("chars/char (1)").scale(1.5).to_corner(UR, buff=SMALL_BUFF)
        char2 = ImageMobject("chars/char (2)").scale(1.5).to_corner(UL, buff=SMALL_BUFF)
        arrow = DoubleArrow(char1.get_left(), char2.get_right(), stroke_width=10, color=RED)
        probability = Text("Xác suất", font_size=70, font="Sans", color=RED).shift(UP)
        same_class = Text("Cùng lớp", font_size=80, font="Sans", color=GREEN).shift(DOWN)
        same_birthday = Text("Cùng ngày sinh", font_size=80, font="Sans", color=YELLOW).next_to(same_class, DOWN)
        self.add(char1, char2, arrow, same_class, same_birthday, probability)


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
            self.my_play(FadeIn(i, shift=UP))


class Scene8(MyScene):
    def construct(self):
        def create_avatar(id, frac):
            tex = str(frac)+r"\over 365"
            return ImageAndMathTex("chars/char ("+str(id)+")", content=tex, tex_color=YELLOW)
        text = Text("Xác xuất 35 bạn có ngày sinh khác nhau:", font="Sans", font_size=35, color=RED).to_corner(UL)
        text2 = Text("Xác xuất xuất hiện trùng ngày sinh:", font="Sans", font_size=40, color=GREEN).shift(DOWN*2).to_corner(LEFT)
        group = Group(create_avatar(5, 365),
                      create_avatar(2, 364),
                      create_avatar(3, 363),
                      create_avatar(4, 362))
        group.add(Text("......."))
        group.add(create_avatar(1, 331))
        group.arrange(RIGHT, buff=SMALL_BUFF)
        group.shift(UP+LEFT*1.2)
        times = VGroup(*[MathTex(r"\times").scale(2).next_to(group[i][1], RIGHT, buff=0.5)
                         for i in range(4)])
        dots = MathTex(r"...\times").scale(2).next_to(times, RIGHT)
        times.add(dots)
        result = MathTex("=", "18.56\%").scale(1.4).next_to(group[-1][1], RIGHT)
        result[1].set_color(RED)
        result2 = MathTex("100\%", "-", "18.56\%", "=", "81.44\%").scale(1.4)
        result2[2].set_color(RED)
        result2[-1].set_color(GREEN)
        result2.next_to(text2, DOWN)
        # self.add(text, group, times, result, text2, result2)
        self.my_play(Write(text))
        for i in group:
            self.my_play(FadeIn(i, shift=UP))
        self.my_play(LaggedStart(*[FadeIn(i, shift=UP) for i in times], lag_ratio=0.2))
        self.my_play(FadeIn(result))
        self.my_play(Write(text2))
        self.my_play(FadeIn(result2[:2], shift=UP))
        self.my_play(Transform(result[-1].copy(), result2[2]))
        self.my_play(FadeIn(result2[3:], shift=UP))


class Scene9(MyScene):
    def construct(self):
        text1 = Text("Xác xuất để ai đó trùng ngày sinh VỚI BẠN", font="Sans", font_size=40, color=RED).shift(UP*2)
        explain1 = Text("(Hiếm khi sảy ra)", font="Sans", font_size=30, color=RED).next_to(text1, DOWN)
        text2 = Text("Xác xuất tồn tại 2 bạn bất kì trùng ngày sinh với nhau", font="Sans", font_size=40, color=GREEN).shift(DOWN)
        explain2 = Text("(Xảy ra thường xuyên)", font="Sans", font_size=30, color=GREEN).next_to(text2, DOWN)
        diff = MathTex(r"\neq ").scale(2.5)
        final = Text("(Lớp 23 bạn thì xác xuất đã trên 50%)", font="Sans", font_size=30, color=GREEN).next_to(explain2, DOWN)
        # self.add(text1, text2, explain1, explain2, diff, final)
        self.my_play(FadeIn(text1, shift=UP))
        self.my_play(FadeIn(explain1, shift=UP))
        self.my_play(FadeIn(diff, shift=UP))
        self.my_play(FadeIn(text2, shift=UP))
        self.my_play(FadeIn(explain2, shift=UP))
        self.my_play(FadeIn(final, shift=UP))


class Scene10(MyScene):
    def construct(self):
        def create_birthday(id, day, is_select=False):
            date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y')
            date = date + datetime.timedelta(days=day)
            if not is_select:
                return ImageAndText("other_chars/other_char (" + str(id) + ")",
                                    content=date.strftime('%Y-%m-%d'),
                                    text_buff=-0.1,
                                    text_size=20)
            else:
                id = random.randint(1, 10)
                image = ImageAndText("chars/char (" + str(id) + ")",
                             content=date.strftime('%Y-%m-%d'),
                             text_buff=-0.1,
                             text_size=20,
                             color=GREEN)
                return Group(Rectangle(color=GREEN, fill_color=GREEN, fill_opacity=0.5).surround(image, stretch=True), image)

        random.seed(2)

        def create_match():
            first = random.randint(0, 34)
            second = random.randint(0, 34)
            list_id = [random.randint(1, 45) for _ in range(35)]
            list_day = random.sample(range(1, 366), 35)
            list_day[second] = list_day[first]
            group = Group(*[create_birthday(i, j, True) if j == list_day[first] or j == list_day[second] else create_birthday(i, j, False) for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 9).scale(
                0.65).shift(UP * 1)
            return group

        def create_not_match():
            list_id = [random.randint(1, 45) for _ in range(35)]
            list_day = random.sample(range(1, 366), 35)
            group = Group(*[
                create_birthday(i, j, False)
                for i, j in zip(list_id, list_day)]).arrange_in_grid(4, 9).scale(
                0.65).shift(UP * 1)
            return group

        match_list = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
        match_list2 = [1, 1, 0, 1, 1]
        group = create_match()
        total = 1
        trung = 1
        tt = Text("Số lớp mô phỏng: "+str(total), font="Sans", font_size=35).to_corner(DL).shift(UP*0.5)
        t = Text("Số lớp trùng ngày sinh: "+str(trung), font="Sans", font_size=35).to_corner(DL).shift(DOWN*0.2)
        self.play(FadeIn(group, shift=LEFT), FadeIn(tt, shift=LEFT), FadeIn(t, shift=LEFT))
        for i in match_list:
            total = total+1
            new_group = create_match()
            if i == 0:
                new_group = create_not_match()
            else:
                trung = trung + 1

            self.play(FadeOut(group, shift=LEFT), FadeIn(new_group, shift=LEFT),
                      Transform(tt, Text("Số lớp mô phỏng: "+str(total), font="Sans", font_size=35).to_corner(DL).shift(UP*0.5)),
                      Transform(t, Text("Số lớp trùng ngày sinh: "+str(trung), font="Sans", font_size=35).to_corner(DL).shift(DOWN*0.2)))
            group = new_group
        trung = 814000
        total = 999995
        for i in match_list2:
            total = total+1
            new_group = create_match()
            if i == 0:
                new_group = create_not_match()
            else:
                trung = trung + 1

            self.play(FadeOut(group, shift=LEFT), FadeIn(new_group, shift=LEFT),
                      Transform(tt, Text("Số lớp mô phỏng: "+str(total), font="Sans", font_size=35).to_corner(DL).shift(UP*0.5)),
                      Transform(t, Text("Số lớp trùng ngày sinh: "+str(trung), font="Sans", font_size=35).to_corner(DL).shift(DOWN*0.2)))
            group = new_group

        # self.add(create_not_match())


class Scene11(MyScene):
    def construct(self):
        table = Table(
            [["25", "56.8%"],
             ["35", "81.44%"],
             ["45", "94.1%"]],
            col_labels=[Text("Sĩ số", font="Sans"),
                        Text("Xác xuất trùng ngày sinh", font="Sans")],
            include_outer_lines=True).set_row_colors(GREEN, YELLOW, ORANGE, RED)
        self.play(Create(table), run_time=3)
        self.wait()


class Scene12(MyScene):
    def construct(self):
        text1 = Text("Trong 1 lớp có 20 bạn nữ", font="Sans", font_size=40, color=GREEN)
        text2 = Text("Tính xác xuất để ít nhất 1 bạn nữ\n       trùng ngày sinh với bạn.",
                     font="Sans", font_size=40, color=YELLOW)
        group = VGroup(text1, text2).arrange(DOWN).to_edge(DOWN)
        self.play(Write(group))