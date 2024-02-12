def has_33(mylist):
    for i in range (len(mylist)-1):
        if mylist[i] == 3 and mylist[i] == mylist[i+1]:
            return True 
    return False
print(has_33([1, 3, 3]))
print(has_33([3, 1, 3]))
print(has_33([1,3,1,3]))
