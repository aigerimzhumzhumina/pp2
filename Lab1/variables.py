#Example 1
"""
x=5 
y="John"
print(x)
print(y)
"""
#Example 2
"""
x=4  #x is of type int
x="Sally"  #x is of type str
print(x)
"""
#Casting
#Example 3
"""
x=str(3)  # x will be '3'
y=int(3)  # x will be 3
z=float(3) # x will be 3.0
"""
#Get the type
#Example 4
"""
x=5 
y="John"
print(type(x))
print(type(y))
"""
#String variables can be declared either by using single or double quotes:
#Example 5
"""
x="John"
is the same as
x='John'
"""
#Variable names are case-sensitive.
#Example 6
"""
a=4
A="Sally"
A will not overwrite a
"""
#Variable names
#Example 7
"""
Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""
#Multi Words Variable Names
#Example 8
"""
Camel Case:
myVariableName = "John"

Pascal Case:
MyVariableName = "John"

Snake Case:
my_variable_name = "John"
"""
#Many Values to Multiple Variables
#Example 9
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
#One Value to Multiple Variables
#Example 10
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
#Unpack a Collection
#Example 11
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
#Output Variables
#Example 12
"""
x="Python is awesome"
print(x)
"""
#Example 13
"""
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
"""
#Example 14
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
""" 
#Example 15
"""
x = 5
y = 10
print(x + y)
"""
#Example 16
"""
We can't combine a str and a number with the operator +
x = 5
y = "John"
print(x + y)

x = 5
y = "John"
print(x, y)

"""
#Global variables
#Example 17
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
"""
#Example 18
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
"""
#Example 19
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""
#Example 20
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""
#Exercise 1: Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"
#Exercise 2: Create a variable named x and assign the value 50 to it.
x = 50
#Exercise 3: Display the sum of 5 + 10, using two variables: x and y.

x = 5
y = 10
print(x + y)

#Exercise 4: Create a variable called z, assign x + y to it, and display the result.
x = 5
y = 10
z = x + y 
print(z)

#Exercise 5: Insert the correct syntax to assign values to multiple variables in one line:
x,y,z = "Orange", "Banana", "Cherry"

#Exercise 6: Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = "Orange"

#Exercise 7: Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
  global x
  x = "fantastic"

