from decimal import Decimal, getcontext


def tb(x1, x2):
    return (x1 + x2) / 2


def repeat_compute(n, gess, loop):
    x1 = gess
    x2 = n / x1
    print(x1)
    print(x2)
    for i in range(loop - 1):
        x1 = tb(x1, x2)
        x2 = (n / x1)
        print(x1)
        print(x2)
    return x1


if __name__ == "__main__":
    getcontext().prec = 7
    import time

    start_time = time.time()
    result = repeat_compute(Decimal(127), Decimal(15), 5)
    print("--- %s seconds ---" % (time.time() - start_time))
    # with open('a.txt', 'r') as file:
    #     data = file.read().replace('\n', '')
    # print(len(data))
    # result = str(result).replace('.', "")
    # for index, i in enumerate(result):
    #     if i != data[index]:
    #         print(index)
    #         break
