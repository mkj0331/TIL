INSERT INTO movie_list (title, genre, release_year) VALUES
('The Matrix',  'Sci-Fi',  1999),
('Gladiator',  'Action',  2000),
('Jurassic Park', 'Sci-Fi',  1993),
('The Fugitive',  'Action', 1993);

SELECT * FROM movie_list;

SELECT title FROM movie_list
WHERE genre = 'Drama' AND release_year is not null
ORDER BY release_year
LIMIT 1;

SELECT title, release_year FROM movie_list
WHERE release_year > 2000
ORDER BY release_year DESC
LIMIT 1;

SELECT * FROM movie_list
WHERE genre IN ('Action', 'Sci-Fi') AND
(release_year IN (
  SELECT release_year FROM movie_list
  WHERE genre = 'Drama'
));


SELECT * FROM movie_list
WHERE genre = 'Sci-Fi' AND
release_year > (
  SELECT AVG(release_year) FROM movie_list
  WHERE genre = 'Action'
)


SELECT * FROM movie_list
WHERE release_year = (
  SELECT MIN(release_year) FROM movie_list
  WHERE genre = 'Action'
) AND genre != 'Action';



