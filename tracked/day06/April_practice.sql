-- CREATE DATABASE student_db; 
-- USE student_db;course
-- CREATE TABLE students (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(50),
--     age INT,
--     course VARCHAR(50)
-- );
-- INSERT INTO students (name, age, course)
-- VALUES ('Alice', 22, 'CS');
-- INSERT INTO students (name, age, course)
-- VALUES
-- ('Bob', 20, 'IT'),
-- ('Charlie', 23, 'CS'),
-- ('David', 21, 'ECE'),
-- ('Emma', 24, 'Mechanical'),
-- ('Frank', 19, 'CS');
-- SELECT * FROM students; 
-- SELECT * FROM students WHERE age > 20;
-- SELECT * FROM students ORDER BY age DESC;
-- SELECT * FROM students ORDER BY age ASC;
-- SELECT * FROM students LIMIT 2;
-- SELECT * FROM users WHERE username='admin';

-- INSERT INTO students (name, age, course)
-- VALUES
-- ('sree', 20, 'CS'),
-- ('Nidhi', 21, 'IT'),
-- ('Reddy', 22, 'DS'),
-- ('vamshi', 23, 'CS'),
-- ('dubba', 19, 'AIML'),
-- ('Vasu', 24, 'CS'),
-- ('suchi', 23, 'CS'),
-- ('pooja', 25, 'IT'),
-- ('prasu', 26, 'ECE'),
-- ('kavya' , 21, 'EEE');

-- SELECT * from students where age > 21;
-- select * from students where course = 'CS';
-- select * from students ORDER BY name;
-- select * from students ORDER BY age ASC LIMIT 3;
-- DROP TABLE IF EXISTS courses;
-- create table courses(
--  id SERIAL PRIMARY KEY,
--  name VARCHAR(50)
--  );
-- insert into courses (name)
-- values 
-- ('CS'),
-- ('Cyber_security'),
-- ('IT'),
-- ('ECE'),
-- ('DS');
-- SELECT *
-- FROM students
-- JOIN courses
-- ON students.course = courses.name;
-- select * from students 
-- RIGHT JOIN courses on students.course = courses.name;
-- select * from students
-- LEFT JOIN courses on students.course = courses.name;
-- select * from students 
-- group by students.id;










