# importation des differentes classes
from classes.module import Module
from classes.note import Note
from classes.student import Student
from classes.year import Year
from classes.depChief import DepChief
from classes.departement import Departement
from classes.faculty import Faculty
from classes.facDirector import FacDir

if __name__ == "__main__":
    
    # teste des classes Module et Note
    # creation d'un module avec sa note
    module1 = Module("Algorithmique", 4)
    module2 = Module("Mathematique", 3)
    note1 = Note(14, module1)
    note2 = Note(12, module2)
    # affichage du module et de la note 
    print("Liste des modules:")
    print(module1)
    print(module2)
    print("--------------------")
    print("Liste des notes:")
    print(note1)
    print(note2)
    print("--------------------")

    # teste de la classe Student
    # Création d’un étudiant
    etudiant1 = Student("Tizi-Ouzou","Dyhia", "dyhia@gmail.com", "0555542355")
    etudiant2 = Student("Tizi-Ouzou","Ali", "ali@mail.com", "0555542786")
    etudiant3 = Student("Tizi-Ouzou","Sara", "sara@mail.com", "0675542355")
    etudiant4 = Student("Tizi-Ouzou","Sabrinel", "sabrinel@mail.com", "0725542359")

    # ajout des notes a la liste des notes 
    etudiant1.addNote(note1)
    etudiant1.addNote(note2)
    etudiant2.addNote(Note(14,module1))
    etudiant2.addNote(Note(16,module2))
    etudiant3.addNote(Note(10,module1))
    etudiant3.addNote(Note(12,module2))
    etudiant4.addNote(Note(6,module1))
    etudiant4.addNote(Note(1,module2))

    # affichage des informations de etudiants crées
    print("Liste des etudiants:")
    print(etudiant1)
    print(etudiant2)
    print(etudiant3)
    print(etudiant4)
    print("--------------------")

    # affichage de la liste des notes 
    print("Liste des notes:")
    etudiant1.displayNotes()
    etudiant2.displayNotes()
    etudiant3.displayNotes()
    etudiant4.displayNotes()
    print("--------------------")

    # teste de la classe Year
    # Creation des sections
    l1 = Year("L1 Informatique")
    l2 = Year("L2 Informatique")
    l3 = Year("L3 Informatique")
    m1 = Year("M1 Reseaux")
    m2 = Year("M2 Reseaux")
    
    # ajout des etudiants et modules aux differentes sections
    l1.addModule(module1)
    l1.addModule(module2)
    l1.addStudent(etudiant1)
    l1.addStudent(etudiant2)
    l2.addStudent(etudiant3)
    l2.addStudent(etudiant4)

    # afficher liste des etudiants de chaque section
    print("Liste des etudiants de chaque section:")
    l1.displayStudents()
    print("--------------------")
    l2.displayStudents()
    print("--------------------")
    l3.displayStudents()
    print("--------------------")

    # supprimer un etudiant 
    print("Suppression de l'etudiant: ",etudiant1.name ) 
    l1.removeStudent(etudiant1)
    print("--------------------")
    # afficher la liste des etudiants de la section apres suppression
    l1.displayStudents()
    print("--------------------")

    # teste de la classe DepChief
    # creation d'un Chef de département
    chefDepInfo = DepChief("Dr. Karim","0765432345", "karim@univ.dz")
    chefDepRsx = DepChief("Dr. Zinedine","0706732345", "zinedine@univ.dz")
    chefDep = DepChief("Dr. El'hocine","0706732116", "elhocine@univ.dz")
    # affichage de information du chef de departement
    print("Chef de departement: ")
    print(chefDepInfo)
    print("--------------------")

    # remplissage de la liste des moyennes 
    chefDepInfo.calculAvg(l1)
    chefDepInfo.calculAvg(l2)
    chefDepInfo.calculAvg(l3)
    # affichage des listes moyennes calculées
    print("liste des moyennes de chaque section:")
    l1.displayMarks()
    print("--------------------")
    l2.displayMarks()
    print("--------------------")
    l3.displayMarks()
    print("--------------------")
 
    # passer un etudiant au next year
    l2.sendStudentToNextYear(etudiant4, l3)
    print("--------------------")
    # affichage de la liste des etudiants apres pasasge d'un etudiant au next year
    l2.displayStudents()
    l3.displayStudents()
    print("--------------------")

    # teste de la classe Departement
    # creation d'un departement
    depInfo = Departement("Departement d'informatique" , chefDepInfo)
    depRsx = Departement("Departement de reseaux" , chefDepRsx)
    # affichage du departement
    print(depInfo)
    print(depRsx)
    print("--------------------")

    # ajout des sections a leur departement
    depInfo.addYear(l1)
    depInfo.addYear(l2)
    depInfo.addYear(l3)
    depRsx.addYear(m1)
    depRsx.addYear(m2)
    # affichage de a liste des sections par departement
    depInfo.displayYears()
    depRsx.displayYears()
    print("--------------------")

    # teste de la classe FacDir
    # creation d'un directeur de fac
    dirFgei = FacDir("Dr. Thanina", "0706712445","thanina@univ.dz",None) # a l'initialisation le directeur n'est pas affecté a une faculte
    #affichage du directeur de la fac
    print(dirFgei)
    print("--------------------")
    
    # teste de la classe Faculty
    # creation de faculty
    fgei = Faculty("Faculty de genie electrique et d'informatique",dirFgei)
    print(fgei)
    print("--------------------")
    # lier la faculte a un directeur
    print("Lier la faculte au directeur:")
    dirFgei.faculty = fgei
    # affichage du directeur de la fac
    print(dirFgei)
    print("--------------------")
    # ajouter les departements a la liste des dep
    fgei.addDep(depInfo)
    fgei.addDep(depRsx)
    # afficher la liste des dep
    fgei.displayDep()
    print("--------------------")
    # suppression d'un dep
    print("Suppression d'un departement")
    fgei.removeDep(depRsx)
    fgei.displayDep()
    print("--------------------")
    # set un chief au departement
    print("Modifier le chef de departement")
    dirFgei.setDepChief(chefDep,depInfo.name)
    # affichage des resultats apres modification du chef de departement
    print(depInfo)
    print("--------------------")

    
    

    

