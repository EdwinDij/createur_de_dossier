from pathlib import Path

cwd = Path.cwd()

current_p = cwd / "dictionnaire" / "creation_de_dossier"

print(current_p )

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]
     }

for dossier_principal, sous_dossiers in d.items():
    for dossier in sous_dossiers:
        chemin_dossier = Path(current_p) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)

