#Example 1
"""
print("Hello")
print('Hello')
"""
#Example 2
"""
a = "Hello"
print(a)
"""
#Example 3

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example 4
"""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
"""
#Strings are arrays
"""
a="Hello, World!"
print(a[1])
"""
#Looping Through a String
"""
for x in "banana":
    print(x)
"""
#String Length
"""
a="hello, world!"
print(len(a))
"""
#Check String
"""
txt = "The best things in life are free!"
print("free" in txt)
"""
"""
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")
"""
#Check if NOT
"""
txt = "The best things in life are free!"
print("expensive" not in txt)
"""
"""
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")
"""
#Slicing
"""
b = "Hello, World!"
print(b[2:5])
"""
#Slice from the start
"""
b = "Hello, World!"
print(b[:5])
"""
#Slice to the end
"""
b = "Hello, World!"
print(b[2:])
"""
#negative indexing
"""
b = "Hello, World!"
print(b[-5:-2])
"""
#Upper Case
"""
a = "Hello, World!"
print(a.upper())
"""
#Lower Case
"""
a = "Hello, World!"
print(a.lower())
"""
#Remove Whitespace
"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
"""
#Replace string
"""
a = "Hello, World!"
print(a.replace("H", "J"))
"""
#Split string
"""
a = "Hello, World!"
print(a.split(","))
"""
#String Concatenation 
"""
a = "Hello"
b = "World"
c = a + b
print(c)
"""
"""
a = "Hello"
b = "World"
c = a + " " + b
print(c)
"""
#String format
"""
age = 36
txt = "My name is John, I am" + age 
print(txt)
"""
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
"""
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""
#Escape Character
"""
txt = "We are the so-called "Vikings" from the north."
"""
"""
txt = "We are the so-called \"Vikings\ from thr north."
"""
#Exercise 1: Use the len function to print the length of the string.
x = "Hello, World"
print(len(x))
#Exercise 2: Get the first character of the string txt.
txt = "Hello, World"
x = txt[0]
#Exercise 3: Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
#Exercise 4: Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
#Exercise 5:Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
#Exercise 6: Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
#Exercise 7: Replace the character H with a J.

txt = "Hello World"
txt = txt.replace("H", "J")
#Exercise 8: Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


