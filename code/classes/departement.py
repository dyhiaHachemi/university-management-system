from classes.year import Year

class Departement():
    def __init__(self,name,depChief):
        self.name = name
        self.dep_chief = depChief
        self.list_of_years = []
    
    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom: {self.name} \n Chef de departement: {self.dep_chief.name}")
    
    # Ajout d'un year a la liste
    def add_year(self,year):
        if (isinstance(year, Year)):
            self.list_of_years.append(year)
        else:
            # l'entree n'est pas un year
            print("Erreur : l'objet doit être une instance de la classe Year.")

    # affichage de la liste des Year
    def display_years(self):
        print(f"- Les Sections de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_years): 
            print("Aucune section disponible.")
            return
        else:
            # pour chaque section de la liste des sections
            for year in self.list_of_years :
                print(f" {year}") # appel de la fct __str__ de la classe Year    
    