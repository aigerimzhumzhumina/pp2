def ispalindrome(s):
    s_r = ''.join(reversed(s))
    if s == s_r:
        return True 
    else:
        return False
s = input()
print(ispalindrome(s))