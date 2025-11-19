from classes.university import University
def main_menu():

    print("---------- Systeme de gestion d'université ----------")
    
    # creation d'une université au démarage
    university = University("Universite Mouloud Mammeri", "026123456", "contact@ummto.dz", "Tizi-Ouzou")
       
    # affichage du menu principal
    while True :
        print("\ === MENU PRINCIPAL ===")
        print("1. Gestion des facultés")
        print("2. Gestion des départements")
        print("3. Gestion des sections")
        print("4. Gestion des étudiants")
        print("5. Affichage de l'université")
        print("0. Quitter")

        

        