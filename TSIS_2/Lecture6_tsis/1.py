def mx(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if c > b:
            return c
        else:
            return b
a, b, c = map(int, input().split())
print(mx(a, b, c))