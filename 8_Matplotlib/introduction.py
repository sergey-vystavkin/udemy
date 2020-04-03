import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Functional method
# plt.plot(x, y)
# plt.plot(x, y, '-r')  # add red color
#
# plt.xlabel('X label')
# plt.ylabel('Y label')
# plt.title('My title')
#
# plt.subplot(1, 2, 1)    # Two plots on one canvas
# plt.plot(x, y, 'r')
# plt.subplot(1, 2, 2)
# plt.plot(y, x, 'b')



# Object oriented method

# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])   # Axe X and axe Y [left, bottom, width, high]
#
# axes.plot(x, y)
#
# axes.set_xlabel('X label')
# axes.set_ylabel('Y label')
# axes.set_title('My title 2')





fig = plt.figure()
axes_1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes_2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes_1.plot(x, y)
axes_1.set_title('Larger plot')

axes_2.plot(y, x)
axes_2.set_title('Smaller plot')

plt.show()

