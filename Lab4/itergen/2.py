n = int(input())

def Evens(n):
    start = 0
    while start < n:
        if start%2==0 and start != 0:
            yield start
        start+=1
 
nums = list(Evens(n))
nums_str = ', '.join(map(str, nums))
print(nums_str)

    

