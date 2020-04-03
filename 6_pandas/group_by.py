import numpy as np
import pandas as pd

dictionary = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
              'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
              'Sales': [200, 124, 340, 124, 243, 350]}

df = pd.DataFrame(dictionary)
by_company = df.groupby('Company')

df_with_mean_values = by_company.mean() # Group all numeric columns by mean,
df_with_sum_values = by_company.sum() # column whch you group by will be as index column
df_with_std_values = by_company.std()
df_with_count_values = by_company.count()
df_with_max_values = by_company.max()
df_with_min_values = by_company.min()



correlation_df = df[['Company', 'Person']].corr()   # Corelation between two columns

df_group_by_hole_methods = by_company.describe()    # Group by hole methods, add new index group with count,mean...
df_group_by_hole_methods_invert = by_company.describe().transpose() # Columns and index replaced 

print(correlation_df)

