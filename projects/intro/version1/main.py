from manim import *
from common.svg.character.number_creature import NumberCreature
from common.svg.character.number_creature_anim import *

list_scene = ("Intro", "TestPi", "Outro", "Logo", "Background", "ColorName")
SCENE_NAME = list_scene[-1]
CONFIG_DIR = "../../../configs/"
CONFIG = "production.cfg"
config.background_color = BLACK

if __name__ == "__main__":
    command = f"manim -t -c {CONFIG_DIR}{CONFIG} {__file__} {SCENE_NAME}"
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
        pi = NumberCreature(file_name_prefix="PiCreatures", mode="wonder")\
            .scale(1.5).align_to(circle, DOWN)
        pi.shift(3 * LEFT)
        truong_anim = Text("@TruongAnim", font_size=25).shift(DOWN * 2.5)
        logo = VGroup(triangle, square, circle, pi)  # order matters
        logo.move_to(ORIGIN)
        bubble_kwargs = {
            "stroke_width":2,
            "stretch_width":3,
            "stretch_height":2,
            "stroke_color":WHITE,
        }
        creature_thinks = NumberCreatureThinks(pi,
                                       Text("Wait... But why?"),
                                       target_mode="wonder",
                                       bubble_kwargs=bubble_kwargs
                                       )
        self.play(SpiralIn(logo), FadeIn(truong_anim, shift=UP),
                  run_time=2, )

        self.play(creature_thinks,
                  ApplyWave(truong_anim),
                  Blink(pi),
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

        truong_anim = Text("@TruongAnim", font_size=25).shift(DOWN * 2.5+ LEFT*4)
        logo = VGroup(triangle, square, circle)  # order matters
        logo.move_to(ORIGIN).shift(LEFT*4)
        self.add(logo, truong_anim)
        self.wait()
        these_videos = MarkupText(f'''These videos are always <span fgcolor="{YELLOW}">free!</span>''')
        if_you_like = MarkupText(f'''If you <span fgcolor="{YELLOW}">like</span> what I do''')
        please_consider = MarkupText(f'''Please consider <span fgcolor="{YELLOW}">subscribing</span>''')
        subcribe = VGroup(these_videos, if_you_like, please_consider)\
            .arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT).scale(0.7).shift(RIGHT*3+UP)
        pi = NumberCreature(file_name_prefix="PiCreatures", color=BLUE, mode="smile1") \
            .align_to(subcribe, LEFT)
        pi.shift(3 * DOWN)
        pi.generate_target().scale(1.2).shift(0.2*UP)
        pi.target.change_mode("smile2")
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
        self.play(FadeIn(pi), FadeIn(rec), FadeIn(sub), ApplyWave(truong_anim))
        self.play(Blink(pi))
        self.play(MoveToTarget(pi), run_time=0.5)
        self.add_sound("click_sub.wav")
        # self.play(MoveToTarget(rec), FadeTransform(sub, sub), run_time=0.5)
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
        pi = NumberCreature(file_name_prefix="PiCreatures", mode="wonder")\
            .scale(1.5).align_to(circle, DOWN)
        pi.shift(3 * LEFT + DOWN*0.5).scale(0.6)
        wbw = MarkupText("Wait, but why?", gradient=(GREEN, BLUE), font_size=30).shift(UP*0.5)
        truong_anim = MarkupText("@TruongAnim", gradient=(BLUE, GREEN), font_size=30)
        truong_anim.next_to(wbw, DOWN)
        logo = VGroup(triangle, square, circle)  # order matters
        logo.move_to(ORIGIN).shift(RIGHT*3).scale(0.6)
        bubble_kwargs = {
            "stroke_width":2,
            "stretch_width":3,
            "stretch_height":2,
            "stroke_color":WHITE,
        }
        creature_thinks = NumberCreatureThinks(pi,
                                       Text("Wait... But why?"),
                                       target_mode="wonder",
                                       bubble_kwargs=bubble_kwargs
                                       )
        self.add(logo, pi)
        self.add(wbw, truong_anim)


class ColorName(Scene):
    def construct(self):
        truong_anim = MarkupText("@TruongAnim", font="Sans", font_size=35, gradient=(BLUE, GREEN))
        self.add(truong_anim)