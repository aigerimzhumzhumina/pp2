# Example 1
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Example 2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Example 3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# Example 4
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Example 5
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# Example 6
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Example 7
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Example 8
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Example 9
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Example 10
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Example 11
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Example 12
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Example 13
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

# Example 14
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Example 15
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Example 16
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Example 17
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Example 18
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Example 19
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

# Example 20
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Example 21
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

# Exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# Exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# Exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# Exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
