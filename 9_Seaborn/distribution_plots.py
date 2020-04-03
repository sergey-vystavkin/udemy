import seaborn as sns
import matplotlib.pyplot as plt



tips = sns.load_dataset('tips') # Make Data Frame with columns: total_bill, tip, sex, smoker, day, time, size

sns.distplot(tips['total_bill'])    # Make histogram
sns.distplot(tips['total_bill'], kde=False) # Histogram without line

sns.distplot(tips['total_bill'], bins=110)   # count of parts of histogram

sns.jointplot(x='total_bill', y='tip', data=tips) # Compare two columns
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')   # Change type of representation(hex, reg, kde)

sns.pairplot(tips)  # visual all numeric data between each other
sns.pairplot(tips, hue='sex')   # divide data on categories
sns.pairplot(tips, hue='sex', palette='coolwarm')   # colors for categories

sns.rugplot(tips['total_bill']) # graphic with one high dashes

sns.kdeplot(tips['total_bill']) # graphic with one line

plt.show()

