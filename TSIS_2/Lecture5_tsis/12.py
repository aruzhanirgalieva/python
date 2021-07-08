a = ["red", "black", "purple"]
with open("text1.txt", "w") as f:
    for i in a:
        f.write("%s\n" % i)
f = open("text1.txt")
print(f.read())