def nums3_4(n):
    start = 0
    while start < n:
        if start%3 == 0 and start%4 == 0:
            yield start 
        start+=1
n = int(input())
mylist = list(nums3_4(n))
mylist_str = ', '.join(map(str, mylist))
print(mylist_str)