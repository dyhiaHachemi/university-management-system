
from classes.faculty import Faculty
from classes.univDirector import UnivDirector

class University():
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.univ_director = None # aucun directeur au depart
        self.list_of_fac = []

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Numero de Telephone: {self.phone_number} \n Email: {self.email} \n Addresse: {self.address} ")
    
    # Ajout d'un departement a la liste
    def add_fac(self,fac):
        if (isinstance(fac, Faculty)):
            self.list_of_fac.append(fac)
        else:
            # l'entree n'est pas une faculty
            print("Erreur : l'objet doit être une instance de la classe Faculty.")

    # affichage de la liste des Departements
    def display_fac(self):
        print(f"- Les Facultes de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_fac): 
            print("Aucune Faculte disponible.")
            return
        else:
            # pour chaque fac de la liste des fac
            for fac in self.list_of_fac :
                print(f" {fac}") # appel de la fct __str__ de la classe faculty    
    
    # suppression d'une faculte 
    def remove_fac(self,fac):
        self.list_of_fac.remove(fac)

    # definir le directeur de l'universite
    def set_univ_director(self, director):
        if (isinstance(director , UnivDirector)):
            self.univ_director = director
            print(f"Le directeur de l'{self.name} a ete defini : {director.name}")
        else:
            print("Erreur : le directeur doit être une instance de UnivDirector")
