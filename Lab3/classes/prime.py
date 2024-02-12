def isprime(N):
    if N==1 or N==0:
        return False 
    elif N==2 or N==3:
        return True 
     
    for i in range(2, N):
        if N%i == 0:
            return False 
    return True 
numbers = [33, 5 , 7, 79, 20, 3, 0]
prime_numbers = list(filter(lambda n: isprime(n), numbers))
print(prime_numbers)