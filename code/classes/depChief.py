from classes.person import Person

class DepChief(Person):
    """
    Represente une personne qui est chef de departement 
    Calcul les moyennes des etudiants de chaque year
    Mets les moyennes des etudiants dans des listes 
    """
    def __init__(self, name, email, phone_number):
        # initialiser les attributs de la classe parente Person
        super().__init__(name, email, phone_number)

    def __str__(self):
        """
        représentation en chaîne de caractères d'un objet
        """
        return (f" - Nom: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phone_number}")
    
    def calcul_avg(self,year):
        """
        Calculer les moyennes des etudiants dans chaque year
        enregister les moyenens dans des listes qu'on trouve dans la classe Year
        """
        year.list_of_marks = [] # vider la liste des moyennes avant de recaluler pour chaque year
        # on calcul la moyenne pour chaque etudiant d'un year
        for student in year.list_of_students :
            total = 0 # la somme des notes * coef
            total_coef = 0 # la somme des coef pour chaque etudiant
            # parcourir la liste des notes de chaque etudiant pour le calcul de la moyenne
            for note in student.notes :
                total += note.value * note.module.coef
                total_coef += note.module.coef
            # calcul de la moyenne 
            if (total_coef > 0) :
                average = total / total_coef
            else:
                average = 0
            # remplir la liste des moyenne de year par l'objet student pas seulement son nom
            year.list_of_marks.append((student, average))

