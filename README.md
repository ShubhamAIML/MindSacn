# 🧠 MindScan — Teen Mental Health Predictor

An AI-powered web application built with **Django** and **XGBoost** that predicts depression risk in teenagers based on their social media habits, lifestyle, and mental health indicators.

## 🔗 Live Demo
**Try the live application**: [MindScan Live Test](https://mindsacn.onrender.com/)

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Features](#features)
- [Input Features](#input-features)
- [Prediction Output](#prediction-output)
- [Run Locally](#run-locally)
- [Deploy on Render](#deploy-on-render)
- [Environment Variables](#environment-variables)
- [Feature Encoding](#feature-encoding)
- [Developer](#developer)

---

## 📖 About the Project

This project addresses a critical challenge in mental health screening: predicting depression risk in teenagers based on behavioral and psychological indicators. The analysis leverages features including daily social media usage, platform preferences (TikTok, Instagram, or both), sleep patterns, and social interaction levels across a dataset of 1,200 teen records.

### The Core Challenge: Data Imbalance

Real-world datasets frequently present class imbalance—a phenomenon clearly evident in this study. Among 1,200 samples, only 31 cases represent the depression class (~2.6%), while the remaining records indicate low risk. Without addressing this imbalance, conventional ML models achieve artificially inflated accuracy (~97%) by simply predicting the majority class, fundamentally undermining the model's clinical utility.

### Objective & Success Metrics

Rather than optimizing for overall accuracy, this project prioritizes **Recall and F1-Score** to ensure reliable detection of the minority class. The goal is to develop a model capable of identifying genuine depression indicators while minimizing false negatives—a critical requirement for mental health applications where missing a true case has serious implications.

### Methodology

The approach combines three key strategies:

- **Stratified Train-Test Split**: Uses stratification to preserve class distribution when partitioning data, ensuring both training and test sets contain representative samples of depression cases.
- **SMOTE Oversampling**: Applies Synthetic Minority Over-sampling Technique to the training set exclusively, generating synthetic minority class samples to balance the dataset while preventing data leakage into evaluation metrics.
- **XGBoost Model**: Employs XGBoost (Extreme Gradient Boosting) classifier, a state-of-the-art gradient boosting algorithm that iteratively builds an ensemble of decision trees, each correcting errors from previous trees. This approach excels at capturing non-linear relationships and provides superior generalization performance while naturally handling feature importance ranking.

> ⚠️ This is an AI screening tool only — not a clinical diagnosis. Always consult a qualified mental health professional.

---

## 🛠️ Tech Stack & Technical Details

### Backend
- **Django 4.x**: Python web framework for building scalable REST APIs and server-side logic
- **XGBoost**: Gradient boosting framework optimized for classification tasks
- **scikit-learn**: Machine learning utilities (SMOTE, preprocessing, model evaluation)
- **NumPy & Pandas**: Data manipulation and numerical computations
- **Joblib**: Model serialization and persistence

### Frontend
- **HTML5/CSS3**: Semantic markup and modern styling
- **JavaScript (Vanilla)**: Dynamic UI interactions and real-time form validation
- **FontAwesome 6**: Icon library for intuitive visual indicators

### Deployment
- **Render**: Cloud hosting platform for live application deployment
- **Gunicorn**: WSGI HTTP Server for production deployment

### About XGBoost

**XGBoost (Extreme Gradient Boosting)** is an advanced ensemble machine learning algorithm that builds multiple decision trees sequentially. Each new tree is trained to minimize the residual errors from previous trees, creating a powerful predictive model. Key advantages for this project:

- **Handles Imbalanced Data**: Built-in support for class weights and scale_pos_weight parameter
- **Feature Importance**: Automatically ranks features by importance, revealing key depression indicators
- **Regularization**: L1 and L2 regularization prevent overfitting on small datasets
- **Speed & Efficiency**: Optimized for both training speed and inference latency
- **Interpretability**: Tree-based models provide explainable predictions

---

## 📁 Project Structure

```
mindscan/
│
├── manage.py                        # Django entry point
├── requirements.txt                 # Python dependencies
├── render.yaml                      # Render deployment config
├── xgboost_depression_model.pkl     # trained model
│
├── core/                            # Django project config
│   ├── __init__.py
│   ├── settings.py                  # App settings
│   ├── urls.py                      # Root URL routing
│   └── wsgi.py                      # WSGI server entry
│
└── predictor/                       # Main Django app
    ├── __init__.py
    ├── apps.py
    ├── views.py                     # Prediction logic
    ├── urls.py                      # App URL routing
    │
    ├── templates/predictor/
    │   ├── base.html                # Shared layout, navbar, footer
    │   ├── index.html               # Assessment form (home page)
    │   ├── result.html              # Prediction result page
    │   └── about.html               # About page with dev links
    │
    └── static/predictor/
        ├── css/style.css            # All styling + dark/light mode
        └── js/main.js               # Theme toggle, sliders, progress bar
```

---

## ✨ Features

- 🤖 **XGBoost AI Model** — predicts depression risk from 12 input features
- 🌗 **Dark / Light Mode** — toggle with localStorage memory
- 📊 **Confidence Ring** — animated SVG ring showing prediction confidence %
- 📋 **Progress Bar** — real-time form completion tracker
- 🎚️ **Interactive Sliders** — for stress, anxiety, and addiction levels
- 💡 **Personalized Tips** — different recommendations for each prediction
- ⚠️ **Error Handling** — friendly error display on bad inputs
- 📱 **Fully Responsive** — works on mobile, tablet, and desktop
- 🚀 **Render Ready** — includes `render.yaml` and WhiteNoise for static files

---

## 📊 Input Features

| # | Feature | Type | Values |
|---|---------|------|--------|
| 1 | Age | Numeric | 13 – 19 |
| 2 | Gender | Categorical | Male / Female |
| 3 | Daily Social Media Hours | Numeric | 0 – 24 hrs |
| 4 | Platform Usage | Categorical | Instagram / TikTok / Both |
| 5 | Sleep Hours | Numeric | 0 – 12 hrs |
| 6 | Screen Time Before Sleep | Numeric | 0 – 10 hrs |
| 7 | Academic Performance | Numeric | GPA 0.0 – 4.0 |
| 8 | Physical Activity | Numeric | 0 – 10 hrs/day |
| 9 | Social Interaction Level | Categorical | Low / Medium / High |
| 10 | Stress Level | Numeric | 1 – 10 |
| 11 | Anxiety Level | Numeric | 1 – 10 |
| 12 | Addiction Level | Numeric | 1 – 10 |

---

## 🔮 Prediction Output

| Label | Result | Meaning |
|-------|--------|---------|
| `0` | ✅ Low Depression Risk | Teen shows a healthy mental health profile |
| `1` | ⚠️ Depression Risk Detected | Teen shows indicators associated with depression |

The result page shows:
- Prediction label and title
- Confidence percentage with animated ring chart
- 4–5 personalized health recommendations

---

## 💻 Run Locally

Follow these steps exactly to run MindScan on your machine.

### Step 1 — Prerequisites

Make sure you have the following installed:
- **Python 3.10 or above** → [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** (optional, if cloning from GitHub)

Check your Python version:
```bash
python --version
```

---

### Step 2 — Get the Project

If you downloaded the zip:
```bash
# Unzip and enter the folder
unzip mindscan.zip
cd mindscan
```

If you cloned from GitHub:
```bash
git clone https://github.com/your-username/mindscan.git
cd mindscan
```

---

### Step 3 — Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line — this means it's active.

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Django, XGBoost, scikit-learn, joblib, WhiteNoise, Gunicorn, and all other required packages.

---

### Step 5 — Add Your Trained Model

Place your trained model file in the **root of the project** (same folder as `manage.py`):

```
mindscan/
├── manage.py
├── xgboost_depression_model.pkl   ← here
├── requirements.txt
...
```

> If you skip this step, the app will still run in **demo mode** with a fallback prediction.

---

### Step 6 — Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

### Step 7 — Run the Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL+BREAK.
```

---

### Step 8 — Open in Browser

```
http://127.0.0.1:8000/
```

| Page | URL |
|------|-----|
| Home / Form | http://127.0.0.1:8000/ |
| About | http://127.0.0.1:8000/about/ |

---

## 🚀 Deploy on Render

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/your-username/mindscan.git
git push -u origin main
```

### Step 2 — Create a Web Service on Render

1. Go to [render.com](https://render.com) and sign in
2. Click **New → Web Service**
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml` — click **Deploy**

### Step 3 — Add Environment Variables

In your Render dashboard → **Environment** tab, add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | any long random string |
| `DEBUG` | `false` |

### Step 4 — Upload Your Model File

Since Render's filesystem is ephemeral, use one of these methods:

**Option A — Render Disk (recommended):**
1. In Render dashboard → **Disks** → Add disk (e.g. mount path `/data`)
2. Upload `xgboost_depression_model.pkl` via the Render Shell:
   ```bash
   # In Render Shell
   cp /path/to/xgboost_depression_model.pkl /data/
   ```
3. Update `MODEL_PATH` in `core/settings.py`:
   ```python
   MODEL_PATH = '/data/xgboost_depression_model.pkl'
   ```

**Option B — Include in repo:**
Simply commit the `.pkl` file to your GitHub repo (fine for small files under 100MB):
```bash
git add xgboost_depression_model.pkl
git commit -m "add model"
git push
```

---

## 🔐 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET_KEY` | `dev-only-secret-key` | Django secret key — change in production |
| `DEBUG` | `true` | Set to `false` in production |

---

## 🧬 Feature Encoding

The encoding in `predictor/views.py` matches exactly what was used during model training:

```python
gender:                   male → 1,  female → 0
platform_usage:           Instagram → 0,  TikTok → 1,  Both → 2
social_interaction_level: low → 0,  high → 1,  medium → 2
```

---

## 👨‍💻 Developer

**Your Name**
ML Engineer & Full Stack Developer

- 🔗 [LinkedIn](https://www.linkedin.com/in/shubham-kumar-016b6816b/)
- 🐙 [GitHub](https://github.com/ShubhamAIML)
- 🌐 [Portfolio](https://portfolio-mxx7.onrender.com/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
