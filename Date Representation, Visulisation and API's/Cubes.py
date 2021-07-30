import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set up chart title and label axis
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set range for each axis
ax.axis([0, 5100, 0, 5000**3 + 1000**3])

plt.show() m