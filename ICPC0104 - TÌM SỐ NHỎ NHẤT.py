def solve():
    s = input() + "@"
    tmp = ""
    res = 10**18

    for i in range(len(s)):
        if not s[i].isdigit():
            if tmp != "":
                res = min(res, int(tmp))
                tmp = ""
        else:
            tmp += s[i]

    print(res)


for i in range(int(input())):
    solve()
