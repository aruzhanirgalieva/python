def append_and_show(name):
    with open(name, "w") as f:
        f.write("Python\n")
    txt = open(name)
    print(txt.read())

append_and_show("text1.txt")