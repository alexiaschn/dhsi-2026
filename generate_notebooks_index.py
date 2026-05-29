from pathlib import Path

notebooks = sorted(Path("notebooks").glob("*_exercice.ipynb"))

content = """---
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


"""

for nb in notebooks:
    name = nb.name
    content += f"""- <a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/{name}', '{name}'); return false;">{name}</a>\n"""

content += f"\n\n# Lire les notebooks au format HTML"

Path("notebooks.md").write_text(content, encoding="utf-8")

print("Page générée.")