from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *

PROJECT_NAME = "Temp"
list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5",
              "Scene6", "Scene7", "Scene8", "Scene9", "Scene10", "Scene11",
              "Scene12", "Scene13", "Scene14", "Scene15")
SCENE_NAME = PROJECT_NAME + "_" + list_scene[12]
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
        self.wait(0.5)


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
                              font="Sans").shift(UP * 2)
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
                          color=WHITE).move_to(bubble).shift(UP * 0.5)
        wbw = Text("But why?", font_size=35, font="Sans").move_to(bubble).shift(UP * 0.3)
        l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
             227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
             349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
             467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
             613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
             751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
             887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        group = VGroup(*[Text(str(i), font="Sans", color=BLUE) for i in l[0:100]])
        group.arrange_in_grid(20, 10).to_edge(UP)
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
        root6 = MathTex("\sqrt{2}=", "{35355339 \over 25000000}", r"(\text{Sai số: }0.0000001 \% )",
                        tex_template=myTemplate)
        root_group = VGroup(root1, root2, root3, root4, root5, root6).arrange(DOWN, aligned_edge=LEFT)
        root_group.set_color_by_gradient(RED, YELLOW)
        root_group.to_edge(RIGHT)
        for i in root_group:
            self.play(FadeIn(i, shift=UP))
        euclid = ImageMobject("hippasus").scale(0.5).to_corner(DR, buff=0)
        bubble = SVGMobject("Bubbles_speech", stroke_color=WHITE).flip(UP).scale(1.7).next_to(euclid, UL, buff=-0.5)
        never = Paragraph("Bọn trẻ bây giờ\ncố chấp thật",
                          font="Sans",
                          color=YELLOW,
                          alignment="center",
                          font_size=35,
                          line_spacing=0.5).move_to(bubble).shift(UP * 0.3)
        self.wait()
        self.play(FadeIn(euclid, shift=LEFT))
        self.play(FadeIn(bubble), Write(never))

        self.wait()


class Temp_Scene8(MyScene):
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
        text2 = MarkupText('Tại sao lại trùng\nnhiều như vậy?', font="sans",
                           font_size=35)
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.my_play(
            NumberCreatureSays(
                pi2,
                text2,
                target_mode="wonder",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Temp_Scene9(MyScene):
    def construct(self):
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder",
            flip_at_start=False
        ).to_corner(DL, buff=SMALL_BUFF)
        bubble_kwargs = {
            "stretch_width": 6,
            "stretch_height": 3.5,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = MathTex(r"\text{Thua}", r"\rightarrow", r"\text{Gấp đôi}", tex_template=myTemplate).scale(3).to_edge(UP)
        text1[0].set_color(RED)
        text1[2].set_color(GREEN)
        text2 = MarkupText('Liệu có thành công?', font="Sans",
                           font_size=100, color=TEAL)
        text3 = MarkupText('1,000,000\n     ván', font="Sans",
                           font_size=80, color=YELLOW).to_edge(RIGHT)
        self.add(text1, text3)
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.my_play(
            NumberCreatureSays(
                pi2,
                text2,
                target_mode="wonder",
                bubble_kwargs=bubble_kwargs,
            )
        )


class Temp_Scene10(MyScene):
    def construct(self):
        pi1 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="smile1",
            flip_at_start=True,
            color=BLUE
        ).scale(1).to_corner(DR, buff=0)
        pi2 = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="plain",
            flip_at_start=False
        ).to_corner(DL, buff=0)
        bubble_kwargs = {
            "stretch_width": 3,
            "stretch_height": 2,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text1 = MarkupText('Đừng vội!', font="sans", font_size=30)
        text2 = MarkupText('<span foreground="yellow">Okê. </span>Hiểu rồi!', font="sans",
                           font_size=30)
        r = ImageMobject("r").to_corner(UL, buff=SMALL_BUFF)
        result = MathTex("n(\mathbb{N})=n(\mathbb{Z})=n(\mathbb{Q})", "=", "n(\mathbb{R})", color=YELLOW).next_to(r,
                                                                                                                  RIGHT)
        brace = Brace(result, DOWN)
        brace_t = MathTex("\infty", color=YELLOW).next_to(brace, DOWN)
        irra = MarkupText('Số thực', font="sans", font_size=40, color=RED).next_to(result, UP, buff=1.3)
        arrow1 = Arrow(irra.get_corner(DR), result[-1].get_top(), color=RED)
        arrow2 = Arrow(irra.get_left(), result[0].get_left() + LEFT * 3.5 + UP * 1.7, color=RED)
        smaller = MathTex("<", color=GREEN).scale(1.2).move_to(result[-2])
        # self.add(r, irra, arrow1, arrow2, result)

        self.play(FadeIn(r))
        self.play(Write(result))
        self.play(FadeIn(brace_t, shift=UP), FadeIn(brace, shift=UP))
        self.play(FadeIn(pi2, shift=RIGHT * 2))
        self.play(
            NumberCreatureSays(
                pi2,
                text2,
                target_mode="plain",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.play(FadeIn(pi1, shift=LEFT * 2))
        self.play(
            NumberCreatureSays(
                pi1,
                text1,
                target_mode="smile1",
                bubble_kwargs=bubble_kwargs,
            )
        )
        self.wait(0.5)
        self.play(Write(irra))
        self.my_play(GrowArrow(arrow1), GrowArrow(arrow2), result[-1].animate.set_color(RED))
        self.my_play(Transform(result[-2], smaller), result[-1].animate.scale(1.5).shift(RIGHT * 0.1))
        self.play(Flash(smaller))
        self.wait(0.5)


class Temp_Scene11(MyScene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix="PiCreatures",
            mode="wonder"
        ).scale(1).to_corner(DL, buff=0)
        bubble_kwargs = {
            "stretch_width": 4,
            "stretch_height": 3,
            "stroke_width": 2,
            "stroke_color": WHITE
        }

        wbw = Paragraph("Hay là ghép cặp\n   thế này?",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5)

        math_table = MathTable(
            [[0, "\pi"],
             [1, "\log_{2}3"],
             [2, "\sqrt{2}"],
             [3, "\mathrm{e}+\sqrt{3}"],
             [4, "0.567985..."],
             [5, "3.917564..."],
             [6, "1.241046..."],
             ["...", "..."]],
            v_buff=0.5,
            h_buff=0.5,
            include_outer_lines=True,
            col_labels=[MathTex("\mathbb{N}", color=GREEN), MathTex("\mathbb{R}", color=PINK)])
        data = math_table.get_entries_without_labels()
        for index, i in enumerate(data):
            if index % 2 == 0:
                i.set_color(GREEN)
            else:
                i.set_color(PINK)
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.wait(0.5)
        self.play(NumberCreatureSays(pi,
                                     wbw,
                                     target_mode="wonder",
                                     bubble_kwargs=bubble_kwargs
                                     ),
                  Write(math_table)
                  )
        name = Text("Cantor", font_size=35, color=BLUE).to_corner(DR, buff=0.2)
        euclid = ImageMobject("cantor").scale(0.6).to_corner(DR, buff=0)
        bubble = SVGMobject("Bubbles_speech", stroke_color=WHITE).flip(UP).scale(1.5).next_to(euclid, UL, buff=-0.7)
        never = Paragraph("Hehe, không bao\n giờ hết!",
                        font="Sans",
                        color=YELLOW,
                        alignment="center",
                        line_spacing=0.5).scale(0.7).move_to(bubble).shift(UP * 0.3)

        self.play(FadeIn(euclid, shift=LEFT), FadeIn(name, shift=LEFT))
        self.play(FadeIn(bubble), Write(never))
        self.wait()


class Temp_Scene12(MyScene):
    def construct(self):
        r = ImageMobject("r").shift(UP)
        result = MathTex("n(\mathbb{N})=n(\mathbb{Z})=n(\mathbb{Q})", "<", "n(\mathbb{R})", color=YELLOW).scale(1.5)\
            .next_to(r, DOWN)
        result[-1].set_color(RED)
        result[-2].set_color(RED)
        brace = Brace(result[0], DOWN)
        brace_t = MathTex("\infty", color=GREEN).scale(1.5).next_to(brace, DOWN)
        irra = MarkupText('Số thực', font="sans", font_size=40, color=RED).next_to(result, UP, buff=1.3)
        brace2 = Brace(result[-1], DOWN)
        brace_t2 = MathTex("\infty", color=GREEN_D).scale(2.5).next_to(brace2, DOWN)
        self.play(FadeIn(r))
        self.play(FadeIn(result[0], shift=UP))
        self.my_play(FadeIn(brace, shift=UP), FadeIn(brace_t, shift=UP))
        self.my_play(FadeIn(result[-1], shift=UP), FadeIn(brace_t2, shift=UP), FadeIn(brace2, shift=UP), FadeIn(result[-2]))


class Temp_Scene13(MyScene):
    def construct(self):
