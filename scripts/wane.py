import random


class TableauCitations:
    def __init__(self):
        self.citations = [
            "J'ai les dents du fond qui baignent.",
            "Je vais mettre la viande dans le torchon.",
            "Je vais couler un bronze.",
            "Y'a pas à tortiller du cul pour chier droit.",
            "J'ai le cigare au bord des lèvres.",
            "Je vais lui casser les pattes arrière.",
            "Y'a les Anglais qui débarquent.",
            "Comme mes couilles lui, toujours entre mes pattes.",
            "Baisse ta culotte, c'est moi qui pilote.",
            "Si le barbec' n’existait pas, il faudrait l’inventer.(Voltaire)",
            "Je pense donc je suce mdr.(Descartes)",
            "Les couilles ont leurs raisons que la raison ne connaît pas.(Blaise Pascal)",
            "L’homme est un loup pour l’homme, et chui pas pd hein(Hobbes)",
            "Tu me remets la p'tite soeur.(Platon)",
        ]

    def ajouter_citation(self, citation):
        self.citations.append(citation)

    def afficher_citation_aleatoire(self):
        if len(self.citations) > 0:
            citation = random.choice(self.citations)
            print(citation)
        else:
            print("Ahah big looser y a même pas de citation dans ton tableau xD !")
