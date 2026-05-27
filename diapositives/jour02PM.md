---
title: "Jour 2 après-midi : Automatisation du prétraitement d'un corpus textuel"
date: 2026-06-09
author: 
    - name: Alexia Schneider 
      orcid: 0009-0000-0651-9792
      email: alexia.schneider@umontreal.ca
    - name: Yann Audin
      orcid: https://orcid.org/0000-0003-3456-9767
      email: yann.audin@umontreal.ca
bibliography: ../dhsi2026.bib
link-citations: true
colorlinks: true
fig-cap-location: top
format:
    revealjs: 
        output-file: "jour02PM.html" 
        # template: simple
        smaller: true
        # incremental: true
        scrollable: true
        slide-number: true
---
    
# Programme de l'après-midi

PM: (2h30)

- Atelier de nettoyage de corpus (45 minutes) @alexia
- PAUSE (15 min)
- Représentations vectorielles (20 minutes + 40 minutes d'exercice) @alexia
    - BOW
    - TF-IDF
- Classification (15 minutes + 15 minutes de démonstration)
    - RandomForest 
    - LR 
    - etc.

## Nettoyer et structurer un corpus avec des Regex

<!--In a world of human REGEX  plowed-sponge.mp4  -->

Les expressions régulières sont des caractères spéciaux qui turbo-chargent la fonction `Ctrl+F`. 

Les possibilités des regex sont infinies :

- identifier des motifs 
- extraire ('capturer') les motifs
- substituer un motif par un autre

Par conséquent, c'est une forme d'automatisation ou IA symboliste de bas niveaux essentielle pour structurer et nettoyer un corpus textuel avec une grande précision à un coût computationnel très très faible.

## Principes de base des regex 


[Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)



## Regex avec Python

Module `re` : 

```
import re 
```


[Documentation](https://docs.python.org/3/library/re.html)




## Atelier Expression régulière ou _Regular Expression_ / Regex

Importer le notebook : 

jour2_regex_exercice.ipynb 

La correction est en HTML : 

jour2_regex_complet.ipynb 


# Pause

## Repésentation vectorielle : Principes



## BOW

## TF-IDF

Term Frequency inverse Document Frequency

## Exercice 



## Algorithmes de classification

## Random Forrest

## Logistic Regression

## Bibliographie


   