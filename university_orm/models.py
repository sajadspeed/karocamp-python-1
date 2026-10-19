from orm import Model, StringField, IntegerField

class Student(Model):
    table_name = "students"

    name = StringField(required=True, min_length=2)
    student_number = StringField(required=True, min_length=4)
    email = StringField(required=False)
    enrollment_year = IntegerField(required=True, min_value=2000)

class Teacher(Model):
    table_name = "teachers"

    name = StringField(required=True, min_length=2)
    email = StringField(required=False)
    department = StringField(required=True)

class Course(Model):
    table_name = "courses"

    name = StringField(required=True, min_length=2)
    code = StringField(required=True, min_length=2)
    unit = IntegerField(required=True, min_value=1)

class ClassEntity(Model):
    table_name = "classes"

class Enrollment(Model):
    table_name = "enrollments"
