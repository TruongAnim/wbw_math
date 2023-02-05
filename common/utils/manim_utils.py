from manim import *


def line_intersection_(line1, line2):
    A, B = line1.get_start_and_end()
    C, D = line2.get_start_and_end()
    # Line AB represented as a1x + b1y = c1
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1 * A[0] + b1 * A[1]
    # Line CD represented as a2x + b2y = c2
    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2 * C[0] + b2 * C[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        # The lines are parallel.This is simplified
        # by returning a pair of None
        return None
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
    return np.array([x, y, 0])


def normal_vector_from_two_point(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return np.array([-dy, dx, 0])


def get_nearest_point(A, B, C):
    slop = (A[1] - B[1]) / (A[0] - B[0])
    if slop == 0:
        slop = 0.0001
    perpendicular = -(1 / slop)
    b = C[1] - perpendicular * C[0]

    def get_point(x):
        return np.array([x, x * perpendicular + b, 0])
    return line_intersection_(Line(get_point(-2), get_point(2)), Line(A, B))

if __name__ == "__main__":
    line1 = Line()
    line2 = Line().shift(UP)
    print(line_intersection_(line1, line2))
