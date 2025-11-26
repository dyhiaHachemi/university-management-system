from menus.main_menu import main_menu
from classes.university import University

def create_university():
    """
    Cree une universite au demarrage du systeme
    """
    print("Creation d'une nouvelle universite:")
    name = input("Entrez le nom de l'universite: ")
    address = input("Entrez l'addresse de l'universite: ")
    email = input("Entrez l'email de l'universite: ")
    phone_number = input("Entrez le numero de telephone de l'universite: ")
    return University(name, phone_number , email, address)

def main():
    universite = create_university()
    print(f"{universite.name} cree avec succes!")
    main_menu(universite) # appel de la fonction main_menu pour afficher le menu principal de l'application

if __name__ == "__main__":
    main()