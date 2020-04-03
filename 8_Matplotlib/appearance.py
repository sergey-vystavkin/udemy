import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color='orange')  # put color
ax.plot(x, y, color='#FF8CC0')  # RGB HEX format
ax.plot(x, y, color='black', alpha=0.2)  # set transparency

ax.plot(x, y, linewidth=5)  # line width cof (current * 5)
ax.plot(x, y, lw=5)

ax.plot(x, y,
        linestyle='steps')  # styles support: '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
ax.plot(x, y, ls='steps')

ax.plot(x, y, marker='o')  # set dot on each value (divide line on short lines)
ax.plot(x, y, marker='*', markersize=10)  # change size of marker
ax.plot(x, y, marker='*', markersize=10, markerfacecolor='yellow')
ax.plot(x, y, marker='*', markerfacecolor='yellow', markeredgewidth=4, markeredgecolor='red')  # set border

ax.set_xlim([0, 1])  # X limit, it's like zoom
ax.set_ylim([0, 2])  # Y limit

# Plot types
plt.scatter(x, y)

from random import sample

data = sample(range(1, 1000), 100)
plt.hist(data)

# rectangular box plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)


plt.style.use('ggplot') # Use custom style from plt library


plt.show()
