# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Generate some example data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # Generate 100 random values for X
y = 4 + 3 * X + np.random.randn(100, 1)  # Generate y based on a linear relationship with noise

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Get the slope (coefficient) and intercept
slope = model.coef_[0][0]  # Get the slope (coefficient) of the linear regression model
intercept = model.intercept_[0]  # Get the intercept of the linear regression model

# Calculate the predicted values
y_pred = model.predict(X)  # Predict y values based on the linear regression model

# Calculate R-squared
r2 = r2_score(y, y_pred)  # Calculate R-squared using the predicted and actual y values

# Print the results
print("Slope (Coefficient):", slope)
print("Intercept:", intercept)
print("R-squared:", r2)

# Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Actual data')  # Plot the actual data points
plt.plot(X, y_pred, color='red', linewidth=2, label='Linear regression')  # Plot the linear regression line
plt.xlabel('X')  # La
