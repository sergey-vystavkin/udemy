import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips') # Make Data Frame with columns: total_bill, tip, sex, smoker, day, time, size
flights = sns.load_dataset('flights') # Make Data Frame with columns: year, month, passengers

tc_correlation_data = tips.corr()

sns.heatmap(tc_correlation_data)    # Matrix plot
sns.heatmap(tc_correlation_data, annot=True)    # Add values annotation to plot
sns.heatmap(tc_correlation_data, cmap='coolwarm')   # Change color of presentation (coolwarm , magma)


fp_pivot_table = flights.pivot_table(index='month', columns='year', values='passengers')

sns.heatmap(fp_pivot_table)
sns.heatmap(fp_pivot_table, cmap='magma', linecolor='white', linewidths=1)  # Add separation

sns.clustermap(fp_pivot_table)  # Similar columns and rows place near each other

plt.show()