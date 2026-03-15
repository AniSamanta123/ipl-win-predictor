# 🏏 IPL Win Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![License](https://img.shields.io/badge/Project-ML%20Project-orange)

A Machine Learning web application that predicts the **winning probability of IPL teams during a live cricket match**.

The application analyzes match conditions such as **current score, overs completed, wickets lost, and target score** to estimate the probability of the batting team winning.

Built with **Python, Machine Learning, and Streamlit**.

---

# 🌐 Live Demo

👉 https://ipl-win.streamlit.app/

---

# 📸 Application Preview



---

# 🚀 Features

✔ Predict win probability during a live match
✔ Interactive Streamlit web interface
✔ Real-time probability calculation
✔ Machine Learning model trained on IPL historical data
✔ Clean and simple UI
✔ Fast prediction using a trained ML pipeline

---

# ⚙️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

### Machine Learning

* Logistic Regression
* Feature Engineering
* Model Pipeline

---

# 📊 Input Features Used in Model

The ML model uses the following match features:

* Batting Team
* Bowling Team
* Match City
* Target Score
* Current Score
* Overs Completed
* Wickets Lost
* Runs Left
* Balls Left
* Current Run Rate (CRR)
* Required Run Rate (RRR)

These values are used to compute the **winning probability of both teams**.

---

# 🧠 Machine Learning Workflow

1️⃣ Data Collection (IPL Dataset)
2️⃣ Data Cleaning and Preprocessing
3️⃣ Feature Engineering
4️⃣ Model Training (Logistic Regression)
5️⃣ Model Serialization using Pickle
6️⃣ Deployment using Streamlit

---

# 📂 Project Structure

```
ipl-win-predictor
│
├── app.py
├── finally.pkl
├── requirements.txt
├── setup.sh
├── Procfile
├── README.md
└── images
    └── app_screenshot.png
```

---

# 🖥 Installation Guide

### Clone the repository

```
git clone https://github.com/AniSamanta123/ipl-win-predictor.git
```

### Navigate to project folder

```
cd ipl-win-predictor
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

# 📈 Example Prediction

Example match scenario:

Target Score: 180
Current Score: 120
Overs Completed: 15
Wickets Lost: 4

The model will estimate the probability of both teams winning the match.

Example Output:

Team A Win Probability: **62%**
Team B Win Probability: **38%**

---

# 👨‍💻 Author

**Anirban Samanta**

GitHub:
https://github.com/AniSamanta123

---

# ⭐ Support

If you like this project, please ⭐ the repository.

---

# 📜 License

This project is created for **learning and educational purposes**.
