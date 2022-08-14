from manim import *
from common.svg.drawing.bubble import SpeechBubble
from common.utils.utils import get_norm

LEFT_EYE_INDEX = 0
RIGHT_EYE_INDEX = 1
LEFT_PUPIL_INDEX = 2
RIGHT_PUPIL_INDEX = 3
BODY_INDEX = 4
MOUTH_INDEX = 5

NUMBER_CREATURE_DIR = config.assets_dir


class NumberCreature(SVGMobject):
    def __init__(
            self,
            file_name_prefix="PiCreatures",
            mode="plain",
            color=RED,
            flip_at_start=False,
            corner_scale_factor=0.5,
            start_corner=None,
            right_arm_range=[0.55, 0.7],
            left_arm_range=[.34, .462],
            pupil_to_eye_width_ratio=0.4,
            pupil_dot_to_pupil_width_ratio=0.3,
            **kwargs
    ):
        self.file_name_prefix = file_name_prefix
        self.mode = mode
        self.body_color = color
        self.right_arm_range = right_arm_range
        self.left_arm_range = left_arm_range
        self.pupil_to_eye_width_ratio = pupil_to_eye_width_ratio
        self.pupil_dot_to_pupil_width_ratio = pupil_dot_to_pupil_width_ratio

        self.parts_named = False
        try:
            svg_file = os.path.join(
                NUMBER_CREATURE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except Exception:
            print("No %s design with mode %s" %
                  (self.file_name_prefix, mode))
            svg_file = os.path.join(
                NUMBER_CREATURE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, "plain")
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)

        self.flip_at_start = flip_at_start
        self.start_corner = start_corner

        if self.flip_at_start:
            self.flip()
        if self.start_corner is not None:
            self.to_corner(self.start_corner)

        self.corner_scale_factor = corner_scale_factor

    def align_data(self, mobject, skip_point_alignment=True):
        # This ensures that after a transform into a different mode,
        # the pi creatures mode will be updated appropriately
        SVGMobject.align_data(self, mobject, skip_point_alignment)
        if isinstance(mobject, NumberCreature):
            self.mode = mobject.get_mode()

    def name_parts(self):
        self.mouth = self.submobjects[MOUTH_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.pupils = VGroup(*[
            self.submobjects[LEFT_PUPIL_INDEX],
            self.submobjects[RIGHT_PUPIL_INDEX]
        ])
        self.eyes = VGroup(*[
            self.submobjects[LEFT_EYE_INDEX],
            self.submobjects[RIGHT_EYE_INDEX]
        ])
        self.eye_parts = VGroup(self.eyes, self.pupils)
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        self.mouth.set_fill(BLACK, opacity=1)
        self.body.set_fill(self.body_color, opacity=1)
        self.eyes.set_fill(WHITE, opacity=1)
        self.init_pupils()
        return self

    def init_pupils(self):
        # Instead of what is drawn, make new circles.
        # This is mostly because the paths associated
        # with the eyes in all the drawings got slightly
        # messed up.
        for eye, pupil in zip(self.eyes, self.pupils):
            pupil_r = eye.get_width() / 2
            pupil_r *= self.pupil_to_eye_width_ratio
            dot_r = pupil_r
            dot_r *= self.pupil_dot_to_pupil_width_ratio

            new_pupil = Circle(
                radius=pupil_r,
                color=BLACK,
                fill_opacity=1,
                stroke_width=0,
            )
            dot = Circle(
                radius=dot_r,
                color=WHITE,
                fill_opacity=1,
                stroke_width=0,
            )
            new_pupil.move_to(pupil)
            pupil.become(new_pupil)
            dot.shift(
                new_pupil.get_boundary_point(UL) -
                dot.get_boundary_point(UL)
            )
            pupil.add(dot)

    def copy(self):
        copy_mobject = SVGMobject.copy(self)
        copy_mobject.name_parts()
        return copy_mobject

    def set_color(self, color):
        self.body.set_fill(color)
        self.body_color = color
        return self

    def change_mode(self, mode, file_name_prefix=None):
        if file_name_prefix is None:
            file_name_prefix = self.get_file_name_prefix()
        new_self = self.__class__(
            mode=mode,
            file_name_prefix=file_name_prefix
        )
        new_self.match_style(self)
        new_self.match_height(self)
        if self.is_flipped() != new_self.is_flipped():
            new_self.flip()
        new_self.shift(self.eyes.get_center() - new_self.eyes.get_center())
        if hasattr(self, "purposeful_looking_direction"):
            new_self.look(self.purposeful_looking_direction)
        self.become(new_self)
        self.mode = mode
        return self

    def get_mode(self):
        return self.mode

    def get_file_name_prefix(self):
        return self.file_name_prefix

    def look(self, direction):
        norm = get_norm(direction)
        if norm == 0:
            return
        direction /= norm
        self.purposeful_looking_direction = direction
        for pupil, eye in zip(self.pupils.split(), self.eyes.split()):
            c = eye.get_center()
            right = eye.get_right() - c
            up = eye.get_top() - c
            vect = direction[0] * right + direction[1] * up
            v_norm = get_norm(vect)
            p_radius = 0.5 * pupil.get_width()
            vect *= (v_norm - 0.75 * p_radius) / v_norm
            pupil.move_to(c + vect)
        self.pupils[1].align_to(self.pupils[0], DOWN)
        return self

    def look_at(self, point_or_mobject):
        if isinstance(point_or_mobject, Mobject):
            point = point_or_mobject.get_center()
        else:
            point = point_or_mobject
        self.look(point - self.eyes.get_center())
        return self

    def change(self, new_mode, look_at_arg=None):
        self.change_mode(new_mode)
        if look_at_arg is not None:
            self.look_at(look_at_arg)
        return self

    def get_looking_direction(self):
        vect = self.pupils.get_center() - self.eyes.get_center()
        return normalize(vect)

    def get_look_at_spot(self):
        return self.eyes.get_center() + self.get_looking_direction()

    def is_flipped(self):
        return self.eyes.submobjects[0].get_center()[0] > \
               self.eyes.submobjects[1].get_center()[0]

    def blink(self):
        eye_parts = self.eye_parts
        eye_bottom_y = eye_parts.get_bottom()[1]
        eye_parts.apply_function(
            lambda p: [p[0], eye_bottom_y, p[2]]
        )
        return self

    def to_corner(self, vect=None, **kwargs):
        if vect is not None:
            SVGMobject.to_corner(self, vect, **kwargs)
        else:
            self.scale(self.corner_scale_factor)
            self.to_corner(DOWN + LEFT, **kwargs)
        return self

    def get_bubble(self, *content, **kwargs):
        bubble_class = kwargs.pop("bubble_class", SpeechBubble)
        bubble = bubble_class(**kwargs)
        if len(content) > 0:
            if isinstance(content[0], str):
                content_mob = Tex(*content)
            else:
                content_mob = content[0]
            bubble.add_content(content_mob)
            if "stretch_width" not in kwargs and "stretch_height" not in kwargs:
                bubble.resize_to_content()
        bubble.pin_to(self)
        self.bubble = bubble
        return bubble

    def make_eye_contact(self, pi_creature):
        self.look_at(pi_creature.eyes)
        pi_creature.look_at(self.eyes)
        return self

    def shrug(self):
        self.change_mode("shruggie")
        top_mouth_point, bottom_mouth_point = [
            self.mouth.points[np.argmax(self.mouth.points[:, 1])],
            self.mouth.points[np.argmin(self.mouth.points[:, 1])]
        ]
        self.look(top_mouth_point - bottom_mouth_point)
        return self

    def get_arm_copies(self):
        body = self.body
        return VGroup(*[
            body.copy().pointwise_become_partial(body, *alpha_range)
            for alpha_range in (self.right_arm_range, self.left_arm_range)
        ])


def filtered_locals(caller_locals):
    result = caller_locals.copy()
    ignored_local_args = ["self", "kwargs"]
    for arg in ignored_local_args:
        result.pop(arg, caller_locals)
    return result


# temporary not use
def digest_config(obj, kwargs, caller_locals={}):
    """
    Sets init args and CONFIG values as local variables

    The purpose of this function is to ensure that all
    configuration of any object is inheritable, able to
    be easily passed into instantiation, and is attached
    as an attribute of the object.
    """

    # Assemble list of CONFIGs from all super classes
    classes_in_hierarchy = [obj.__class__]
    static_configs = []
    while len(classes_in_hierarchy) > 0:
        Class = classes_in_hierarchy.pop()
        classes_in_hierarchy += Class.__bases__
        if hasattr(Class, "CONFIG"):
            static_configs.append(Class.CONFIG)

    # Order matters a lot here, first dicts have higher priority
    caller_locals = filtered_locals(caller_locals)
    all_dicts = [kwargs, caller_locals, obj.__dict__]
    all_dicts += static_configs
    obj.__dict__ = merge_dicts_recursively(*reversed(all_dicts))


# temporary not use
def get_all_pi_creature_modes():
    result = []
    prefix = "%s_" % NumberCreature.CONFIG["file_name_prefix"]
    suffix = ".svg"
    for file in os.listdir(NUMBER_CREATURE_DIR):
        if file.startswith(prefix) and file.endswith(suffix):
            result.append(
                file[len(prefix):-len(suffix)]
            )
    return result


# temporary not use
class Eyes(VMobject):
    CONFIG = {
        # "height": 0.3,
        "thing_to_look_at": None,
        "mode": "plain",
    }

    def __init__(self, body, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.body = body
        eyes = self.create_eyes()
        self.become(eyes, copy_submobjects=False)

    def create_eyes(self, mode=None, thing_to_look_at=None):
        if mode is None:
            mode = self.mode
        if thing_to_look_at is None:
            thing_to_look_at = self.thing_to_look_at
        self.thing_to_look_at = thing_to_look_at
        self.mode = mode
        looking_direction = None

        number = NumberCreature(mode=mode)
        eyes = VGroup(number.eyes, number.pupils)
        if self.submobjects:
            eyes.match_height(self)
            eyes.move_to(self, DOWN)
            looking_direction = self[1].get_center() - self[0].get_center()
        else:
            eyes.set_height(self.height)
            eyes.move_to(self.body.get_top(), DOWN)

        height = eyes.get_height()
        if thing_to_look_at is not None:
            number.look_at(thing_to_look_at)
        elif looking_direction is not None:
            number.look(looking_direction)
        eyes.set_height(height)

        return eyes

    def change_mode(self, mode, thing_to_look_at=None):
        new_eyes = self.create_eyes(
            mode=mode,
            thing_to_look_at=thing_to_look_at
        )
        self.become(new_eyes, copy_submobjects=False)
        return self

    def look_at(self, thing_to_look_at):
        self.change_mode(
            self.mode,
            thing_to_look_at=thing_to_look_at
        )
        return self

    def blink(self, **kwargs):  # TODO, change Blink
        bottom_y = self.get_bottom()[1]
        for submob in self:
            submob.apply_function(
                lambda p: [p[0], bottom_y, p[2]]
            )
        return self
