def number_near_thousand(n):
    return((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(number_near_thousand(900))
print(number_near_thousand(1000))
print(number_near_thousand(2200))
print(number_near_thousand(100))
