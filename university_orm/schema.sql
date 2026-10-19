CREATE TABLE students (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 student_number TEXT NOT NULL UNIQUE,
 email TEXT UNIQUE,
 enrollment_year INTEGER NOT NULL
);

CREATE TABLE teachers (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 email TEXT UNIQUE,
 department TEXT NOT NULL
);

CREATE TABLE classes (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 course_id INTEGER NOT NULL,
 teacher_id INTEGER NOT NULL,
 term TEXT NOT NULL,
 capacity INTEGER NOT NULL,
 classroom TEXT NOT NULL,
 schedule TEXT NOT NULL,
 FOREIGN KEY(course_id) REFERENCES courses(id),
 FOREIGN KEY(teacher_id) REFERENCES teachers(id)
);

CREATE TABLE courses (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 code TEXT NOT NULL UNIQUE,
 unit INTEGER NOT NULL
);

CREATE TABLE enrollments (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 student_id INTEGER NOT NULL,
 class_id INTEGER NOT NULL,
 enrolled_at TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'active',
 final_grade REAL,
 FOREIGN KEY(student_id) REFERENCES students(id),
 FOREIGN KEY(class_id) REFERENCES classes(id),
 UNIQUE(student_id, class_id)
);
