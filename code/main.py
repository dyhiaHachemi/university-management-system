# importation des differentes classes
from classes.module import Module
from classes.note import Note
from classes.student import Student
from classes.year import Year
from classes.depChief import DepChief
from classes.departement import Departement
from classes.faculty import Faculty
from classes.facDirector import FacDir
from classes.univDirector import UnivDirector
from classes.university import University

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
    etudiant1.add_note(note1)
    etudiant1.add_note(note2)
    etudiant2.add_note(Note(14,module1))
    etudiant2.add_note(Note(16,module2))
    etudiant3.add_note(Note(10,module1))
    etudiant3.add_note(Note(12,module2))
    etudiant4.add_note(Note(6,module1))
    etudiant4.add_note(Note(1,module2))

    # affichage des informations de etudiants crées
    print("Liste des etudiants:")
    print(etudiant1)
    print(etudiant2)
    print(etudiant3)
    print(etudiant4)
    print("--------------------")

    # affichage de la liste des notes 
    print("Liste des notes:")
    etudiant1.display_notes()
    etudiant2.display_notes()
    etudiant3.display_notes()
    etudiant4.display_notes()
    print("--------------------")

    # teste de la classe Year
    # Creation des sections
    l1 = Year("L1 Informatique")
    l2 = Year("L2 Informatique")
    l3 = Year("L3 Informatique")
    m1 = Year("M1 Reseaux")
    m2 = Year("M2 Reseaux")
    
    # ajout des etudiants et modules aux differentes sections
    l1.add_module(module1)
    l1.add_module(module2)
    l1.add_student(etudiant1)
    l1.add_student(etudiant2)
    l2.add_student(etudiant3)
    l2.add_student(etudiant4)

    # afficher liste des etudiants de chaque section
    print("Liste des etudiants de chaque section:")
    l1.display_students()
    print("--------------------")
    l2.display_students()
    print("--------------------")
    l3.display_students()
    print("--------------------")

    # supprimer un etudiant 
    print("Suppression de l'etudiant: ",etudiant1.name ) 
    l1.remove_student(etudiant1)
    print("--------------------")
    # afficher la liste des etudiants de la section apres suppression
    l1.display_students()
    print("--------------------")

    # teste de la classe DepChief
    # creation d'un Chef de département
    chef_dep_info = DepChief("Dr. Karim","0765432345", "karim@univ.dz")
    chef_dep_rsx = DepChief("Dr. Zinedine","0706732345", "zinedine@univ.dz")
    chef_dep = DepChief("Dr. El'hocine","0706732116", "elhocine@univ.dz")
    chef_dep_math = DepChief("Dr. Lylia","0706732234", "lylia@univ.dz")
    # affichage de information du chef de departement
    print("Chef de departement: ")
    print(chef_dep_info)
    print("--------------------")

    # remplissage de la liste des moyennes 
    chef_dep_info.calcul_avg(l1)
    chef_dep_info.calcul_avg(l2)
    chef_dep_info.calcul_avg(l3)
    # affichage des listes moyennes calculées
    print("liste des moyennes de chaque section:")
    l1.display_marks()
    print("--------------------")
    l2.display_marks()
    print("--------------------")
    l3.display_marks()
    print("--------------------")
 
    # passer un etudiant au next year
    l2.send_student_to_next_year(etudiant4, l3)
    print("--------------------")
    # affichage de la liste des etudiants apres pasasge d'un etudiant au next year
    l2.display_students()
    l3.display_students()
    print("--------------------")

    # teste de la classe Departement
    # creation d'un departement
    dep_info = Departement("Departement d'informatique" , chef_dep_info)
    dep_rsx = Departement("Departement de reseaux" , chef_dep_rsx)
    dep_math = Departement("Departement de Mathematique" , chef_dep_math)
    # affichage du departement
    print(dep_info)
    print(dep_rsx)
    print(dep_math)
    print("--------------------")

    # ajout des sections a leur departement
    dep_info.add_year(l1)
    dep_info.add_year(l2)
    dep_info.add_year(l3)
    dep_rsx.add_year(m1)
    dep_rsx.add_year(m2)
    # affichage de a liste des sections par departement
    dep_info.display_years()
    dep_rsx.display_years()
    print("--------------------")

    # teste de la classe FacDir
    # creation d'un directeur de fac
    dir_fgei = FacDir("Dr. Thanina", "0706712445","thanina@univ.dz",None) # a l'initialisation le directeur n'est pas affecté a une faculte
    dir_fs = FacDir("Dr. Lyna", "0767812445","lyna@univ.dz",None)
    #affichage du directeur de la fac
    print(dir_fgei)
    print(dir_fs)
    print("--------------------")
    
    # teste de la classe Faculty
    # creation de faculty
    fgei = Faculty("Faculty de genie electrique et d'informatique",dir_fgei)
    fs = Faculty("Faculty des sciences",dir_fs)
    print(fgei)
    print("--------------------")
    # lier la faculte a un directeur
    print("Lier la faculte au directeur:")
    dir_fgei.faculty = fgei
    dir_fs.faculty = fs
    # affichage du directeur de la fac
    print(dir_fgei)
    print(dir_fs)
    print("--------------------")
    # ajouter les departements a la liste des dep
    fgei.add_dep(dep_info)
    fgei.add_dep(dep_rsx)
    fs.add_dep(dep_math)
    # afficher la liste des dep
    fgei.display_dep()
    fs.display_dep()
    print("--------------------")
    # suppression d'un dep
    print("Suppression d'un departement")
    fgei.remove_dep(dep_rsx)
    fgei.display_dep()
    print("--------------------")
    # set un chief au departement
    print("Modifier le chef de departement")
    dir_fgei.set_dep_chief(chef_dep,dep_info.name)
    # affichage des resultats apres modification du chef de departement
    print(dep_info)
    print("--------------------")

    # teste de la classe universite 
    # création université
    ummto = University("Universite Mouloud Mammeri", "026123456", "contact@ummto.dz", "Tizi-Ouzou")
    usthb = University("Universite Houari Boumediene", "026127896", "contact@usthb.dz", "Alger")
    # affichage des universites crees 
    print(ummto)
    print(usthb)
    # affichage de la liste des faculte
    ummto.add_fac(fgei)
    ummto.add_fac(fs)
    ummto.display_fac()
    # création directeur
    ummto_director = UnivDirector("Pr. Salah", "salah@ummto.dz", "0555000011",ummto)
    usthb_director = UnivDirector("Pr. Farida", "farida@usthb.dz", "0555345611",usthb)
    # affichage des directeurs des universite 
    print(ummto_director)
    print(usthb_director)
    # assignation
    print('assignation de directeur aux universite')
    ummto.set_univ_director(ummto_director)
    usthb.set_univ_director(usthb_director)
    print(ummto)
    print(usthb)
    print("--------------------")
    # supprimer une faculte
    print("Suppression d'une faculte:")
    ummto.remove_fac(fs)
    ummto.display_fac()
    print("--------------------")
    # set un chief au departement
    print("Modifier le chef de departement:")
    ummto_director.set_dep_chief(chef_dep_info,dep_info.name,fgei.name)
    # affichage des resultats apres modification du chef de departement
    print(dep_info)
    print("--------------------")
    # set un directeur de faculte
    print("Modifier le directeur de faculte:")
    ummto_director.set_fac_director(dir_fs,fgei.name)
    # affichage des resultats apres modification du directeur de faculte
    print(fgei)
    print("--------------------")
    
    
