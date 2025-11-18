"""
    class Note(value, module)
    module est un objet de type Module uttilisé pour le calcul de la moyenne 
"""
class Note:
    def __init__(self, value, module):
        self.value = value        
        self.module = module    
    
    #représentation en chaîne de caractères d'un objet
    def __str__(self):
        return(f"{self.module.name} : {self.value} /Coefficient: {self.module.coef}")