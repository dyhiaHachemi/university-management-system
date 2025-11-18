from classes.year import Year

class Departement():
    """
    Represente un departement dans une faculte
    A un chef de departement designé par le directeur de la faculte
    Possède differentes sections (years)
    """
    def __init__(self,name,depChief):
        self.name = name
        self.dep_chief = depChief
        self.list_of_years = []
    
    def __str__(self):
        """
        représentation en chaîne de caractères d'un objet
        """
        return (f" - Nom: {self.name} \n Chef de departement: {self.dep_chief.name}")
    
    def add_year(self,year : Year):
        """
        Ajouter une section a la liste des section d'un departement
        """
        if (isinstance(year, Year)):
            self.list_of_years.append(year)
        else:
            # l'entree n'est pas un year
            print("Erreur : l'objet doit être une instance de la classe Year.")

    def display_years(self):
        """
        Afficher la liste des sections dans un departement
        """
        print(f"- Les Sections de {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_years): 
            print("Aucune section disponible.")
            return
        else:
            # pour chaque section de la liste des sections
            for year in self.list_of_years :
                print(f" {year}") # appel de la fct __str__ de la classe Year    
    