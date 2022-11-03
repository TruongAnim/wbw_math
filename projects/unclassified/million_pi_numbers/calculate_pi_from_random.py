def calculate_pi(sample):
    import random
    import time
    start_time = time.time()
    count = 0
    for i in range(sample):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            count += 1
        if i % 10000000 == 0:
            print(i, "--- %s seconds ---" % (time.time() - start_time))
        if i == 999990000:
            print(i, "--- %s seconds ---" % (time.time() - start_time))
            print(count, sample)
    print(count, sample)
    print("--- %s seconds ---" % (time.time() - start_time))
    return (count / sample) * 4


print(calculate_pi(1000000000))
