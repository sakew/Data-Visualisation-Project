import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

# Set the chart title and label axes.

plt.title("Square Numbers", fontsize = 12)

plt.xlabel("Value", fontsize = 15)
plt.ylabel("Square of Value", fontsize = 15)

# Set size of tick labels.
plt.tick_params(axis = 'both', labelsize = 12)

plt.show()