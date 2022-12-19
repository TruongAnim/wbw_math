from manim import *

list_scene = ("Scene0", "Scene1", "Scene2", "Scene3")
SCENE_NAME = list_scene[0]
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
        sqrt1 = MathTex("\sqrt{2}", r"\times", "\sqrt{2}", "=", "2")
        sqrt2 = MathTex("x", r"\times", "x", "=", "2")
        sqrt3 = MathTex("x", "=", "{2", "\over", "x}")
        group = VGroup(sqrt1, sqrt2, sqrt3).set_color(YELLOW).scale(3)

        table = MathTable(
            [[r"\text{Lần 1}", "1.5", "1.333333"],
             [r"\text{Lần 2}", "1.416667", "1.411764"],
             [r"\text{Lần 3}", "1.414216", "1.414211"],
             [r"\text{Lần 4}", "1.414214", "1.414213"],
             [r"\text{Lần 5}", "1.4142135", "1.4142135"]],
            col_labels=[Text("Thử", font="Sans", font_size=35), MathTex("x"), MathTex("2", "\over", "x")],
            include_outer_lines=True,
            element_to_mobject_config={"tex_template": myTemplate}).to_corner(UL).shift(UP * 0.4)
        # self.add(sqrt1, sqrt2, sqrt3)
        self.my_play(Write(sqrt1))
        self.my_play(ReplacementTransform(sqrt1, sqrt2))
        self.my_play(ReplacementTransform(sqrt2[0], sqrt3[0]),
                     ReplacementTransform(sqrt2[1], sqrt3[3]),
                     ReplacementTransform(sqrt2[2], sqrt3[4]),
                     ReplacementTransform(sqrt2[3], sqrt3[1]),
                     ReplacementTransform(sqrt2[4], sqrt3[2]))
        labels = table.get_col_labels()
        labels.set_color(YELLOW)
        entries = table.get_entries_without_labels()
        self.play(Transform(sqrt3[0], labels[1]),
                  Transform(sqrt3[2:], labels[2]),
                  FadeOut(sqrt3[1]))
        self.play(Create(table.get_vertical_lines()),
                  Create(table.get_horizontal_lines()),
                  Write(labels[0]))

        self.play(FadeIn(entries[0], shift=UP), run_time=0.5)
        self.play(FadeIn(entries[1], shift=UP), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(entries[2], shift=UP), run_time=0.5)
        tb = MathTex("{(", "1.5", "+", "1.333333", ")", "\over", "2}").next_to(entries[2], RIGHT, buff=1.5)
        tb2 = MathTex("=", "1.416667").next_to(entries[5], RIGHT, buff=1.5)
        self.play(ReplacementTransform(entries[1].copy(), tb[1]),
                  ReplacementTransform(entries[2].copy(), tb[3]))
        self.play(LaggedStart(*[FadeIn(tb[i]) for i in (0, 2, 4, 5, 6)]))
        self.play(Write(tb2))
        self.play(FadeIn(entries[3], shift=UP))
        self.play(Transform(tb2[-1], entries[4]), FadeOut(tb), FadeOut(tb2[0]))
        self.play(FadeIn(entries[5], shift=UP))

        self.play(FadeIn(entries[6], shift=UP))
        self.play(Transform(entries[4].copy(), entries[7]),
                  Transform(entries[5].copy(), entries[7]))
        self.play(FadeIn(entries[8], shift=UP))

        self.play(FadeIn(entries[9], shift=UP))
        self.play(Transform(entries[7].copy(), entries[10]),
                  Transform(entries[8].copy(), entries[10]))
        self.play(FadeIn(entries[11], shift=UP))

        self.play(FadeIn(entries[12], shift=UP))
        self.play(Transform(entries[10].copy(), entries[13]),
                  Transform(entries[11].copy(), entries[13]))
        self.play(FadeIn(entries[14], shift=UP))
        table.add_highlighted_cell((6, 2), color=GREEN)
        table.add_highlighted_cell((6, 3), color=GREEN)
        self.add(table)
        sqrt4 = MathTex("\Leftarrow \sqrt{2}", color=YELLOW).scale(1.5).next_to(entries[14], RIGHT, buff=1)
        self.play(FadeIn(sqrt4, shift=LEFT))
