def distance_between_two_points(p1, p2):
    import math
    return math.sqrt(sum((pow(p1[i]-p2[i], 2) for i in range(3))))

if __name__ == "__main__":
    print(distance_between_to_points([1, 2, 0], [2, 3, 0]))
