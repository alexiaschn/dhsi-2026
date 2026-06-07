---
title: "Jour 4 PM : Les modèles génératifs (suite)"
date: 2026-06-11
author: 
    - name: Alexia Schneider 
      orcid: 0009-0000-0651-9792
      email: alexia.schneider@umontreal.ca
    - name: William Bouchard
      orcid: "https://orcid.org/0009-0003-3683-2415"
      email: william.bouchard2@umontreal.ca
bibliography: ../dhsi2026.bib
link-citations: true
colorlinks: true
fig-cap-location: top
format:
    revealjs: 
        output-file: "jour04PM.html" 
        # template: simple
        smaller: true
        # incremental: true
        scrollable: true
        slide-number: true
---

# L'affinage de modèle

## Du prompt à l’affinage

- Ce matin, nous avons surtout contrôlé le modèle par le prompt.
- Cet après-midi, nous allons voir comment adapter un modèle par entraînement.
- Le prompt modifie ce que l’on demande au modèle.
- L’affinage modifie une partie de ce que le modèle sait faire.
- Fine-tuner, en bref, c’est modifier ses poids.


## Pourquoi affiner un modèle ?

- On affine un modèle quand une tâche revient souvent.
- C’est utile quand le domaine est spécialisé ou très codifié.
- Cela peut aider à produire un format de sortie plus stable.
- Cela permet parfois de mieux gérer un vocabulaire technique.
- Cela évite aussi de dépendre d’un prompt interminable, fragile et franchement pénible.


## Exemple d’usage

- On pourrait demander à un modèle de classifier des épigrammes avec un prompt.
- Mais si la tâche revient souvent, le prompt devient vite répétitive.
- Un modèle affiné peut apprendre une consigne stable.
- Exemple : associer chaque épigramme à une catégorie comme funéraire, votive, érotique...
- L’objectif est alors d’apprendre un comportement récurrent.


## Ce que le fine-tuning n’est pas

- Le fine-tuning n’est pas une base de données.
- Ce n’est pas une mémoire parfaite.
- Ce n’est pas une garantie de vérité.
- Ce n’est pas toujours nécessaire.
- Si le problème est surtout d’ajouter des documents, le RAG est souvent plus adapté.


## Fine-tuning ou RAG ?

- Demain, nous parlerons de la Retrieval Augmented Generation (RAG).
- Le fine-tuning sert surtout à apprendre un comportement.
- Le RAG sert surtout à fournir de l’information au modèle.
- Pour changer un style, une structure ou une tâche répétée, l’affinage peut être utile.
- Pour donner accès à des documents précis, il vaut mieux les récupérer au moment de la requête.
- Le fine tuning change le comportement, pas l'information.


## Les grands types d’affinage

- Le fine-tuning complet modifie tous les poids du modèle.
- Le supervised fine-tuning entraîne le modèle sur des exemples entrée → sortie.
- L’instruction tuning apprend au modèle à suivre des consignes.
- PEFT et LoRA modifient seulement une petite partie du modèle.


## Les données d’entraînement

- Un affinage repose sur des exemples bien préparés.
- Chaque exemple contient une entrée et une sortie attendue.
- Pour une classification, la sortie peut être un label.
- Pour un modèle instructionnel, on utilise souvent un format instruction / input / output.
- Les données doivent être séparées en entraînement, validation et test.


## Exemple de format

```json
{
  "instruction": "Classe cette épigramme.",
  "input": "...",
  "output": "érotique"
}
```

- L’instruction dit au modèle quoi faire.
- L’entrée contient le texte à traiter.
- La sortie donne la réponse attendue.
- Le modèle apprend à reproduire ce type de correspondance.

## Pipeline général
```text
Corpus brut
→ nettoyage
→ annotation / labels
→ formatage
→ entraînement
→ évaluation
→ comparaison au modèle de base
```

- Le vrai travail consiste à préparer des données fiables.
- Un modèle affiné apprend à partir de ce qu’on lui donne.
- Si les exemples sont flous, le comportement appris sera flou aussi.

## Évaluer un modèle affiné

Il faut comparer le modèle avant et après l’affinage.
Pour une classification, on peut utiliser l’accuracy ou le F1-score.
L’évaluation humaine reste essentielle pour les cas ambigus.
L’analyse des erreurs permet de comprendre ce que le modèle rate.
Il faut toujours tester des exemples difficiles, pas seulement les cas gentils qui sourient au modèle.

## Risques et limites
Le modèle peut surapprendre les exemples d’entraînement.
Un petit dataset peut donner une impression trompeuse d’amélioration.
Les biais présents dans les données peuvent être amplifiés.
Le modèle peut oublier certains comportements utiles : c’est le catastrophic forgetting.
Si ton dataset est croche, ton modèle sera croche avec confiance.

## Quand choisir quoi ?

| Besoin | Solution |
|---------|:------|
| Changer le style ou le format | Prompt 
Ajouter des documents précis | RAG 
Apprendre une tâche répétée | Fine-tuning 
Classer avec peu d’exemples | Prompting ou modèle classique 
Domaine très spécialisé | Fine-tuning possible      

## Démonstration

Nous allons :
- charger un petit modèle ;
- observer le format des exemples.
- lancer un entraînement.
- comparer le comportement avant et après.