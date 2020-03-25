import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
df_column = df['W']
df_column = df.W
type_series = type(df_column)
df_with_two_columns = df[['W', 'X']]
df['new_col'] = df['W'] + df['Y']

df_without_column = df.drop('new_col', axis=1)  # axis=1 mean that indexes in df is not in correct format
df.drop('new_col', axis=1, inplace=True)  # inplace=True mean that df will save without column
df_without_row = df.drop('A')

shape_tuple = df.shape  # (5, 4) rows, columns
row_series = df.loc['A']
row_series_by_index = df.iloc[1]

value = df.loc['B', 'Y']  # row, col

croped_df = df.loc[['A', 'B'], ['W', 'Y']]

bool_df = df < 0  # Is value negative

select_bool_df = df[bool_df]  # NaN if value has false bool
select_bool_df = df[df < 0]

bool_column = df['W'] < 0
df_filtered_by_one_column = df[df['Z'] < 0]

bool_df_with_and_operator = df[(df['W'] < 0) & (df['Y'] > 0)]  # condition with "and" operator
bool_df_with_or_operator = df[(df['W'] < 0) | (df['Y'] > 0)]  # "or"

df_reset_index = df.reset_index()  # add to df new column "index" with current indexes and make default indexes

new_indexes = ['CA', 'NY', 'WY', 'OR', 'CO']
df['States'] = new_indexes  # Add new column to df
df_with_new_indexes = df.set_index('States')  # Set column to be index

#   Index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])  #   df with two levels index
one_half_df = df.loc['G1']   # Get section
first_row_of_one_half_df = df.loc['G1'].loc[1]

df.index.names = ['Group', 'Num']   # Set names of index groups
value = df.loc['G1'].loc[2]['B']    # Get value

one_half_df = df.xs('G1')   # Get section
first_rows_df = df.xs(1, level='Num')   # Get first rows from each section


print(df)
