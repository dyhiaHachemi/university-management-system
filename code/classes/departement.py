from classes.year import Year

class Departement():
    def __init__(self,name,depChief):
        self.name = name
        self.depChief = depChief
        self.listOfYears = []
    
    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Chef de departement: {self.depChief.name}")
    
    # Ajout d'un year a la liste
    def addYear(self,year):
        if (isinstance(year, Year)):
            self.listOfYears.append(year)
        else:
            # l'entree n'est pas un year
            print("Erreur : l'objet doit être une instance de la classe Year.")

    # affichage de la liste des Year
    def displayYears(self):
        print(f"- Les Sections de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.listOfYears): 
            print("Aucune section disponible.")
            return
        else:
            # pour chaque section de la liste des sections
            for year in self.listOfYears :
                print(f" {year}") # appel de la fct __str__ de la classe Year    
    