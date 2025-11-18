from classes.person import Person
from classes.depChief import DepChief

class FacDir (Person):
    def __init__(self, name, phone_number, email,faculty):
        super().__init__(name, phone_number, email)
        self.faculty = faculty
    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phone_number}")
        
    # modifier un chef de dep
    def set_dep_chief(self,dep_chief,dep_name):
        for dep in self.faculty.list_of_dep :
            if (dep.name == dep_name) :
                if (isinstance (dep_chief, DepChief)):
                    dep.dep_chief = dep_chief
                    print(f"Le chef du {dep_name} a ete change.")
                    return
                else :
                    # l'entree n'est pas un chef de departement
                    print("Erreur : l'objet doit être une instance de la classe DepChief.")
                    return
            
        print("Erreur : Departement introuvable dans cette faculte.")        
                    