from classes.person import Person
from classes.facDirector import FacDir
from classes.depChief import DepChief

class UnivDirector(Person):
    """
    Represente le directeur de l'universite designé par l'universite
    Peut affecter un chef de departement a un departement
    Peut affecter un directeur a une faculte
    """
    def __init__(self, name, phone_number, email, university):
        super().__init__(name, phone_number, email)
        self.university = university

    def __str__(self):
        """
        représentation en chaîne de caractères d'un objet
        """
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phone_number}")
     
    def set_dep_chief(self,dep_chief : DepChief ,dep_name,fac_name):
        """
        set le chef de departement
        """
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

    def set_fac_director(self,fac_director : FacDir ,fac_name):
        """
        set le directeur d'une faculte
        """
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
                    