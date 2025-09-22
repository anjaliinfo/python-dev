#This is a comment
if 5 > 2:
 print("Five is greater than two!")

x = 5
y = "John"
print(x)
print(y)


#Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = 5
print(type(x)) 

# Write a function that:
# 1. Takes a list of integers.
# 2. Removes duplicates.
# 3. Returns them in ascending order.