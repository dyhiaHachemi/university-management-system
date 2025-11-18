
from classes.faculty import Faculty
from classes.univDirector import UnivDirector

class University():
    """
    Contient plusieurs Facultes
    A un directeur designé par l'universite
    Peut ajouter ou supprimer une faculté 
    
    """
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.univ_director = None # aucun directeur au depart
        self.list_of_fac = []

    def __str__(self):
        """
        représentation en chaîne de caractères d'un objet
        """
        return (f" - Nom: {self.name} \n Numero de Telephone: {self.phone_number} \n Email: {self.email} \n Addresse: {self.address} ")
    
    def add_fac(self,fac : Faculty):
        """
        Ajout une faculté a un université
        """
        if (isinstance(fac, Faculty)):
            self.list_of_fac.append(fac)
        else:
            # l'entree n'est pas une faculty
            print("Erreur : l'objet doit être une instance de la classe Faculty.")

    def display_fac(self):
        """
        Affiche la liste des facultés dans une université
        """
        print(f"- Les Facultes de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_fac): 
            print("Aucune Faculte disponible.")
            return
        else:
            # pour chaque fac de la liste des fac
            for fac in self.list_of_fac :
                print(f" {fac}") # appel de la fct __str__ de la classe faculty    
    
    def remove_fac(self,fac : Faculty):
        """
        Supprime une faculté d'une université
        """
        self.list_of_fac.remove(fac)

    def set_univ_director(self, director : UnivDirector):
        """
        definir le directeur de l'universite
        """
        if (isinstance(director , UnivDirector)):
            self.univ_director = director
            print(f"Le directeur de l'{self.name} a ete defini : {director.name}")
        else:
            print("Erreur : le directeur doit être une instance de UnivDirector")
