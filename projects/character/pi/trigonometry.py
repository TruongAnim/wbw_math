from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Trigonometry"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[6]
CONFIG_DIR = "../../../configs/"
CONFIG = "develop.cfg"

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
