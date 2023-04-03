import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a DataFrame to store the data
data = pd.DataFrame({
    'Height (IN CMS)': [158, 158, 160, 160, 163, 163, 165, 165, 168, 170],
    'WEIGHT IN KO)': [58, 62, 60, 59, 61, 60, 61, 65, 66, 64],
    'T-SHIRT SIZE': ['M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L'],
    })

# Encode T-shirt size as numerical values
data['T-SHIRT SIZE'] = data['T-SHIRT SIZE'].replace({'M': 0, 'L': 1})

# Extract the input and output variables
X = data[['Height (IN CMS)', 'WEIGHT IN KO)']]
y = data['T-SHIRT SIZE']

# Create a LinearRegression object and fit the data
model = LinearRegression()
model.fit(X, y)

# Predict T-shirt size for a new customer with height 170 cm and weight 70 kg
new_customer = pd.DataFrame({'Height (IN CMS)': [170], 'WEIGHT IN KO)': [70]})
predicted_tshirt = model.predict(new_customer)

# Convert the predicted numerical value to the corresponding T-shirt size
if predicted_tshirt[0] == 0:
    print('Predicted T-shirt size: M')
else:
    print('Predicted T-shirt size: L')