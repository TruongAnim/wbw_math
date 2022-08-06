from manim import *

SCENE_NAME = "TestBrace"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class TestNumberLine(Scene):
    def setup(self):
        line1 = NumberLine(x_range=[0, 10, 1])
        self.add(line1.set_stroke(width=1))
        self.add(MathTex(r"f(x)={x}^{2}").next_to(line1, DOWN))


class TestTable(Scene):
    def setup(self):
        table = Table(
            [list(map(str,[1,2,3])),
             list(map(str,[4,5,6]))],
            col_labels=[Text(f"Col {i+1}") for i in range(3)],
            row_labels=[Text(f"Row {i+1}") for i in range(2)],
            include_outer_lines=True
        )
        self.add(table)
        cell = table.get_cell([1,2])

class TestBrace(Scene):
    def setup(self):
        square = Square(color=RED).scale(2)
        brace1 = Brace(square, LEFT)
        brace2 = Brace(square, RIGHT)
        self.add(square, brace1, brace2)

class TestMatrix(Scene):
    def setup(self):
        col = 4
        row = 5
        matrix = Matrix(
            [[i+j*col for i in range(col)] for j in range(row)]
        )
        self.add(matrix)
