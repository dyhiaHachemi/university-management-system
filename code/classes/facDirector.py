from classes.person import Person
from classes.depChief import DepChief

class FacDir (Person):
    """
    Represente le directeur de faculte design& par le directeur de l'universite
    Peut affecter un chef de departement a un departement
    """
    def __init__(self, name, phone_number, email,faculty):
        super().__init__(name, phone_number, email)
        self.faculty = faculty
    
    def __str__(self):
        """
        Représente en chaîne de caractères un objet
        """
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phone_number}")
        
    def set_dep_chief(self, dep_chief : DepChief , dep_name):
        """
        Set un chef de departement 
        """
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
                    