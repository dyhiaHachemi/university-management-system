# importation des differentes classes
from classes.module import Module
from classes.note import Note

if __name__ == "__main__":

    # teste des classes Module et Note
    # creation d'un module avec sa note
    module1 = Module("Algorithmique", 4)
    note1 = Note(14, module1)
    # affichage du module et de la note 
    print(module1)
    print(note1)

