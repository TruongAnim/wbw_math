import sys

def tb(x1, x2):
    return (x1 + x2) // 2


def repeat_compute(n, gess, loop):
    x1 = gess
    x2 = n // x1
    for i in range(loop - 1):
        x1 = tb(x1, x2)
        x2 = (n // x1)
    return x1


if __name__ == "__main__":
    digit = 2000000
    result = repeat_compute(2*(10**digit), 15*(10**(int(digit/2-1))), 20)
    text = str(int(result))
    print(len(text))
    with open('a.txt', 'r') as file:
        data = file.read().replace('\n', '')
    print(len(data))
    final = ""
    for index, i in enumerate(text):
        if i!= data[index]:
            print(index)
            break
        final += i
    with open("final.txt", 'wt') as outfile:
        # Insert the decimal point after the first digit '3'.
        outfile.write(final[0] + '.' + final[1:] + '\n')


