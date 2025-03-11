class Student:
    def __init__(self, name: str, studentID: int, age: int):
        """Constructeur de la classe Student qui initialise un étudiant avec son nom, son ID et son âge."""
        self.__name = name              # Attribut privé (Nom de l'étudiant)
        self.__studentID = studentID    # Attribut privé (ID de l'étudiant)
        self.__age = age                # Attribut privé (Âge de l'étudiant)
        self.__grades = []              # Attribut privé (Liste des notes)

    # Getters (permettent d'accéder aux attributs privés)
    def get_name(self):
        return self.__name

    def get_studentID(self):
        return self.__studentID

    def get_age(self):
        return self.__age

    def get_grades(self):
        return self.__grades

    # Setters (permettent de modifier les attributs privés)
    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        self.__age = age

    def add_grade(self, grade: float):
        """Ajoute une note à la liste des notes."""
        if 0 <= grade <= 20:  # Vérification pour éviter d'ajouter des notes invalides
            self.__grades.append(grade)
        else:
            print("Erreur : la note doit être entre 0 et 20.")

    def get_average_grade(self):
        """Calcule et retourne la moyenne des notes."""
        if len(self.__grades) == 0:
            return 0  # Si aucun note, la moyenne est 0
        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        """Retourne une représentation textuelle de l'étudiant."""
        return f"Étudiant: {self.__name}, ID: {self.__studentID}, Âge: {self.__age}, Moyenne: {self.get_average_grade():.2f}"

# Exemple d'utilisation
student1 = Student("Alice", 101, 20)
student1.add_grade(15)
student1.add_grade(18)
student1.add_grade(12)

print(student1)  # Affiche les infos de l'étudiant avec sa moyenne
