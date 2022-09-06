import math
import random
import matplotlib.pyplot as plt

from common.svg.character.number_creature import *
from common.svg.character.number_creature_anim import *
from common.utils.mobject_utils import get_indexes

list_scene = ("Scene1", "Scene2", "Scene3", "Scene4", "Scene5", "Scene6", "Scene7")
SCENE_NAME = list_scene[4]
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


class Scene1(Scene):
    def construct(self):
        property_ = 10000000
        bet_ = 100000
        turn = 0
        continue_ = 0

        actual = Integer(number=333).shift(UP * 2)
        even = Text("Chẵn", font="Sans", font_size=35)
        odd = Text("Lẻ", font="Sans", font_size=35)
        turn_text = Text("Lượt:", font="Sans", font_size=25) \
            .shift(RIGHT * 2)
        turn_value = Integer(number=0) \
            .next_to(turn_text, RIGHT)
        continue_text = Text("Thua liên tiếp:", font="Sans", font_size=25) \
            .align_to(turn_text, LEFT)
        continue_text.shift(DOWN)
        continue_value = Integer(number=0).next_to(continue_text, RIGHT)
        property_text = Text("Tài sản:",
                             font="Sans",
                             font_size=30).shift(UP * 2 + RIGHT * 3)
        property_value = DecimalNumber(
            number=property_,
            group_with_commas=True,
            num_decimal_places=1
        ).next_to(property_text)

        def get_random():
            r = random.randint(1, 2)
            if r == 1:
                return odd
            elif r == 2:
                return even

        square = Square(fill_color=YELLOW_E, fill_opacity=1).move_to(actual)
        self.play(*[
            Write(i)
            for i in (actual, square, property_text,
                      property_value, turn_text, continue_text,
                      continue_value, turn_value)
        ])
        self.wait()
        time = 1
        for i in range(10):
            self.play(Wiggle(square), run_time=time)
            actual.set_value(random.randint(1, 1000))
            new_predict = get_random()
            bet_value = Integer(
                number=bet_,
                group_with_commas=True,
                include_sign=False
            ).shift(DOWN)
            property_ -= bet_
            turn += 1
            self.play(Write(new_predict),
                      Write(bet_value),
                      turn_value.animate.set_value(turn),
                      property_value.animate.set_value(property_),
                      run_time=time)
            self.wait(time)
            bet_value.generate_target()
            if property_ < 0:
                break
            if (actual.get_value() % 2 == 0 and new_predict == even) or \
                    (actual.get_value() % 2 == 1 and new_predict == odd):
                bet_value.target = Integer(
                    number=bet_ * 2,
                    group_with_commas=True,
                    include_sign=True,
                    color=GREEN
                ).shift(DOWN)
                property_ += bet_ * 2
                bet_ = 100000
                continue_ = 0
            else:
                bet_value.target = Integer(
                    number=bet_value.get_value() * -1,
                    group_with_commas=True,
                    include_sign=True,
                    color=RED
                ).shift(DOWN)
                bet_ *= 2
                continue_ += 1
            self.play(FadeOut(square), run_time=time)
            self.play(MoveToTarget(bet_value),
                      property_value.animate.set_value(property_),
                      continue_value.animate.set_value(continue_),
                      run_time=time)
            self.play(FadeOut(new_predict),
                      FadeIn(square),
                      FadeOut(bet_value),
                      run_time=time)


class Scene3(Scene):
    def construct(self):
        property_ = 10000000
        bet_ = 100000
        turn = 0
        continue_ = 0

        actual = Integer(number=333).shift(UP * 2)
        even = Text("Chẵn", font="Sans", font_size=35)
        odd = Text("Lẻ", font="Sans", font_size=35)
        turn_text = Text("Lượt:", font="Sans", font_size=25) \
            .shift(RIGHT * 2)
        turn_value = Integer(number=0) \
            .next_to(turn_text, RIGHT)
        continue_text = Text("Thua liên tiếp:", font="Sans", font_size=25) \
            .align_to(turn_text, LEFT)
        continue_text.shift(DOWN)
        continue_value = Integer(number=0).next_to(continue_text, RIGHT)
        property_text = Text("Tài sản:",
                             font="Sans",
                             font_size=30).shift(UP * 2 + RIGHT * 3)
        property_value = DecimalNumber(
            number=property_,
            group_with_commas=True,
            num_decimal_places=1
        ).next_to(property_text)

        def get_random():
            r = random.randint(1, 2)
            if r == 1:
                return odd
            elif r == 2:
                return even

        square = Square(fill_color=YELLOW_E, fill_opacity=1).move_to(actual)
        self.add(actual, square, property_text,
                 property_value, turn_text, continue_text,
                 continue_value, turn_value)
        time = 0.3
        property_data = []
        turn_data = []
        for i in range(5000):
            actual.set_value(random.randint(1, 1000))
            new_predict = get_random()
            bet_value = Integer(
                number=bet_,
                group_with_commas=True,
                include_sign=False
            ).shift(DOWN)
            property_data.append(property_ / 1000)
            turn_data.append(turn)
            property_ -= bet_
            turn += 1
            self.add(new_predict, bet_value)
            turn_value.set_value(turn)
            property_value.set_value(property_)
            self.wait(time)
            bet_value.generate_target()
            if property_ < 0 or property_ > 50000000:
                break
            if (actual.get_value() % 2 == 0 and new_predict == even) or \
                    (actual.get_value() % 2 == 1 and new_predict == odd):
                bet_value.target = Integer(
                    number=bet_ * 2,
                    group_with_commas=True,
                    include_sign=True,
                    color=GREEN
                ).shift(DOWN)
                property_ += bet_ * 2
                bet_ = 100000
                continue_ = 0
            else:
                bet_value.target = Integer(
                    number=bet_value.get_value() * -1,
                    group_with_commas=True,
                    include_sign=True,
                    color=RED
                ).shift(DOWN)
                bet_ *= 2
                continue_ += 1
            self.remove(square)
            bet_value.become(bet_value.target)
            self.add(bet_value)
            property_value.set_value(property_)
            continue_value.set_value(continue_)
            self.wait(time)
            self.remove(new_predict, bet_value)
            self.add(square)
            self.wait(time)
        plt.plot(turn_data, property_data, color='red', marker='o')
        plt.title('Biến động tài sản', fontsize=25)
        plt.xlabel('Lượt', fontsize=25)
        plt.ylabel('Tài sản', fontsize=25)
        plt.grid(True)
        plt.show()


class Scene4(Scene):
    def construct(self):
        property_ = 10000000
        bet_ = 100000
        turn = 0
        continue_ = 0

        actual = Integer(number=333).shift(UP * 2)
        even = Text("Chẵn", font="Sans", font_size=35)
        odd = Text("Lẻ", font="Sans", font_size=35)
        turn_text = Text("Lượt:", font="Sans", font_size=25) \
            .shift(RIGHT * 2)
        turn_value = Integer(number=0) \
            .next_to(turn_text, RIGHT)
        continue_text = Text("Thua liên tiếp:", font="Sans", font_size=25) \
            .align_to(turn_text, LEFT)
        continue_text.shift(DOWN)
        continue_value = Integer(number=0).next_to(continue_text, RIGHT)
        property_text = Text("Tài sản:",
                             font="Sans",
                             font_size=30).shift(UP * 2 + RIGHT * 3)
        property_value = DecimalNumber(
            number=property_,
            group_with_commas=True,
            num_decimal_places=1
        ).next_to(property_text)

        def get_random():
            r = random.randint(1, 2)
            if r == 1:
                return odd
            elif r == 2:
                return even

        square = Square(fill_color=YELLOW_E, fill_opacity=1).move_to(actual)
        self.add(actual, square, property_text,
                 property_value, turn_text, continue_text,
                 continue_value, turn_value)
        time = 0.2
        property_data = []
        turn_data = []
        for i in range(50000):
            actual.set_value(random.randint(1, 1000))
            new_predict = get_random()
            bet_value = Integer(
                number=bet_,
                group_with_commas=True,
                include_sign=False
            ).shift(DOWN)
            if bet_ > property_ and property_ > 100000:
                bet_ = 100000
            property_data.append(property_ / 1000)
            turn_data.append(turn)
            property_ -= bet_
            turn += 1
            self.add(new_predict, bet_value)
            turn_value.set_value(turn)
            property_value.set_value(property_)
            self.wait(time)
            bet_value.generate_target()
            if property_ < 0 or property_ > 50000000:
                property_ = 0
                property_data.append(property_ / 1000)
                turn_data.append(turn)
                break
            if (actual.get_value() % 2 == 0 and new_predict == even) or \
                    (actual.get_value() % 2 == 1 and new_predict == odd):
                bet_value.target = Integer(
                    number=bet_ * 2,
                    group_with_commas=True,
                    include_sign=True,
                    color=GREEN
                ).shift(DOWN)
                property_ += bet_ * 2
                bet_ = 100000
                continue_ = 0
            else:
                bet_value.target = Integer(
                    number=bet_value.get_value() * -1,
                    group_with_commas=True,
                    include_sign=True,
                    color=RED
                ).shift(DOWN)
                bet_ *= 2
                continue_ += 1
            self.remove(square)
            bet_value.become(bet_value.target)
            self.add(bet_value)
            property_value.set_value(property_)
            continue_value.set_value(continue_)
            self.wait(time)
            self.remove(new_predict, bet_value)
            self.add(square)
            self.wait(time)

        plt.plot(turn_data, property_data, color='red', marker='o')
        plt.title('Biến động tài sản', fontsize=25)
        plt.xlabel('Lượt', fontsize=25)
        plt.ylabel('Tài sản', fontsize=25)
        plt.grid(True)
        plt.show()


class Scene2(Scene):
    def construct(self):
        start_property = 1000000000
        end_property = 1100000000
        start = 100000
        count = 0
        total = 0
        for match in range(1000000):
            property_ = start_property
            bet_ = start
            for i in range(1000000):
                predict = random.randint(1, 1000)
                if property_ >= end_property:
                    count += 1
                    total += i
                    # print("done in:",i, property_)
                    break
                if property_ < bet_ and property_ >= 100000:
                    bet_ = 100000
                property_ -= bet_
                if property_ < 0:
                    # print("end in:", i, property_)
                    break
                # print("-", bet_)
                if predict % 2 == 0:
                    property_ += bet_ * 2
                    # print("+", bet_ * 2)
                    bet_ = start
                else:
                    bet_ *= 2
            # print("property:", property_)
            if match % 1000 == 0:
                print(match)
                print(count)
                if count > 0:
                    print(total / count)
        print(count)
        print(total / count)


class Scene5(Scene):
    def create_label(self, obj, investment, target, turn):
        text_kwargs = {
            "font": "Sans",
            "font_size": 17
        }
        brace = Brace(obj, DOWN)
        investment_text = Text("Vốn:" + investment, **text_kwargs) \
            .next_to(brace, DOWN)
        target_text = Text("Mục tiêu:" + target, **text_kwargs) \
            .next_to(investment_text, DOWN)
        tb = Text("TB số lượt:" + turn, **text_kwargs) \
            .next_to(target_text, DOWN)
        return VGroup(brace, investment_text, target_text, tb)

    def construct(self):
        chart = BarChart(
            values=[199654, 800346, 500384, 499616, 504632, 495368, 909362, 90638],
            bar_names=["", "", "", "", "", "", "", ""],
            bar_colors=[GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED],
            y_range=[0, 1000000, 500000],
            y_length=5,
            x_length=10,
            x_axis_config={"font_size": 30},
        ).shift(UP)

        c_bar_lbls = chart.get_bar_labels(font_size=30)
        green_square = Square(color=GREEN, fill_opacity=0.8, side_length=0.5) \
            .to_edge(UP).shift(RIGHT * 4.5)
        red_square = Square(color=RED, fill_opacity=0.8, side_length=0.5) \
            .next_to(green_square, DOWN)
        success = Text("Đạt mục tiêu", font="Sans", font_size=25) \
            .next_to(green_square, RIGHT)
        fail = Text("Trắng tay", font="Sans", font_size=25) \
            .next_to(red_square, RIGHT)
        bars = chart.bars
        chart.remove(chart.bars)
        investments = [" 10Tr", " 10Tr", " 1 Tỉ", " 1 Tỉ"]
        targets = [" 50Tr", " 20Tr", " 2 Tỉ", " 1.1 Tỉ"]
        turns = ["1123", "265", "27687", "2608"]
        g_bar = [VGroup(bars[i:i + 2], c_bar_lbls[i:i + 2]) for i in range(0, 7, 2)]
        labels = [self.create_label(
            g_bar[i],
            investments[i],
            targets[i],
            turns[i]
            ) for i in range(4)]
        self.play(Write(chart),
                  *[Write(i)
                    for i in (green_square, red_square, success, fail)])
        for i in range(4):
            self.play(Write(labels[i]))
            self.wait()
            self.play(Write(g_bar[i]))
            self.wait()
