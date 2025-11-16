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
    def addMark(self,depChief):
        # appeller la fct calculAvg qui est dans la classe ChiefDepartement
        depChief.calculAvg(self)

    # supprimer un etudiant de la liste des etudiant d'un year
    def removeStudent(self,student):
        self.listOfStudents.remove(student)
    
    # fonction pour reccuperer la moyenne d'un etudiant 
    def getAvg (self,student):
        # chercher la moyenne de l'etudiant dans la liste des moyennes par son nom
        for (stud, avg ) in self.listOfMarks :
            if (stud == student) :
                return avg # reccuperer la moyenne 
        return None
        
    # fonction pour envoyer un etudiant a un niv supperieur
    def sendStudentToNextYear(self,student, nextYear):
        # reccuperer la moyenne de l'etudiant
        average = self.getAvg(student)
        # verifier si l'etudiant peut passer au year suivant
        if (average is None) : 
           # si aucune moyenne n'est retrouvée
           print("Impossible de passer au next year: la moyenne de l'etudiant n'est pas calculé")
           return 
        elif (average < 10):
            print(f"Impossible de passer au year suivant: L'etudiant n'a pas de moyenne minimale (moyenne = {average})")
            return
        else:
            # supprimer l'etudiant de la liste des etudiant du year actuel
            if (student in self.listOfStudents):
                self.removeStudent(student)
            # ajouter l"etudiant aà la liste des etudiants du next year
            nextYear.addStudent(student)
            print(f"{student.name} est passe de {self.name} a {nextYear.name}")
    
    # affichage de la liste des etudiants
    def displayStudents(self):
        print(f"La liste des etudiants de la section {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.listOfStudents): 
            print("Aucun etudiant disponible.")
            return
        else:
            # pour chaque etudiant de la liste des etudiants
            for student in self.listOfStudents :
                print(f"{student} \n") # appel de la fct __str__ de la classe Student
    
    # affichage de la liste des modules
    def displayModules(self):
        print(f"La liste des modules de la section {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.listOfModules): 
            print("Aucun module disponible.")
            return
        else:
            # pour chaque etudiant de la liste des etudiants
            for module in self.listOfModules :
                print(f"- {module}") # appel de la fct __str__ de la classe Student

    # affichage de la liste des moyennes
    def displayMarks(self):
        print(f"Les moyennes des etudiants de la section {self.name} :")
        # vérifier si la liste est vide
        if (not self.listOfMarks):
            print("Aucune moyenne calculee pour le moment.")
            return
        # afficher toutes les moyennes
        for (student, avg) in self.listOfMarks:
            print(f" - {student.name} : {avg:.2f}")    
