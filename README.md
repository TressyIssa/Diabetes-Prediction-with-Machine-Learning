# Diabetes-Prediction-with-Machine-Learning
![Intro](https://github.com/user-attachments/assets/f979b44e-cce8-41a6-a11f-75d284d12232)

# Contexte

Le diabète est une maladie chronique caractérisée par une hyperglycémie (taux de sucre élevé dans le sang)
due à une production insuffisante d'insuline ou à une utilisation inefficace de l'insuline par l'organisme.
Dans le contexte de la prédiction de cette maladie, l'objectif est d'utiliser des modèles de machine learning
pour identifier les individus à risque de développer le diabète en analysant diverses caractéristiques cliniques et biologiques,
telles que la glycémie, l'indice de masse corporelle (IMC), l'âge, et d'autres facteurs pertinents.
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
   git clone https://github.com/TressyIssa/Diabetes-Prediction-with-Machine-Learning.git
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

# **8.Conclusion**

Dans cette étude, nous avons analysé plusieurs algorithmes de classification en tenant compte des particularités du dataset,
notamment un déséquilibre modéré entre les classes. Cette situation a nécessité une attention particulière pour garantir une performance équitable sur les deux classes.
Les modèles d'ensemble comme Gradient Boosting et LightGBM ont démontré leur efficacité avec une exactitude de 94 %, tout en maintenant un bon équilibre entre précision et rappel.
Bien que la régression logistique ait obtenu une exactitude acceptable (84 %), son approche linéaire s'est révélée moins adaptée au contexte des données. Après optimisation,
le modèle KNN a montré une amélioration notable (82 % d'exactitude), mais reste moins performant que les méthodes d'ensemble.
Ces résultats soulignent l'importance de l'optimisation dans des conditions spécifiques et confirment que Gradient Boosting et LightGBM sont les meilleurs choix pour gérer efficacement les caractéristiques complexes de ce dataset.
