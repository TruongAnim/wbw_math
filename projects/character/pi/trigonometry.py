from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Trigonometry"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Scene12", "Scene13", "Scene14", "Scene15")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[11]
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class MyScene(Scene):
    def setup(self):
        self.slice_stroke_color = RED
        self.slice_fill_color = TEAL,
        self.slice_fill_opacity = 0.5

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


class Trigonometry_Scene0(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Paragraph("Cái cây kia cao\n bao nhiêu mét nhỉ?",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.my_play(NumberCreatureThinks(pi,
                                          wbw,
                                          target_mode="wonder",
                                          bubble_kwargs=bubble_kwargs
                                          )
                     )
        self.wait()


class Trigonometry_Scene1(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain"
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        sin = MathTex("sin(60^\circ)=\sqrt{3}/2", color=RED).scale(1.8)
        wbw = Paragraph("Sách giáo khoa bảo thế.",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5).next_to(sin, DOWN)
        group = VGroup(sin, wbw)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.my_play(NumberCreatureSays(pi,
                                        group,
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs
                                        )
                     )
        self.wait()


class Trigonometry_Scene2(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True).to_corner(DR)
        computer = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "stretch_width": 4,
            "stretch_height": 1.5
        }

        self.my_play(NumberCreatureSays(pi,
                                        MathTex(r"sin(53.6^\circ)=???"),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.my_play(NumberCreatureSays(computer,
                                        MathTex(r"\text{Easy: } 0.80489"),
                                        target_mode="plain",
                                        bubble_kwargs=bubble_kwargs))
        self.wait()


class Trigonometry_Scene3(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1"
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = Text("Tưởng gì, dễ!", font="Sans")
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()

        self.my_play(
            NumberCreatureSays(
                pi,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )
        text2 = Text("À ừ nhỉ\ntính kiểu gì bây giờ?", font="Sans", font_size=30)
        self.my_play(
            NumberCreatureSays(pi,
                               text2,
                               target_mode="wonder",
                               use_fade_transform=True,
                               bubble_kwargs=bubble_kwargs
                               ))


class Trigonometry_Scene4(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR)
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = MarkupText('Chúng ta sẽ tìm hiểu\n   về <span foreground="yellow">lượng giác</span>', font="sans")
        text2 = MarkupText('<span foreground="yellow">sin cos</span> các thứ\nchắc khó lắm...', font="sans",
                           font_size=25)
        self.play(FadeIn(pi1, shift=LEFT * 2))
        self.my_play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.my_play(
            NumberCreatureThinks(
                pi2,
                text2,
                target_mode="wonder",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Trigonometry_Scene5(MyScene):
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{vntex}")

    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR)
        text1 = Text("sin cos tan là gì?", font="Sans", font_size=27)
        text2 = Text("Bảng giá trị lượng giác từ đâu ra?", font="Sans", font_size=27)
        text3 = MathTex(r"\text{Tại sao } sin(45^\circ)={\sqrt{2}\over{2}}?", tex_template=self.myTemplate)
        text4 = Text("Làm sao sử dụng sin cos trong tam giác không vuông?", font_size=27, font="Sans")
        text5 = MathTex(r"\text{Tại sao } sin^{2}a+cos^{2}a=1?", tex_template=self.myTemplate)
        text6 = Text("...", font_size=27, font="Sans")

        group = VGroup(text1, text2, text3, text4, text5, text6).arrange(DOWN, aligned_edge=LEFT).shift(UP)
        group.scale(1.2)
        self.play(FadeIn(pi, shift=LEFT * 2))
        for i in group:
            self.play(Write(i))
        self.wait()


class Trigonometry_Scene6(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Paragraph("Đây đâu phải tam giác vuông?",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.my_play(NumberCreatureThinks(pi,
                                          wbw,
                                          target_mode="wonder",
                                          bubble_kwargs=bubble_kwargs
                                          )
                     )
        self.wait()


class Trigonometry_Scene7(Scene):
    def construct(self):
        fomular = MathTex("sin(", "60^\circ", ")=", "{\sqrt{3}\over 2}", "?").scale(1.5)
        fomular[1].set_color(RED)
        fomular[3].set_color(YELLOW)
        why = Text("Tại sao", font="Sans", color=TEAL).next_to(fomular, UP, aligned_edge=LEFT)
        pi = NumberCreature(file_name_prefix="PiCreatures", mode="wonder", color=RED).scale(1.5).shift(LEFT * 4 + DOWN)
        self.add(fomular, why, pi)


class Trigonometry_Scene8(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            flip_at_start=True,
            mode="wonder"
        ).to_corner(DR)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 3,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Text("Đây đâu phải tam giác vuông?",
                   font="Sans",
                   color=YELLOW,
                   font_size=30)
        self.play(FadeIn(pi, shift=LEFT * 2))
        self.wait()
        self.my_play(NumberCreatureThinks(pi,
                                          wbw,
                                          target_mode="wonder",
                                          bubble_kwargs=bubble_kwargs
                                          )
                     )
        self.wait()


class Trigonometry_Scene9(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR)
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = MarkupText('Đó mới là <span foreground="yellow">khởi đầu</span>', font="sans")
        text2 = MarkupText('Đâu còn gì để học nữa?', font="sans",
                           font_size=25)
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.my_play(
            NumberCreatureSays(
                pi2,
                text2,
                target_mode="wonder",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.play(FadeIn(pi1, shift=LEFT * 2))
        self.my_play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Trigonometry_Scene10(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR)
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        fomular = MathTex("sin(x)={1 \over 2}", color=YELLOW).scale(1.5).shift(UP * 3)
        text0 = Text("Tìm x?", font="Sans", font_size=32, color=YELLOW).next_to(fomular, DOWN, aligned_edge=LEFT)
        text1 = MarkupText("Không đơn giản như thế", font="sans", font_size=28)
        text2 = MathTex(r'sin(\pi \backslash 6)=1 \backslash 2')
        text3 = Text("chứ có gì đâu?", font="Sans", font_size=27).next_to(text2, DOWN)
        self.play(Write(fomular), Write(text0))
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.wait()
        self.my_play(
            NumberCreatureSays(
                pi2,
                VGroup(text2, text3),
                target_mode="wonder",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.play(FadeIn(pi1, shift=LEFT * 2))
        self.my_play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Trigonometry_Scene11(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR).shift(DOWN * 0.5)
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL).shift(DOWN * 0.5)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        fomular = Group(*[ImageMobject(str(i)) for i in range(1, 4)]).arrange(DOWN, buff=0).shift(UP * 2.2)
        text0 = Text("Tìm x?", font="Sans", font_size=32, color=YELLOW).next_to(fomular, DOWN, aligned_edge=LEFT)
        text1 = MarkupText("Thử một ví dụ thực tế xem sao!", font="sans", font_size=28)
        text2 = Text("Khó thế này", font="Sans", font_size=27)
        text3 = Text("chắc mình không làm nổi", font="Sans", font_size=27).next_to(text2, DOWN)
        self.play(FadeIn(fomular, shift=UP))
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.wait()
        self.my_play(
            NumberCreatureSays(
                pi2,
                VGroup(text2, text3),
                target_mode="wonder",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.play(FadeIn(pi1, shift=LEFT * 2))
        self.my_play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Trigonometry_Scene12(MyScene):
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

    def setup(self):
        from datetime import datetime
        # self.now = datetime.now()
        self.nowhour = 12
        self.nowminute = 20
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
        self.dot = Dot(self.circle.get_center())
        self.number = [
            Text("{hour:.0f}".format(hour=12 if i == 0 else i / 5), color=YELLOW).scale(0.7).move_to(line.point_from_proportion(0.2))
            for i, line in enumerate(self.list_line) if i % 5 == 0]
        self.tick = [line.get_subcurve(0, 0.1) if i % 5 == 0 else line.get_subcurve(0, 0.03) for i, line in
                     enumerate(self.list_line)]
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number)

    def construct(self):
        self.clock.shift(UP * 2.3).scale(0.8)
        number = self.create_number().next_to(self.circle, DOWN)
        self.add(number)
        self.add(self.clock)
        self.remove(self.hour_hand, self.minute_hand)
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR).shift(DOWN * 0.5)
        pi2 = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            flip_at_start=False
        ).to_corner(DL).shift(DOWN * 0.5)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = Text("Vẽ kim phút chỉ số 4 đi...", font="sans", font_size=28)
        text2 = Text("Ủa, là sao???", font="Sans", font_size=28)
        text3 = Text('Cụ thể hơn được hem?', font="Sans", font_size=28).next_to(text2, DOWN)

        self.play(FadeIn(pi2, shift=RIGHT * 2), FadeIn(pi1, shift=LEFT * 2))
        self.wait()
        self.my_play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="plain",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.my_play(
            NumberCreatureSays(
                pi2,
                VGroup(text2, text3),
                target_mode="plain",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Trigonometry_Scene13(MyScene):
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

    def setup(self):
        from datetime import datetime
        # self.now = datetime.now()
        self.nowhour = 12
        self.nowminute = 20
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
        self.dot = Dot(self.circle.get_center())
        self.number = [
            Text("{hour:.0f}".format(hour=12 if i == 0 else i / 5)).scale(0.7).move_to(
                line.point_from_proportion(0.2))
            for i, line in enumerate(self.list_line) if i % 5 == 0]
        self.tick = [line.get_subcurve(0, 0.1) if i % 5 == 0 else line.get_subcurve(0, 0.03) for i, line in
                     enumerate(self.list_line)]
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number)

    def construct(self):
        self.clock.shift(UP * 2.3).scale(0.8)
        number = self.create_number().next_to(self.circle, DOWN)
        self.add(number)
        self.add(self.clock)
        self.remove(self.hour_hand, self.minute_hand)
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR).shift(DOWN * 0.5)
        pi2 = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            flip_at_start=False
        ).to_corner(DL).shift(DOWN * 0.5)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = Text("Okê bạn êiii!", font="sans", font_size=28)
        O_t = Text("O", font_size=25).next_to(self.dot, DL, buff=SMALL_BUFF)
        A = Dot(self.circle.point_from_proportion(1/3), color=YELLOW)
        A_t = Text("A", font_size=25, color=YELLOW).next_to(A, DR, buff=SMALL_BUFF)
        step1 = MarkupText('12:<span foreground="yellow">20</span>', font="sans")
        step2 = MarkupText('<span foreground="yellow">insert</span> quá trình\ntính toán các thứ', font="sans")
        step3 = MarkupText('Điểm <span foreground="yellow">A(0.87,-0.5)</span>', font="sans")
        step4 = MarkupText('Vẽ một mũi tên\ntừ <span foreground="yellow">O</span> đến <span foreground="yellow">A</span>', font="sans")
        step_group = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=1).scale(0.70).to_corner(UR)
        arrows = VGroup(*[Arrow(step_group[i].get_bottom(), step_group[i+1].get_top(), buff=0.05) for i in range(len(step_group)-1)])
        self.play(FadeIn(pi2, shift=RIGHT * 2), FadeIn(pi1, shift=LEFT * 2))
        self.wait()
        # self.play(Write(step_group))
        self.play((LaggedStart(*[Write(i) for i in (step1, arrows[0], step2, arrows[1])], lag_ratio=0.5)))
        self.play(*[Write(i) for i in (A, A_t, O_t, step3)])
        self.play(Write(arrows[2]), Write(step4))
        self.my_play(
            NumberCreatureSays(
                pi2,
                text1,
                target_mode="plain",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.play(GrowArrow(self.minute_hand))


class Trigonometry_Scene14(MyScene):
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
        self.dot = Dot(self.circle.get_center())
        self.number = [
            Text("{hour:.0f}".format(hour=12 if i == 0 else i / 5)).scale(0.7).move_to(
                line.point_from_proportion(0.2))
            for i, line in enumerate(self.list_line) if i % 5 == 0]
        self.tick = [line.get_subcurve(0, 0.1) if i % 5 == 0 else line.get_subcurve(0, 0.03) for i, line in
                     enumerate(self.list_line)]
        self.clock = VGroup(self.hour_hand, self.minute_hand, self.circle, self.dot, *self.tick, *self.number)

    def construct(self):
        self.clock.shift(UP * 2).scale(0.8)
        # number = self.create_number().next_to(self.circle, DOWN)
        # self.add(number)
        self.add(self.clock)
        self.remove(self.hour_hand, self.minute_hand)
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=True,
            color=BLUE
        ).to_corner(DR).shift(DOWN * 0.5)
        pi2 = NumberCreature(
            file_name_prefix="computer",
            mode="plain",
            flip_at_start=False
        ).to_corner(DL).shift(DOWN * 0.5)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = Text("Cái này dễ hơn", font="sans", font_size=28)
        O_t = Text("O", font_size=25).next_to(self.dot, DL, buff=SMALL_BUFF)
        A = Dot(self.circle.point_from_proportion(0), color=YELLOW)
        A_t = Text("A", font_size=25, color=YELLOW).next_to(A, UP, buff=SMALL_BUFF)
        step1 = MarkupText('12:<span foreground="yellow">20</span>', font="sans")
        step2 = MathTex(r"\alpha", "={2\pi \over 3}").scale(1.2)
        step3 = MarkupText("Vẽ mũi tên O->A", font="sans").scale(0.8)
        step4 = MarkupText("Quay mũi tên 1 góc ", font="sans").scale(0.8)
        step_group = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=1).scale(0.70).to_corner(UR).shift(LEFT)
        arrows = VGroup(*[Arrow(step_group[i].get_bottom(), step_group[i+1].get_top(), buff=0.05) for i in range(len(step_group)-1)])
        step41 = MathTex(r"-\alpha").next_to(step4, RIGHT, buff=SMALL_BUFF)
        step2[0].set_color(RED)
        step41.set_color(RED)
        self.play(FadeIn(pi2, shift=RIGHT * 2), FadeIn(pi1, shift=LEFT * 2))
        self.wait()
        # self.play(Write(step_group))
        self.play((LaggedStart(*[Write(i) for i in (step1, arrows[0], step2, arrows[1])], lag_ratio=0.5)))
        self.play(*[Write(i) for i in (A, A_t, O_t, step3)], Write(self.minute_hand))
        A_copy = A.copy()
        hand = self.minute_hand.copy()
        self.play(Write(arrows[2]), Write(step4), Write(step41),
                  Rotate(A_copy, -2*PI/3, about_point=self.dot.get_center()),
                  Rotate(A_t.copy(), -2*PI/3, about_point=self.dot.get_center()),
                  Rotate(hand, -2*PI/3, about_point=self.dot.get_center()),
                  self.minute_hand.animate.set_fill(opacity=0.5).set_stroke(opacity=0.5))
        angle = Angle(self.minute_hand, hand, other_angle=True, color=RED, radius=0.3)
        self.play(Create(angle),
                  step2[0].copy().animate.move_to(Angle(self.minute_hand, hand, other_angle=True, radius=0.5).point_from_proportion(0.5)))
        self.my_play(
            NumberCreatureSays(
                pi2,
                text1,
                target_mode="plain",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Trigonometry_Scene15(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).scale(1.5).to_corner(DR)
        bubble_kwargs = {
            "stretch_width": 6,
            "stretch_height": 4,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = MarkupText('Thank you <span foreground="yellow">so much!</span>', font="sans", font_size=40)

        self.play(FadeIn(pi1, shift=LEFT * 2))
        self.my_play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )