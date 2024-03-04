def isuplow(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    return upper, lower

string = input()
print(isuplow(string))
        
