# importation de la classe mère Person pour instanciation de l'objet Student
from classes.person import Person
# importation de la classe Note pour creation de la liste des notes pour chaque etudiant
from classes.note import Note

class Student(Person):
    """
    Classe heritée de la classe Person 
    Chaque etudiant a une liste des notes
    """
    def __init__(self, address, name, email, phone_number):
        # initialiser les attributs de la classe parente Person
        super().__init__(name, email, phone_number)
        # initialiser les attributs définis dans la classe enfant Student
        self.address = address
        self.notes = []  # liste de Note vide à l'initialisation
        
    def __str__(self):
        """
        représente en chaîne de caractères un objet
        """
        return (f"- Etudiant: {self.name} \n Addresse: {self.address} \n Email: {self.email} \n Numero de Telephone: {self.phone_number}")
    
    def add_note(self,note : Note):
        """
        Ajout d'une note a la liste des notes de l'etudiant
        """
        # on verifie si l'entree d'utilisateur est bien un objet de la classe Note ex:(12,'math')
        if (isinstance(note,Note)):
            # ajout de la note a la liste des notes de l'etudiant
            self.notes.append(note) 
        else: 
            # l'entree n'est pas une note ex: ("math", 12) 
            print("Erreur : l'objet doit être une instance de la classe Note.")

    # affichage de la liste des notes
    def display_notes(self):
        """
        Affiche la liste des notes de chaque etudiant
        """
        print(f"- Les notes de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.notes): 
            print("Aucune note disponible.")
            return
        else:
            # pour chaque note de la liste des notes
            for note in self.notes :
                print(f" {note}") # appel de la fct __str__ de la classe Note