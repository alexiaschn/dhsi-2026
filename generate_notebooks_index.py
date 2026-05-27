from pathlib import Path

notebooks = sorted(Path("notebooks").glob("*_exercice.ipynb"))

content = """---
title: Index des notebooks
listing: 
    contents: notebooks/*_complet.ipynb
    type: table
    sort: "date"
---

# Télécharger les notebooks au format ipynb

Pour obtenir les notebooks au format ipynb: 

``` Clic droit + Enregistrer la cible du lien sous...```

"""

for nb in notebooks:
    name = nb.name
    content += f'- [{name}]({nb.as_posix()}){{download="{name}"}}\n'
    content += f"\n\n# Lire les notebooks au format HTML"

Path("notebooks.md").write_text(content, encoding="utf-8")

print("Page générée.")