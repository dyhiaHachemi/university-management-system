from classes.person import Person
from classes.facDirector import FacDir
from classes.depChief import DepChief

class UnivDirector(Person):
    def __init__(self, name, phone_number, email, university):
        super().__init__(name, phone_number, email)
        self.university = university

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phone_number}")
     
     # modifier un chef de dep
    
    # set le chef de departement
    def set_dep_chief(self,dep_chief : DepChief ,dep_name,fac_name):
        # trouver la faculte
        for fac in self.university.list_of_fac:
            if (fac.name == fac_name):
                # trouver le departement
                for dep in fac.list_of_dep :
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
        print("Erreur : Faculte introuvable dans cette universite.")    

    # set le directeur de faculty
    def set_fac_director(self,fac_director : FacDir ,fac_name):
        for fac in self.university.list_of_fac :
            if (fac.name == fac_name) :
                if (isinstance (fac_director, FacDir)):
                    fac.fac_director = fac_director
                    print(f"Le directeur de {fac_name} a ete change.")
                    return
                else :
                    # l'entree n'est pas un chef de departement
                    print("Erreur : l'objet doit être une instance de la classe FacDirector.")
                    return
        print("Erreur : Faculte introuvable dans cette universite.")        
                    