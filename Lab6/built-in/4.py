import time 
import math
x = int(input())
ms = int(input())
time.sleep(ms/1000)
def square(x):
    return math.sqrt(x)
print(f'Square root of {x} after {ms} miliseconds is {square(x)}')