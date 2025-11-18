# importation de la classe Module pour la liste des modules
from classes.module import Module
# importation de la classe Note pour creation de la liste des etudiantspour chaque section
from classes.student import Student
class Year:
    """
    Represente une section dans un departement
    Possède une liste des etudiants de moyennes et de modules 
    """
    def __init__(self, name):
        self.name = name
        self.list_of_students = []
        self.list_of_modules = []
        self.list_of_marks = []

    def __str__(self):
        """
        représentation en chaîne de caractères d'un objet
        """
        return (f"- Section: {self.name} ")
    
    def add_student(self,student : Student):
        """
        Ajoute un etudiant a un year donné
        """
        # on verifie si l'entree d'utilisateur est bien un objet de la classe Student
        if (isinstance(student,Student)):
            # ajout de l'etudiant' a la liste des etudiants
            self.list_of_students.append(student) 
        else: 
            # l'entree n'est pas un etudiant
            print("Erreur : l'objet doit être une instance de la classe Student.")

    def add_module(self,module : Module):
        """
        Ajoute un module a un year donné
        """
        # on verifie si l'entree d'utilisateur est bien un objet de la classe Student
        if (isinstance(module,Module)):
            # ajout de l'etudiant' a la liste des etudiants
            self.list_of_modules.append(module) 
        else: 
            # l'entree n'est pas un etudiant
            print("Erreur : l'objet doit être une instance de la classe Module.")

    # Liste des moyennes calculées par le chief de departement 
    def add_mark(self,depChief ):
        """
        Ajoute une moyenne a la liste des moyennes d'un year donné
        """
        # appeller la fct calculAvg qui est dans la classe ChiefDepartement
        depChief.calcul_avg(self)

    def remove_student(self,student : Student):
        """
        supprime un etudiant de la liste des etudiant d'un year
        """
        self.list_of_students.remove(student)
    
    def get_avg (self,student : Student):
        """
        reccuperer la moyenne d'un etudiant calculé par le chef de departement
        """
        # chercher la moyenne de l'etudiant dans la liste des moyennes par son nom
        for (stud, avg ) in self.list_of_marks :
            if (stud == student) :
                return avg # reccuperer la moyenne 
        return None
        
    def send_student_to_next_year(self,student :Student, next_year):
        """
        envoyer un etudiant a un niv supperieur s'il a une moyenne superieure ou egale a 10
        """
        # reccuperer la moyenne de l'etudiant
        average = self.get_avg(student)
        # verifier si l'etudiant peut passer au year suivant
        if (average is None) : 
           # si aucune moyenne n'est retrouvée
           print("Impossible de passer au next year: la moyenne de l'etudiant n'est pas calculé")
           return 
        elif (average < 10):
            average = round(average, 2)
            print(f"Impossible de passer au year suivant: L'etudiant n'a pas de moyenne minimale (moyenne = {average})")
            return
        else:
            # supprimer l'etudiant de la liste des etudiant du year actuel
            if (student in self.list_of_students):
                self.remove_student(student)
            # ajouter l"etudiant aà la liste des etudiants du next year
            next_year.add_student(student)
            print(f"{student.name} est passe de {self.name} a {next_year.name}")
    
    def display_students(self):
        """
        affiche la liste des etudiants
        """
        print(f"La liste des etudiants de la section {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_students): 
            print("Aucun etudiant disponible.")
            return
        else:
            # pour chaque etudiant de la liste des etudiants
            for student in self.list_of_students :
                print(f"{student} \n") # appel de la fct __str__ de la classe Student
    
    def display_modules(self):
        """
        affichage de la liste des modules
        """
        print(f"La liste des modules de la section {self.name}:")
        # verifier si la liste n'est pas vide
        if (not self.list_of_modules): 
            print("Aucun module disponible.")
            return
        else:
            # pour chaque etudiant de la liste des etudiants
            for module in self.list_of_modules :
                print(f"- {module}") # appel de la fct __str__ de la classe Student

    def display_marks(self):
        """
        affichage de la liste des moyennes
        """
        print(f"Les moyennes des etudiants de la section {self.name} :")
        # vérifier si la liste est vide
        if (not self.list_of_marks):
            print("Aucune moyenne calculee pour le moment.")
            return
        # afficher toutes les moyennes
        for (student, avg) in self.list_of_marks:
            print(f" - {student.name} : {avg:.2f}")    
