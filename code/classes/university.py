
from classes.faculty import Faculty
from classes.univDirector import UnivDirector

class University():
    def __init__(self, name, phoneNumber, email, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address
        self.univDirector = None # aucun directeur au depart
        self.listOfFac = []

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Numero de Telephone: {self.phoneNumber} \n Email: {self.email} \n Addresse: {self.address} ")
    
    # Ajout d'un departement a la liste
    def addFac(self,fac):
        if (isinstance(fac, Faculty)):
            self.listOfFac.append(fac)
        else:
            # l'entree n'est pas une faculty
            print("Erreur : l'objet doit être une instance de la classe Faculty.")

    # affichage de la liste des Departements
    def displayFac(self):
        print(f"- Les Facultes de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.listOfFac): 
            print("Aucune Faculte disponible.")
            return
        else:
            # pour chaque fac de la liste des fac
            for fac in self.listOfFac :
                print(f" {fac}") # appel de la fct __str__ de la classe faculty    
    
    # suppression d'une faculte 
    def removeDep(self,fac):
        self.listOfFac.remove(fac)

    # definir le directeur de l'universite
    def setUnivDirector(self, director):
        if (isinstance(director , UnivDirector)):
            self.univDirector = director
            print(f"Le directeur de l'universite a ete defini : {director.name}")
        else:
            print("Erreur : le directeur doit être une instance de UnivDirector")
