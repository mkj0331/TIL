SELECT * FROM authors;

SELECT * FROM books;

SELECT * FROM genres;

SELECT ab.title as BookTitle, ab.name as AuthorName, g.genre_name as GenreName
FROM (SELECT b.*, a.name 
FROM books b INNER JOIN authors a
on b.author_id = a.id) ab INNER JOIN genres g
on ab.genre_id = g.id



CREATE INDEX idx_authors_name
on authors(name);

CREATE INDEX idx_genres_genre_name
on genres(genre_name);
 
SELECT ab.title as BookTitle, ab.name as AuthorName, g.genre_name as GenreName
FROM (SELECT b.*, a.name 
FROM books b INNER JOIN authors a
on b.author_id = a.id
WHERE a.name = 'J.K. Rowling'
) ab INNER JOIN genres g
on ab.genre_id = g.id
WHERE g.genre_name = 'Fantasy';
