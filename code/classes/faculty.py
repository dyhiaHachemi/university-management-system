from classes.departement import Departement

class Faculty():
    """
    Represente une faculte dans une universite
    Contient plusieurs departements
    A un directeur designé par le directeur de l'universite
    Peut ajouter ou supprimer un departement d'une faculte
    """
    def __init__(self, name, fac_director):
        self.name = name
        self.fac_director = fac_director
        self.list_of_dep = []

    def __str__(self):
        """
        représentation en chaîne de caractères d'un objet
        """
        return (f" - Nom: {self.name} \n Directeur: {self.fac_director.name}")
    
    def add_dep(self,dep : Departement):
        """
        Ajouté un departement à la liste des departements dans la faculte
        """
        if (isinstance(dep, Departement)):
            self.list_of_dep.append(dep)
        else:
            # l'entree n'est pas un departement
            print("Erreur : l'objet doit être une instance de la classe Departement.")

    # affichage de la liste des Departements
    def display_dep(self):
        """
        Affiche les departement dans la faculté
        """
        print(f"- Les Departements de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_dep): 
            print("Aucun departement disponible.")
            return
        else:
            # pour chaque dep de la liste des dep
            for dep in self.list_of_dep :
                print(f" {dep}") # appel de la fct __str__ de la classe Year    
    
    # suppression d'un departement 
    def remove_dep(self,dep : Departement):
        """
        supprime un departement d'une faculte
        """
        self.list_of_dep.remove(dep)