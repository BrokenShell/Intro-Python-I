"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

print(x + int(y))

# Write a print statement that combines x + y into the string value 57

print(str(x) + y)

"""
Saying 'Python is strongly typed' should be avoided in training materials.
It only confuses students and does not help understand Python.

If anything Python is dynamically typed, but unlike Javascript, 
Python will not coerce a variable of one type to another type for you.
THIS DOES NOT MAKE IT STRONGLY TYPED!
"""
