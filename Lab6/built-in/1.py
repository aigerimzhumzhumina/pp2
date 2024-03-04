from functools import reduce
nums = []
n = int(input())
for i in range (0, n):
    num = int(input())
    nums.append(num)
mult = reduce(lambda x, y: x*y, nums)
print(mult)