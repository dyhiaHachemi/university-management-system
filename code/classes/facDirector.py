from classes.person import Person
from classes.depChief import DepChief

class FacDir (Person):
    def __init__(self, name, phoneNumber, email):
        super().__init__(name, phoneNumber, email)

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phoneNumber}")
        
    # modifier un chef de dep
    def setDepChief(self,depChief):
        if (isinstance (depChief, DepChief)):
            depChief.name = depChief
        else :
            # l'entree n'est pas un chef de departement
            print("Erreur : l'objet doit être une instance de la classe DepChief.")
