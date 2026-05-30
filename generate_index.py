from pathlib import Path
import glob
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

<table><thead><tr><th>Document</th></tr></thead>
"""

for nb in notebooks:
    name = nb.name
    content += f"""<tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/{name}', '{name}'); return false;">{name}</a></td></tr>"""

content += f"</table>\n\n# Lire les notebooks au format HTML"

Path("notebooks.md").write_text(content, encoding="utf-8")
print("Index des notebooks générés.")

# corpus_files = [file for file in glob.glob('notebooks/corpus/*')]
corpus_files = sorted(Path("notebooks/corpus").glob("*"))


corpus_content = """

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
# Jeux de données utilisés au cours de la semaine\n\n <table><thead><tr><th>Document</th><th>Format</th></tr></thead>

"""

for file in corpus_files:
  name = file.name
  corpus_content += f"""<tr><td><a href="#" onclick="downloadFile('https://raw.githubusercontent.com/alexiaschn/dhsi-2026/main/notebooks/corpus/{name}', '{name}'); return false;">{name}</a></td><td>{file.suffix}</td></tr>"""

corpus_content += '</table>'
Path("corpus.md").write_text(corpus_content, encoding="utf-8")

print('Index du corpus généré')