from classes.faculty import Faculty
from classes.university import University
from classes.depChief import DepChief

def faculty_menu (universite : University):
    print("---------- Systeme de gestion des facultes ----------")
    
    # affichage du menu de gestion de faculte
    while True :
        print("\n === GESTION DE FACULTE ===")
        print("1. Ajouter une faculte")
        print("2. Supprimer une faculte")
        print("3. Afficher une faculte")
        print("4. Lister les facultes")
        print("5. Definir un chef de departement (par le directeur de faculte)")
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
            case "5":
                # definir un chef de departement a un departement de la faculte
                fac_name = input("Entrez le nom de la faculte: ")
                try:
                    # on commence par reccuperer l'objet faculte apartir de son nom
                    faculte = None
                    for fac in universite.list_of_fac :
                        if (fac.name.lower() == fac_name.lower()):
                            faculte = fac # faculte trouvé
                            break
                    # si on n'a pas trouvé de faculte
                    if (faculte is None):
                        print(f"Faculte {name} introuvable!")
                        break
                    else: 
                        # on verifie qu'il existe un directeur pour cette faculte
                        fac_director = getattr(faculte.fac_director)
                        if (fac_director is None):
                            print(f"la faculte {faculte.name} n'a pas de directeur! seul le directeur peut definir un chef de departement.")
                            break
                        else: 
                            dep_name = input ("Entrez le nom du departement: ")
                            # creation d'un chef de departement
                            chief_name = ("Entrez le nom du chef de departement: ")
                            chief_phone_number = ("Entrez le numero de telephone du chef de departement: ")
                            chief_email = ("Entrez l'email du chef de departement: ")
                            dep_chief = DepChief(chief_name,chief_email,chief_phone_number)
                            # definir un chef de departement
                            fac_director.set_dep_chief(dep_chief, dep_name)
                            print(f"Chef du departement {dep_name} definit a '{chief_name}")
                except Exception as e:
                    print(f"Erreur {e}")
                
            case "0" :
                print("Retour au menu principal!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")