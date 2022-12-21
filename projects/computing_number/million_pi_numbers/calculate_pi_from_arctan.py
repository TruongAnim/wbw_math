def calculate(n):
    import time
    start_time = time.time()
    sum = 0
    for i in range(n):
        if i%2==0:
            sum+= (1/(2*i+1))
        else:
            sum-= (1/(2*i+1))
        print(i, "--- %s seconds ---" % (time.time() - start_time))
    print("--- %s seconds ---" % (time.time() - start_time))
    return 4*sum

print(calculate(8))