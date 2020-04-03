import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2)

# If one plot
axes.plot(x, y)

# If there are few subplots
for current_ax in axes:
    current_ax.plot(x, y)

# Or only one ax
axes[0].plot(x, y)
axes[0].set_title('First Plot')
axes[1].plot(y, x)
axes[1].set_title('Second Plot')

size_fig = plt.figure(figsize=(8, 4), dpi=100)  # figsize(width, high), dpi is scale or window size
ax = size_fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)

size_fig.savefig('my_picture.png')  # Saving support formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, label='X Squared') # label needs for legend of plot
ax.plot(x, x**3, label='X Cubed')

ax.legend(loc=0)    # loc is code of location, 0 mean - best location
ax.legend(loc=(0.1, 0.2))   # you can also write size manually (left, bottom)

plt.tight_layout()  # Better view
plt.show()
