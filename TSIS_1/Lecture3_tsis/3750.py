k, t = [int(i) for i in input().split()], [int(i) for i in input().split()]
s = set.intersection(set(k), set(t))
print(len(s))