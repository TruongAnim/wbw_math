def distance_between_two_points(p1, p2):
    import math
    return math.sqrt(sum((pow(p1[i]-p2[i], 2) for i in range(3))))


def get_norm(vect):
    return sum([x ** 2 for x in vect]) ** 0.5


def double_factorial(n):
    start = 1
    if n%2 ==0:
        start = 2
    result = 1
    for i in range(start, n+1, 2):
        result*=i
    return result


if __name__ == "__main__":
    for i in range(10):
        print(double_factorial(i))
