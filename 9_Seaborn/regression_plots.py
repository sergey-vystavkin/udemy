import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # Make Data Frame with columns: total_bill, tip, sex, smoker, day, time, size


sns.lmplot(x='total_bill', y='tip', data=tips)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], # Separate markers
           scatter_kws={'s': 100})  # Change size of markers

# Separate columns and rows
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time',
           aspect=0.6, size=8)    # Change size of each separate plot



