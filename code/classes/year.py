# importation de la classe Module pour la liste des modules
from classes.module import Module
# importation de la classe Note pour creation de la liste des etudiantspour chaque section
from classes.student import Student

class Year:
    def __init__(self, name):
        self.name = name
        self.listOfStudents = []
        self.listOfModules = []
        self.listOfMarks = []

    # Liste des etudiants
    def addStudent(self,student):
        # on verifie si l'entree d'utilisateur est bien un objet de la classe Student
        if (isinstance(student,Student)):
            # ajout de l'etudiant' a la liste des etudiants
            self.listOfStudents.append(student) 
        else: 
            # l'entree n'est pas un etudiant
            print("Erreur : l'objet doit être une instance de la classe Student.")

    # Liste des modules
    def addModule(self,module):
        # on verifie si l'entree d'utilisateur est bien un objet de la classe Student
        if (isinstance(module,Module)):
            # ajout de l'etudiant' a la liste des etudiants
            self.listOfModules.append(module) 
        else: 
            # l'entree n'est pas un etudiant
            print("Erreur : l'objet doit être une instance de la classe Module.")

    # Liste des moyennes calculées par le chief de departement 
    def addMark(self,chefDep):
        # appeller la fct calculAvg qui est dans la classe ChiefDepartement
        chefDep.calculAvg(self)