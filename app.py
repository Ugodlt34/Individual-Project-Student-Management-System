from flask import Flask, request, jsonify

# je importe les classes depuis les fichiers où elles sont définies
from Student import Student
from course import Course
from Enrollment import Enrollment

app = Flask(__name__)

# je stocke les étudiants et les cours dans des dictionnaires (simulation d'une base de données)
students = {}  
courses = {}   
enrollments = []  

# Ajouter un étudiant
@app.route("/students", methods=["POST"])
def create_student():
    data = request.json
    student_id = data["studentID"]

    if student_id in students:
        return jsonify({"error": "L'étudiant existe déjà"}), 400

    student = Student(data["name"], student_id, data["age"])
    students[student_id] = student
    return jsonify({"message": "Étudiant ajouté avec succès"}), 201


# Ajouter un cours
@app.route("/courses", methods=["POST"])
def create_course():
    data = request.json
    course_code = data["courseCode"]

    if course_code in courses:
        return jsonify({"error": "Le cours existe déjà"}), 400

    course = Course(data["courseName"], course_code, data["creditHours"])
    courses[course_code] = course
    return jsonify({"message": "Cours ajouté avec succès"}), 201


# Inscrire un étudiant à un cours
@app.route("/enrollments", methods=["POST"])
def enroll_student():
    data = request.json
    student_id = data["studentID"]
    course_code = data["courseCode"]

    if student_id not in students or course_code not in courses:
        return jsonify({"error": "Étudiant ou cours non trouvé"}), 404

    student = students[student_id]
    course = courses[course_code]

    enrollment = Enrollment(student, course)
    enrollment.register()
    enrollments.append(enrollment)

    return jsonify({"message": f"{student.get_name()} inscrit à {course.get_courseName()}"}), 201


# Récupérer les infos d’un étudiant
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Étudiant non trouvé"}), 404

    return jsonify({
        "name": student.get_name(),
        "studentID": student.get_studentID(),
        "age": student.get_age(),
        "grades": student.get_grades(),
        "averageGrade": student.getAverageGrade()
    })


# Récupérer les infos d’un cours et la liste des étudiants inscrits
@app.route("/courses/<course_code>", methods=["GET"])
def get_course(course_code):
    course = courses.get(course_code)
    if not course:
        return jsonify({"error": "Cours non trouvé"}), 404

    return jsonify({
        "courseName": course.get_courseName(),
        "courseCode": course.get_courseCode(),
        "creditHours": course.get_creditHours(),
        "studentsEnrolled": course.getEnrolledStudents()
    })


# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
