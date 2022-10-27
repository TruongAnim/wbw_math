from manim import *
from color_utils import HSL
from color_utils import interpolate_color_range

SCENE_NAME = "TestGetIndexes"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class TestFuncion(Scene):
    def construct(self):
        points = [
            (0, 0, 0),
            (1, 1, 0),
            (2, 1, 0),
            (1, 2, 0)
        ]
        line = VMobject().set_points_as_corners(points)
        point = line.point_from_proportion(0.5)
        self.add(line)
        print(point)

class TestGetIndexes(Scene):
    def setup(self):
        from mobject_utils import get_indexes
        source_tex = MathTex("a^2+b^2 = c^2")
        group = VGroup(*[
            Square() for i in range(5)
        ]).arrange_in_grid(rows= 2)
        t1 = Table(
            [["This", "is a"],
             ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        # self.add(source_tex, get_indexes(source_tex[0], font_size=15))
        # self.add(group, get_indexes(group, font_size=25))
        self.add(t1, get_indexes(t1[0]))

# Get mid color from two color
mid_color = interpolate_color(RED, BLUE, 0.5)

# Get interpolate of multiple color
multi_color = interpolate_color_range(RED, GREEN, BLUE, 0.5)

# Get averange color from list
average_color_ = average_color(*[RED, GREEN, BLUE])

# Get a list of color along the list
gradient = color_gradient([RED, GREEN, BLUE], 10)

# Set a list object gradient color
# Use for group or text
Text("hello").set_color_by_gradient(*[RED, GREEN, BLUE])

# Set an object gradient color
Square().set_color([RED, GREEN, BLUE])

# Set how the gradient color affect
Square().set_sheen_direction(UP)

# Add background from an image
Square().color_using_background_image("facebook.png")

# Add line from given points
points = [
    (0, 0, 0),
    (1, 1, 0),
    (2, 1, 0),
    (1, 2, 0)
]
corner_line = VMobject().set_points_as_corners(points)

# Add smooth line from given points
smooth_line = VMobject().set_points_smoothly(points)

# Make the line smooth
corner_line.animate.make_smooth()

# Make the line jagged
smooth_line.animate.make_jagged()

# Concatenate more lines
line = VMobject()
another_line = VMobject().set_points_as_corners(points)
line.append_vectorized_mobject(another_line)

# Add more points
line.append_points(another_line.points)

# Get a point from line
point = line.point_from_proportion(0.5)

# Get a part of a line
part_line = line.get_subcurve(0.3, 0.6)

# Save state and restore state of object
square = Square().save_state()
Restore(square)  # self.play(Restore(square))
# => opposite from generate_target() and MoveToTarget()

# Move a point along the path
MoveAlongPath(Dot(), part_line)  # self.play(MoveAlongPath(Dot(), part_line))

# Create a rectangle surround an object
Rectangle().surround(square)

# => just change hue from 0 to 1
partitions = 100
colors = [HSL(i / partitions) for i in range(partitions)]
