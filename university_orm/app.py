import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from models import Student, Teacher, Course

app = Flask(__name__)
DB_PATH = "university.db"

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

@app.route('/')
def index():
    return render_template('index.html',
                           student_count=len(Student.all()),
                           teacher_count=len(Teacher.all()),
                           course_count=len(Course.all()))

@app.route('/students', methods=['GET', 'POST'])
def students():
    errors = {}
    form_data = {}
    if request.method == 'POST':
        form_data = {
            'name': request.form.get('name'),
            'student_number': request.form.get('student_number'),
            'email': request.form.get('email'),
            'enrollment_year': request.form.get('enrollment_year')
        }

        student = Student(**form_data)
        try:
            student.save()
            return redirect(url_for('students'))
        except ValueError:
            errors = student.errors

    all_students = Student.all()
    return render_template('students.html', students=all_students, errors=errors, form=form_data)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    errors = {}
    form_data = {}
    if request.method == 'POST':
        form_data = {
            'name': request.form.get('name'),
            'code': request.form.get('code'),
            'unit': request.form.get('unit')
        }

        course = Course(**form_data)
        try:
            course.save()
            return redirect(url_for('courses'))
        except ValueError:
            errors = course.errors

    all_courses = Course.all()
    return render_template('courses.html', courses=all_courses, errors=errors, form=form_data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
