from classes.person import Person
from classes.facDirector import FacDir
from classes.depChief import DepChief
class UnivDirector(Person):
    def __init__(self, name, phoneNumber, email):
        super().__init__(name, phoneNumber, email)

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phoneNumber}")
     
     # modifier un chef de dep
    
    # set le chef de departement
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

    # set le directeur de faculty
    def setFacDirector(self,facDirector,facName):
        for fac in self.university.listOfFac :
            if (fac.name == facName) :
                if (isinstance (facDirector, FacDir)):
                    fac.facDirector = facDirector
                    print(f"Le directeur de {facName} a ete change.")
                    return
                else :
                    # l'entree n'est pas un chef de departement
                    print("Erreur : l'objet doit être une instance de la classe FacDirector.")
                    return
        print("Erreur : Faculte introuvable dans cette universite.")        
                    