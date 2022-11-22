import random


def calculate(students):
    product = 1
    for i in range(365, 365 - students, -1):
        product *= (i / 365)
        print(i)
    print(product)
    return 1 - product


def calculate_to_one(students):
    return 1-((364/365)**students)


def test_probability(students, run_times):
    count = 0
    for t in range(run_times):
        m = {random.randint(1, 365), }
        for i in range(students - 1):
            m.add(random.randint(1, 365))
        if len(m) == students:
            count += 1
    print(run_times - count)
    print(1 - (count / run_times))


def test_probability_to_one(students, run_times):
    count = 0
    m = 10
    for t in range(run_times):
        for i in range(students):
            if random.randint(1, 365) == m:
                count += 1
                break
    print(count)
    print(count / run_times)


if __name__ == "__main__":
    print("hello")
    print(calculate(45))
    # test_probability(45, 1000000)
    # print(calculate_to_one(20))
    # test_probability_to_one(20, 1000000)
