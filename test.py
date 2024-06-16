import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Sample Data')

# Add a title and labels
plt.title('Example Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Add a legend
plt.legend()

# Show the plot
plt.show()
