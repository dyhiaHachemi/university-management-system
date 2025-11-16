"""
la classe Student est une classe heritée de la classe Person 

"""
# importation de la classe mère Person pour instanciation de l'objet Student
from classes.person import Person
# importation de la classe Note pour creation de la liste des notes pour chaque etudiant
from classes.note import Note

class Student(Person):
    def __init__(self, address, name, email, phoneNumber):
        # initialiser les attributs de la classe parente Person
        super().__init__(name, email, phoneNumber)
        # initialiser les attributs définis dans la classe enfant Student
        self.address = address
        self.notes = []  # liste de Note vide à l'initialisation
        
    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f"- Etudiant: {self.name} \n Addresse: {self.address} \n Email: {self.email} \n Numero de Telephone: {self.phoneNumber}")
    
    # Liste des notes
    def addNote(self,note):
        # on verifie si l'entree d'utilisateur est bien un objet de la classe Note ex:(12,'math')
        if (isinstance(note,Note)):
            # ajout de la note a la liste des notes de l'etudiant
            self.notes.append(note) 
        else: 
            # l'entree n'est pas une note ex: ("math", 12) 
            print("Erreur : l'objet doit être une instance de la classe Note.")

    # affichage de la liste des notes
    def displayNotes(self):
        print(f"- Les notes de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.notes): 
            print("Aucune note disponible.")
            return
        else:
            # pour chaque note de la liste des notes
            for note in self.notes :
                print(f" {note}") # appel de la fct __str__ de la classe Note