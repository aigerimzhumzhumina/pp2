def isprime(n):
    if n == 1 or n==0:
        return False 
    elif n == 2 or n == 3:
        return True 
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True 
def filter(mylist):
    primelist = []
    for n in mylist:
        if isprime(n):
            primelist.append(n)
    return primelist

mylist = [3, 6, 33, 37, 99, 0, 1]
primelist = filter(mylist)
for n in primelist:
    print(n)



