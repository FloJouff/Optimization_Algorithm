## Etapes à suivre pour l'installation et l'utilisation du Programme de sélection optimisée d'un portefeuille d'actions

### Etapes d'installation:

#### Installer Python

L’installation de Python est très simple ! Rendez-vous sur [python.org](https://www.python.org/downloads/), choisissez votre système d’exploitation (Mac/Windows, etc.) et cliquez sur le bouton de téléchargement pour installer Python sur votre ordinateur.

Si vous utilisez Windows, pensez à bien cocher la case "Add to path" pour ajouter Python aux variables d'environnement.

#### Faire une copie du repository.

A partir du lien GitHub: https://github.com/FloJouff/Optimization_Algorithm, créer un clone du projet en local sur votre ordinateur

#### Création de l'environnement virtuel

Depuis votre terminal, à la racine du projet, créer un environnement virtuel, afin d'y installer uniquement les paquets Python nécessaires à l'exécution du script.

    $ python -m venv env

#### Activation de l'environnement virtuel

A partir du terminal, taper la commande suivante:

    $ source env/bin/activate (pour MacOs, Linux)
    $ env\scripts\activate (pour Windows)

### Exécution du code d'application:

Exécuter à partir d'un terminal de commande :

    $ python bruteforce.py

Permet d'exécuter le fichier bruteforce.

Ou :

    $ python optimized.py datas/[nom du fichier à analyser].csv

Permet d'exécuter le fichier optimized pour l'analyse du set de données souhaité.
