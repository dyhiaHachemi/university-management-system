"""
pour tester la classe Student il faut avoir d'abord creer des notes et des modules
"""

# importation des differentes classes
from classes.module import Module
from classes.note import Note
from classes.student import Student

if __name__ == "__main__":
    
    # teste des classes Module et Note
    # creation d'un module avec sa note
    module1 = Module("Algorithmique", 4)
    module2 = Module("Mathematique", 3)
    note1 = Note(14, module1)
    note2 = Note(12, module2)
    # affichage du module et de la note 
    print(module1)
    print(note1)

    # teste de la classe Student
    # Création d’un étudiant
    etudiant = Student("Tizi-Ouzou", "Dyhia", "dyhia@gmail.com", "0555542355")
    # ajout des notes a la liste des notes de l'etudiant
    etudiant.addNote(note1)
    etudiant.addNote(note2)
    # affichage des informations de l'etudiant crée 
    print(etudiant)
    # affichage de la liste des notes 
    etudiant.displayNotes()