def ispalindrome(string):
    string1 = ''.join(reversed(string))
    if string1 == string:
        return True 
    else:
        return False 

print(ispalindrome('madam'))