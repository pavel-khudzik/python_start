# MAP
#print(list(map(int, "10 25".split()))) # int() and list() -> int(10), int(25)

# FILTER
"""
def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))
"""

# LAMBDA
"""
is_even = lambda x : x % 2 == 0
print("Function -", list(filter(is_even, [1, 2, 3, 4, 5, 6])))
print("Lambda   -", list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))


x = [
    ("Guido", "van", "Rossum"),
    ("Haskel", "Curry"),
    ("John", "Backus")
]

def length(name):
    return len(" ".join(name))

x.sort(key=length)
print(x)

x.sort(key=lambda name: len(" ".join(name)), reverse=True)
print(x)

"""

# OPERATOR
"""
import operator as op

x = [1, 2, 3]

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains(x, 4))

"""

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True