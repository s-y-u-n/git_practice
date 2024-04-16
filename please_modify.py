import numpy as np

def square_input(x):
    return np.square(x)

def cube_input(x):
    return np.power(x, 3)

input = 3.5
output = square_input(input)
print(output)