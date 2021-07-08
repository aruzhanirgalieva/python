f = open("text2.txt").readlines()
print([s.rstrip('\n') for s in f])