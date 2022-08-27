import math

from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *
from common.utils.mobject_utils import get_indexes

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6")
SCENE_NAME = list_scene[5]
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


class Scene1(MyScene):
    def construct(self):
        A = np.array([-1, 2, 0])
        B = np.array([-2, 0, 0])
        C = np.array([2, 0, 0])
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)

        triangle = VMobject().set_points_as_corners([A, B, C, A])
        self.add(triangle)
        brace1 = Brace(BC, DOWN)
        brace2 = Brace(AB, AB.copy().rotate(-PI / 2).get_unit_vector())
        brace3 = Brace(AC, AC.copy().rotate(PI / 2).get_unit_vector())
        text1 = brace1.get_tex("{:.2f}".format((BC.get_length())))
        text2 = brace2.get_tex("{:.2f}".format((AB.get_length())))
        text3 = brace3.get_tex("{:.2f}".format((AC.get_length())))

        area_text = Text("Area = ?", font_size=27).shift(LEFT * 0.5 + UP * 0.5)

        self.play(Create(triangle))
        fadein_map = (
            ((brace1, text1), (brace2, text2), (brace3, text3)),
            (UP, DR, DL)
        )
        self.play(*[
            FadeIn(i, shift=direction)
            for obj, direction in zip(fadein_map[0], fadein_map[1])
            for i in obj
        ])
        self.play(Write(area_text))

        pi = NumberCreature(mode="smile1", color=BLUE).to_corner(DL)
        bubble_kwargs = {
            "stretch_height": 1.6,
            "stroke_width": 2,
            "stroke_color": WHITE
        }
        text_heron = Text("Mình sẽ dùng heron",
                          font_size=20,
                          font="Times New Romance")
        self.play(FadeIn(pi, shift=RIGHT * 2))
        self.play(NumberCreatureSays(pi,
                                     text_heron,
                                     target_mode="smile1",
                                     bubble_kwargs=bubble_kwargs)
                  )

        pi2 = NumberCreature(mode="plain",
                             color=RED,
                             flip_at_start=True).to_corner(DR)
        self.play(FadeIn(pi2, shift=LEFT * 2))
        self.play(NumberCreatureSays(pi2,
                                     MarkupText("Đừng dùng heron\n"
                                                "Sai số lớn lắm",
                                                font_size=20,
                                                font="Times New Romance"),
                                     target_mode="plain",
                                     bubble_kwargs=bubble_kwargs)
                  )
        pi_wonder = NumberCreature(mode="wonder", color=BLUE).to_corner(DL)
        text_really = Text("Có thật không nhỉ?",
                           font_size=20,
                           font="Times New Romance").move_to(text_heron)
        self.play(FadeTransform(pi, pi_wonder), FadeTransform(text_heron, text_really))


class Scene2(MyScene):
    def construct(self):
        A = np.array([-1, 2, 0])
        B = np.array([-2, 0, 0])
        C = np.array([2, 0, 0])
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)

        triangle = VMobject().set_points_as_corners([A, B, C, A])
        self.add(triangle)
        brace1 = Brace(BC, DOWN)
        brace2 = Brace(AB, AB.copy().rotate(-PI / 2).get_unit_vector())
        brace3 = Brace(AC, AC.copy().rotate(PI / 2).get_unit_vector())
        text1 = brace1.get_tex("a", "=", "{:.2f}".format((BC.get_length())))
        text2 = brace2.get_tex("b", "=", "{:.2f}".format((AB.get_length())))
        text3 = brace3.get_tex("c", "=", "{:.2f}".format((AC.get_length())))
        color_map = {
            text1: RED,
            text2: GREEN,
            text3: BLUE
        }
        for i in color_map:
            i.set_color(color_map[i])

        self.play(Create(triangle))
        fadein_map = (
            ((brace1, text1), (brace2, text2), (brace3, text3)),
            (UP, DR, DL)
        )
        self.play(*[
            FadeIn(i, shift=direction)
            for obj, direction in zip(fadein_map[0], fadein_map[1])
            for i in obj
        ])

        s = MathTex(r"s", "={{", "a", "+", "b", "+", "c", r"}\over 2}",
                    "=", "4.925").shift(DOWN * 2 + LEFT * 2).scale(0.8)
        color_map_2 = {
            "a": RED,
            "b": GREEN,
            "c": BLUE,
            "s": PURPLE,
            "4.925": PURPLE,
            "sqrt": WHITE,
            "Area": WHITE,
            "4.01": YELLOW
        }
        s.set_color_by_tex_to_color_map(color_map_2)
        self.play(*[
            Write(s[i]) for i in (0, 1, 3, 5, 7)
        ])

        self.play(*[
            Transform(i, j) for i, j in zip(
                (text1[0].copy(), text2[0].copy(), text3[0].copy()),
                (s[2], s[4], s[6])
            )
        ])

        self.play(Write(s[8]), Write(s[9]))
        self.wait()
        area = MathTex(r"\text{Area}=", "\sqrt{", "s", "(", "s", "-", "a", ")(",
                       "s", "-", "b", ")(", "s", "-", "c", ")}", "=", "4.01").scale(0.8)
        area.set_color_by_tex_to_color_map(color_map_2)
        area.next_to(s, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        self.play(*[
            Write(area[i]) for i in (0, 1, 3, 5, 7, 9, 11, 13, 15)
        ])
        self.play(LaggedStart(*[
            Transform(i, area[j]) for i, j in zip(
                (text1[0].copy(),
                 text2[0].copy(),
                 text3[0].copy(),
                 s[0].copy(),
                 s[0].copy(),
                 s[0].copy(),
                 s[0].copy()),
                (6, 10, 14, 2, 4, 8, 12)
            )
        ], lag_ratio=0.2))
        triangle.set_style(fill_opacity=0.8, fill_color=YELLOW)
        self.play(*[
            Write(area[16]), Write(area[17]),
            Wiggle(triangle)
        ])


class Scene3(MyScene):
    def construct(self):
        shift = DOWN * 2 + LEFT * 3
        A = np.array([1, 3.5, 0]) + shift
        B = np.array([-2, 0, 0]) + shift
        C = np.array([2, 0, 0]) + shift
        H = np.array([1, 0, 0]) + shift
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        AH = Line(A, H, color=TEAL)
        len_a = BC.get_length()
        len_b = AB.get_length()
        len_c = AC.get_length()
        len_h = AH.get_length()
        a = "{:.4f}".format(len_a)
        b = "{:.4f}".format(len_b)
        c = "{:.4f}".format(len_c)
        h = "{:.4f}".format(len_h)
        ha2 = "{:.4f}".format(len_h * len_a / 2)
        s = (len_a + len_b + len_c) / 2
        heron = "{:.4f}".format(math.sqrt(s * (s - len_a) * (s - len_b) * (s - len_c)))

        triangle = VMobject().set_points_as_corners([A, B, C, A])
        self.add(triangle)
        brace1 = Brace(BC, DOWN)
        brace2 = Brace(AB, AB.copy().rotate(-PI / 2).get_unit_vector())
        brace3 = Brace(AC, AC.copy().rotate(PI / 2).get_unit_vector())
        text1 = MathTex("a", "=", a).scale(0.5)
        text2 = MathTex("b", "=", b).scale(0.5)
        text3 = MathTex("c", "=", c).scale(0.5)
        text4 = MathTex("h", "=", h).scale(0.5)
        brace1.put_at_tip(text1, buff=SMALL_BUFF)
        brace2.put_at_tip(text2, buff=SMALL_BUFF)
        brace3.put_at_tip(text3, buff=SMALL_BUFF)
        text4.next_to(AH, LEFT, buff=SMALL_BUFF)
        color_map = {
            text1: RED,
            text2: GREEN,
            text3: BLUE,
            text4: TEAL
        }
        for i in color_map:
            i.set_color(color_map[i])

        self.play(Create(triangle), Create(AH))
        fadein_map = (
            ((brace1, text1), (brace2, text2), (brace3, text3)),
            (UP, DR, DL)
        )
        self.play(*[
            FadeIn(i, shift=direction)
            for obj, direction in zip(fadein_map[0], fadein_map[1])
            for i in obj
        ], FadeIn(text4))

        table = MathTable(
            [["a", a],
             ["b", b],
             ["c", c],
             ["h", h],
             [r"(h \times a)/2", ha2],
             [r"\text{Heron}", heron]],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        table.add(table.get_cell((5, 2), color=YELLOW))
        table.add(table.get_cell((6, 2), color=YELLOW))
        table.scale(0.8)
        table.shift(RIGHT * 4)
        content = table[0]
        table.remove(table[0])
        for i, j in zip((
                0, 2, 4, 6
        ), (
                RED, GREEN, BLUE, TEAL
        )):
            content[i].set_color(j)
            content[i + 1].set_color(j)
        content[9].set_color(YELLOW)
        content[11].set_color(YELLOW)
        self.play(Write(table), *[
            Write(content[i]) for i in range(0, 11, 2)
        ])
        self.play(Wiggle(content[8]))
        self.play(Wiggle(content[10]))
        self.play(LaggedStart(*[
            Transform(i[2].copy(), content[j])
            for i, j in zip((
                text1, text2, text3, text4
            ), (
                1, 3, 5, 7
            ))
        ], lag_ratio=0.3))
        self.play(Write(content[9]), Write(content[11]))
        self.play(Wiggle(content[9]), Wiggle(content[11]))


class Scene4(MyScene):
    def construct(self):
        shift = DOWN * 2 + LEFT * 2
        A = np.array([-3.5, 3.5, 0]) + shift
        B = np.array([0, 0, 0]) + shift
        C = np.array([3, 0, 0]) + shift
        H = np.array([-3.5, 0, 0]) + shift
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        AH = Line(A, H, color=TEAL)
        HB = DashedLine(H, B)
        len_a = BC.get_length()
        len_b = AB.get_length()
        len_c = AC.get_length()
        len_h = AH.get_length()
        a = "{:.4f}".format(len_a)
        b = "{:.4f}".format(len_b)
        c = "{:.4f}".format(len_c)
        h = "{:.4f}".format(len_h)
        ha2 = "{:.4f}".format(len_h * len_a / 2)
        s = (len_a + len_b + len_c) / 2
        heron = "{:.4f}".format(math.sqrt(s * (s - len_a) * (s - len_b) * (s - len_c)))

        triangle = VMobject().set_points_as_corners([A, B, C, A])
        self.add(triangle)
        brace1 = Brace(BC, DOWN)
        brace2 = Brace(AB, AB.copy().rotate(-PI / 2).get_unit_vector())
        brace3 = Brace(AC, AC.copy().rotate(PI / 2).get_unit_vector())
        text1 = MathTex("a", "=", a).scale(0.5)
        text2 = MathTex("b", "=", b).scale(0.5)
        text3 = MathTex("c", "=", c).scale(0.5)
        text4 = MathTex("h", "=", h).scale(0.5)
        brace1.put_at_tip(text1, buff=SMALL_BUFF)
        brace2.put_at_tip(text2, buff=SMALL_BUFF)
        brace3.put_at_tip(text3, buff=SMALL_BUFF)
        text4.next_to(AH, LEFT, buff=SMALL_BUFF)
        color_map = {
            text1: RED,
            text2: GREEN,
            text3: BLUE,
            text4: TEAL
        }
        for i in color_map:
            i.set_color(color_map[i])

        self.play(Create(triangle), Create(AH), Create(HB))
        fadein_map = (
            ((brace1, text1), (brace2, text2), (brace3, text3)),
            (UP, DR, DL)
        )
        self.play(*[
            FadeIn(i, shift=direction)
            for obj, direction in zip(fadein_map[0], fadein_map[1])
            for i in obj
        ], FadeIn(text4))

        table = MathTable(
            [["a", a],
             ["b", b],
             ["c", c],
             ["h", h],
             [r"(h \times a)/2", ha2],
             ["Heron", heron]],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        table.add(table.get_cell((5, 2), color=YELLOW))
        table.add(table.get_cell((6, 2), color=YELLOW))
        table.scale(0.8)
        table.shift(RIGHT * 4)
        content = table[0]
        table.remove(table[0])
        for i, j in zip((
                0, 2, 4, 6
        ), (
                RED, GREEN, BLUE, TEAL
        )):
            content[i].set_color(j)
            content[i + 1].set_color(j)
        content[9].set_color(YELLOW)
        content[11].set_color(YELLOW)
        self.play(Write(table), *[
            Write(content[i]) for i in range(0, 11, 2)
        ])
        self.play(LaggedStart(*[
            Transform(i[2].copy(), content[j])
            for i, j in zip((
                text1, text2, text3, text4
            ), (
                1, 3, 5, 7
            ))
        ], lag_ratio=0.3))
        self.play(Write(content[9]), Write(content[11]))
        self.play(Wiggle(content[9]), Wiggle(content[11]))


class Scene5(MyScene):
    def construct(self):
        shift = DOWN * 3 + LEFT * 3
        A = np.array([0, 5, 0]) + shift
        B = np.array([-0.1, 0, 0]) + shift
        C = np.array([0.1, 0, 0]) + shift
        H = np.array([0, 0, 0]) + shift
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        AH = Line(A, H, color=TEAL)
        len_a = BC.get_length()
        len_b = AB.get_length()
        len_c = AC.get_length()
        len_h = AH.get_length()
        a = "{:.4f}".format(len_a)
        b = "{:.4f}".format(len_b)
        c = "{:.4f}".format(len_c)
        h = "{:.4f}".format(len_h)
        ha2 = "{:.4f}".format(len_h * len_a / 2)
        s = (len_a + len_b + len_c) / 2
        heron = "{:.4f}".format(math.sqrt(s * (s - len_a) * (s - len_b) * (s - len_c)))

        triangle = VMobject().set_points_as_corners([A, B, C, A])
        self.add(triangle)
        brace1 = Brace(BC, DOWN)
        brace2 = Brace(AB, AB.copy().rotate(-PI / 2).get_unit_vector())
        brace3 = Brace(AC, AC.copy().rotate(PI / 2).get_unit_vector())
        text1 = MathTex("a", "=", a).scale(0.5)
        text2 = MathTex("b", "=", b).scale(0.5)
        text3 = MathTex("c", "=", c).scale(0.5)
        text4 = MathTex("h", "=", h).scale(0.5)
        brace1.put_at_tip(text1, buff=SMALL_BUFF)
        brace2.put_at_tip(text2, buff=SMALL_BUFF)
        brace3.put_at_tip(text3, buff=SMALL_BUFF)
        arrow = Arrow(start=ORIGIN + UP * 2 + LEFT * 1, end=AH.get_center())
        text4.move_to(ORIGIN + UP * 2.5 + LEFT * 1)
        color_map = {
            text1: RED,
            text2: GREEN,
            text3: BLUE,
            text4: TEAL
        }
        for i in color_map:
            i.set_color(color_map[i])

        self.play(Create(triangle), Create(arrow), Create(AH))
        fadein_map = (
            ((brace1, text1), (brace2, text2), (brace3, text3)),
            (UP, DR, DL)
        )
        self.play(*[
            FadeIn(i, shift=direction)
            for obj, direction in zip(fadein_map[0], fadein_map[1])
            for i in obj
        ], FadeIn(text4))

        table = MathTable(
            [["a", a],
             ["b", b],
             ["c", c],
             ["h", h],
             [r"(h \times a)/2", ha2],
             ["Heron", heron]],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        table.add(table.get_cell((5, 2), color=YELLOW))
        table.add(table.get_cell((6, 2), color=YELLOW))
        table.scale(0.8)
        table.shift(RIGHT * 4)
        content = table[0]
        table.remove(table[0])
        for i, j in zip((
                0, 2, 4, 6
        ), (
                RED, GREEN, BLUE, TEAL
        )):
            content[i].set_color(j)
            content[i + 1].set_color(j)
        content[9].set_color(YELLOW)
        content[11].set_color(YELLOW)
        self.play(Write(table), *[
            Write(content[i]) for i in range(0, 11, 2)
        ])
        self.play(LaggedStart(*[
            Transform(i[2].copy(), content[j])
            for i, j in zip((
                text1, text2, text3, text4
            ), (
                1, 3, 5, 7
            ))
        ], lag_ratio=0.3))
        self.play(Write(content[9]), Write(content[11]))
        self.play(Wiggle(content[9]), Wiggle(content[11]))


class Scene6(MyScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")
        shift = DOWN * 3 + LEFT * 3
        A = np.array([100, 10000, 0]) + shift
        B = np.array([-0.1, 0, 0]) + shift
        C = np.array([0.1, 0, 0]) + shift
        H = np.array([100, 0, 0]) + shift
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        AH = Line(A, H, color=TEAL)
        len_a = BC.get_length()
        len_b = AB.get_length()
        len_c = AC.get_length()
        len_h = AH.get_length()
        a = "{:.10f}".format(len_a)
        b = "{:.10f}".format(len_b)
        c = "{:.10f}".format(len_c)
        h = "{:.10f}".format(len_h)
        ha2 = "{:.10f}".format(len_h * len_a / 2)
        s = (len_a + len_b + len_c) / 2
        heron = "{:.10f}".format(math.sqrt(s * (s - len_a) * (s - len_b) * (s - len_c)))

        triangle = VMobject().set_points_as_corners([A, B, C, A])
        self.add(triangle)
        brace1 = Brace(BC, DOWN)
        brace2 = Brace(AB, AB.copy().rotate(-PI / 2).get_unit_vector())
        brace3 = Brace(AC, AC.copy().rotate(PI / 2).get_unit_vector())
        text1 = MathTex(r"\text{Rộng}", ":", "20cm", tex_template=myTemplate).scale(0.5)
        text2 = MathTex("b", "=", b).scale(0.5)
        text3 = MathTex("c", "=", c).scale(0.5)
        text4 = MathTex(r"\text{Cao}", ":", "10km").scale(0.5)
        brace1.put_at_tip(text1, buff=SMALL_BUFF)
        brace2.put_at_tip(text2, buff=SMALL_BUFF)
        brace3.put_at_tip(text3, buff=SMALL_BUFF)
        text4.move_to(ORIGIN + LEFT * 2)
        color_map = {
            text1: RED,
            text2: GREEN,
            text3: BLUE,
            text4: TEAL
        }
        for i in color_map:
            i.set_color(color_map[i])

        self.play(Create(triangle))
        # fadein_map = (
        #     ((brace1, text1), (brace2, text2), (brace3, text3)),
        #     (UP, DR, DL)
        # )
        self.play(*[
            # FadeIn(i, shift=direction)
            # for obj, direction in zip(fadein_map[0], fadein_map[1])
            # for i in obj
        ], Write(text4), Write(text1))

        table = MathTable(
            [["a", a],
             ["b", b],
             ["c", c],
             ["h", h],
             [r"(h \times a)/2", ha2],
             ["Heron", heron]],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT})
        table.add(table.get_cell((5, 2), color=YELLOW))
        table.add(table.get_cell((6, 2), color=YELLOW))
        table.scale(0.8)
        table.shift(RIGHT * 4)
        content = table[0]
        table.remove(table[0])
        for i, j in zip((
                0, 2, 4, 6
        ), (
                RED, GREEN, BLUE, TEAL
        )):
            content[i].set_color(j)
            content[i + 1].set_color(j)
        content[9].set_color(YELLOW)
        content[11].set_color(YELLOW)
        self.play(Write(table), *[
            Write(content[i]) for i in range(0, 11, 2)
        ])
        self.play(LaggedStart(*[
            Transform(i[2].copy(), content[j])
            for i, j in zip((
                text1, text2, text3, text4
            ), (
                1, 3, 5, 7
            ))
        ], lag_ratio=0.3))
        self.play(Write(content[9]), Write(content[11]))
        self.play(Wiggle(content[9]), Wiggle(content[11]))
        result = MathTex(r"\text{Lệch:}","<0.00001",r"\text{ micro mét}",
                         tex_template=myTemplate)
        result[1].set_color(YELLOW)
        result.next_to(table, DOWN)
        self.play(Write(result))
