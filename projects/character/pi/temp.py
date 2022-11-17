from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Temp"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Scene12", "Scene13", "Scene14", "Scene15")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[7]
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


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Temp_Scene0(Scene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).scale(1.5).to_corner(DL, buff=0)
        bubble_kwargs = {
            "stretch_width": 5,
            "stretch_height": 4,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Paragraph("Khi nào thì tìm được\nsố lớn nhất?",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.play(NumberCreatureSays(pi,
                                     wbw,
                                     target_mode="wonder",
                                     bubble_kwargs=bubble_kwargs
                                     )
                  )
        euclid = ImageMobject("euclid").to_corner(DR, buff=0)
        bubble = SVGMobject("Bubbles_speech", stroke_color=WHITE).flip(UP).scale(1.5).next_to(euclid, UL, buff=-0.5)
        never = Text("Không bao giờ", font_size=35, font="Sans", color=YELLOW).move_to(bubble).shift(UP * 0.3)

        self.play(FadeIn(euclid, shift=LEFT))
        self.play(FadeIn(bubble), Write(never))

        self.wait()


class Temp_Scene1(Scene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile2"
        ).scale(1.5).to_corner(DL)
        question = MarkupText("Số nguyên tố nào lớn nhất bạn biết\nmà đồng thời là số fibonacci?", font_size=40,
                        font="Sans").shift(UP*2)
        example = Text("Ví dụ: 5, 13, 89, v.v...", color=GREEN, font="Sans").next_to(question, DOWN)
        self.play(FadeIn(pi, shift=RIGHT))
        self.play(Write(question))
        self.play(Write(example))
        self.wait()


class Temp_Scene2(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).scale(1.5).to_corner(DR)
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=False
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4.5,
            "stretch_height": 3,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = MarkupText('Vậy thử làm câu này xem...', font="sans", font_size=25)
        text2 = MarkupText('Em được <span foreground="yellow">8 phẩy</span> toán', font="sans",
                           font_size=25)
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.my_play(
            NumberCreatureSays(
                pi2,
                text2,
                target_mode="plain",
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


class Temp_Scene3(MyScene):
    def construct(self):
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4.5,
            "stretch_height": 3,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text2 = MarkupText('Vậy làm sao để tính\nsố <span foreground="yellow">Pi</span> chính xác hơn?', font="sans",
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


class Temp_Scene4(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).scale(1).to_corner(DR)
        self.play(FadeIn(pi1, shift=LEFT * 2))

        def create_text(content):
            return Text(content, font_size=40, font="Sans", color=YELLOW)

        group = VGroup(*[create_text(i) for i in (
            "B1: Tìm một công thức toán học nào đó có số Pi",
            "B2: Rút Pi sang một vế",
            "B3: Tìm cách tính vế còn lại"
        )]).arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT).shift(LEFT)
        for i in group:
            self.my_play(Write(i))


class Temp_Scene5(MyScene):
    def construct(self):
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL)
        bubble_kwargs = {
            "stretch_width": 4.5,
            "stretch_height": 3,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text2 = MarkupText('Chắc gì đã đúng???', font="sans",
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


class Temp_Scene6(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).scale(1.5).to_corner(DL, buff=0)
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }

        euclid = ImageMobject("euclid").to_corner(DR, buff=0)
        bubble = SVGMobject("Bubbles_speech", stroke_color=WHITE).flip(UP).scale(2).next_to(euclid, UL, buff=-0.8)
        text = MarkupText('Tồn tại <span foreground="yellow">vô hạn</span>\nsố nguyên tố',
                        font="Sans",
                        font_size=40,
                        color=WHITE).move_to(bubble).shift(UP*0.5)
        wbw = Text("But why?", font_size=35, font="Sans").move_to(bubble).shift(UP * 0.3)
        l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        group = VGroup(*[Text(str(i), font="Sans", color=BLUE) for i in l[0:100]])
        group.arrange_in_grid(20,10).to_edge(UP)
        self.play(AnimationGroup(
            Write(group, run_time=3),
            AnimationGroup(
                FadeIn(euclid, shift=LEFT),
                Wait(0.5),
                FadeIn(bubble),
                Write(text),
                lag_ratio=1
            )
        ))
        self.wait()
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.play(NumberCreatureSays(pi,
                                     wbw,
                                     target_mode="wonder",
                                     bubble_kwargs=bubble_kwargs
                                     )
                  )
        self.wait()


class Temp_Scene7(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1"
        ).scale(1).to_corner(DL, buff=0)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 3.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        wbw = Paragraph("Mình nhất định\nsẽ tìm ra",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        font_size=35,
                        line_spacing=0.5)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait()
        self.play(NumberCreatureSays(pi,
                                     wbw,
                                     target_mode="smile1",
                                     bubble_kwargs=bubble_kwargs
                                     )
                  )

        root1 = MathTex("\sqrt{2}=", "{7 \over 5}", r"(\text{Sai số: }1 \% )", tex_template=myTemplate)
        root2 = MathTex("\sqrt{2}=", "{141 \over 100}", r"(\text{Sai số: }0.3 \% )", tex_template=myTemplate)
        root3 = MathTex("\sqrt{2}=", "{707 \over 500}", r"(\text{Sai số: }0.015 \% )", tex_template=myTemplate)
        root4 = MathTex("\sqrt{2}=", "{7071 \over 5000}", r"(\text{Sai số: }0.001 \% )", tex_template=myTemplate)
        root5 = MathTex("\sqrt{2}=", "{141421 \over 100000}", r"(\text{Sai số: }0.00025 \% )", tex_template=myTemplate)
        root6 = MathTex("\sqrt{2}=", "{35355339 \over 25000000}", r"(\text{Sai số: }0.0000001 \% )", tex_template=myTemplate)
        root_group = VGroup(root1, root2, root3, root4, root5, root6).arrange(DOWN, aligned_edge=LEFT)
        root_group.set_color_by_gradient(RED, YELLOW)
        root_group.to_edge(RIGHT)
        for i in root_group:
            self.play(FadeIn(i, shift=UP))
        euclid = ImageMobject("hippasus").scale(0.5).to_corner(DR, buff=0)
        bubble = SVGMobject("Bubbles_speech", stroke_color=WHITE).flip(UP).scale(1.7).next_to(euclid, UL, buff=-0.5)
        never = Paragraph("Bọn trẻ bây giờ\ncứng đầu thật",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        font_size=35,
                        line_spacing=0.5).move_to(bubble).shift(UP * 0.3)

        self.play(FadeIn(euclid, shift=LEFT))
        self.play(FadeIn(bubble), Write(never))

        self.wait()