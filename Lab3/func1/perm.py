from itertools import permutations 
def printperms():
    word = input()
    perm = permutations(word)
    for p in perm:
        print(''.join(p))
printperms()