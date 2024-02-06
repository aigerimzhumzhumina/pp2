# Example 1
thislist = ["cat", "penguin", "rabbit"]
print(thislist)

# Example 2
thislist = ["cat", "penguin", "rabbit", "horse", "penguin"]
print(thislist)

# Example 3
thislist = ["cat", "penguin", "rabbit"]
print(len(thislist))

# Example 4
list1 = ["cat", "penguin", "rabbit"]
list2 = [98348, 0.38383, -100000]
list3 = [True, None, False]

# Example 5
mylist = [98348, 0.38383, -100000]
print(type(mylist))

thislist = list(("cat", "penguin", "rabbit"))
print(thislist)

# Example 6
mylist = [98348, 0.38383, -100000]
print(mylist[0], mylist[-1])

# Example 7
thislist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(thislist[4:8], thislist[:6], thislist[3:], thislist[-4:-1])

# Example 8
thislist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 6 in thislist:
    print("Yes, 6 is in the numbers list")

# Example 9
mylist = [98348, 0.38383, -100000, 8888, 12345]
mylist[4]=0 
mylist[1:3] = [222, -100]
print(mylist) 

# Example 10
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Example 11
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Example 12
thislist = ["blue", "red", "yellow"]
thislist.insert(2, "white")
print(thislist)

# Example 13
thislist = [1, 37, 89, 0, 87]
thislist.append("sun")
print(thislist)

# Example 14
thislist = [66, 88, 10, 5]
mylist = ['water', 'apple', 'sky', 'math']
thislist.extend(mylist)
print(thislist)

# Example 15
mylist = ['sun', 'rock', 'sea']
thistuple = ('banana', 'tea')
thislist.extend(thistuple)
print(thislist)

# Example 16
mylist = [34, 25, 5, 98, 5]
mylist.remove(34)
mylist.remove(5)
print(mylist)

# Example 17
thelist = ['cake', 'soup', 'bread', 'water', 'chips']
thelist.pop(0)
thelist.pop()
del thislist[3]
print(thelist)

# Example 18
thelist = ['cake', 'soup', 'bread', 'water', 'chips']
del thelist 

# Example 19
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Example 20
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Example 21
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Example 22
thislist = ["apple", "banana", "cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i==i+1

# Example 23
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Example 24
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Example 25
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Example 26
newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in range(10)]

# Example 27
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

# Example 28
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Example 29
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Example 30
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Example 31
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Example 32
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Example 33
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Example 34
#1st way
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#2nd way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#3rd way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# Exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
# Exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# Exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
# Exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# Exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
# Exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# Exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))