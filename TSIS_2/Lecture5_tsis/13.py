f = open("text1.txt", "r")
text = f.readlines()
f.close()
with open("text2.txt", "w") as f:
    for i in text:
        f.write(i)
f = open("text2.txt")
print(f.read())