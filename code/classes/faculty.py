from classes.departement import Departement

class Faculty():
    def __init__(self, name, fac_director):
        self.name = name
        self.fac_director = fac_director
        self.list_of_dep = []

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Directeur: {self.fac_director.name}")
    
    # Ajout d'un departement a la liste
    def add_dep(self,dep : Departement):
        if (isinstance(dep, Departement)):
            self.list_of_dep.append(dep)
        else:
            # l'entree n'est pas un departement
            print("Erreur : l'objet doit être une instance de la classe Departement.")

    # affichage de la liste des Departements
    def display_dep(self):
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
        self.list_of_dep.remove(dep)