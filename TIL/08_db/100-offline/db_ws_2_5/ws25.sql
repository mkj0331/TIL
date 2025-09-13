SELECT genre FROM movie_list
GROUP BY genre
ORDER BY COUNT(id) DESC
LIMIT 1;

SELECT genre, COUNT(id) AS movie_count, AVG(release_year) as avg_release_year FROM movie_list
GROUP BY genre;

SELECT genre, title, release_year FROM movie_list
WHERE (genre, release_year) IN (
  SELECT genre, MAX(release_year) FROM movie_list
  GROUP BY genre
)


SELECT * FROM movie_list
WHERE release_year IN (
  SELECT MIN(release_year) FROM movie_list WHERE genre = 'Action'
) AND genre != 'Action'
ORDER BY release_year, title;


SELECT * FROM movie_list
WHERE genre IN ('Sci-Fi', 'Action') AND
release_year IN (
  SELECT release_year FROM movie_list WHERE genre = 'Drama'
)
ORDER BY release_year;