import streamlit as st
import numpy as np
import pickle

# Chargement du modèle
try:
    with open("XGBoost_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Le fichier du modèle n'a pas été trouvé. Assurez-vous que 'Gradient Boosting_model.pkl' est dans le même dossier que ce script.")
    st.stop()

# Fonction pour effectuer une prédiction
def predict_diabetes(data):
    try:
        return model.predict(data), model.predict_proba(data)
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
        st.stop()

# Configuration de la page
st.title("Application de Prédiction du Diabète")
st.markdown("Entrez vos informations pour prédire si vous êtes à risque de diabète.")

# Formulaire d'entrée utilisateur
pregnancies = st.number_input("Nombre de grossesses", min_value=0, value=1, step=1, format='%d')
glucose = st.number_input("Taux de glucose", min_value=0, value=120, step=1, format='%d')
blood_pressure = st.number_input("Pression artérielle (mm Hg)", min_value=0, value=70, step=1, format='%d')
skin_thickness = st.number_input("Épaisseur cutanée (mm)", min_value=0, value=20, step=1, format='%d')
insulin = st.number_input("Insuline (mu U/ml)", min_value=0, value=80, step=1, format='%d')
bmi = st.number_input("BMI (Indice de Masse Corporelle)", min_value=0.0, value=25.0, step=0.1, format='%f')
dpf = st.number_input("Fonction Héréditaire du Diabète (DPF)", min_value=0.0, value=0.5, step=0.01, format='%f')
age = st.number_input("Âge", min_value=0, value=30, step=1, format='%d')

# Création de l'entrée utilisateur sous forme de tableau
user_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

st.write("**Debug : Données utilisateur entrées**", user_data)

# Bouton pour effectuer la prédiction
if st.button("Prédire"):
    prediction, probabilities = predict_diabetes(user_data)

    # Affichage du résultat
    if prediction[0] == 1:
        st.error(f"Résultat : Diabétique avec une probabilité de {probabilities[0][1] * 100:.2f} %.")
    else:
        st.success(f"Résultat : Non diabétique avec une probabilité de {probabilities[0][0] * 100:.2f} %.")

# Instructions supplémentaires
st.markdown("---")
st.markdown(
    "**Instructions** :\n"
    "- Assurez-vous que toutes les entrées sont correctes.\n"
    "- Les valeurs doivent correspondre aux données attendues par le modèle.\n"
    "- Contactez l'administrateur en cas de problème.")
