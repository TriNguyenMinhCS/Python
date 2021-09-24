x = int(input())
y = int(input())
z = int(input())
s1 = min(x, y, z)
s3 = max(x, y, z)
s2 = (x + y + z) - s1 - s3
print("sort three integers:", s1, s2 , s3)