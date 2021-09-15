N = int(input())
for i in range(0, N):
    listNum = int(input())
def isOdd(num):
    print(num)
    return (num%2)!=0

isOddList = []
isEvenList = []

for i in range(0, listNum):
    if isOdd(i):
        isOddList.append(i)
    else:
        isEvenList.append(i)

print('Dãy chẵn: {}'.format(isEvenList))
print('Dãy lẻ: {}'.format(isOddList))
