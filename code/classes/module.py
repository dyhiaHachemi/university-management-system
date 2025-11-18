class Module:
    """
    Represente une matiere d'etude 
    Possede un nom et un coefiscient
    """
    # constructeur de la classe Module
    def __init__(self, name, coef):
        self.name = name
        self.coef = coef

    def __str__(self):
        """
        représente en chaîne de caractères un objet
        """
        return(f"{self.name} (coef {self.coef})")