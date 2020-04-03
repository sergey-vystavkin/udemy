import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips') # Make Data Frame with columns: total_bill, tip, sex, smoker, day, time, size
iris = sns.load_dataset('iris') # Make Data Frame with columns: sepal_length, sepal_width, petal_length, petal_width, species

sns.pairplot(iris)
pair_plot = sns.PairGrid(iris)  # Same with pairplot, but need setting manually
pair_plot.map(plt.scatter)
# OR
pair_plot.map_diag(sns.distplot)    # Set different kinds in different place
pair_plot.map_upper(plt.scatter)
pair_plot.map_lower(sns.kdeplot)


tip_facet_grid = sns.FacetGrid(data=tips, col='time', row='smoker')
tip_facet_grid.map(sns.distplot, 'total_bill')
tip_facet_grid.map(plt.scatter, 'total_bill', 'tip')


plt.show()



