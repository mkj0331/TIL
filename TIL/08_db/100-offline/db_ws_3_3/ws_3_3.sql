SELECT * FROM courses;
SELECT * FROM feedback;
SELECT * FROM students;


SELECT f.comment 
FROM feedback f JOIN students s ON f.student_id = s.id
ORDER BY f.created_at ASC LIMIT 1;


CREATE VIEW student_feedback_with_courses AS
SELECT s.username as username, c.title as course_title, f.comment as comment, f.created_at as created_at
FROM students s JOIN feedback f on f.student_id = s.id
JOIN courses c on c.id = f.course_id;

SELECT * FROM student_feedback_with_courses
WHERE username = 'john_doe';