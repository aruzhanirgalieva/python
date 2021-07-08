f = open("text1.txt", "r")
line = f.readlines()
n = 1
last_line = line[-n:]
print(last_line)