def unique(firstlist):
    uniquelist = []
    for x in firstlist:
        if x not in uniquelist:
            uniquelist.append(x)
    return uniquelist 
firstlist = [2, 5, 44, 7, 2, 57, 44]
uniquelist = unique(firstlist)
print(uniquelist)