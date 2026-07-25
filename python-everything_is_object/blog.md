# Python3: Mutable, Immutable... everything is object!
---
# Introduction
What is an object? this is a question i've asked myself many times while learning python, why and how different pieces of 
data are saved, or why doesnt it always work as im expecting it to? 


This is the "fun" part of python, eveything in python is an object. Its stored somewhere in memory, has a type and a value.
Some which are mutable and some immutable, but whats the different you may ask. Mutable objects are ones that you can change after
you create and initialize them, while immutable objects you cant change them once initialized. Though will go more indepth on each of these later, with learning and knowing
the difference between ```is``` and ```==```.


```==```, check if the objects have the same data/contents.

```is```, checks if the objects have the same Id (Same place in memory).

```
>>> list1 = [1, 2, 3]
>>> list2 = [1, 2, 3]
>>> print(list1 == list2)
True
>>> print(list1 is list2)
False
```

list1 and list2 both have the same data/contents, but have a different location in memory, I will go more into this later.

# Type and ID
Every object and a Type and an ID, you can test this simply like so:
```
>>> x = 123
>>> print(type(x))
<class 'int'>
>>> print(id(x))
140711789515704
```
Type, its your data type or class of the object, these can range from int, str, list, bool, etc.. in python you dont have to declare the type like other languages,
it self assigns the data type of the object when created or updated.


Id, its a unique id that represents the memory address of the object. This will be evident later, you can have 2 different objects have the exact same value
but its Id will be different, as its independent of that object but has the same value. BUT two different variables can also use the same id, even though they are assigned
a different variable name.


# Mutable Objects
Whats mutable mean? simply put, it means its an objects value that can be modified and changed after created, keeping the same Id.

A good example of this would be the following:
```
>>> list1
[1, 2, 3]
>>> id(list1)
2810460909504
>>> type(list1)
<class 'list'>
>>> list1.append(4)
>>> list1
[1, 2, 3, 4]
>>> type(list1)
<class 'list'>
>>> id(list1)
2810460909504
```
This shows how mutable objects work, the id of both the list NEVER changed, i edited and made the list longer, but the lists location
in the memory never changed. 

# Immutable Objects
Whats immutable mean?it means the object can never be changed once created. It may seem its being changed, but its location in memory
is actually different, meaning that its actually a new object, its not the one you originally had.

A good example of this would be the following:

```
>>> a = 92
>>> id(a)
140711789514712
>>> type(a)
<class 'int'>
>>> a += 7
>>> a
99
>>> type(a)
<class 'int'>
>>> id(a)
140711789514936
```
As you can see, the id of a changed, this is because when we changed the value of a, it remade the variable at a different memory address.

# Why does it matter?

Because knowing what can see what within your code and how it interacts with another!

Knowing what kind of object your dealing with is important, because of how different interactions work. As you have different functions and definitions, certain 
objects wont keep there "original value", so know when a value changes and how is important. When you pass an argument into a function using an object, a new reference to the same object is actually being pass through,
if the object is mutable the function will change it and keep the Id. If immutable, any change inside actually creates a new object with a new memory using the variable passed throughs values.

It can be seen in following:
```
def add(b):
  b += 1
  print(b)

a = 6
add(a)
print(a)
```
You are using the variable a = 6 the whole time, so SURELY when you run this, it will print 7 both time?

Well you would be wrong, it would print 6, 7.

This is because its immutable, your creating a new object with ``` b += 1```, if we were to check the id, it would produce two different memory locations.





