from classes.university import University
from menus.faculty_menu import faculty_menu

def main_menu():

    print("---------- Systeme de gestion d'universite ----------")
    
    # creation d'une université au démarage
    universite = University("Universite Mouloud Mammeri", "026123456", "contact@ummto.dz", "Tizi-Ouzou")
       
    # affichage du menu principal
    while True :
        print("\n === MENU PRINCIPAL ===")
        print("1. Gestion des facultes")
        print("2. Gestion des departements")
        print("3. Gestion des sections")
        print("4. Gestion des etudiants")
        print("5. Affichage de l'universite")
        print("0. Quitter")

        choix = input("Veuillez saisir votre choix (0 - 5) : ")

        match choix :
            case "1" :
                faculty_menu(universite)
            case "2" :
                departement_menu(universite)
            case "3" :
                year_menu(universite)
            case "4" :
                student_menu(universite)
            case "5" :
                print(universite)
            case "0" :
                print("Au-revoir!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")