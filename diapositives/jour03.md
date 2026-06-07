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

- Introduction à l'apprentissage profond (30 minutes) 
- Réseaux de neurones (45 minutes + 15 minutes démonstration) 
    - [3 blue 1 brown?](https://www.youtube.com/watch?v=aircAruvnKk)
- PAUSE (15 minutes)
- GloVe/Word2Vec (45 minutes + 30 minutes atelier) 

PM: (2h30)

- BERT (60 minutes + 15 minutes démonstration) 
    - Mécanisme d'attention
- PAUSE (15 minutes)
- Préparation du travail final (60 minutes) 
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

# BERT et les représentations contextualisées

## Pourquoi BERT ? 

- Jusqu’ici, nous avons surtout représenté les textes avant de les donner aux modèles.
- Avec BERT, la représentation devient elle-même une partie du modèle.
- Le même mot peut recevoir des vecteurs différents selon son contexte.
- C’est ce changement qui rend BERT important pour l’analyse du texte.

## Limites des approches vues jusqu’ici

- Bag-of-Words et TF-IDF comptent les mots, mais perdent l’ordre et le contexte.
- Word2Vec et GloVe captent des proximités sémantiques, mais donnent une représentation stable.
- Les modèles classiques restent utiles, mais dépendent beaucoup des traits construits au départ.
- Le problème central n’est donc pas seulement de classer.
- Le problème est aussi de représenter des mots dont le sens change selon la phrase.

## L’idée centrale de BERT

- BERT signifie **Bidirectional Encoder Representations from Transformers**.
- Il lit le texte en tenant compte de ce qui vient avant et après un token.
- Il produit une représentation vectorielle pour chaque token.
- Cette représentation dépend du contexte précis où le token apparaît.
- BERT ne donne donc pas seulement un vecteur au mot : il donne un vecteur au mot dans une phrase.

## Un même mot, plusieurs contextes

- Le mot “tombe” ne joue pas le même rôle dans “il tombe” et “une tombe funéraire”.
- Le mot “chant” peut désigner une voix, une œuvre poétique ou une pratique rituelle.
- Dans BERT, ces usages peuvent recevoir des représentations différentes.
- Le modèle tient compte des mots voisins pour construire le sens local.
- C’est ce qui rend BERT intéressant pour des corpus littéraires.

## Tokenisation BERT

- BERT ne lit pas exactement des mots.
- Il lit des **tokens**, souvent des mots ou des fragments de mots.
- Un mot long ou rare peut être découpé en sous-mots.
- Par exemple, “internationalisation” peut être divisé en plusieurs morceaux selon le tokenizer.
- Ce découpage permet au modèle de traiter des mots qu’il n’a pas vus exactement sous cette forme.

## Tokens spéciaux

- BERT utilise aussi des tokens spéciaux.
- `[CLS]` sert à représenter l’ensemble d’une séquence.
- `[SEP]` sert à séparer des segments ou à marquer la fin d’une séquence.
- `[MASK]` sert pendant l’entraînement à cacher un token que le modèle doit deviner.
- Ces tokens sont des balises de travail pour le modèle.

## Le Transformer en une image mentale

- BERT est une pile d’encodeurs Transformer.
- Chaque couche transforme les représentations produites par la couche précédente.
- Les embeddings donnent une première représentation des tokens.
- L’attention permet aux tokens de tenir compte les uns des autres.
- À la sortie, chaque token possède une représentation enrichie par le contexte.

## Le mécanisme d’attention

- L’attention permet à chaque token de regarder les autres tokens de la séquence.
- Le modèle calcule quels autres tokens sont utiles pour construire sa représentation.
- Ce calcul produit des relations entre tokens.
- Ces relations ne sont pas forcément une explication humaine.
- Mais elles indiquent comment l’information circule dans le modèle.

## Exemple d’attention

> Le roi donne son épée à son fils parce qu’*il* part à la guerre.

- Le pronom “il” dépend du contexte.
- Pour l’interpréter, certains mots deviennent importants : “roi”, “fils”, “donne”, “part”, “guerre”.
- Le modèle calcule des liens entre ces tokens.
- L’attention sert à pondérer ces liens.
- Elle aide donc à construire une représentation contextualisée de “il”.

## Self-attention

- On parle de **self-attention** parce que la phrase s’analyse à partir d’elle-même.
- Chaque token reçoit de l’information des autres tokens de la même séquence.
- Le mot “roi” peut être enrichi par “donne”, “épée”, “fils” ou “guerre”.
- Le mot “fils” peut être enrichi par “donne”, “épée” ou “il”.
- Le mot “il” peut être enrichi par les mots qui aident à résoudre la référence.

## Mini-schème de self-attention

```text
roi  → regarde → donne / épée / fils / guerre
fils → regarde → donne / épée / il
il   → regarde → roi / fils / part / guerre
```
- Le mot ne reste pas isolé.
- Il devient une représentation nourrie par les autres mots.
- Le contexte n’est pas ajouté après coup : il est construit dans le modèle.

## Multi-head attention

- Une seule attention ne suffit pas toujours.
- BERT utilise plusieurs têtes d’attention en parallèle.
- Chaque tête peut capter un type différent de relation.
- Certaines relations peuvent être syntaxiques, référentielles ou thématiques.

## Comment BERT est entraîné

- BERT est d’abord pré-entraîné sur de grands corpus.
- Pendant cet entraînement, certains tokens sont masqués.
- Le modèle doit prédire les tokens cachés à partir du contexte.
- Exemple : “Le chat boit du [MASK].”
- Il apprend des régularités linguistiques avant d’être adapté à une tâche précise.

## Pré-entraînement et adaptation

- Le pré-entraînement donne à BERT une compétence linguistique générale.
- Ensuite, on peut l’utiliser pour une tâche particulière.
- On peut l’utiliser directement pour extraire des embeddings.
- On peut aussi l’adapter avec des exemples annotés : c’est le fine-tuning.
- Dans les deux cas, le modèle hérite de ce qu’il a appris dans ses corpus de départ.

## Utiliser BERT pour une tâche

- BERT peut servir à classifier des textes.
- Il peut comparer la similarité entre deux passages.
- Il peut aider à extraire des informations.
- Il peut soutenir l’annotation ou l’exploration de corpus.
- En SHS, il peut aider à comparer des usages, des motifs ou des catégories.

## Les limites de BERT

- BERT ne comprend pas comme un lecteur humain.
- Il dépend fortement des corpus sur lesquels il a été entraîné.
- Il peut encoder des biais présents dans ces corpus.
- Il peut être fragile sur des textes spécialisés, anciens ou très bruités.
- Il produit des représentations, pas des interprétations.

## Prudence interprétative

- Un vecteur proche n’est pas automatiquement une preuve littéraire.
- Une attention forte n’est pas automatiquement une explication.
- Une bonne performance ne signifie pas que le modèle raisonne comme nous.
- Les résultats doivent être replacés dans le corpus, la tâche et les choix de méthode.

## Démonstration

- Nous allons :
    - charger un modèle de type BERT.
    - tokeniser une ou plusieurs phrases.
    - observer les tokens produits par le tokenizer.
    - obtenir des embeddings contextualisés.