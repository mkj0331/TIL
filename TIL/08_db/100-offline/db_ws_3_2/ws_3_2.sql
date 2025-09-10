-- SELECT * FROM courses;

-- SELECT * FROM feedback;

-- SELECT * FROM students;

SELECT s.username as username, c.title as course_title, f.comment as comment
FROM students s INNER JOIN feedback f ON s.id = f.student_id
INNER JOIN courses c on c.id = f.course_id
WHERE username = 'john_doe';


SELECT s.username as username, c.title as course_title, f.comment as comment
FROM students s LEFT JOIN feedback f ON s.id = f.student_id
LEFT JOIN courses c on c.id = f.course_id
WHERE username = 'jane_smith';


SELECT f.comment
FROM feedback f INNER JOIN students s on f.student_id = s.id
WHERE s.username = 'mary_jones' AND
f.created_at = (SELECT MAX(created_at) FROM feedback f2 WHERE f2.student_id = s.id);


