def float_range(start,stop,step):
    numbers =[]
    while start <= stop:
        numbers.append(start)
        start += step
    print(numbers)
float_range(2.0,5.5,0.5)