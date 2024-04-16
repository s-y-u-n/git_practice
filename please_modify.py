import numpy as np

def square_input(x):
    return np.square(x)

def return_negative(x):
    return -x

input = 3.5
output_1 = square_input(input)
output_2 = return_negative(input)
print(output_1)
print(output_2)