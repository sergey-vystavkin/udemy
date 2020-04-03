import pandas as pd

# Concatenation

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[1, 2, 3, 4])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[1, 2, 3, 4])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[1, 2, 3, 4])

conctenated_df = pd.concat([df1, df2, df3])  # Concat all df in one
conctenated_df = pd.concat([df1, df2, df3], axis=1) # Replace rows and columns

# Mergin

left_df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right_df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                         'C': ['C8', 'C9', 'C10', 'C11'],
                         'D': ['D8', 'D9', 'D10', 'D11']})

merged_df = pd.merge(left_df, right_df, how='inner', on='key')  # merge df by "key" column

left_df = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right_df = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                         'key2': ['K0', 'K0', 'K0', 'K0'],
                         'C': ['A0', 'A1', 'A2', 'A3'],
                         'D': ['B0', 'B1', 'B2', 'B3']})

merged_df = pd.merge(left_df, right_df, on=['key1', 'key2'])  # merge df by two "key" columns
merged_df = pd.merge(left_df, right_df, how='outer', on=['key1', 'key2'])
merged_df = pd.merge(left_df, right_df, how='right', on=['key1', 'key2'])
merged_df = pd.merge(left_df, right_df, how='left', on=['key1', 'key2'])

# Joining

left_df = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                        'B': ['B0', 'B1', 'B2']},
                       index=['K0', 'K1', 'K2'])

right_df = pd.DataFrame({'C': ['A0', 'A1', 'A2'],
                        'D': ['B0', 'B1', 'B2']},
                       index=['K0', 'K2', 'K3'])

joined_df = left_df.join(right_df)  # inner join
joined_df = left_df.join(right_df, how='outer')

print(left_df)
print(joined_df)
