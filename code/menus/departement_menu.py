from classes.university import University
from classes.univDirector import UnivDirector

def departement_menu (universite : University, university_director: UnivDirector):
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
                pass