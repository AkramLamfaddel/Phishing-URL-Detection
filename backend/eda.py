import pandas as pd


df=pd.read_csv('data/phishing_url_dataset_unique.csv')

print(df.head())

print(df.info())

print(df.isnull().sum())

print(df.describe())

print(df['label'].value_counts())

print("duplicate",df.duplicated().sum())
