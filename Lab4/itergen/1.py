N = int(input())
nums = []
for i in range(N):
    num = int(input())
    nums.append(num)
nums_iter = iter(nums)
for num in nums_iter:
    print(num**2, end=" ")