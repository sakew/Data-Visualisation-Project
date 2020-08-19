import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]


plt.title('Cubes', fontsize = 20)
plt.xlabel('Value', fontsize = 10)
plt.ylabel('Cube of Value', fontsize = 10)

plt.scatter(x_values, y_values, s = 60, edgecolors='none',c = y_values, cmap=plt.cm.BuGn)
plt.axis([0, 5100, 0, 5100**3])


plt.show()