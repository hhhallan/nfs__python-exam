class Animal:
    def __init__(self, age, prenom, couleur):
        self.age = age
        self.prenom = prenom
        self.couleur = couleur

    def to_dict(self):
        return {
            'age': self.age,
            'prenom': self.prenom,
            'couleur': self.couleur
        }