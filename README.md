# Firestore-Python-Writer

## Description

Firestore-Python-Writer est un script Python permettant de générer une valeur et de mettre à jour un document Firestore avec cette valeur. Idéal pour illustrer l'écriture dans Firestore avec Python.

## Fonctionnalités

- Génère une valeur prédéfinie.
- Met à jour un document spécifique dans une collection Firestore.

## Prérequis

- Python 3.x
- Compte de service Google Cloud avec accès à Firestore
- Bibliothèque Python : `google-cloud-firestore`

## Installation

1. Clonez le repository :

```bash
git clone https://github.com/Gabin221/Firestore-Python-Writer.git
cd Firestore-Python-Writer
```

2. Installez les dépendances nécessaires :
```bash
pip install google-cloud-firestore
```

3. Configurez votre environnement :
+ Téléchargez le fichier JSON de compte de service depuis la console Google Cloud.
+ Définissez la variable d'environnement **GOOGLE_APPLICATION_CREDENTIALS** pour pointer vers votre fichier JSON.

## Utilisation

Exécutez le script principal pour générer une valeur et mettre à jour Firestore :
```bash
python main.py
```

Le script affichera la valeur générée et confirmera la mise à jour réussie de Firestore.
