import pandas as pd
from app import extract_features, model  # ton fichier app.py avec extract_features et le modèle

# 1️⃣ Charger le nouveau dataset
new_data = pd.read_csv("data/Phishing URL.csv")
print("Nombre de lignes:", len(new_data))

# 2️⃣ Extraire les features pour toutes les URLs
features_list = [extract_features(url) for url in new_data['url']]
X_new = pd.concat(features_list, ignore_index=True)

# 3️⃣ Faire les prédictions
y_pred = model.predict(X_new)
y_proba = model.predict_proba(X_new)

# 4️⃣ Ajouter les résultats au dataframe
new_data['prediction'] = y_pred
new_data['confidence'] = [round(y_proba[i][y_pred[i]], 3) for i in range(len(y_pred))]
new_data['label_name'] = new_data['prediction'].apply(lambda x: "Phishing" if x == 1 else "Legitimate")

# 5️⃣ Afficher un aperçu
print(new_data.head())

# 6️⃣ Évaluer les performances (si labels présents)
from sklearn.metrics import accuracy_score, classification_report

y_true = new_data['label'].values
print("Accuracy:", accuracy_score(y_true, y_pred))
print(classification_report(y_true, y_pred))

# 7️⃣ Sauvegarder les résultats
new_data.to_csv("data/Phishing_URL_predictions.csv", index=False)
print("Predictions saved to Phishing_URL_predictions.csv")
