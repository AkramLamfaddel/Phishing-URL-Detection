from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
import re
import math
from collections import Counter
import joblib
import os


model_path = os.path.join(os.path.dirname(__file__), "model", "phishing_rf_model.pkl")
model = joblib.load(model_path)


app = FastAPI(title="Phishing URL Detection API")

class URLItem(BaseModel):
    url: str
    
    
    
def entropy(s):
    probs = [n / len(s) for n in Counter(s).values()]
    return -sum(p * math.log2(p) for p in probs)


def extract_features(url):
    features={}
    features['url_length']=len(url)
    features['count_digits']=sum(char.isdigit() for char in url)
    features['has_at']=1 if "@" in url else 0
    features['has_https']=1 if url.startswith('https') else 0
    features['count_dots']=url.count('.')
    features['has_hyphen']=1 if "-" in url else 0
    features['has_ip']=1 if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", url) else 0
    features['count_special_chars']=len(re.findall(r"[?=&%_]", url))
    features['count_slash']=url.count('/')
    path = url.split('/', 3)
    features['path_length']=len(path[3]) if len(path) > 3 else 0
    domain = url.split('//')[-1].split('/')[0]
    features['count_subdomains']=max(0, domain.count('.') - 1)
    suspicious_words=[
    'login', 'verify', 'update', 'secure', 'account',
    'bank', 'confirm', 'signin', 'free', 'paypal'
    ]
    features['has_suspicious_words']=int(
    any(word in url.lower() for word in suspicious_words)
    )
    features['url_entropy'] = entropy(url)
    features['digit_ratio'] = features['count_digits'] / features['url_length']
    features['has_port'] = 1 if re.search(r":\d{2,5}", url) else 0
    tld = domain.split('.')[-1]
    features['tld_length'] = len(tld)
    shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 't.co', 'ow.ly']

    features['is_shortened_url'] = int(
        any(s in url.lower() for s in shorteners)
    )

    return pd.DataFrame([features])


@app.post("/predict")
def predict(item: URLItem):
    features_df = extract_features(item.url)
    prediction = model.predict(features_df)[0]
    proba = model.predict_proba(features_df)[0][prediction]
    label = "Phishing" if prediction == 1 else "Legitimate"
    return {"url": item.url, "prediction": label, "confidence": round(proba, 3)}

frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open(os.path.join(frontend_path, "index.html"), "r", encoding="utf-8") as f:
        return f.read()