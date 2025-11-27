from classes.university import University
from classes.univDirector import UnivDirector
from menus.faculty_menu import faculty_menu

def main_menu(universite : University, university_director: UnivDirector):
    # affichage du menu principal
    while True :
        print("\n === MENU PRINCIPAL ===")
        print("1. Gestion des facultes")
        print("2. Gestion des departements")
        print("3. Gestion des sections")
        print("4. Gestion des etudiants")
        print("5. Affichage de l'universite et son directeur")
        print("0. Quitter")

        choix = input("Veuillez saisir votre choix (0 - 5) : ").strip()
        
        match choix :
            case "1" :
                faculty_menu(universite, university_director)
                pass
            case "2" :
                #departement_menu(universite)
                pass
            case "3" :
                #year_menu(universite)
                pass
            case "4" :
                #student_menu(universite)
                pass
            case "5" :
                print("\n Affichage de l'universite:")
                print(universite)
                print("\n Affichage du directeur de l'universite")
                print(university_director)
                pass
            case "0" :
                print("Au-revoir!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")