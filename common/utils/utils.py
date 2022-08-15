def distance_between_two_points(p1, p2):
    import math
    return math.sqrt(sum((pow(p1[i]-p2[i], 2) for i in range(3))))


def get_norm(vect):
    return sum([x ** 2 for x in vect]) ** 0.5

if __name__ == "__main__":
    print(distance_between_two_points([1, 2, 0], [2, 3, 0]))
