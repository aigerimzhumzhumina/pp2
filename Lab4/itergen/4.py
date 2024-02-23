def squares(a, b):
    while a <= b:
        yield a**2
        a+=1
a = int(input())
b = int(input())
for square in squares(a,b):
    print(square, end = ' ')