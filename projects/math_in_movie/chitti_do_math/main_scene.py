from manim import *
from common.utils.color_utils import HSL

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Thumbnail")
# SCENE_NAME = list_scene[5]
SCENE_NAME = " ".join(list_scene[:5])
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"

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


class Scene0(Scene):
    def construct(self):
        formula = MathTex(r"""F(n) :=\left\{\begin{matrix}
        0\\ 
        1\\ 
        F(n-1)+F(n-2)
        \end{matrix}\right.""")
        condition0 = MathTex(r"\text{khi }n=0;")
        condition1 = MathTex(r"\text{khi }n=1;")
        condition2 = MathTex(r"\text{khi }n>1;")
        condition_group = VGroup(condition0, condition1, condition2).arrange(DOWN).next_to(formula, RIGHT)
        fibo = VGroup(formula, condition_group).shift(LEFT * 2 + UP * 2)
        list_fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        def create_square(number):
            square = Square(side_length=1)
            text = MathTex(str(number)).move_to(square)
            return VGroup(square, text)

        fibo_square = VGroup(*[create_square(i) for i in list_fibo]).arrange(RIGHT).shift(DOWN)
        list_F = VGroup(
            *[MathTex("F({0})".format(i)).scale(0.7).next_to(fibo_square[i], DOWN) for i in range(len(fibo_square))])
        for i in range(len(fibo_square)):
            fibo_square[i].set_color(HSL(i / len(fibo_square) / 2))
            list_F[i].set_color(HSL(i / len(fibo_square) / 2))

        self.play(Write(formula[0][0:9]))
        self.play(Write(formula[0][9]), Write(condition0))
        self.play(Write(formula[0][10]), Write(condition1))
        self.play(Write(formula[0][11:]), Write(condition2))

        self.play(Create(fibo_square[0]), Create(fibo_square[1]), Write(list_F[0]), Write(list_F[1]))
        for i in range(2, len(fibo_square)):
            self.play(Create(fibo_square[i][0]), Write(list_F[i]))
            self.play(Transform(fibo_square[i - 2][1].copy(), fibo_square[i][1], path_arc=-PI),
                      Transform(fibo_square[i - 1][1].copy(), fibo_square[i][1], path_arc=-PI))
        # self.add(fibo, fibo_square, list_F)


class Scene1(Scene):
    def construct(self):
        def get_fibo_list(n):
            a = [0, 1]
            for i in range(n - 2):
                a.append(a[-1] + a[-2])
            return a

        def get_F(i, number):
            f = MathTex("F({0}):".format(i))
            n = Integer(number, num_decimal_places=0).next_to(f, RIGHT, buff=SMALL_BUFF)
            return VGroup(f, n)

        list_fibo = get_fibo_list(51)
        fibo = VGroup(*[get_F(i, list_fibo[i]) for i in range(1, 51)]).arrange_in_grid(10, 5, flow_order="dr")
        fibo.scale(0.8).shift(LEFT*1.7)
        for i in range(len(fibo)):
            fibo[i].set_color(HSL(i / len(fibo)-0.5))
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in fibo], lag_ratio=0.1))
        self.play(Circumscribe(fibo[36]))


class Scene2(Scene):
    def construct(self):
        vertical_line = Line(UP * 3, DOWN * 3)
        horizontal_line = Line(UP * 2 + LEFT * 4, UP * 2 + RIGHT * 4)
        prime_vn = Text("Số nguyên tố", font_size=35, font="Sans")
        prime_en = Text("(Prime number)", font_size=30)
        prime = VGroup(prime_vn, prime_en).arrange(DOWN).shift(LEFT*2+UP*2.8)
        composite_vn = Text("Hợp số", font_size=35, font="Sans")
        composite_en = Text("(Composite number)", font_size=30)
        composite = VGroup(composite_vn, composite_en).arrange(DOWN).shift(RIGHT*2+UP*2.8)
        prime_con1 = MarkupText('<span foreground="red">Không thể </span>viết thành\ntích của 2 số tự nhiên\nnhỏ hơn', font="Sans", font_size=32)
        prime_example = Text("Ví dụ: 2, 3, 5, 7, ...", font="Sans", font_size=35)
        composite_con1 = MarkupText('<span foreground="green">Có thể </span>viết thành\ntích của 2 số tự nhiên\nnhỏ hơn', font="Sans", font_size=32)
        composite_example = Text("Ví dụ: 4, 6, 8, 9, ...", font="Sans", font_size=35)
        prime_state = VGroup(prime_con1, prime_example).arrange(DOWN, buff=LARGE_BUFF).shift(LEFT*3)
        composite_state = VGroup(composite_con1, composite_example).arrange(DOWN, buff=LARGE_BUFF).shift(RIGHT*3)

        self.play(Write(prime), Write(composite), Create(vertical_line), Create(horizontal_line))
        self.play(Write(prime_con1))
        self.play(Write(composite_con1))
        self.play(Write(prime_example))
        self.play(Write(composite_example))
        # self.add(vertical_line, horizontal_line, prime, composite, prime_state, composite_state)


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")


class Scene3(Scene):
    def construct(self):
        prime = MathTex(r"\text{Số nguyên tố: }M_{44}", tex_template=myTemplate).shift(UP)
        prime1 = MathTex(r"2^{32,582,657}-1", "=", "124575026015...154053967871").shift(DOWN)
        brace = Brace(prime1[2], DOWN)
        brace_t = MathTex(r"9,808,358\text{ chữ số}", color=YELLOW, tex_template=myTemplate).move_to(brace.get_tex("a"))
        self.play(Write(prime))
        self.play(Write(prime1))
        self.wait()
        self.play(Write(brace), Write(brace_t))
        # self.add(prime, prime1, brace, brace_t)


class Scene4(Scene):
    def construct(self):
        chitti = ImageMobject("chitti").to_corner(DL, buff=0)
        chat = SVGMobject("conversation", color=WHITE).scale(2).next_to(chitti, UR, buff=-1.5)
        prime = Text("Số nguyên tố\nlớn nhất là", font_size=32, font="Sans")
        prime1 = MathTex(r"2^{32,582,657}-1").scale(1.2).next_to(prime, DOWN)
        group = VGroup(prime1, prime).move_to(chat).shift(UP*0.5)
        joker = ImageMobject("joker").scale(0.6)
        prime2 = MathTex("2^{43,112,609}-1", color=YELLOW).scale(1.4).move_to(joker)
        group = Group(joker, prime2).to_corner(DR, buff=0)
        self.play(FadeIn(chitti, shift=RIGHT))
        self.play(FadeIn(chat), Write(prime))
        self.play(Write(prime1))
        self.wait()
        self.play(FadeIn(group, shift=LEFT), rate_func=linear)
        self.wait()


class Scene5(Scene):
    def construct(self):
        for1 = MathTex("2^{57885161}-1", color=YELLOW)
        for2 = MathTex("2^{74207281}-1", color=ORANGE)
        for3 = MathTex("2^{77232917}-1", color=RED)
        for4 = MathTex("2^{82589933}-1", color="#940d00")
        group = VGroup(for1, for2, for3, for4).scale(3).arrange(DOWN)
        self.add(group)


