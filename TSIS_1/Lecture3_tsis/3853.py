j = list(input().split())
k = int(input()) % len(j)
print(*(j[-k:] + j[:-k]))