s = input()
cnt_s = 0
cnt_b = 0
for i in s:
    if i.isupper():
        cnt_b += 1
    if i.islower():
        cnt_s += 1
print("No. of Upper case characters: ", cnt_b)
print("No. of Lower case characters: ", cnt_s)