f = open("text1.txt", "r")
text = f.readlines()
ls = []
for i in text:
    ls.append(i)
print(*ls)