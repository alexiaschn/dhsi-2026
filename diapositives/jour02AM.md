---
title: "Jour 2 matin : Automatisation du prétraitement d'un corpus textuel"
date: 2026-06-09
author: 
    - name: Yann Audin
      orcid: https://orcid.org/0000-0003-3456-9767
      email: yann.audin@umontreal.ca
    - name: William Bouchard
      orcid: "https://orcid.org/0009-0003-3683-2415"
      email: william.bouchard2@umontreal.ca
    
bibliography: ../dhsi2026.bib
link-citations: true
colorlinks: true
fig-cap-location: top
format:
    revealjs: 
        output-file: "jour02AM.html" 
        # template: simple
        smaller: true
        # incremental: true
        scrollable: true
        slide-number: true
---
## Programme de la matinée 

AM: (3h)

- Présentation du corpus et des projets (30min) @william
- Principes (45 minutes) @yann
    - Shit in shit out
    - Structuration des données
- PAUSE (15 minutes)
- Manipuler des données dans Python (20 minutes + 10 minutes atelier) @yann
    - API
- Prétraitement du texte (60 minutes) @yann
    - Nettoyage
    - Segmentation
    - Tokenisation

# Manipulation de données

## Où suis-je?

Non, mais vraiment : où suis-je très exactement?

:::{.incremental}

- En utilisant comme point de départ la Terre, combien d'étapes sont nécessaires pour ce rendre jusqu'à moi?

- À partir de quel moment est-il pertinent d'arrêter de chercher et de simplement dire mon nom pour me trouver?

- Certaines étapes sont arbitraires. D'autres sont seulement utiles dans des contextes spécifiques. D'autres encore sont problématiques, ou encore limitent nos possibilités.

:::

## Visualiser son ~~chemin~~ *path*

Les fichiers dans un ordinateur sont organisés en arborescence: tout commence par une racine, puis nous voyageons le long des branches vers des régions de plus en plus spécifiques de notre ordinateur.

- Sur PC: `C:\Users\Username\Documents\fichier.txt`
- Sur MacOS: `/Users/Username/Documents/fichier.txt`
- Sur Linux: `/home/Username/Documents/fichier.txt`

## Interlude : les librairies

Lorsque nous désirons faire des opérations complexes---par exemple obtenir une racine carrée ou le contenu d’une page web---nous nous référons au travail d'autres programmeur·euses\ : il n'est pas nécessaire de réinventer la roue tous les jours!

Dans ce genre de cas, nous faisons appel à une librairie en l'important (e.g. `import os`), plus en l'appelant (e.g. `os.getcwd()`).

## Trouver sa position

`os` est une librairie Python spécialisée en manipulation de fichier. 

Par manipulation, on entend trouver, créer, déplacer, copier, supprimer et accéder aux fichiers et aux dossiers.

```python
import os
os.getcwd()
```

- `cwd` signifie "current working directory".

## Explorer les alentours

Lister les éléments dans le dossier où nous sommes (le *current working directory*)\ :

```python
os.listdir()
```

## Explorer un dossier spécifique

Créer un *path* vers un dossier spécifique et explorer son contenu\ :


```python
path = os.path.join("data", "corpus")

os.listdir(path)
```

## `os`\ : fonctions plus avancées

Créer et supprimer un fichier\ :

```python
import os
os.remove(path)
```

Créer et supprimer un dossier\ :

```python
os.mkdir(path)
os.rmdir(path) # Ne fonctionne que sur un dossier vide
```

Déplacer ou renommer un fichier ou un dossier\ :

```python
os.rename(old_path, new_path)
```

## Interlude : les types de fichiers

L'extension à la fin d'un fichier (e.g. `.txt`, `.docx`, `.mp3`, ...) est une indication quant à comment l'ordinateur doit le lire. 

Certains types de fichiers sont plus faciles à manipuler que d'autre\ ; dans le cadre de cet atelier et de projets en humanités numériques, nous utilisons surtout les extensions suivantes\ :

- Plain text\ : `.txt`\ ;
- JSON\ : `.json`\ ;
- XML-TEI\ : `.xml`\ ;
- Comma Separated Values\ : `.csv`.

## Accéder aux données d'un fichier

Pour manipuler des données dans un Jupyter Notebook, il faut connaître sa position exacte.

```python
import os

path = os.path.join("data", "corpus", "fichier.txt")

with open(path, 'r', encoding="utf-8") as f:
    content = f.read()
```

## Accéder à plusieurs fichiers dans un même dossier

```python
import os
folder = os.path.join("data", "corpus")
file_list = os.listdir(folder)

corpus = {}

for file in file_list:
    if file.endswith(".txt"):
        file_path = os.path.join(folder, file)
        with open(file_path, "r", encoding = "utf-8") as f:
            file_content = f.read()
            corpus[file] = file_content
```

## Interlude : les formats propriétaires

Les formats plus complexes comme `.pdf` et `.docx` sont particulièrement difficiles à manipuler en dehors de logiciels dédiés. Certaines librairies permettent d'accéder au contenu utile de ces fichiers (par exemple, isoler le texte dans un pdf), mais pour des raisons de temps, nous n'en parlerons pas dans cet atelier. 

## API

Parfois, on veut accéder à des données (des fichiers de toutes sortes) qui ne sont pas sur notre ordinateur, mais plutôt en ligne. 

Dans ce genre de cas, on fait appel à une API, une *Application Programming Interface*. 

## Un exemple d'API

Tous les livres du Projet Gutenberg sont référencés dans un format lisible pour un ordinateur dans `https://gutendex.com/books`.

```{python}
import requests

url = "https://gutendex.com/books"
parameters = {"search": "shelley percy"}

response = requests.get(url, parameters)
donnees = response.json()

for book in donnees["results"]:
    print(20*"=")
    print("\t" + book["title"])
    print("\t" + book["formats"]["text/plain; charset=utf-8"])
```

```{python}
book_response = requests.get(url="https://www.gutenberg.org/ebooks/76161.txt.utf-8")

print(book_response.text)
```

# Structure de données

TODO

# Présentation du corpus de travail 


## L’*Anthologia Graeca*

- Un recueil d’épigrammes grecques, de l’Antiquité à l’époque byzantine.
- Une épigramme est d’abord un texte bref, souvent lié à une inscription, une tombe, une offrande ou un objet.
- Dans l’*Anthologie*, le genre s’élargit fortement.
- On y trouve des textes funéraires, votifs, amoureux, satiriques, descriptifs ou moraux.
- C’est un **corpus complexe**, déjà structuré par une histoire de transmission et d’édition.


## Un corpus stratifié

- Des époques différentes, des auteurs différents, des contextes socioculturels variés.
- Elle conserve des traces de traditions multiples.
- Différents états manuscrits, attributions douteuses...
- L’*Anthologie* : une forme d’organisation des données?

(Pas de panique, nous travaillerons principalement le texte)

## Une anthologie n'est jamais neutre

- Une anthologie suppose toujours des choix.
- Ces choix orientent la lecture et rendent certains liens plus visibles que d’autres.
- Le numérique permet de rendre cette organisation plus explicite.
- On peut alors parcourir le corpus autrement : par auteur, thème, lieu, mot-clé ou témoin.
- Ce passage du texte à la donnée est au cœur de notre atelier.


## Le livre VII

- Consacré aux épigrammes funéraires.
- Thèmes : mort, tombeaux, mémoire, perte et le monde des morts.
- Pourtant, le corpus résiste vite aux catégories trop simples.
- Même dans un livre funéraire, on trouve des animaux, des personnages mythologiques...
- Le thème général est clair, mais chaque texte peut porter plusieurs motifs à la fois.


## Le projet Anthologia Graeca

- Une édition numérique collaborative de l’Anthologie grecque.
- Projet de structuration des données autour des épigrammes.
- La plateforme associe :
    - Textes grecs et traductions ;
    - Auteurs et attributions ;
    - Annotations (mots-clés, lieux cités, etc.).
- Démonstration. 

## Ce que la plateforme change

- L’édition imprimée propose surtout un ordre de lecture.
- La plateforme numérique ajoute des possibilités de lecture. 
- Une épigramme = un poème à lire et une entrée dans une base de données.
- Elle peut être exportée, reliée, filtrée, comptée, vectorisée ou comparée.
- La plateforme devient une **anthologie de l’Anthologie** : elle rassemble les textes, mais aussi les relations entre les textes.


## Pourquoi ce projet pour un atelier d’IA ?

- Le projet montre une chaîne complète, de l'objet littéraire au traitement computationnel.
- Le modèle d’IA n’est qu’une étape dans cette chaîne.
- Avant lui, il y a déjà des choix éditoriaux, de structure, d’export et de représentation.

Ces choix déterminent ce que le modèle peut voir, ignorer, regrouper...


## Pourquoi un CSV ?

- CSV : format lisible, tabulaire, facile à ouvrir et à manipuler
- Il permet d’apprendre les gestes de base : inspecter, nettoyer, transformer et analyser.
- Chaque ligne correspond à une entrée textuelle, ici une épigramme de 2 à 6 vers. 


## Ce que contient l’export

Le fichier contient **15 épigrammes** du livre VII.

| Colonne | Contenu |
|---|---|
| `epigramme_id` | identifiant lisible de l’épigramme |
| `book` | livre de l’Anthologie |
| `fragment` | numéro dans le livre |
| `urn` | identifiant stable |
| `author_fr` | auteur ou attribution en français |
| `text_fr` | traduction française |

## Texte et métadonnées

- La colonne `text_fr` servira aux opérations sur le texte : nettoyage, segmentation, fréquences et vectorisation.
- Les métadonnées permettent de situer chaque épigramme dans le corpus.
- La colonne `author_fr` contient parfois des attributions simples, parfois des attributions multiples.

## Que faire de ce corpus ?

- Même un petit corpus permet de poser des questions intéressantes.
- Exemple : Projet IAL.
- Autres projets : Égée, NER, Linked Open Data...
- Avez-vous des exemples de questions ? 

## Récapitulatif

- Nous avons maintenant :
    - Un objet textuel ; 
    - Un export CSV ;
    - Des métadonnées ;  
    - Même quelques questions de départ.

## Transition vers Python

- La prochaine étape consiste à transformer ces éléments en opérations concrètes :
    - charger le fichier dans Python ;
    - inspecter la structure du corpus ;
    - nettoyer les textes ;
    - segmenter les chaînes de caractères ;
    - compter certains phénomènes ;
    - préparer les données pour des analyses plus avancées.

# Exercice

TODO

# Pause 

# Prétraitement du texte 

## Nettoyage

## Segmentation 

## Tokenisation

## Principes du prétraitement <!-- Yann -->

## _Shit in shit out_

# Pause de midi 

## Bibliographie

