import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips') # Make Data Frame with columns: total_bill, tip, sex, smoker, day, time, size

sns.barplot(x='sex', y='total_bill', data=tips) # get mean bill of each category
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)   # choose a function which will be account

sns.countplot(x='sex', data=tips)   # Count of each category

sns.boxplot(x='day', y='total_bill', data=tips) # Boxes graphic
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker') # Boxes graphic divided on different categories

sns.violinplot(x='day', y='total_bill', data=tips)  # Graphic like violin
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)   # Split mean that violin will be have two different halfs depands of category

sns.stripplot(x='day', y='total_bill', data=tips)   # Graphic with dots in one line
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)  # Add random noise
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)  # Divide columns by category


sns.swarmplot(x='day', y='total_bill', data=tips, color='black')   # Graphic combination of stipplot and violinplot

sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')  # General plot where we can set all kinds of plot (bar, violin)

plt.show()
