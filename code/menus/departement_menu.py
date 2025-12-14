from classes.university import University
from classes.univDirector import UnivDirector
from classes.faculty import Faculty

def departement_menu (universite : University):
    print("\n ---------- Systeme de gestion des departements ----------")
    
    # affichage du menu de gestion de faculte
    while True :
        print("\n === GESTION DE DEDARTEMENT ===")
        print("1. Ajouter un departement")
        print("2. Supprimer un departement")
        print("3. Afficher un departement")
        print("4. Afficher le chef du departement")
        print("5. Lister les departements")
        print("0. Retour")

        choix = input("Veuillez saisir votre choix (0 - 5) : ").strip()
        
        match choix :
            case "1" :
                print("\nAjout d'un departement a la faculte:")
                nameDep = input("Le nom du departement a ajouter: ").strip()
                departement = Departement(nameDep)  # creation d'un departement 
                Faculty.add_dep(departement) # ajout du departement a la liste des departements de la faculte
                print(f"Departement '{departement.name}' ajoute avec succes.")
            case "2":
                print("\nSuppression d'un departement: ")
                name = input("Le nom du departement a supprimer: ").strip()
                # on commence par reccuperer l'objet departement apartir de son nom
                departement = None
                for dep in departement.list_of_dep :
                    if (dep.name.lower() == name.lower()):
                        departement = dep # departement trouvé
                        break
                # si on n'a pas trouvé de departement
                if (departement is None):
                    print(f"Departement {name} introuvable!")
                else: 
                    try:
                        # suppression du departement
                        Faculty.remove_fac(departement)
                        print(f"Departement '{departement.name}' supprime avec succes.")
                    except Exception as e:
                        print(f"Erreur {e}")
            case "3":
                print("\nAffichage d'un departement:")
                # affichage d'un departement
                name = input("Entrez le nom du departement a afficher: ").strip()
                # on commence par reccuperer l'objet departement apartir de son nom
                departement = None
                for dep in Faculty.list_of_dep :
                    if (dep.name.lower() == name.lower()):
                        departement = dep # departement trouvé                            
                        break
                # si on n'a pas trouvé de departement
                if (departement is None):
                    print(f"Departement {name} introuvable!")
                else: 
                    # affichage de la faculte                        
                    print(departement)
            case "5":
                # affichage de la liste des departement dans la faculte
                Faculty.display_fac()
            case "0" :
                print("Retour au menu principal!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")