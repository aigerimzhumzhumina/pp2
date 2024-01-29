#Getting the data type
"""
x=5
print(type(x))
"""
#Example 2
"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	

"""
#Example 3
"""
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""
#Exercise 1: The following code example would print the data type of x, what data type would that be?
x = 5
print(type(x)) 
#answer: int

#Exercise 2: The following code example would print the data type of x, what data type would that be?
x = "Hello, World!"
print(type(x))
#answer: str

#Exercise 3: The following code example would print the data type of x, what data type would that be?
x = 20.5
print(type(x))
#float

#Exercise 4:The following code example would print the data type of x, what data type would that be?
x = ["apple", "banana", "cherry"]
print(type(x))
#list

#Exercise 5: The following code example would print the data type of x, what data type would that be?
x = ("apple", "banana", "cherry")
print(type(x))
#tuple

#Exercise 6: The following code example would print the data type of x, what data type would that be?
x = {"name":"John", "age": 36}
print(type(x))
#dict

#Exercise 7: The following code example would print the data type of x, what data type would that be?
x = True 
print(type(x))
#bool
