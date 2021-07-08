import os

def read_file(name):
    txt = open(name)
    print(txt.read())

read_file('text1.txt')