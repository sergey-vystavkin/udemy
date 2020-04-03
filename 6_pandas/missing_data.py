import numpy as np
import pandas as pd

dictionary = {'A': [1, 2, np.nan], 'B': [1, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(dictionary)   # Data Frame from dictionary

df_rows_without_nan = df.dropna()    # remove all rows with nan value
df_columns_without_nan = df.dropna(axis=1)  # remove all columns with nan value
df_with_two_not_nan = df.dropna(thresh=2)   # remove all rows which has more then two not nan values

df_with_replaced_nans = df.fillna(value='Nothing')  # replace all nan values

column_with_replaced_nans = df['A'].fillna(value=df['A'].mean())    # replace on middle value

print(column_with_replaced_nans)
