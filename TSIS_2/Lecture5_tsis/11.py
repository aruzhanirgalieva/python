import os 
size = os.stat("text1.txt")
print(size.st_size)