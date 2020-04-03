import pandas as pd
import numpy as np
import seaborn as sns   # If we import it lats will show in good looking format
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')

df1['A'].hist(bins=30)  # Make histogram
df1['A'].plot(kind='hist', bins=30)   # Make histogram
df1['A'].plot.hist(bins=30)   # Make histogram

df2.plot.area(alpha=0.4)    # Area of all values

df2.plot.bar()  # Barplot with indexes as category
df2.plot.bar(stacked=True)  # Each column values combine in one

df1.plot.line(x='A', y='B', figsize=(12, 3), lw=1)    # Lines graphic

df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')      # Dots graphic, c - add gradient color of values
df1.plot.scatter(x='A', y='B', s=df1['C'] * 100)    # Each dot will have a size depends of value

df2.plot.box()
df2[['a', 'b']].plot.box()

df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a', y='b', gridsize=25)   # gridsize - size of values

df2.plot.kde()
df2['a'].plot.kde()
df2['a'].plot.density() # Same as kde

plt.show()
