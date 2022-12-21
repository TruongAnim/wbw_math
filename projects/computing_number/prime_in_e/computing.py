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


def get_prime(start, end):
    result = [i for i in range(start, end) if check_prime_fast1(i)]
    return result


def computing_e(n):
    decimal.getcontext().prec = 2000
    sum = decimal.Decimal(0)
    for i in range(n):
        sum += (decimal.Decimal(1) / math.factorial(i))
    return sum

if __name__ == "__main__":
    # data = "718281828459045235360287"
    # # print(get_prime(1, 1000))
    # for i in get_prime(100, 1000000):
    #     if str(i) in data:
    #         print(i)
    result = str(computing_e(450))[:1000]
    print(result)
    with open('e.txt', 'r') as file:
        data = file.read()

    if result in data:
        print(result)
    else:
        print("Wrong!")
    print(len(data))