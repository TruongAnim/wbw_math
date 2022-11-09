lower_value = 10000
upper_value = 100000

print("The Prime Numbers in the range are: ")
count = 0
for number in range(lower_value, upper_value + 1):
    for i in range(2, number // 2):
        if (number % i) == 0:
            # print(n,"is not a prime number")
            break
    else:
        count += 1
    if number%lower_value == 0:
        print(count)
print(count)