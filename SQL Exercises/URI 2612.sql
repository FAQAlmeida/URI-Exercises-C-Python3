select movies.id, movies.name from movies
inner join genres on (genres.id = movies.id_genres)
inner join movies_actors on (movies.id = movies_actors.id_movies)
inner join actors on (actors.id = movies_actors.id_actors)
where (actors.name = 'Marcelo Silva' or actors.name = 'Miguel Silva') and genres.description = 'Action'