def find_group_size(N):
    for i in range(2, N + 1):
        if N % i == 0:
            return i
    return N
N = int(input())
print(find_group_size(N))
