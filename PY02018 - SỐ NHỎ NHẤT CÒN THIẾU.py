def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print(a[i - 1] + 1)
            return

    print(a[n - 1] + 1)


solve()
