from classes.departement import Departement

class Faculty():
    def __init__(self, name, facDirector):
        self.name = name
        self.facDirector = facDirector
        self.listOfDep = []

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Directeur: {self.facDirector.name}")
    
    # Ajout d'un departement a la liste
    def addDep(self,dep):
        if (isinstance(dep, Departement)):
            self.listOfDep.append(dep)
        else:
            # l'entree n'est pas un departement
            print("Erreur : l'objet doit être une instance de la classe Departement.")

    # affichage de la liste des Departements
    def displayDep(self):
        print(f"- Les Departements de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.listOfDep): 
            print("Aucun departement disponible.")
            return
        else:
            # pour chaque dep de la liste des dep
            for dep in self.listOfDep :
                print(f" {dep}") # appel de la fct __str__ de la classe Year    
    
    # suppression d'un departement 
    def removeDep(self,dep):
        self.listOfDep.remove(dep)