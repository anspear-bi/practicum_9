def ways_to_build_stairs(n, max_height):
    if n == 0:
        return 1
    count = 0
    for i in range(1, max_height + 1):
        if n >= i:
            count += ways_to_build_stairs(n - i, i - 1)
    return count

N = int(input("Введите количество кубиков: "))
print(ways_to_build_stairs(N, N))
