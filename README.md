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

Modèle utilisé : Gradient Boosting Classifier.

Division des données en ensembles d'entraînement (80 %) et de test (20 %).

Optimisation des hyperparamètres pour améliorer les performances.

**Évaluation :**

Précision du modèle : 89 %.

Métriques supplémentaires : Matrice de confusion, précision, rappel, F1-score.

Installation

Clonez le dépôt :

bash

Copier le code

git clone https://github.com/votre-repo/prediction-diabete.git

cd prediction-diabete

Installez les dépendances :

bash

Copier le code

pip install -r requirements.txt

Lancer l'application Streamlit :

bash

Copier le code

streamlit run app.py

Utilisation
Lancez l'application via Streamlit.
Entrez les informations médicales demandées :
Nombre de grossesses, glucose, pression artérielle, etc.
Cliquez sur le bouton "Prédire" pour obtenir le résultat.
Le résultat s'affiche avec :
Une prédiction binaire (Diabétique/Non diabétique).
La probabilité associée à la prédiction.

**Exemple de Résultat**
Entrées :

Grossesses : 2
Glucose : 150
Pression artérielle : 85
Épaisseur cutanée : 32
Insuline : 130
BMI : 28.7
DPF : 0.672
Âge : 45
Sorties :

Prédiction : Diabétique
Probabilité d'être diabétique : 78.2 %
