def function(n, input):
    main = list(range(1, n + 1))
    output = [x for x in main if x not in input]
    print(output)

function(10, [2, 3, 7, 4, 9])