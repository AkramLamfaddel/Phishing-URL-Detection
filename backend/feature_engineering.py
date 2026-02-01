import pandas as pd 
import re
import math
from collections import Counter


df=pd.read_csv('data/phishing_url_dataset_unique.csv')


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

    return features

features_df = df["url"].apply(extract_features).apply(pd.Series)



print(features_df.head())

final_df=features_df.copy()
final_df["label"]=df["label"]

print(final_df.head())

print("duplicate",final_df.duplicated().sum())

final_df_no_dup = final_df.drop_duplicates()
print("new shape",final_df_no_dup.shape)

final_df_no_dup.to_csv("data/phishing_features_dataset.csv", index=False)
