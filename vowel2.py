str = input()
strList = str.split()

def isVowel(ch):
    if ch in 'ueoai':
        return True
    return False

result = [] 

for i in range (0, len(strList)):   
    a = 0
    for j in strList[i]:
        if isVowel(j):
            a += 1
    if a >= 3:
        result.append(strList[i])
        result.append(a)
print(result)

   
