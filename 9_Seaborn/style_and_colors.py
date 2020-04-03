import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # Make Data Frame with columns: total_bill, tip, sex, smoker, day, time, size

sns.set_style('white')  # Change background or set ticks (white, dark, whitegrid, darkgrid, ticks)

plt.figure(figsize=(12, 3))     # Change size of figures

sns.set_context('notebook', font_scale=1)    # Change context (paper, notebook, talk, poster) and it size

sns.countplot(x='sex', data=tips, palette='seismic')

sns.despine()   # Remove right spine and top spine
sns.despine(left=True, bottom=True, top=False)  # Remove each beside top side


plt.show()
