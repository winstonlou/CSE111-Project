SELECT data2_filtered.d2f_id, data2_filtered.d2f_imbd_id, data2_filtered.d2f_rdate, data2_filtered.d2f_title, data2_filtered.d2f_genres
FROM data2_filtered,data1
WHERE data2_filtered.d2f_imbd_id = data1.d1_imbd_id;


SELECT m_title, ra_rated, du_runtime, da_releaseyear FROM movies
INNER JOIN rated ON movies.m_raid = rated.ra_raid
INNER JOIN duration ON movies.m_duid = duration.du_duid
INNER JOIN dates ON movies.m_daid = dates.da_daid
WHERE m_title = "Toy Story";

cur.execute("SELECT m_mid FROM movies")
        mkeys=cur.fetchall()
        count=1
        for mid in mkeys:
            sql = (f"""SELECT m_title, g_gname FROM movies, movie_genre, genre
            WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND movies.m_mid = {mid[0]}""")

            cur.execute(sql)
            results=cur.fetchall()
            print(results);



SELECT m_title, g_gname FROM movies, movie_genre, genre
WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND movies.m_title = "Toy Story";

SELECT m_title, g_gname FROM movies, movie_genre, genre
            WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND
            g_gname = "Comedy"
            ORDER BY m_title;

SELECT movies.m_mid,movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        WHERE m_title LIKE '%S%';

SELECT m_title FROM movies, movie_genre, genre
WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = "Drama"
INTERSECT
SELECT m_title FROM movies, movie_genre, genre
WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = "Thriller";


SELECT movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear, genre.g_gname, director.di_diname FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        WHERE instr(m_title, ?);

SELECT movies.m_title, genre1.g_gname, genre2.g_gname, genre3.g_gname FROM movies, movie_genre AS movie_genre1, movie_genre AS movie_genre2, movie_genre AS movie_genre3, genre AS genre1, genre AS genre2, genre AS genre3
WHERE movies.m_mid = movie_genre1.mg_mid AND movies.m_mid = movie_genre2.mg_mid AND movies.m_mid = movie_genre3.mg_mid AND
genre1.g_gid = movie_genre1.mg_gid AND genre2.g_gid = movie_genre2.mg_gid AND genre3.g_gid = movie_genre3.mg_gid AND 
movies.m_title = "Toy Story" AND genre1.g_gname IS NOT genre2.g_gname AND genre1.g_gname IS NOT genre3.g_gname AND genre3.g_gname IS NOT genre2.g_gname;


SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
INNER JOIN rated ON movies.m_raid = rated.ra_raid
INNER JOIN duration ON movies.m_duid = duration.du_duid
INNER JOIN dates ON movies.m_daid = dates.da_daid
WHERE m_mid NOT IN (SELECT u_mid FROM user);

SELECT total.di_diname AS D1 
FROM (
        SELECT movies.m_mid, movies.m_title, director.di_diname FROM movies
        INNER JOIN director ON movie_director.md_diid = director.di_diid
        INNER JOIN movie_director ON movies.m_mid = movie_director.md_mid) AS total 
WHERE total.m_title = "Four Rooms";

SELECT m_title FROM movies, movie_genre, genre
WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, "C") AND g_gname = "Romance"
INTERSECT
SELECT m_title FROM movies, movie_genre, genre
WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, "C") AND g_gname = "Drama";


SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
INNER JOIN rated ON movies.m_raid = rated.ra_raid
INNER JOIN duration ON movies.m_duid = duration.du_duid
INNER JOIN dates ON movies.m_daid = dates.da_daid
ORDER BY duration.du_runtime ASC;

SELECT m_title, ra_ratings, du_runtime, da_releaseyear FROM movies
INNER JOIN rated ON movies.m_raid = rated.ra_raid
INNER JOIN duration ON movies.m_duid = duration.du_duid
INNER JOIN dates ON movies.m_daid = dates.da_daid;
ORDER BY random()
LIMIT 1;

SELECT DISTINCT md_genres FROM merged_data
WHERE md_genres NOT LIKE "Comedy";

Music Animation Sci-Fi
Animation Horror Drama
Drama Action Romance Comedy
Comedy Drama Action
Music Comedy Documentary
Fantasy Horror Action Comedy Sci-Fi Foreign Animation
Western Sci-Fi
Horror Comedy Mystery
Comedy Action Documentary
Horror Action Sci-Fi Comedy
Fantasy Comedy Romance Drama
Action Mystery Thriller Horror

SELECT DISTINCT md_genres FROM merged_data
WHERE md_genres LIKE "%Movie%";

SELECT md_title, ad_adid, da_daid, du_duid FROM merged_data, dates, adult, duration
WHERE da_releaseyear = md_rdate AND md_adult = ad_ratings AND du_runtime = md_runtime
LIMIT 10;