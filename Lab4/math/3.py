import math
s = int(input())
n = int(input())
a = s/(2*math.tan((math.pi)/n))
area = (s*n*a)/2
print(int(area))