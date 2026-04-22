from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import numpy as np
import joblib
import os

app = FastAPI()

# 
model = joblib.load(os.path.join("model", "titanic_pipeline.pkl"))
print("Model Loaded Successfully 🚀")


# 
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Titanic Predictor</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-dark text-white">

    <div class="container mt-5">
        <h1 class="text-center mb-4">🚢 Titanic Survival Predictor</h1>

        <form action="/predict_form" method="post" class="card p-4 bg-secondary">

            <div class="mb-3">
                <label>Sex (0=Female, 1=Male)</label>
                <input class="form-control" name="Sex">
            </div>

            <div class="mb-3">
                <label>Fare</label>
                <input class="form-control" name="Fare">
            </div>

            <div class="mb-3">
                <label>Pclass (1-3)</label>
                <input class="form-control" name="Pclass">
            </div>

            <div class="mb-3">
                <label>Age</label>
                <input class="form-control" name="Age">
            </div>

            <div class="mb-3">
                <label>FamilySize</label>
                <input class="form-control" name="FamilySize">
            </div>

            <div class="mb-3">
                <label>SibSp</label>
                <input class="form-control" name="SibSp">
            </div>

            <div class="mb-3">
                <label>Parch</label>
                <input class="form-control" name="Parch">
            </div>

            <div class="mb-3">
                <label>IsAlone (0/1)</label>
                <input class="form-control" name="IsAlone">
            </div>

            <div class="mb-3">
                <label>Embarked_S</label>
                <input class="form-control" name="Embarked_S">
            </div>

            <div class="mb-3">
                <label>Embarked_Q</label>
                <input class="form-control" name="Embarked_Q">
            </div>

            <button class="btn btn-primary w-100">Predict</button>

        </form>
    </div>

    </body>
    </html>
    """


# 
@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(
    Sex: int = Form(...),
    Fare: float = Form(...),
    Pclass: int = Form(...),
    Age: float = Form(...),
    FamilySize: int = Form(...),
    SibSp: int = Form(...),
    Parch: int = Form(...),
    IsAlone: int = Form(...),
    Embarked_S: int = Form(...),
    Embarked_Q: int = Form(...)
):

    features = np.array([[
        Sex, Fare, Pclass, Age, FamilySize,
        SibSp, Parch, IsAlone, Embarked_S, Embarked_Q
    ]])

    prediction = model.predict(features)[0]

    result = "Survived 🚢" if prediction == 1 else "Did NOT survive 💀"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Result</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-dark text-white text-center">

        <div class="container mt-5">
            <h1 class="mb-4">Prediction Result</h1>

            <div class="alert alert-info">
                <h2>{result}</h2>
            </div>

            <a href="/" class="btn btn-light">🔙 Back</a>
        </div>

    </body>
    </html>
    """