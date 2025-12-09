"""
avant de creer une faculte il faut avoir un directeur de faculte
"""

from classes.faculty import Faculty
from classes.university import University
from classes.depChief import DepChief
from classes.facDirector import FacDir
from classes.univDirector import UnivDirector

def faculty_menu (universite : University, university_director: UnivDirector):
    print("\n ---------- Systeme de gestion des facultes ----------")
    
    # affichage du menu de gestion de faculte
    while True :
        print("\n === GESTION DE FACULTE ===")
        print("1. Ajouter une faculte")
        print("2. Supprimer une faculte")
        print("3. Afficher une faculte")
        print("4. Afficher le directeur de la faculte")
        print("5. Lister les facultes")
        print("6. Definir un directeur de faculte (par le directeur de l'universite)")
        print("7. Definir un chef de departement (par le directeur de faculte)")
        print("0. Retour")

        choix = input("Veuillez saisir votre choix (0 - 7) : ").strip()
        
        match choix :
            case "1" :
                print("\nAjout d'une faculte a l'universite:")
                nameFac = input("Le nom de la faculte a ajouter: ").strip()
                faculte = Faculty(nameFac)  # creation d'une faculté 
                universite.add_fac(faculte) # ajout de la faculte a la liste des facultes dans universite
                print(f"Faculte '{faculte.name}' ajoutee avec succes.")
            case "2" :
                print("\nSuppression d'une faculte: ")
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
                print("\nAffichage d'une faculte:")
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
                print("\nAffichage du directeur de la faculte:")
                name = input("Entrez le nom de la faculte: ").strip()
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
                    # affichage du directeur de la faculte      
                    fac_director = getattr(faculte, "fac_director", None)
                    if fac_director is None:
                        print(f"La faculte {faculte.name} n'a pas de directeur. ")
                    else:
                        print(f"\nDirecteru de la faculte {faculte.name}:")
                        print(fac_director)
            case "5":
                # affichage de la liste des facultes dans l'universite
                universite.display_fac()
            case "6":
                print("\nDefinir un directeur de faculte par le directeur de l'universite:")

                # verifier d'abord si la faculte n'a pas de directeur
                fac_name = input("Entrez le nom de la faculte: ").strip()
                # on commence par reccuperer l'objet faculte apartir de son nom
                faculte = None
                for fac in universite.list_of_fac :
                    if (fac.name.lower() == fac_name.lower()):
                        faculte = fac # faculte trouvé                            
                        break
                # si on n'a pas trouvé de faculte
                if (faculte is None):
                    print(f"Faculte {fac_name} introuvable!")
                else: 
                    # on verifie qu'il n'existe pas de directeur pour cette faculte
                    fac_director = getattr(faculte,"fac_director", None)
                    if (fac_director is None):
                        # creation d'un directeur et affectation 
                        name_dir = input("Entrez le nom du directeur: ")
                        email_dir = input("Entrez l'email du directeur: ")
                        phone_number_dir = input("Entrez le numero de telephone du directeur: ")
                        faculty_director = FacDir(name_dir, phone_number_dir, email_dir,None)  # à la creation le directeur n'est pas affecté a une faculte
                        print(f"Affectation d'un directeur a la faculte {fac_name}:")
                        # le directeur de l'universite affecte le directeur a la faculte
                        university_director.set_fac_director(faculty_director,fac_name)
                    else:
                        print(f"la faculte {faculte.name} a deja un directeur!")
               
            case "7" :
                print("\nDefinir un chef de departement par le directeur de la faculte:")
                # definir un chef de departement a un departement de la faculte par le directeru de la faculte
                fac_name = input("Entrez le nom de la faculte: ").strip()
                # on commence par reccuperer l'objet faculte apartir de son nom
                faculte = None
                for fac in universite.list_of_fac :
                    if (fac.name.lower() == fac_name.lower()):
                        faculte = fac # faculte trouvé                            
                        break
                # si on n'a pas trouvé de faculte
                if (faculte is None):
                    print(f"Faculte {fac_name} introuvable!")
                    break
                else: 
                    # on verifie qu'il existe un directeur pour cette faculte
                    fac_director = getattr(faculte,"fac_director", None)
                    if (fac_director is None):
                        print(f"la faculte {faculte.name} n'a pas de directeur! seul le directeur peut definir un chef de departement.")
                        break
                    else: 
                        # la faculte a un directeur
                        dep_name = input ("Entrez le nom du departement: ").strip()
                        # creation d'un chef de departement
                        print(f"Affectation d'un chef au departement {dep_name}:")
                        chief_name = input("Entrez le nom du chef de departement: ").strip()
                        chief_phone_number = input("Entrez le numero de telephone du chef de departement: ").strip()
                        chief_email = input("Entrez l'email du chef de departement: ").strip()
                        try:
                            dep_chief = DepChief(chief_name,chief_email,chief_phone_number)
                            print("1111")
                        except Exception as e:
                            print(f"Impossible de creer l'objet DepChief {e}")

                        # set departement chief par le directeur de faculte              
                        try:             
                            print("2222")
                            fac_director.set_dep_chief(dep_chief, dep_name)
                            print("33333")
                        except Exception as e :
                            print("44444")
                            print(f"Erreur de la definition du chef de departement {e}")   
            case "0" :
                print("Retour au menu principal!")
                break
            case _ :
                print("Choix invalid! veuillez reessayer")