def read_n_lines(name, n):
        from itertools import islice
        f = open(name)
        for line in islice(f, n):
                print(line)

read_n_lines("text1.txt", 2)