def f(x):
    for i in range(2, x):
        if x%i == 0:
            return False
            break
    return True
x = int(input())
print(f(x))