# Example 1
print(10>9)
print(10==9)
print(10<9)

# Example 2
a = 200
b = 33
if b > a:
    print("b is  greater than a")
else:
    print("b is not greather than a")

# Example 3
print(bool("hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))

# Example 4
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
 
# Example 5
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Example 6
def myfunction():
    return True 
print(myfunction())

# Example 7
def myFunction():
    return True 
if myFunction():
    print("YES!")
else:
    print("NO!")

# Example 8
x = 2938479
print(isinstance(x, int))

# Exercise 1-5: The statement below would print a Boolean value, which one?
print(10 > 9) # True

print(10==9) # False

print(10 < 9) # False
 
print(bool("abc")) # True

print(bool(0)) # False

