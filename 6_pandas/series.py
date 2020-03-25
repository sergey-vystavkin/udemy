import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

series = pd.Series(data=my_data)
series = pd.Series(arr)
series_with_another_index = pd.Series(data=my_data, index=labels)
series_with_index_as_dict_key = pd.Series(d)
series_with_functions_obj = pd.Series(data=[sum, print, len])

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Japan', 'Germany', 'USSR'])
print(ser1['USA'])
ser2 = pd.Series([1, 2, 3, 4], ['USA', 'Japan', 'Germany', 'Italy'])
series_sum = ser1 + ser2

print(ser1)
