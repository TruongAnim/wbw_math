from manim import *
from common.svg.drawing.bubble import *

class NumberCreatureBubbleIntroduction(AnimationGroup):
    def __init__(
            self,
            creature,
            *content,
            target_mode="speaking",
            bubble_class=SpeechBubble,
            change_mode_kwargs={},
            bubble_creation_class=FadeIn,
            bubble_creation_kwargs={},
            bubble_kwargs={},
            content_introduction_class=Write,
            content_introduction_kwargs={},
            look_at_arg=None,
            use_fade_transform=False,
            **kwargs
    ):
        self.target_mode = target_mode
        self.bubble_class = bubble_class
        self.change_mode_kwargs = change_mode_kwargs
        self.bubble_creation_class = bubble_creation_class
        self.bubble_creation_kwargs = bubble_creation_kwargs
        self.bubble_kwargs = bubble_kwargs
        self.content_introduction_class = content_introduction_class
        self.content_introduction_kwargs = content_introduction_kwargs
        self.look_at_arg = look_at_arg

        bubble = creature.get_bubble(
            *content,
            bubble_class=self.bubble_class,
            **self.bubble_kwargs
        )
        Group(bubble, bubble.content).shift_onto_screen()

        creature.generate_target()
        creature.target.change_mode(self.target_mode, creature.get_file_name_prefix())
        if self.look_at_arg is not None:
            creature.target.look_at(self.look_at_arg)

        if use_fade_transform:
            change_mode = FadeTransform(creature, creature.target, **self.change_mode_kwargs)
        else:
            change_mode = MoveToTarget(creature, **self.change_mode_kwargs)
        bubble_creation = self.bubble_creation_class(
            bubble, **self.bubble_creation_kwargs
        )
        content_introduction = self.content_introduction_class(
            bubble.content, **self.content_introduction_kwargs
        )
        AnimationGroup.__init__(
            self, change_mode, bubble_creation, content_introduction,
            **kwargs
        )


class NumberCreatureSays(NumberCreatureBubbleIntroduction):
    def __init__(
            self,
            creature,
            *content,
            target_mode="speaking",
            bubble_class=SpeechBubble,
            **kwargs
    ):
        super().__init__(
            creature,
            *content,
            target_mode=target_mode,
            bubble_class=bubble_class,
            **kwargs
        )


class NumberCreatureThinks(NumberCreatureBubbleIntroduction):
    def __init__(
            self,
            creature,
            *content,
            target_mode="thinking",
            bubble_class=ThoughtBubble,
            **kwargs
    ):
        super().__init__(
            creature,
            *content,
            target_mode=target_mode,
            bubble_class=bubble_class,
            **kwargs
        )


class Blink(ApplyMethod):
    def __init__(self, pi_creature, **kwargs):
        if "rate_func" not in kwargs:
            kwargs["rate_func"] = squish_rate_func(there_and_back)
        ApplyMethod.__init__(self, pi_creature.blink, **kwargs)
