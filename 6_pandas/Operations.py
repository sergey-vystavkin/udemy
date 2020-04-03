import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

unique_arr = df['col2'].unique()
number_of_unique_arr = df['col2'].nunique()
counts_of_each_value = df['col2'].value_counts()  # value will be as index

filter_df = df[df['col1'] > 2]  # Get all rows where value in col1 greater then 2
filter_df_two_conditions = df[(df['col1'] > 2) & (df['col2'] == 444)]


def times(x):
    return x * 2


column_with_two_times_vales = df['col1'].apply(times)
len_of_each_value = df['col3'].apply(len)
column_with_two_times_vales_lamb = df['col2'].apply(lambda x: x * 2)
trim_each_value = df['col3'].apply(lambda x: x.strip())

df_without_col = df.drop('col2', axis=1)

column_names = df.columns
range_of_index = df.index

sorted_df = df.sort_values('col2')

bools_df = df.isnull()

# Pivot Table

df1 = pd.DataFrame({'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
                    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
                    'C': ['x', 'y', 'x', 'y', 'x', 'y'],
                    'D': [1, 3, 2, 5, 4, 1]})

pivot_table_of_df = df1.pivot_table(values='D', index=['A', 'B'], columns=['C'])

print(pivot_table_of_df)
