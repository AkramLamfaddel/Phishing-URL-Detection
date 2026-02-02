# Phishing URL Detection 🔐🤖

A complete **Machine Learning pipeline** for detecting **phishing URLs**, from exploratory data analysis (EDA) to model training, evaluation on an external dataset, and deployment-ready API.

---

## 📁 Project Structure

```

├── 📁 backend/
│   ├── 📁 data/
│   │   ├── 📄 Phishing URL.csv
│   │   ├── 📄 Phishing_URL_predictions.csv
│   │   ├── 📄 phishing_features_dataset.csv
│   │   └── 📄 phishing_url_dataset_unique.csv
│   ├── 📁 model/
│   │   └── 📄 phishing_rf_model.pkl
│   ├── 🐍 app.py
│   ├── 🐍 eda.py
│   ├── 🐍 feature_engineering.py
│   ├── 🐍 testfinal.py
│   └── 🐍 training.py
├── 📁 frontend/
│   ├── 📁 img/
│   │   ├── 🖼️ codiia.png
│   │   └── 🖼️ hackerBack.png
│   ├── 🌐 index.html
│   ├── 📄 script.js
│   └── 🎨 style.css
├── 📝 readme.md
└── 📄 requirements.txt

```

---

## ⚙️ Requirements Installation

Before running any script, make sure you have **Python 3.9+** installed.

# 1️⃣ Create a virtual environment (venv)
```
python -m venv venv
```

Activate the virtual environment:

Windows
```
venv\Scripts\activate
```

Linux / macOS
```
source venv/bin/activate
```

## 2️⃣ Install required dependencies
```
pip install -r requirements.txt
```


---

## 🚀 Execution Order (IMPORTANT)

To reproduce the full pipeline correctly, **follow this exact order**:

---

### 1️⃣ Exploratory Data Analysis (EDA)

Analyze and understand the dataset (distribution, duplicates, statistics).

```bash
python eda.py
```

Purpose:
- Understand phishing vs legitimate URLs
- Detect duplicates and anomalies
- Prepare for feature design

---

### 2️⃣ Feature Engineering

Extract intelligent features from URLs and generate the final ML dataset.

```bash
python feature_engineering.py
```

# 🔍 Purpose

This module extracts security-related features from URLs to help detect phishing websites.

Extracted Features

URL length, entropy, digits ratio

Suspicious keywords detection

Subdomains count, TLD length

IP address usage, URL shorteners

Special characters, ports, paths analysis

These features are later used to train a Machine Learning model for phishing detection.

# ⚙️ Feature Extraction Details

Each URL is transformed into a numerical feature vector using the extract_features(url) function.

# 📌 Features Explanation

url_length:
Total number of characters in the URL. Phishing URLs are often longer than normal ones.

count_digits:
Number of numeric characters in the URL. Excessive digits may indicate phishing.

digit_ratio:
Ratio of digits to total URL length. Helps normalize digit usage.

has_at:
Checks if the URL contains @. Often used to mislead users.

count_dots:
Number of dots (.) in the URL. Many dots may indicate multiple subdomains.

has_hyphen:
Detects hyphens (-) in the URL, commonly used in fake domains

has_ip:
Checks if the URL uses an IP address instead of a domain name.

count_special_chars:
Counts special characters like ?, =, &, %, _. Often abused in phishing URLs

count_slash:
Number of slashes (/) in the URL. Deep paths may hide malicious content.

path_length:
Length of the URL path (after the domain).

count_subdomains:	
Number of subdomains. Phishing URLs often use many subdomains.

has_suspicious_words:	
Detects presence of phishing-related keywords such as login, verify, secure, paypal, etc.

url_entropy:
Measures randomness of the URL string. High entropy may indicate obfuscation.

has_port:	
Checks if a port number is explicitly used (e.g., :8080).

tld_length:	
Length of the Top-Level Domain (TLD). Unusual TLDs can be suspicious

is_shortened_url:
Detects URL shortening services like bit.ly, tinyurl, t.co.

---

### 3️⃣ Model Training

Train the Machine Learning model (Random Forest) and save it.

```bash
python training.py
```

Purpose:
- Train classifier
- Evaluate performance (accuracy, precision, recall, F1-score)
- Save trained model to:

```
backend/model/phishing_rf_model.pkl
```

---

### 4️⃣ Model Testing on External Dataset

Test the trained model on a **new unseen dataset**.

```bash
python testfinal.py
```

Purpose:
- Validate generalization on a different dataset
- Generate predictions + confidence scores

Output:
- `Phishing_URL_predictions.csv`

---

## 📊 Final Model Performance (External Dataset)

- **Accuracy:** ~98.6%
- **Precision / Recall / F1-score:** ~99%

This confirms strong generalization and robustness of the model.

---

## 🌐 Deployment (Optional)

To launch the FastAPI backend:

```bash
uvicorn backend.app:app --reload   
```

API endpoint:
```
POST /predict
```

Frontend can be accessed via:
```
http://127.0.0.1:8000
```

---

## 🧠 Technologies Used

- Python
- Scikit-learn
- Pandas / NumPy
- FastAPI
- HTML / CSS / JavaScript

---

## 📌 Author

Developed by **Akram Lamfaddel codi-ia**  
Machine Learning & Web Developer

---

✅ This project is ideal for:
- Cybersecurity learning
- Machine Learning portfolios
- Academic projects
- Real-world phishing detection systems

---

⚠️ Disclaimer: This project is for educational and research purposes only.

