def nums(n):
    stop = 0
    while n>0:
        yield n 
        n-=1 
n = int(input())
for num in nums(n):
    print(num, end = ' ')