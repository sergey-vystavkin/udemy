import numpy as np
from numpy.random import randint

my_list = [1, 2, 3]

arr = np.array(my_list)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mat = np.array(my_mat)

arange = np.arange(1, 10, 3)

zeros_arr = np.zeros(5)
zeros_mat = np.zeros((5,5))
ones_arr = np.ones(5)

divide_equal_parts = np.linspace(2, 10, 3)
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""
sq = np.eye(5)

rand_arr = np.random.rand(5)
rand_mat = np.random.rand(5,5)
rand_arr_with_negative = np.random.randn(5)
rand_integer = np.random.randint(5, 10)
rand_integer_arr = np.random.randint(5, 10, 10)

arr_for_example = np.arange(1, 65)
chess_desk = arr_for_example.reshape(8, 8)

highest = arr_for_example.max()
highest_idx = arr_for_example.argmax()
lowest = arr_for_example.min()
lowest_idx = arr_for_example.argmin()

type_of_data = arr_for_example.dtype

shape_of_array = arr_for_example.shape

print(arr_for_example.dtype)
