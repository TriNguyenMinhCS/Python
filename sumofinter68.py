numberList = int(input())
n1 = numberList // 1000
n2 = (numberList - n1 * 1000) // 100
n3 = (numberList - n1 * 1000 - n2 * 100) // 10
n4 = numberList - n1 * 1000 - n2 * 100 - n3 * 10
print("tổng các số trong số nguyên", numberList, "là:", n1 + n2 + n3 + n4)