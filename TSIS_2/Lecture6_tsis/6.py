def check(n, l, r):
    if n in range(l, r):
        return True
    else:
        return False
n = int(input())
l, r = map(int, input().split())
print(check(n, l, r))