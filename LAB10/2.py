import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a DataFrame to store the data
data = pd.DataFrame({
    'Duration': [30, 30, 45, 45, 45, 60, 60, 60, 75, 75],
    'Average Pulse': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    'Max Pulse': [120, 120, 130, 130, 140, 140, 145, 145, 150, 150],
    'Caloric Damage': [240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
    'Hours Work': [10, 10, 8, 8, 0, 7, 7, 8, 0, 8],
    'Hours Sleep': [7, 7, 7, 7, 7, 8, 8, 8, 8, 8],
    })

# Extract the input and output variables
X = data[['Average Pulse']]
y = data['Caloric Damage']

# Create a LinearRegression object and fit the data
model = LinearRegression()
model.fit(X, y)

# Predict Caloric Damage for a new patient with an Average Pulse of 110
new_patient = pd.DataFrame({'Average Pulse': [110]})
predicted_calories = model.predict(new_patient)

print('Predicted Caloric Damage:', predicted_calories[0])