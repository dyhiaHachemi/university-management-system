from menus.main_menu import main_menu
from classes.university import University

def create_university():
    """
    Cree une universite au demarrage du systeme
    """
    print("\n Creation d'une nouvelle universite:")
    name = input("Entrez le nom de l'universite: ")
    address = input("Entrez l'addresse de l'universite: ")
    email = input("Entrez l'email de l'universite: ")
    phone_number = input("Entrez le numero de telephone de l'universite: ")
    return University(name, phone_number , email, address)

def main():
    print("---------- Systeme de gestion d'universite ----------")
    while True :
        print("\n === MENU D'ACCEUIL ===")
        print("1. Creer une nouvelle université")
        print("0. Quitter")
        choix = input("Entrez votre choix (0/1):")
        match choix:
            case "1":
                universite = create_university()
                print(f"Universite {universite.name} cree avec succes!")
                main_menu(universite) # appel de la fonction main_menu pour afficher le menu principal de l'application
            case "0":
                print("Au revoir!")
                break
            case _ :
                print("Choix invalid! Veuillez reessayer") 

if __name__ == "__main__":
    main()