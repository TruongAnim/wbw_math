import math
import decimal

def check_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def check_prime_fast1(n):
    prime_flag = 0
    if (n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def get_prime(start, end):
    result = [i for i in range(start, end) if check_prime_fast1(i)]
    return result


def computing_e(n):
    decimal.getcontext().prec = 2000
    sum = decimal.Decimal(0)
    for i in range(n):
        sum += (decimal.Decimal(1) / math.factorial(i))
    return sum


def computing_e2(n):
    decimal.getcontext().prec = 1050
    return (1+decimal.Decimal(1)/n)**n


if __name__ == "__main__":
    # data = "718281828459045235360287"
    # # print(get_prime(1, 1000))
    # for i in get_prime(100, 1000000):
    #     if str(i) in data:
    #         print(i)

    # result = str(computing_e(451))[:1002]
    # import time
    # start_time = time.time()
    # result = str(computing_e2(10**1003))[:1002]
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print(result)
    # with open('e.txt', 'r') as file:
    #     data = file.read()
    #
    # if result in data:
    #     print(result)
    # else:
    #     print("Wrong!")
    # print(len(data))

    with open('e.txt', 'r') as file:
        data = file.read()
    first = data[:1002]
    print(first)
    # for i in range(2, 990):
    #     combo = int(first[i:i+10])
    #     if is_prime(combo):
    #         print(i, ":", combo)