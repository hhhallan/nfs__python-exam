class Animal:
    # Initialisation de la classe avec ses infos
    def __init__(self, age, prenom, couleur):
        self.age = age
        self.prenom = prenom
        self.couleur = couleur

    # Fonction qui convertit les informations en dictionnaire
    def to_dict(self):
        return {
            'age': self.age,
            'prenom': self.prenom,
            'couleur': self.couleur
        }