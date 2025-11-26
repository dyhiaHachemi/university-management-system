from menus.main_menu import main_menu
from classes.university import University
from classes.univDirector import UnivDirector

def create_university(universite):
    """
    Creer une universite au demarrage du systeme
    """
    print("Creation d'une nouvelle universite:")
    name = input("Entrez le nom de l'universite: ")
    address = input("Entrez l'addresse de l'universite: ")
    email = input("Entrez l'email de l'universite: ")
    phone_number = input("Entrez le numero de telephone de l'universite: ")
    return University(name, phone_number , email, address)

def set_university_director(universite):
    """
    Creer un directeur d'universite au demarrage du systeme 
    apres la creation d'une universite
    """
    print(f"Affectation d'un directeur a {universite.name}")
    name = input("Entrez le nom du directeur: ")
    email = input("Entrez l'email du directeur: ")
    phone_number = input("Entrez le numero de telephone du directeur: ")
    university_director = UnivDirector(name, phone_number, email, universite)
    universite.set_univ_director(university_director)
    return

def main():
    universite = create_university()
    print(f"{universite.name} cree avec succes!")
    # l'universite cree affecte un directeur a l'universite 
    set_university_director(universite)
    #print(f"Le directeur {university_director.name} a ete affecte a {universite.name} avec succes!")
    main_menu(universite) # appel de la fonction main_menu pour afficher le menu principal de l'application

if __name__ == "__main__":
    main()