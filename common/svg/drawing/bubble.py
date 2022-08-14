from manim import *


class Bubble(SVGMobject):
    def __init__(
            self,
            file_name=None,
            direction=LEFT,
            stretch_width=3,
            stretch_height=2,
            center_point=ORIGIN,
            content_scale_factor=0.75,
            bubble_center_adjustment_factor=1.0 / 8,
            **kwargs
    ):
        self.file_name = file_name
        self.direction = direction
        self.stretch_width = stretch_width
        self.stretch_height = stretch_height
        self.center_point = center_point
        self.content_scale_factor = content_scale_factor
        self.bubble_center_adjustment_factor = bubble_center_adjustment_factor

        if self.file_name is None:
            raise Exception("Must invoke Bubble subclass")
        try:
            SVGMobject.__init__(self, file_name=self.file_name, **kwargs)
        except IOError as err:
            self.file_name = os.path.join(config.assets_dir, self.file_name)
            SVGMobject.__init__(self, file_name=self.file_name, **kwargs)
        self.center()
        self.stretch_to_fit_height(self.stretch_height)
        self.stretch_to_fit_width(self.stretch_width)
        if self.direction[0] > 0:
            self.flip()
        self.direction_was_specified = "direction" in kwargs
        self.content = Mobject()

    def get_tip(self):
        # TODO, find a better way
        return self.get_corner(DOWN + self.direction) - 0.6 * self.direction

    def get_bubble_center(self):
        factor = self.bubble_center_adjustment_factor
        return self.get_center() + factor * self.get_height() * UP

    def move_tip_to(self, point):
        mover = VGroup(self)
        if self.content is not None:
            mover.add(self.content)
        mover.shift(point - self.get_tip())
        return self

    def flip(self, axis=UP):
        Mobject.flip(self, axis=axis)
        if abs(axis[1]) > 0:
            self.direction = -np.array(self.direction)
        return self

    def pin_to(self, mobject):
        mob_center = mobject.get_center()
        want_to_flip = np.sign(mob_center[0]) != np.sign(self.direction[0])
        can_flip = not self.direction_was_specified
        if want_to_flip and can_flip:
            self.flip()
        boundary_point = mobject.get_critical_point(UP - self.direction)
        vector_from_center = 1.0 * (boundary_point - mob_center)
        self.move_tip_to(mob_center + vector_from_center)
        return self

    def position_mobject_inside(self, mobject):
        scaled_width = self.content_scale_factor * self.get_width()
        if mobject.get_width() > scaled_width:
            mobject.set_width(scaled_width)
        mobject.shift(self.get_bubble_center() - mobject.get_center())
        return mobject

    def add_content(self, mobject):
        self.position_mobject_inside(mobject)
        self.content = mobject
        return self.content

    def write(self, *text):
        self.add_content(Tex(*text))
        return self

    def resize_to_content(self):
        target_width = self.content.get_width()
        target_width += max(MED_LARGE_BUFF, 2)
        target_height = self.content.get_height()
        target_height += 2.5 * LARGE_BUFF
        tip_point = self.get_tip()
        self.stretch_to_fit_width(target_width)
        self.stretch_to_fit_height(target_height)
        self.move_tip_to(tip_point)
        self.position_mobject_inside(self.content)

    def clear(self):
        self.add_content(VMobject())
        return self


class SpeechBubble(Bubble):
    def __init__(self, **kwargs):
        super().__init__(file_name="Bubbles_speech.svg", **kwargs)


# temporary not use
class DoubleSpeechBubble(Bubble):
    def __init__(self, **kwargs):
        super().__init__(file_name="Bubbles_double_speech.svg", **kwargs)


class ThoughtBubble(Bubble):
    def __init__(self, **kwargs):
        super().__init__(file_name="Bubbles_thought.svg", **kwargs)
        self.submobjects.sort(key=lambda m: m.get_bottom()[1])

    def make_green_screen(self):
        self.submobjects[-1].set_fill(GREEN, opacity=1)
        return self
