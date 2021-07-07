j, k, res = [int(i) for i in input().split()], [int(i) for i in input().split()], []
s = set.intersection(set(j), set(k))
for i in s: res.append(i)
res.sort()
print(*res)