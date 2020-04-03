import cufflinks as cf   # it connect plotly with pandas
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# DATA
df1 = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})
df3 = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 20, 10], 'z': [500, 400, 300, 200, 100]})


# init_notebook_mode(connected=True)  # connect JavaScript and notebook

cf.go_offline() # For using cufflinks offline


# df1.iplot() # Interactive plot
# df1.iplot(kind='scatter', x='A', y='B', mode='markers') # mode - graphic mode with dots
#
# df2.iplot(kind='bar', x='Category', y='Values') # Interactive barplot
#
# # If there are many values, get them group
# df1.count().iplot(kind='bar')
# df1.sum().iplot(kind='bar')
#
# df1.iplot(kind='box')
#
# fig = df3.iplot(asFigure=True, kind='surface', colorscale='rdylbu')   # surface plot
#
# df1['A'].iplot(asFigure=True, kind='hist', bins=50)
#
# df1[['A', 'B']].iplot(kind='spread')
#
# df1.iplot(kind='bubble', x='A', y='B', size='C')

df1.scatter_matrix()

plt.show()