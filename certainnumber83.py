def test(b, n):
    for i in b:
        if i > n:
           continue 
    return False
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = int(input())
print("\nTest all numbers in list greater than", n,":")
print(test(a,n))
