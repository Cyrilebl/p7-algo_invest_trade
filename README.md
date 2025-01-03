# Optimiser ses stratégies d'investissement

### ✨ À propos

Ce projet propose deux algorithmes. Ils suggèrent une liste des actions les plus rentables à acheter afin de maximiser le profit d'un client après deux ans.

- **Premier algorithme (bruteforce)** : Explore toutes les combinaisons possibles d'actions respectant la contrainte du budget et sélectionne le meilleur résultat.  
  ⚠️ Cet algorithme n'est pas adapté à un grand nombre d'actions en raison de sa complexité.

- **Second algorithme (optimisé)** : Calcule un ratio pour chaque action : `profit / prix`. Les actions sont ensuite triées par ordre décroissant de ce ratio. Les actions les plus rentables sont ajoutées à la sélection tant que le budget le permet.

---

### 📌 Étape 1 : Cloner le repository

Téléchargez le projet sur votre ordinateur.

- Dans le terminal exécutez :

```bash
git clone <repository-url>
```

---

### 📌 Étape 2 : Initialiser un environnement virtuel

Un environnement virtuel permet d'isoler les dépendances du projet.
Utilisez le module Python venv pour créer et gérer cet environnement.

- Créer un environnement :

```bash
python3 -m venv env
```

- Activer l'environnement :

```bash
source env/bin/activate
```

- Désactiver l’environnement :

```bash
deactivate
```

---

### 📌 Étape 3 : Installer les packages nécessaires

Installez les dépendances listées dans le fichier `requirements.txt`.

- Dans le terminal, exécutez :

```bash
pip install -r requirements.txt
```

---

### 📌 Étape 4 : Exécuter le code

- Dans le terminal, exécutez :

```bash
python3 main.py
```

---

### 📁 Organisation des données

Les données se trouvent dans le dossier `data` et sont au format CSV.  
Elles sont organisées en **3 colonnes** :

- **Nom de l'action**
- **Prix de l'action**
- **Rentabilité (profit)**
