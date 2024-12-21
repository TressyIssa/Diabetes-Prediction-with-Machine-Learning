# Prédiction du Diabète avec Machine Learning
![Intro](https://github.com/user-attachments/assets/f979b44e-cce8-41a6-a11f-75d284d12232)

![Intro](https://github.com/user-attachments/assets/66e1b5c5-2f1f-4525-bbe7-1d5982028589)


**Description du Projet**

Ce projet utilise un modèle de machine learning pour prédire le risque de diabète chez un individu en fonction de données médicales et démographiques.
Il s'agit d'une application développée avec Streamlit pour fournir une interface utilisateur interactive et simple à utiliser.

**Fonctionnalités**

Chargement des données utilisateur via un formulaire interactif.
Prédiction binaire (diabétique/non diabétique) basée sur les données fournies.
Affichage des probabilités associées à chaque prédiction.
Modèle de machine learning préentraîné : Gradient Boosting Classifier.
Données Utilisées
Les données d'entraînement proviennent d'un jeu de données médical contenant les variables suivantes :

**Pregnancies :** Nombre de grossesses.

**Glucose :** Niveau de glucose.

**Blood Pressure :** Pression artérielle (mm Hg).

**Skin Thickness :** Épaisseur cutanée (mm).

**Insulin :** Niveau d'insuline (mu U/ml).

**BMI :** Indice de masse corporelle (kg/m²).

**Diabetes Pedigree Function (DPF) :** Fonction indiquant l'historique familial du diabète.

**Age :** Âge du patient.

**Outcome :** Résultat binaire (1 = diabétique, 0 = non diabétique).

# Prétraitement des Données

**Nettoyage des Données :**

Remplissage des valeurs manquantes par la médiane calculée séparément pour les individus diabétiques et non diabétiques.
Vérification des valeurs aberrantes et normalisation des données.

# Entraînement du Modèle :

- Précision du modèle : 89 %.
  
- Métriques supplémentaires : Matrice de confusion, précision, rappel, F1-score.

Installation
Clonez le dépôt

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TressyIssa/Plateforme-de-detection-des-anomalies-du-sommeil.git
   cd sleep-disorder-prediction
   ```

2. **Installez les dépendances : bash Copier le code**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Lancer l'application Streamlit **:

   ```bash
   streamlit run app.py
   ```
**Utilisation**

1. Lancez l'application via Streamlit.
2. Entrez les informations médicales demandées :
3. Nombre de grossesses, glucose, pression artérielle, etc.
  - Cliquez sur le bouton "Prédire" pour obtenir le résultat.
4. Le résultat s'affiche avec :
  - Une prédiction binaire (Diabétique/Non diabétique).
  - La probabilité associée à la prédiction.

# Exemple de Résultat

**Entrées :**

**Grossesses : 2**

**Glucose : 150**

**Pression artérielle : 85**

**Épaisseur cutanée : 32**

**Insuline : 130**

**BMI : 28.7**

**DPF : 0.672**

**Âge : 45**

**Sorties :**

**Prédiction : Diabétique**

**Probabilité d'être diabétique : 78.2 %**
