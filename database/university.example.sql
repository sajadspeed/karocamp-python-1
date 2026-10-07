-- DB Tables

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



-- Practical SQL examples for the university database


-- =========================================================
-- SELECT
-- =========================================================

-- Get all students
SELECT *
FROM students;


-- Get student names and student numbers
SELECT name, student_number
FROM students;


-- Get students enrolled after 2024
SELECT *
FROM students
WHERE enrollment_year > 2024;


-- Find a student by student number
SELECT *
FROM students
WHERE student_number = 'ST1003';


-- Find students whose name contains "Roya"
SELECT *
FROM students
WHERE name LIKE '%Roya%';


-- Get students ordered by enrollment year
SELECT *
FROM students
ORDER BY enrollment_year DESC;


-- Get the first 5 students
SELECT *
FROM students
LIMIT 5;


-- Get different teacher departments
SELECT DISTINCT department
FROM teachers;


-- =========================================================
-- WHERE
-- =========================================================

-- Get teachers from the Computer Science department
SELECT *
FROM teachers
WHERE department = 'Computer Science';


-- Get classes with a capacity greater than 30
SELECT *
FROM classes
WHERE capacity > 30;


-- Get classes in the Fall 2026 term
SELECT *
FROM classes
WHERE term = 'Fall 2026';


-- Get enrollments with a final grade
SELECT *
FROM enrollments
WHERE final_grade IS NOT NULL;


-- Get active enrollments
SELECT *
FROM enrollments
WHERE status = 'active';


-- Get students enrolled between 2023 and 2025
SELECT *
FROM students
WHERE enrollment_year BETWEEN 2023 AND 2025;


-- Get active or completed enrollments
SELECT *
FROM enrollments
WHERE status IN ('active', 'completed');


-- =========================================================
-- INSERT
-- =========================================================

-- Add a new student
INSERT INTO students (
    name,
    student_number,
    email,
    enrollment_year
)
VALUES (
    'Roya Ahmadi',
    'ST1010',
    'roya@example.com',
    2026
);


-- Add a new teacher
INSERT INTO teachers (
    name,
    email,
    department
)
VALUES (
    'Ali Mohammadi',
    'ali@example.com',
    'Computer Science'
);


-- Add a new course
INSERT INTO courses (
    name,
    code,
    unit
)
VALUES (
    'Web Programming',
    'CS205',
    3
);


-- Add a new class
INSERT INTO classes (
    course_id,
    teacher_id,
    term,
    capacity,
    classroom,
    schedule
)
VALUES (
    2,
    1,
    'Fall 2026',
    30,
    'Room 204',
    'Saturday 10:00'
);


-- Enroll a student in a class
INSERT INTO enrollments (
    student_id,
    class_id,
    enrolled_at
)
VALUES (
    1,
    2,
    '2026-09-25'
);


-- =========================================================
-- UPDATE
-- =========================================================

-- Change a student's email
UPDATE students
SET email = 'newemail@example.com'
WHERE id = 1;


-- Change a student's enrollment year
UPDATE students
SET enrollment_year = 2025
WHERE id = 3;


-- Change a teacher's department
UPDATE teachers
SET department = 'Software Engineering'
WHERE id = 2;


-- Increase class capacity
UPDATE classes
SET capacity = capacity + 5
WHERE id = 3;


-- Change a classroom
UPDATE classes
SET classroom = 'Room 305'
WHERE id = 2;


-- Change an enrollment status
UPDATE enrollments
SET status = 'completed'
WHERE id = 5;


-- Set a student's final grade
UPDATE enrollments
SET final_grade = 18.5
WHERE id = 5;


-- Update multiple columns
UPDATE enrollments
SET status = 'completed',
    final_grade = 17.25
WHERE id = 7;


-- IMPORTANT:
-- Always check the WHERE condition before UPDATE.


-- =========================================================
-- DELETE
-- =========================================================

-- Delete an enrollment
DELETE FROM enrollments
WHERE id = 10;


-- Delete a class
DELETE FROM classes
WHERE id = 8;


-- Delete a teacher
DELETE FROM teachers
WHERE id = 5;


-- Delete a student
DELETE FROM students
WHERE id = 12;


-- IMPORTANT:
-- Always check the WHERE condition before DELETE.


-- =========================================================
-- SIMPLE JOIN
-- =========================================================

-- Get students and their class IDs
SELECT
    students.name,
    enrollments.class_id
FROM students
JOIN enrollments
    ON students.id = enrollments.student_id;


-- Get students and their enrollment dates
SELECT
    students.name,
    enrollments.enrolled_at
FROM students
JOIN enrollments
    ON students.id = enrollments.student_id;


-- Get classes and their course IDs
SELECT
    classes.id,
    classes.course_id,
    classes.term
FROM classes;


-- Get classes with course names
SELECT
    classes.id,
    courses.name AS course_name,
    classes.term
FROM classes
JOIN courses
    ON classes.course_id = courses.id;


-- Get classes with teacher names
SELECT
    classes.id,
    teachers.name AS teacher_name,
    classes.term
FROM classes
JOIN teachers
    ON classes.teacher_id = teachers.id;


-- =========================================================
-- JOIN WITH MORE TABLES
-- =========================================================

-- Get course name and teacher name for each class
SELECT
    courses.name AS course_name,
    teachers.name AS teacher_name,
    classes.term
FROM classes
JOIN courses
    ON classes.course_id = courses.id
JOIN teachers
    ON classes.teacher_id = teachers.id;


-- Get students and the courses they are taking
SELECT
    students.name AS student_name,
    courses.name AS course_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id;


-- Get students, courses, and final grades
SELECT
    students.name AS student_name,
    courses.name AS course_name,
    enrollments.final_grade
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id;


-- Get students, courses, and teachers
SELECT
    students.name AS student_name,
    courses.name AS course_name,
    teachers.name AS teacher_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id
JOIN teachers
    ON classes.teacher_id = teachers.id;


-- =========================================================
-- JOIN + WHERE
-- =========================================================

-- Get all courses taken by Roya
SELECT
    students.name AS student_name,
    courses.name AS course_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id
WHERE students.name = 'Roya Ahmadi';


-- Get all students in a specific course
SELECT
    students.name AS student_name,
    courses.name AS course_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id
WHERE courses.code = 'CS101';


-- Get students taking classes in Fall 2026
SELECT
    students.name,
    courses.name AS course_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id
WHERE classes.term = 'Fall 2026';


-- Get students who got a grade higher than 17
SELECT
    students.name,
    courses.name AS course_name,
    enrollments.final_grade
FROM enrollments
JOIN students
    ON enrollments.student_id = students.id
JOIN classes
    ON enrollments.class_id = classes.id
JOIN courses
    ON classes.course_id = courses.id
WHERE enrollments.final_grade > 17;


-- =========================================================
-- JOIN WITH ALIAS
-- =========================================================

-- Use aliases to make the query shorter
SELECT
    s.name AS student_name,
    c.name AS course_name
FROM enrollments AS e
JOIN students AS s
    ON e.student_id = s.id
JOIN classes AS cl
    ON e.class_id = cl.id
JOIN courses AS c
    ON cl.course_id = c.id;


-- =========================================================
-- LEFT JOIN
-- =========================================================

-- Get all students, including students with no enrollments
SELECT
    students.name,
    enrollments.class_id
FROM students
LEFT JOIN enrollments
    ON students.id = enrollments.student_id;


-- Get all courses, including courses with no classes
SELECT
    courses.name,
    classes.id AS class_id
FROM courses
LEFT JOIN classes
    ON courses.id = classes.course_id;


-- Get all classes, including classes with no students
SELECT
    courses.name AS course_name,
    classes.id AS class_id,
    students.name AS student_name
FROM classes
JOIN courses
    ON classes.course_id = courses.id
LEFT JOIN enrollments
    ON classes.id = enrollments.class_id
LEFT JOIN students
    ON enrollments.student_id = students.id;


-- =========================================================
-- COUNT
-- =========================================================

-- Count all students
SELECT COUNT(*)
FROM students;


-- Count all teachers
SELECT COUNT(*)
FROM teachers;


-- Count all courses
SELECT COUNT(*)
FROM courses;


-- Count active enrollments
SELECT COUNT(*)
FROM enrollments
WHERE status = 'active';


-- Count students enrolled in a specific class
SELECT COUNT(*)
FROM enrollments
WHERE class_id = 2;


-- =========================================================
-- AGGREGATE FUNCTIONS
-- =========================================================

-- Find the average final grade
SELECT AVG(final_grade)
FROM enrollments;


-- Find the highest final grade
SELECT MAX(final_grade)
FROM enrollments;


-- Find the lowest final grade
SELECT MIN(final_grade)
FROM enrollments;


-- Find the total units of all courses
SELECT SUM(unit)
FROM courses;


-- Find the average course unit
SELECT AVG(unit)
FROM courses;


-- =========================================================
-- GROUP BY
-- =========================================================

-- Count students by enrollment year
SELECT
    enrollment_year,
    COUNT(*) AS student_count
FROM students
GROUP BY enrollment_year;


-- Count teachers in each department
SELECT
    department,
    COUNT(*) AS teacher_count
FROM teachers
GROUP BY department;


-- Count classes in each term
SELECT
    term,
    COUNT(*) AS class_count
FROM classes
GROUP BY term;


-- Count enrollments by status
SELECT
    status,
    COUNT(*) AS enrollment_count
FROM enrollments
GROUP BY status;


-- =========================================================
-- GROUP BY + JOIN
-- =========================================================

-- Count students in each class
SELECT
    class_id,
    COUNT(*) AS student_count
FROM enrollments
GROUP BY class_id;


-- Show course names with number of enrolled students
SELECT
    courses.name AS course_name,
    COUNT(enrollments.student_id) AS student_count
FROM courses
JOIN classes
    ON courses.id = classes.course_id
JOIN enrollments
    ON classes.id = enrollments.class_id
GROUP BY courses.id, courses.name;


-- Count students for each teacher
SELECT
    teachers.name AS teacher_name,
    COUNT(enrollments.student_id) AS student_count
FROM teachers
JOIN classes
    ON teachers.id = classes.teacher_id
JOIN enrollments
    ON classes.id = enrollments.class_id
GROUP BY teachers.id, teachers.name;


-- =========================================================
-- HAVING
-- =========================================================

-- Find classes with more than 3 students
SELECT
    class_id,
    COUNT(*) AS student_count
FROM enrollments
GROUP BY class_id
HAVING COUNT(*) > 3;


-- Find departments with more than 2 teachers
SELECT
    department,
    COUNT(*) AS teacher_count
FROM teachers
GROUP BY department
HAVING COUNT(*) > 2;


-- =========================================================
-- ORDER BY + GROUP BY
-- =========================================================

-- Show courses from most enrolled to least enrolled
SELECT
    courses.name AS course_name,
    COUNT(enrollments.student_id) AS student_count
FROM courses
JOIN classes
    ON courses.id = classes.course_id
JOIN enrollments
    ON classes.id = enrollments.class_id
GROUP BY courses.id, courses.name
ORDER BY student_count DESC;


-- =========================================================
-- SUBQUERY
-- =========================================================

-- Find students who enrolled in the university
-- after the average enrollment year
SELECT *
FROM students
WHERE enrollment_year > (
    SELECT AVG(enrollment_year)
    FROM students
);


-- Find enrollments with a grade higher than
-- the average final grade
SELECT *
FROM enrollments
WHERE final_grade > (
    SELECT AVG(final_grade)
    FROM enrollments
);


-- =========================================================
-- A MORE COMPLEX EXAMPLE
-- JOIN + GROUP BY + HAVING + ORDER BY
-- =========================================================

-- Find teachers whose classes have at least 3 students
-- and show the teachers with the most students first
SELECT
    teachers.name AS teacher_name,
    teachers.department,
    COUNT(enrollments.student_id) AS total_students
FROM teachers
JOIN classes
    ON teachers.id = classes.teacher_id
JOIN enrollments
    ON classes.id = enrollments.class_id
GROUP BY
    teachers.id,
    teachers.name,
    teachers.department
HAVING COUNT(enrollments.student_id) >= 3
ORDER BY total_students DESC;


-- =========================================================
-- ANOTHER COMPLEX EXAMPLE
-- Find courses with their average final grade
-- and only show courses with an average above 15
-- =========================================================

SELECT
    courses.name AS course_name,
    COUNT(enrollments.student_id) AS student_count,
    AVG(enrollments.final_grade) AS average_grade
FROM courses
JOIN classes
    ON courses.id = classes.course_id
JOIN enrollments
    ON classes.id = enrollments.class_id
WHERE enrollments.final_grade IS NOT NULL
GROUP BY
    courses.id,
    courses.name
HAVING AVG(enrollments.final_grade) > 15
ORDER BY average_grade DESC;
