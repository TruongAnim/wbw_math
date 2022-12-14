from manim import *
from common.svg.character.number_creature import NumberCreature
from common.svg.character.number_creature_anim import *

list_scene = ("Intro", "TestPi", "Outro", "Logo", "Background", "ColorName")
SCENE_NAME = list_scene[4]
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"
config.background_color = BLACK

if __name__ == "__main__":
    command = f"manim -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
    print("cmd[" + command + "]")
    os.system(command)


class Intro(Scene):
    def construct(self):
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        truong_anim = MarkupText("@TruongAnim", font_size=25, gradient=(BLUE, GREEN)).shift(DOWN * 3)
        logo = VGroup(triangle, square, circle)  # order matters
        logo.move_to(ORIGIN).shift(RIGHT*3+DOWN)
        sticker214 = ImageMobject("outfit1 (214)").scale(1.5).shift(LEFT*2).align_to(logo, DOWN)
        bubble = SVGMobject("Bubbles_thought", stroke_color=WHITE).stretch_to_fit_width(4).stretch_to_fit_height(2)\
            .next_to(sticker214, UR, buff=-1)
        wbw = Text("Wait... But why?", font_size=30, color=YELLOW).move_to(bubble).shift(UP*0.2)
        self.play(SpiralIn(logo),
                  FadeIn(truong_anim, shift=UP),
                  FadeIn(sticker214, shift=RIGHT),
                  run_time=2)

        self.play(ApplyWave(truong_anim),
                  FadeIn(bubble), Write(wbw),
                  run_time=2)
        self.wait()



class Outro(Scene):
    def construct(self):
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)

        truong_anim = MarkupText("@TruongAnim", font_size=25, gradient=(BLUE, GREEN)).shift(DOWN * 2.5+ LEFT*4)
        logo = VGroup(triangle, square, circle)  # order matters
        logo.move_to(ORIGIN).shift(LEFT*4)
        self.add(logo, truong_anim)
        self.wait()
        these_videos = MarkupText(f'''These videos are made with <span fgcolor="{YELLOW}">passion</span>''')
        if_you_like = MarkupText(f'''If you <span fgcolor="{YELLOW}">like</span> what I do''')
        please_consider = MarkupText(f'''Please consider <span fgcolor="{YELLOW}">subscribing</span>''')
        subcribe = VGroup(these_videos, if_you_like, please_consider)\
            .arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT).scale(0.7).shift(RIGHT*3+UP*2)
        pi = ImageMobject("outfit1 (244)")\
            .align_to(subcribe, LEFT).scale(1.5).shift(UP)
        pi.shift(3 * DOWN)
        sub = Text("SUBSCRIBE", font="Arial", weight=BOLD, font_size=27, color=WHITE)\
            .next_to(pi, RIGHT).shift(UP*1.7)
        rec = Rectangle(
            width=2.7, height=0.7,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=0
            ).move_to(sub)
        sub_ed = Text("SUBSCRIBED", font="Arial", weight=BOLD, font_size=27, color=DARK_GRAY)\
            .next_to(pi, RIGHT).shift(UP*1.7)
        rec.generate_target()
        rec.target.stretch_to_fit_width(3).move_to(sub_ed).set_color(WHITE)
        self.play(LaggedStart(*[
            FadeIn(i, shift=LEFT*5)
            for i in subcribe
        ], lag_ratio=0.5), run_time=2)
        self.wait(0.3)
        self.play(FadeIn(pi, shift=UP*2), FadeIn(rec), FadeIn(sub), ApplyWave(truong_anim))
        self.add_sound("click_sub.wav")
        self.play(MoveToTarget(rec), FadeTransform(sub, sub_ed), run_time=0.5)
        self.wait()


class TestPi(Scene):
    def construct(self):
        pi = NumberCreature(
            file_name_prefix='PiCreatures',
            flip_at_start=False,
            mode="wonder"
        ).shift(LEFT*3+DOWN)
        self.play(Create(pi))
        self.wait()
        self.play(Blink(pi),  run_time=1)
        self.wait()
        bubble_kwargs = {
            "fill_color":BLACK,
            "fill_opacity": 0.5,
            "stroke_width":3,
            "stroke_color":WHITE,
            "stretch_width": 7,
            "stretch_height":3
        }
        self.play(NumberCreatureSays(
            pi,
            Tex("hello!", color=BLUE),
            target_mode="wonder",
            bubble_kwargs=bubble_kwargs
        ))
        self.wait()


class Logo(Scene):
    def construct(self):
        pi = NumberCreature(file_name_prefix="PiCreatures", mode="wonder")
        pi.scale(3)
        self.add(pi)

class Background(Scene):
    def construct(self):
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        pi = ImageMobject("outfit1 (165)")
        pi.shift(3 * LEFT).scale(0.85)
        wbw = MarkupText("Wait, but why?", gradient=(GREEN, BLUE), font_size=30).shift(UP*0.5)
        truong_anim = MarkupText("@TruongAnim", gradient=(BLUE, GREEN), font_size=30)
        truong_anim.next_to(wbw, DOWN)
        logo = VGroup(triangle, square, circle)  # order matters
        logo.move_to(ORIGIN).shift(RIGHT*3).scale(0.6)
        self.add(logo, pi)
        self.add(wbw, truong_anim)


class ColorName(Scene):
    def construct(self):
        truong_anim = MarkupText("@TruongAnim", font="Sans", font_size=35, gradient=(BLUE, GREEN))
        self.add(truong_anim)