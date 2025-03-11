class Enrollment :
    def __init__(self, student, course):
        """Initialise l'inscription avec un étudiant et un cours."""
        self.__student = student  # Attribut privé
        self.__course = course    # Attribut privé

    def register(self):
        """Ajoute l'étudiant au cours."""
        self.__course.enrollStudent(self.__student)

    def get_student(self):
        """Retourne l'étudiant inscrit."""
        return self.__student

    def get_course(self):
        """Retourne le cours concerné."""
        return self.__course

    def __str__(self):
        """Retourne une description simple de l'inscription."""
        return f"{self.__student.get_name()} est inscrit à {self.__course.get_courseName()}"

# Exemple d'utilisation
if __name__ == "__main__":
    from Student import Student
    from course import Course

    # Création d'un étudiant et d'un cours
    student1 = Student("Alice", 101, 20)
    course1 = Course("Mathématiques", "MATH101", 3)

    # Création de l'inscription et enregistrement
    enrollment1 = Enrollment(student1, course1)
    enrollment1.register()

    # Affichage du résultat
    print(enrollment1)
    print("Étudiants inscrits :", course1.getEnrolledStudents())  # Vérifie l'inscription
