def test(nums, n):
    return(all(x > n for x in nums))
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = int(input())
print("\nTest all numbers in list greater than", n,":")
print(test(nums,n))
