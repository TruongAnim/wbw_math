lower_value = 2
upper_value = 1000

print("The Prime Numbers in the range are: ")
count = 0
l = []
for number in range(lower_value, upper_value + 1):
    for i in range(2, (number // 2)+1):
        if (number % i) == 0:
            # print(n,"is not a prime number")
            break
    else:
        count += 1
        l.append(number)
    # if number%lower_value == 0:
    #     print(count)
print(count)
print(l)