import math
from common.utils.utils import double_factorial


def area_of_ellipse(a, b, accurate=4):
    h = math.pow(a - b, 2) / math.pow(a + b, 2)
    loop = 1 + h / 4
    for i in range(2, accurate + 1):
        numerator = double_factorial(2 * i - 3)
        denominator = pow(2, i) * math.factorial(i)
        loop += (pow(numerator / denominator, 2) * pow(h, i))
    return math.pi * (a + b) * loop


if __name__ == "__main__":
    print(area_of_ellipse(3,30,accurate=10))
