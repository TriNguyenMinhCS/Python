def gcd(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y
print('gcd of 15 and 5:', gcd(15, 5))
print('gcd of 30 and 24:', gcd(30, 24))
print('gcd of 81 and 72:', gcd(81, 72))
