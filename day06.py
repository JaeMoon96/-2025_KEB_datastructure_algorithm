import numpy as np

narray = np.array([1, 3.1, 2, 9])
print(type(narray), type(narray[2]), type(narray[3]))

array = [9, -11, '8', 7]
print(array[0], array[1], array[2], array[3])
print(type(array), type(array[2]), type(array[3]))
print(id(array[0]),id(array[1]),id(array[2]),id(array[3]))