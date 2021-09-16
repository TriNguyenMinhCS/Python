def sum(a, b):
    sum = a + b
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(15, 4))
