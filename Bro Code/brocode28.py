# *args = parameter that will pack all arguments into a tuple

def add(*args):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))