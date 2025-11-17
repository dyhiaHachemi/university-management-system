from classes.person import Person
from classes.depChief import DepChief
from classes.faculty import Faculty

class FacDir (Person):
    def __init__(self, name, phoneNumber, email,faculty):
        super().__init__(name, phoneNumber, email)
        self.faculty = faculty
    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phoneNumber}")
        
    # modifier un chef de dep
    def setDepChief(self,depChief,depName):
        for dep in self.faculty.listOfDep :
            if (dep.name == depName) :
                if (isinstance (depChief, DepChief)):
                    dep.depChief = depChief
                    print(f"Le chef du {depName} a ete change.")
                    return
                else :
                    # l'entree n'est pas un chef de departement
                    print("Erreur : l'objet doit être une instance de la classe DepChief.")
                    return
            
        print("Erreur : Departement introuvable dans cette faculte.")        
                    