import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("data.csv")

# Features (all skill columns + experience)
X = data[["python", "java", "html", "css", "ml", "experience"]]

# Target
y = data["job"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function
def predict_job(python, java, html, css, ml, experience):
    input_data = [[python, java, html, css, ml, experience]]
    prediction = model.predict(input_data)[0]
    return prediction
