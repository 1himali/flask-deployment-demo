from flask import Flask, render_template

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Himali Suresh",
        "course": "BCA",
        "semester": 5,
        "email": "himali@example.com",
        "subjects": ["Python", "Web Development", "Database Management"]
    },
    {
        "id": 2,
        "name": "Ananya Sharma",
        "course": "BCA",
        "semester": 5,
        "email": "ananya@example.com",
        "subjects": ["Python", "Computer Networks", "Java"]
    },
    {
        "id": 3,
        "name": "Rahul Menon",
        "course": "BCA",
        "semester": 5,
        "email": "rahul@example.com",
        "subjects": ["Java", "Database Management", "Web Development"]
    }
]

subjects = [
    {"code": "BCA501", "name": "Python Programming", "credits": 4},
    {"code": "BCA502", "name": "Web Development", "credits": 4},
    {"code": "BCA503", "name": "Database Management", "credits": 4},
    {"code": "BCA504", "name": "Computer Networks", "credits": 3},
    {"code": "BCA505", "name": "Java Programming", "credits": 4}
]


@app.route("/")
def home():
    return render_template("home.html", students=students, subjects=subjects)


@app.route("/students")
def student_list():
    return render_template("students.html", students=students)


@app.route("/student/<int:student_id>")
def student_details(student_id):
    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        return "Student not found", 404

    return render_template("student.html", student=student)


@app.route("/subjects")
def subject_list():
    return render_template("subjects.html", subjects=subjects)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)