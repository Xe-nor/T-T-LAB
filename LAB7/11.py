import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([8,12,11,5,14,3,6,8,4,9])
y = np.array([25,35,29,24,38,12,18,27,17,30])

# Fit linear regression
coefficients = np.polyfit(x, y, 1)
m = coefficients[0]
b = coefficients[1]
regression_line = m*x + b

# Plot data points and regression line
plt.scatter(x, y)
plt.plot(x, regression_line, color='red')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')

# Display plot
plt.show()
