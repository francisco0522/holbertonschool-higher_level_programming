-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linkede
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_show_genres.genre_id ORDER BY COUNT(tv_show_genres.genre_id) DESC;
