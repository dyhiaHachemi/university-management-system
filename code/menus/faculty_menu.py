"""
avant de creer une faculte il faut avoir un directeur de faculte
"""

from classes.faculty import Faculty
from classes.university import University
from classes.depChief import DepChief
from classes.facDirector import FacDir

def faculty_menu (universite : University):
    print("\n ---------- Systeme de gestion des facultes ----------")
    
    # affichage du menu de gestion de faculte
    while True :
        print("\n === GESTION DE FACULTE ===")
        print("1. Ajouter une faculte")
        print("2. Supprimer une faculte")
        print("3. Afficher une faculte")
        print("4. Afficher le directeur de la faculte")
        print("5. Lister les facultes")
        print("6. Definir un chef de departement (par le directeur de faculte)")
        print("0. Retour")

        choix = input("Veuillez saisir votre choix (0 - 6) : ").strip()
        
        match choix :
            case "1" :
                print("\n Ajout d'une faculte a l'universite:")
                nameFac = input("Le nom de la faculte a ajouter: ").strip()

                print(f"Affectation d'un directeur a la faculte {nameFac}:")
                nameDir = input("Entrez le nom du directeur: ")
                email = input("Entrez l'email du directeur: ")
                phone_number = input("Entrez le numero de telephone du directeur: ")
                faculty_director = FacDir(nameDir, phone_number, email,None) # le directeur n'a pas de faculte pour l'instant

                faculte = Faculty(nameFac,faculty_director)  # creation d'une faculté 

                # lier la faculte au directeur cree
                faculty_director.faculty = faculte

                universite.add_fac(faculte) # ajout de la faculte a la liste des facultes dans universite
                print(f"Faculte '{faculte.name}' ajoutee avec succes.")
            case "2" :
                print("Suppression d'une faculte: ")
                name = input("Le nom de la faculte a supprimer: ").strip()
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
                    try:
                        # suppression de la faculte
                        universite.remove_fac(faculte)
                        print(f"Faculte '{faculte.name}' supprimee avec succes.")
                    except Exception as e:
                        print(f"Erreur {e}")
            case "3":
                print("Affichage d'une faculte:")
                # affichage d'une faculte
                name = input("Entrez le nom de la faculte a afficher: ").strip()
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
            case "4" :
               pass
            case "5":
                """# definir un chef de departement a un departement de la faculte
                fac_name = input("Entrez le nom de la faculte: ").strip()
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
                    fac_director = getattr(faculte,"fac_director", None)
                    if (fac_director is None):
                        print(f"la faculte {faculte.name} n'a pas de directeur! seul le directeur peut definir un chef de departement.")
                        break
                    else: 
                        dep_name = input ("Entrez le nom du departement: ").strip()
                        # creation d'un chef de departement
                        chief_name = ("Entrez le nom du chef de departement: ").strip()
                        chief_phone_number = ("Entrez le numero de telephone du chef de departement: ").strip()
                        chief_email = ("Entrez l'email du chef de departement: ").strip()
                        try:
                            dep_chief = DepChief(chief_name,chief_email,chief_phone_number)
                        except Exception as e:
                            print(f"Impossible de creer l'objet DepChief {e}")
                        # definir un chef de departement               
                        try:             
                            fac_director.set_dep_chief(dep_chief, dep_name)
                            print(f"Chef du departement {dep_name} definit a '{chief_name}")
                        except Exception as e :
                            print(f"Erreur de la deficnition du chef de departement {e}")
                """
                # affichage de la liste des facultes dans l'universite
                print("\n")
                universite.display_fac()
            case "0" :
                print("Retour au menu principal!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")