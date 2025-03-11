# Student Management System API

# Description
Ce projet est une API REST développée en Python avec Flask pour la gestion des étudiants, des cours et des inscriptions.

# Fonctionnalités
- Ajouter un étudiant
- Ajouter un cours
- Inscrire un étudiant à un cours
- Lister les étudiants, les cours et les inscriptions

# Technologies utilisées
- Python 3
- Flask

# Installation
Prérequis
- Python 3.x installé
- `pip` installé

# Étapes d'installation
1. Cloner le projet :
   ```bash
   git clone https://github.com/votre-repo/student-management.git
   cd student-management
   ```
2. Installer les dépendances :
   ```bash
   pip install flask
   ```
3. Lancer l'API :
   ```bash
   python app.py
   ```
4. L'API est accessible à : `http://127.0.0.1:5000`

 # Routes de l'API

| Méthode | Route | Description |
|---------|------|-------------|
| **POST** | `/students` | Ajouter un étudiant |
| **POST** | `/courses` | Ajouter un cours |
| **POST** | `/enrollments` | Inscrire un étudiant à un cours |
| **GET** | `/students` | Lister les étudiants |
| **GET** | `/courses` | Lister les cours |
| **GET** | `/enrollments` | Lister les inscriptions |

 # Exemples d'utilisation

 1. Ajouter un étudiant
bash
curl -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d '{"studentID": "1", "name": "Alice", "age": 20}'


2. Ajouter un cours
bash
curl -X POST http://127.0.0.1:5000/courses -H "Content-Type: application/json" -d '{"courseCode": "MATH101", "courseName": "Mathématiques", "creditHours": 3}'


3. Inscrire un étudiant à un cours
bash
curl -X POST http://127.0.0.1:5000/enrollments -H "Content-Type: application/json" -d '{"studentID": "1", "courseCode": "MATH101"}'



