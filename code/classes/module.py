"""
    class Module (Name, Coef)
"""
class Module:
    # constructeur de la classe Module
    def __init__(self, name, coef):
        self.name = name
        self.coef = coef

    # affichage des objets de la classe Module
    def __str__(self):
        return(f"{self.name} (coef {self.coef})")