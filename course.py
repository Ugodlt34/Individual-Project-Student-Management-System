class Course:
    def __init__(self, courseName: str, courseCode: str, creditHours: int):
        """Constructeur de la classe Course qui initialise un cours avec un nom, un code et un nombre d'heures de crédit."""
        self.__courseName = courseName       # Attribut privé (Nom du cours)
        self.__courseCode = courseCode       # Attribut privé (Code unique du cours)
        self.__creditHours = creditHours     # Attribut privé (Nombre d'heures de crédit)
        self.__students = []                 # Attribut privé (Liste des étudiants inscrits)

    # Getters
    def get_courseName(self):
        return self.__courseName

    def get_courseCode(self):
        return self.__courseCode

    def get_creditHours(self):
        return self.__creditHours

    def get_students(self):
        return self.__students

    # Setters (permettent de modifier certains attributs)
    def set_courseName(self, courseName: str):
        self.__courseName = courseName

    def set_creditHours(self, creditHours: int):
        self.__creditHours = creditHours

    def enrollStudent(self, student):
        """Ajoute un étudiant à la liste des inscrits au cours."""
        if student not in self.__students:  # Vérifie si l'étudiant n'est pas déjà inscrit
            self.__students.append(student)
        else:
            print(f"{student.get_name()} est déjà inscrit à ce cours.")

    def getEnrolledStudents(self):
        """Retourne la liste des étudiants inscrits au cours."""
        return [student.get_name() for student in self.__students]

    def __str__(self):
        """Retourne une représentation textuelle du cours."""
        return f"Cours: {self.__courseName}, Code: {self.__courseCode}, Crédit: {self.__creditHours}, Étudiants inscrits: {len(self.__students)}"

# Exemple d'utilisation
if __name__ == "__main__":
    from Student import Student  # Assurez-vous que la classe Student est définie dans un fichier student.py
    
    student1 = Student("Alice", 101, 20)
    student2 = Student("Bob", 102, 22)

    course1 = Course("Mathématiques", "MATH101", 3)
    course1.enrollStudent(student1)
    course1.enrollStudent(student2)

    print(course1)  # Affiche les infos du cours
    print("Étudiants inscrits:", course1.getEnrolledStudents())  # Liste des étudiants inscrits
