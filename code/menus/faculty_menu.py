from classes.faculty import Faculty
from classes.university import University

def faculty_menu (universite : University):
    print("---------- Systeme de gestion de faculte ----------")
    
    # affichage du menu de gestion de faculte
    while True :
        print("\n === GESTION DE FACULTE ===")
        print("1. Ajouter une faculte")
        print("2. Supprimer une faculte")
        print("3. Afficher une faculte")
        print("4. Lister les facultes")
        print("0. Retour")

        choix = input("Veuillez saisir votre choix (0 - 5) : ")

        match choix :
            case "1" :
                name = input("Le nom de la faculte a ajouter: ")
                faculte = Faculty(name)  # creation d'une faculté
                universite.add_fac(faculte) # ajout de la faculte a la liste des facultes dans universite
                print(f"Faculte '{faculte.name}' ajoutee avec succes.")
            case "2" :
                name = input("Le nom de la faculte a supprimer: ")
                try:
                    # on commence par reccuperer l'objet faculte apartir de son nom
                    faculte = None
                    for fac in universite.list_of_fac :
                        if (fac.name.lower() == name.lower()):
                            faculte = fac # faculte trouvé
                            break
                    # si on n'a pas trouvé de faculte
                    if (faculte is None):
                        print(f"Faculte {name} introuvable!")
                    else: 
                        # suppression de la faculte
                        universite.remove_fac(name)
                        print(f"Faculte '{faculte.name}' supprimee avec succes.")
                except Exception as e:
                    print(f"Erreur {e}")
            case "3":
                # affichage d'une faculte
                name = input("Entrez le nom de la faculte a afficher: ")
                try:
                    # on commence par reccuperer l'objet faculte apartir de son nom
                    faculte = None
                    for fac in universite.list_of_fac :
                        if (fac.name.lower() == name.lower()):
                            faculte = fac # faculte trouvé
                            break
                    # si on n'a pas trouvé de faculte
                    if (faculte is None):
                        print(f"Faculte {name} introuvable!")
                    else: 
                        # affichage de la faculte
                        print(faculte)
                except Exception as e:
                    print(f"Erreur {e}")
            case "4" :
                # affichage de la liste des facultes dans l'universite
                universite.display_fac()
            case "0" :
                print("Retour au menu principal!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")