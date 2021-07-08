with open("text1.txt") as f1, open("text2.txt") as f2:
    for i, j in zip(f1, f2):
        print(i+j)