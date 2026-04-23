# Titanic Project
# 🚢 Titanic Survival Prediction

## 📌 Project Overview
This project predicts whether a passenger survived the Titanic disaster using Machine Learning.

The model takes user input (like age, gender, fare, etc.) and returns a prediction.

---

## 🧠 Model
- Algorithm: Random Forest Classifier
- Built using: Scikit-learn
- Saved using: Joblib

---

## 📊 Features Used
- Sex
- Fare
- Pclass
- Age
- FamilySize
- SibSp
- Parch
- IsAlone
- Embarked_S
- Embarked_Q

---

## 🚀 How to Run

### 1) Install dependencies
pip install fastapi uvicorn numpy joblib scikit-learn

### 2) Run the server
uvicorn main:app --reload

### 3) Open in browser
http://127.0.0.1:8000

---

## 🎯 Prediction Output
- Survived 🚢
- Did NOT survive 💀

---

## 💡 Future Improvements
- Improve model accuracy
- Add frontend UI
- Deploy online

---

🚀 Live Demo  
Try the model here:  

👉 https://titanic-project-production.up.railway.app

## 👨‍💻 Author
Mostafa
