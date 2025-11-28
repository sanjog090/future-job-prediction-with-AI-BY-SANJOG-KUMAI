# main.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from fastapi import FastAPI

# ---------------------
# 1️⃣ ML Model
# ---------------------
data = pd.read_csv("data.csv")

X = data[["python", "java", "html", "css", "ml", "experience"]]
y = data["job"]

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_job(python, java, html, css, ml, experience):
    input_data = [[python, java, html, css, ml, experience]]
    prediction = model.predict(input_data)[0]
    return prediction

# ---------------------
# 2️⃣ FastAPI
# ---------------------
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Predictor API is running"}

@app.post("/predict")
def get_prediction(data: dict):
    python = data.get("python", 0)
    java = data.get("java", 0)
    html = data.get("html", 0)
    css = data.get("css", 0)
    ml = data.get("ml", 0)
    experience = data.get("experience", 0)

    result = predict_job(python, java, html, css, ml, experience)

    return {"predicted_job": result}
