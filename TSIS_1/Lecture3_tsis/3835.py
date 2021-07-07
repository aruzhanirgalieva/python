a, jb = [int(i) for i in input().split()], 0
for i in a:
    if i > 0:
        jb = i
        break
for i in a:
    if i > 0 and jb > i: jb = i
print(jb)