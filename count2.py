N = int(input())
for i in range(0, N):
    listNum = int(input())
k = int(input())
for i in range(0, N):
    if i == k or i % k == 0:
        print(i)