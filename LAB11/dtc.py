import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("C:/Users/amare/OneDrive/Documents/vscode/6TH SEM/T&T LAB/LAB11/data.csv")

data = pd.get_dummies(data, columns=['age', 'income', 'student', 'credit_rating'])

data.head()

X = data.drop('buys_computer', axis=1)
y = data['buys_computer']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy*100)

