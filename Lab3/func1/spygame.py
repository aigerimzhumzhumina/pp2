def spy_game(mylist):
    net=0
    return '007' in ''.join(str(i) for i in mylist)

    for num in mylist:
        if num == 0:
            num += net 
            break 
        if num == 0 :
            num += net 
            break 
        if num == 7:
            return True
        else:
            return False  
            
        
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))