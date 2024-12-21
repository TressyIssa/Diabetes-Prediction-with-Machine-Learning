# Prédiction du Diabète avec Machine Learning

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

Installation
Clonez le dépôt

git clone https://github.com/votre-repo/prediction-diabete.git
cd prediction-diabete
