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

## Principes du prétraitement <!-- Yann -->

## _Shit in shit out_

## Structuration des données

# Pause 

## Manipuler des données avec Python

## API

# Prétraitement du texte 

## Nettoyage

## Segmentation 

## Tokenisation

# Pause de midi 

## Bibliographie

