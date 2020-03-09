import numpy as np

arr = np.arange(0, 11)

third_item = arr[3]

array_slice = arr[1:5]

arr[1:5] = 25   # Assign all digits in slice

arr_copy = arr.copy()   # Should do always because you can change data in first array


arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_item = arr_2d[0][0]   # row, column
first_item = arr_2d[0, 0]   # row, column

slice_2d_array = arr_2d[1:, 1:]   # rows slice, columns slice

arr_of_booleans = arr > 5

filtered_array = arr[arr_of_booleans]
filtered_array = arr[arr > 5]



