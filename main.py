import json
from flask import Flask, render_template

from scripts import wane, tout, tri

# --- PARTIE 1 ---
tableau_citations = wane.TableauCitations()  # Initialisation du tableau de citations
tableau_citations.afficher_citation_aleatoire()  # Affichage d'une citation au hasard

# --- PARTIE 2 ---
chat = tout.Animal(2, "Miaou", "Roux")  # Création d'un Animal
chat_dict = chat.to_dict()  # Conversion Animal => Dictionnaire
json_string = json.dumps(chat_dict)  # Conversion du dictionnaire en objet JSON
print(json_string)  # Affichage dans le terminal

# --- PARTIE 3 ---
app = Flask(__name__)


@app.route('/')
def home():
    system_info = tri.SystemInfo()
    return render_template('table.html', system_info=system_info)


if __name__ == '__main__':
    app.run(debug=True)

# LIVRABLE
# Deadline : 17h 16/03/2023, vous organisez votre journée comme vous le sentez.
# Livraison un dépôt git PUBLIC, mettez le lien de votre dépôt direct sur Teams dans le rendu de devoir.
