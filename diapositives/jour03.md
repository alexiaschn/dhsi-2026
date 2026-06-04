---
# layout: slide
title: "Jour 3 : Apprentissage profond " 
date: 2026-06-10
author: 
    - name: William Bouchard
      orcid: "https://orcid.org/0009-0003-3683-2415"
      email: william.bouchard2@umontreal.ca
    - name: Yann Audin
      orcid: https://orcid.org/0000-0003-3456-9767
      email: yann.audin@umontreal.ca
bibliography: ../dhsi2026.bib
link-citations: true
colorlinks: true
fig-cap-location: top
format:
    revealjs: 
        output-file: "jour03.html" 
        # template: simple
        smaller: true
        # incremental: true
        scrollable: true
        slide-number: true
---

## Programme 

AM: (3h)

- Introduction à l'apprentissage profond (30 minutes) @william + @yann
- Réseaux de neurones (45 minutes + 15 minutes démonstration) @william
    - [3 blue 1 brown?](https://www.youtube.com/watch?v=aircAruvnKk)
- PAUSE (15 minutes)
- GloVe/Word2Vec (45 minutes + 30 minutes atelier) @yann

PM: (2h30)

- BERT (60 minutes + 15 minutes démonstration) @william + @yann
    - Mécanisme d'attention
- PAUSE (15 minutes)
- Préparation du travail final (60 minutes) @all
    - Travail en groupe, projet

# Introduction à l’apprentissage profond

## Objectif du bloc

- Comprendre pourquoi on parle d’**apprentissage profond**.
- Voir en quoi il diffère du machine learning classique.
- Comprendre pourquoi il est particulièrement utile pour les textes.
- On prépare le terrain pour la suite : réseaux, embeddings, transformers et LLM.
- Identifier aussi ses limites : données, calcul, biais et interprétation.


## Le rôle des représentations

- Jusqu’ici, nous avons surtout construit les représentations nous-mêmes.
- Avec une méthode comme TF-IDF, nous décidons comment transformer le texte en nombres.
- Le modèle apprend ensuite à partir de ces nombres.
- Cette approche dépend beaucoup de la représentation choisie au départ.
- Le problème est surtout de bien représenter.


## La limite du machine learning classique

- Un modèle peut voir “mort”, “perte” et “absence” comme des mots très différents.
- Pourtant, dans un corpus littéraire, ces mots peuvent participer à un même champ de sens.
- Si la représentation ne capture pas cette proximité, le modèle ne peut pas l’inventer facilement.
- Le modèle classique apprend sur une représentation déjà préparée.
- L’apprentissage profond cherche justement à apprendre une partie de cette représentation.


## L’idée centrale du deep learning

- Un modèle profond apprend à la fois une représentation et une tâche.
- Dans une approche classique : texte → représentation fabriquée → modèle.
- Dans une approche profonde : texte → représentations apprises → prédiction.
- Le modèle transforme progressivement les données pour faire émerger des régularités utiles.
- Ce n’est pas de la compréhension humaine, mais ce n’est pas non plus un simple comptage de mots.


## Pourquoi “profond” ?

- “Profond” signifie que le modèle contient plusieurs couches de transformation.
- Une première couche peut capter des indices simples.
- Les couches suivantes combinent ces indices en représentations plus complexes.
- La sortie finale sert ensuite à produire une décision, une classe ou une prédiction.

## Exemple avec les images

- Une image commence comme une grille de pixels.
- Certaines couches peuvent détecter des lignes ou des contrastes.
- D’autres couches peuvent combiner ces indices en formes.
- Des couches plus profondes peuvent aider à reconnaître des objets.


## Et pour le texte ?

- Un texte commence par des caractères, des mots ou des sous-mots.
- Le modèle peut apprendre des régularités de contexte et de cooccurrence.
- Il peut aussi capter certaines relations syntaxiques ou sémantiques.
- Ces couches ne correspondent pas directement à nos catégories humaines.

## Exemple textuel

> Le roi meurt au début du livre.

- On peut analyser cette phrase par ses mots : “roi”, “meurt”, “début”, “livre”.
- On peut aussi y voir une structure grammaticale.
- On peut encore y lire un rôle narratif : un événement déclencheur.
- Selon la tâche, le modèle peut apprendre certaines de ces régularités.
- Mais l’interprétation littéraire reste une opération humaine.


## Pourquoi c’est devenu important ?

- Les corpus numériques sont devenus beaucoup plus nombreux.
- La puissance de calcul a fortement augmenté.
- Les architectures sont devenues plus efficaces.
- Les embeddings ont permis de représenter les mots autrement que par simple comptage.
- Les transformers et les LLM ont ensuite changé l’échelle du problème.


## Ce que le deep learning fait très bien

- Il reconnaît des régularités complexes dans de grands ensembles de données.
- Il apprend des représentations plutôt que de dépendre seulement de règles préparées.
- Il peut travailler avec des données peu structurées : texte, image, son.
- Il généralise parfois bien à partir de nombreux exemples.
- Il est particulièrement utile quand les régularités sont difficiles à formaliser à la main.


## Ce qu’il fait moins bien

- Il demande souvent beaucoup de données.
- Il peut coûter cher en temps, en calcul et en énergie.
- Il est souvent difficile à interpréter.
- Il peut apprendre et amplifier des biais présents dans les données.
- Il peut donner une impression de compréhension sans réellement comprendre.


## En SHS : intérêt et prudence

- En SHS, ces modèles peuvent aider à explorer de grands corpus.
- Ils peuvent servir à classifier des textes, détecter des similarités ou repérer des motifs.
- Ils peuvent aussi soutenir l’annotation, la stylométrie ou l’analyse thématique.
- Mais la qualité du corpus reste centrale.
- Les catégories doivent être définies avec soin.

## Vers les réseaux de neurones

- Pour comprendre l’apprentissage profond, il faut commencer par son unité de base.
- Cette unité est le **réseau de neurones**.
- Nous allons voir comment il transforme des entrées en sorties.
- Nous verrons pourquoi cette idée simple peut devenir très puissante... et opaque!

[Vidéo](https://www.youtube.com/watch?v=aircAruvnKk)

# Les réseaux de neurones

## Un réseau de neurones, concrètement

- Un réseau de neurones est une fonction paramétrée.
- Il transforme une entrée en sortie en passant par plusieurs couches.
- Chaque couche applique des calculs aux données reçues.
- Le modèle apprend en ajustant progressivement ses paramètres.
- Entrée → couche cachée → sortie.


## Le neurone artificiel

- Un neurone artificiel reçoit plusieurs valeurs en entrée.
- Il combine ces valeurs avec des poids.
- Il ajoute parfois un biais.
- Il applique ensuite une fonction d’activation.
- En gros, c'est une petite fonction avec des boutons réglables.

$$
y = activation(w_1x_1 + w_2x_2 + w_3x_3 + b)
$$


## Les poids et le biais

- Les poids contrôlent l’importance accordée à chaque entrée.
- Un poids élevé signifie qu’un indice compte davantage dans le calcul.
- Le biais permet de décaler la décision du neurone.
- Pendant l’entraînement, le modèle ajuste ces valeurs.
- Apprendre, ici, c’est modifier les chiffres jusqu’à réduire l’erreur.


## Les fonctions d’activation

- On applique une fonction d’activation avant d’envoyer le résultat plus loin.
- Cette étape permet au réseau d’apprendre des relations plus complexes qu’une simple ligne droite.
- Sans activation, ajouter des couches ne rendrait pas vraiment le modèle plus expressif.
- Exemple courant : **ReLU**, qui coupe les valeurs négatives et garde les valeurs positives.

## Les couches

- La couche d’entrée reçoit les données.
- Les couches cachées transforment progressivement ces données.
- La couche de sortie produit la prédiction finale.
- Pour une classification, la sortie peut être une probabilité par classe.
- Exemple : texte vectorisé → couches cachées → probabilités de catégories.


## Exemple de classification

- On peut donner au réseau une représentation numérique d’un texte.
- Le réseau transforme cette représentation à travers ses couches.
- La sortie peut indiquer une catégorie probable.
- Pour des épigrammes, on pourrait imaginer : funéraire, votif, amoureux ou satirique.
- Le modèle associe des régularités numériques à des classes.


## La fonction de perte

- La perte mesure l’écart entre la prédiction du modèle et la réponse attendue.
- Si la bonne réponse est “funéraire” et que le modèle prédit seulement 40 % “funéraire”, la perte est élevée.
- Si le modèle prédit 92 % “funéraire”, la perte est plus faible.
- La perte sert donc de signal d’erreur.
- L’entraînement cherche à réduire cette perte.


## L’entraînement

- Le modèle commence avec des paramètres imparfaits.
- Il produit une prédiction.
- On mesure l’erreur avec la fonction de perte.
- On ajuste les poids pour réduire cette erreur.
- On recommence plusieurs fois : c’est le principe des **epochs**.


## Descente de gradient

- La perte dépend des poids du modèle : si les poids changent, l’erreur change aussi.
- Le **gradient** indique dans quelle direction l’erreur augmente le plus vite.
- La descente de gradient consiste à aller dans la direction inverse.
- Le **learning rate** contrôle la taille de cette modification.
- Trop petit : l’apprentissage est lent. Trop grand : le modèle peut dépasser la bonne zone.


## Surapprentissage

- Le surapprentissage arrive quand le modèle apprend trop bien les exemples d’entraînement.
- Il obtient alors de bons résultats sur les données vues.
- Mais il généralise mal sur de nouveaux exemples.
- Un modèle qui mémorise n’est pas forcément un modèle utile.


## Hyperparamètres

- On peut régler le nombre de couches.
- On peut régler le nombre de neurones par couche.
- On peut choisir le learning rate.
- On peut choisir le nombre d’epochs.
- On peut aussi ajuster la taille des lots de données, ou **batch size**.
- Ces choix s’appellent des **hyperparamètres** et peuvent avoir des effets variés.


## Dans la démonstration

- Nous allons :
    - créer un petit réseau de neurones ;
    - l’entraîner sur des données simples ;
    - observer l’évolution de la perte ;
    - regarder comment les prédictions changent ;
    - modifier un paramètre pour voir son effet.