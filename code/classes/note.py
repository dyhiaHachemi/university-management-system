class Note:
    """
    Represente la note de chaque module
    module est un objet de type Module uttilisé pour le calcul de la moyenne 
    """
    def __init__(self, value, module):
        self.value = value        
        self.module = module    
    
    def __str__(self):
        """
        représente en chaîne de caractères un objet
        """
        return(f"{self.module.name} : {self.value} /Coefficient: {self.module.coef}")