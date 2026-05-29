---
title: Index des notebooks
listing: 
    contents: notebooks/*_complet.ipynb
    type: table
    sort: "date"
---

<script>
function downloadFile(url, filename) {
  fetch(url)
    .then(response => response.blob())
    .then(blob => {
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    })
    .catch(error => console.error("Erreur de téléchargement:", error));
}
</script>
# Télécharger les notebooks au format ipynb

Pour obtenir les notebooks au format ipynb: 

``` Clic droit + Enregistrer la cible du lien sous...```


- <a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/jour1_IASymboliqueConnexionniste_exercice.ipynb', 'jour1_IASymboliqueConnexionniste_exercice.ipynb'); return false;">jour1_IASymboliqueConnexionniste_exercice.ipynb</a>
- <a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/jour2_BoW_TFiDF_exercice.ipynb', 'jour2_BoW_TFiDF_exercice.ipynb'); return false;">jour2_BoW_TFiDF_exercice.ipynb</a>


# Lire les notebooks au format HTML