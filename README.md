# ❤️ Heart Disease Prediction Web App

A professional **Machine Learning Web Application** that predicts the likelihood of heart disease using patient medical data.
Built with **Flask**, **HTML/CSS**, and a trained **Machine Learning model**, this project is ready for local use and cloud deployment on **Render**. 🚀

---

## 📌 Project Overview

This application allows users to enter patient health details such as:

* Age
* Blood Pressure
* Cholesterol
* Heart Rate
* ECG Results
* Other clinical parameters

The system uses a trained Machine Learning model (`model.pkl`) to predict whether the patient is at:

* ❤️ **High Risk of Heart Disease**
* 💚 **Low Risk of Heart Disease**

---

## 🖼️ Project Preview

![Heart Disease Prediction Banner]<img width="1881" height="896" alt="Screenshot 2026-05-01 195341" src="https://github.com/user-attachments/assets/030330dd-8694-4c88-a933-78f564829d06" />


> Professional healthcare prediction interface powered by Machine Learning 🏥🤖

---

## ✨ Features

* ❤️ Heart Disease Prediction using Machine Learning
* 📊 Real-time prediction from user input
* 🎨 Professional responsive UI
* ⚡ Flask backend integration
* 🧠 Pre-trained ML model (`model.pkl`)
* ☁️ Ready for Render deployment

---

## 🛠️ Tech Stack

* 🐍 Python
* 🌐 Flask
* 🎨 HTML5
* 💅 CSS3
* 🔢 NumPy
* 🤖 Scikit-learn
* 🚀 Gunicorn

---

## 📂 Project Structure

```bash id="r9f2k1"
suchi/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
│
├── models/
│   └── model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── favicon.ico   (optional)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash id="a7k3m1"
git clone <your-repo-url>
cd suchi
```

### 2️⃣ Create Virtual Environment

```bash id="m4p8q2"
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### 🪟 Windows

```bash id="v2n7k5"
venv\Scripts\activate
```

#### 🍎 Mac / 🐧 Linux

```bash id="p8m1q4"
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash id="q3w8e1"
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash id="n6m2k9"
python app.py
```

Open in browser:

```bash id="x1p7r4"
http://127.0.0.1:5000
```

---

## 🧠 Model Training

The model is trained separately in **Google Colab** using the heart disease dataset.

After training:

* Save the trained model as `model.pkl`
* Place it inside the `models/` folder

```bash id="b4n8m2"
models/model.pkl
```

---

## 📈 Prediction Output

The application predicts one of the following:

* ❤️ **High Risk of Heart Disease**
* 💚 **Low Risk of Heart Disease**

---

## ☁️ Deployment on Render

This project is ready for deployment on **Render** 🚀

### Required Files

* `requirements.txt`
* `Procfile`
* `app.py`

### Procfile

```txt id="k8m2p5"
web: gunicorn app:app
```

### 🔗 Render Deployment Link

👉 https://render.com/

Deploy by connecting your GitHub repository to Render.

---

## 📦 Requirements

```txt id="z7m4n1"
Flask==3.1.3
numpy==2.4.4
scikit-learn==1.8.0
gunicorn==22.0.0
```

---

## 🚀 Future Improvements

* 🗄️ Add database integration
* 📝 Store prediction history
* 🔐 Add user authentication
* 📂 Upload CSV for bulk prediction
* 📊 Add charts and analytics dashboard
* 🧠 Improve model accuracy

---

## 👨‍💻 Author

Developed as a **Machine Learning Mini Project** for ❤️ Heart Disease Prediction.
