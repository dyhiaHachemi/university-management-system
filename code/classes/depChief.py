"""
classe DepChief calcul la moyenne des etudiants
"""
from classes.person import Person
class DepChief(Person):
    def __init__(self, name, email, phoneNumber):
        # initialiser les attributs de la classe parente Person
        super().__init__(name, email, phoneNumber)

    # représentation en chaîne de caractères d'un objet
    def __str__(self):
        return (f" - Nom du Chef de Departement: {self.name} \n Email: {self.email} \n Numero de Telephone: {self.phoneNumber}")
    
    # fonction pour le calcul etle remplissage de la liste des moyennes
    def calculAvg(self,year):
        year.listOfMarks = [] # vides la liste des moyennes avant de recaluler pour chaque year
        # on calcul la moyenne pour chaque etudiant d'un year
        for student in year.listOfStudents :
            total = 0 # la somme des notes * coef
            totalCoef = 0 # la somme des coef pour chaque etudiant
            # parcourir la liste des notes de chaque etudiant pour le calcul de la moyenne
            for note in student.notes :
                total += note.value * note.module.coef
                totalCoef += note.module.coef
            # calcul de la moyenne 
            if (totalCoef > 0) :
                average = total / totalCoef
            else:
                average = 0
            # remplir la liste des moyenne de year par l'objet student pas seulement son nom
            year.listOfMarks.append((student, average))

