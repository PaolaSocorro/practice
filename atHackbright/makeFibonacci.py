def make_fib():
    fib_list = []
    first = 0
    second = 1

    fib_list.append(first).append(second)

    for i in range(2, 12):
        fib_list.append(first + second)
        first = fib_list[i-1]
        second = fib_list[i]

    return fib_list


make_fib()
