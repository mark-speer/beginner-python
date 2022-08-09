# Python is completely object oriented, and not "statically typed". You do not need to declare variables before using, or declare their type.
# Every variable in Python is an object

# NUMBERS
# Python supports two types of numbers - 
# Integers - Whole numbers
# Floating Point Numbers - Decimals

# Defining integers
myint = 7
print(myint)

# Defining floating point numbers

myfloat = 7.0
print(myfloat)

# or

myfloat = float(7)
print(myfloat)

# STRINGS

# Strings are defined either with a single quote or a double quote.

mystring = 'hello'
print(mystring)

# or

mystring = "hello"
print(mystring)

# Double quotes make it easier to include apostrophes

mystring = "Don't worry about apostrophes"
print(mystring)

# Simple operators can be executed on numbers and strings - 

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line like -

a, b = 3, 4
print(a, b)

# Mixing operators between numbers and strings is not supported

# this will not work
one = 1
two = 2
hello = "hello"

print(one + two + hello)

