from manim import *
from typing import Callable, Iterable, Optional, Tuple, Type, Union


class FillAndFade(Transform):
    def __init__(
        self,
        mobject: "Mobject",
        fill_color_: str = RED,
        rate_func: Callable[[float, Optional[float]], np.ndarray] = there_and_back,
        **kwargs
    ) -> None:
        self.fill_color_ = fill_color_
        super().__init__(mobject, rate_func=rate_func, **kwargs)

    def create_target(self) -> "Mobject":
        target = self.mobject.copy()
        target.set_fill(self.fill_color_, 0.8)
        return target


class ShinkToPoint(Transform):
    def __init__(
        self, mobject: Mobject, point: np.ndarray, point_color: str = None, **kwargs
    ) -> None:
        self.point = point
        self.point_color = point_color
        super().__init__(mobject, remover=True, **kwargs)

    def create_target(self) -> Mobject:
        start = super().create_starting_mobject()
        start.scale(0)
        start.move_to(self.point)
        if self.point_color:
            start.set_color(self.point_color)
        return start


class ShinkToEdge(ShinkToPoint):
    def __init__(
        self, mobject: Mobject, edge: np.ndarray, point_color: str = None, **kwargs
    ) -> None:
        point = mobject.get_critical_point(edge)
        super().__init__(mobject, point, point_color=point_color, **kwargs)


class ShinkToCenter(ShinkToPoint):
    def __init__(
        self, mobject: Mobject, point_color: str = None, **kwargs
    ) -> None:
        point = mobject.get_center()
        super().__init__(mobject, point, point_color=point_color, **kwargs)


class Indicate2(Transform):
    def __init__(
        self,
        mobject: "Mobject",
        offset: float = 0.5*UP,
        color: str = YELLOW,
        rate_func: Callable[[float, Optional[float]], np.ndarray] = there_and_back,
        **kwargs
    ) -> None:
        self.color = color
        self.offset = offset
        super().__init__(mobject, rate_func=rate_func, **kwargs)

    def create_target(self) -> "Mobject":
        target = self.mobject.copy()
        target.shift(self.offset)
        target.set_color(self.color)
        return target