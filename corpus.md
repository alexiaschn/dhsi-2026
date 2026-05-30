

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
# Jeux de données utilisés au cours de la semaine

 <table><thead><tr><th>Document</th><th>Format</th></tr></thead>

<tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/epigrammes_a_nettoyer.txt', 'epigrammes_a_nettoyer.txt'); return false;">epigrammes_a_nettoyer.txt</a></td><td>.txt</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/epigrammes_anthologia_graeca_fr.csv', 'epigrammes_anthologia_graeca_fr.csv'); return false;">epigrammes_anthologia_graeca_fr.csv</a></td><td>.csv</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/epigrammes_anthologia_graeca_fr.txt', 'epigrammes_anthologia_graeca_fr.txt'); return false;">epigrammes_anthologia_graeca_fr.txt</a></td><td>.txt</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/epigrammes_classification_animal.csv', 'epigrammes_classification_animal.csv'); return false;">epigrammes_classification_animal.csv</a></td><td>.csv</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/epigrammes_no_animal.csv', 'epigrammes_no_animal.csv'); return false;">epigrammes_no_animal.csv</a></td><td>.csv</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/flow-classification-animal.cforge', 'flow-classification-animal.cforge'); return false;">flow-classification-animal.cforge</a></td><td>.cforge</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/pca_epigrammes_fr.html', 'pca_epigrammes_fr.html'); return false;">pca_epigrammes_fr.html</a></td><td>.html</td></tr><tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/similarites_top5_epigrammes_fr.csv', 'similarites_top5_epigrammes_fr.csv'); return false;">similarites_top5_epigrammes_fr.csv</a></td><td>.csv</td></tr></table>