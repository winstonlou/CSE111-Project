import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE dates(
                    da_daid decimal (9,0),
                    da_releaseyear Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE duration(
                    du_duid decimal (9,0),
                    du_runtime Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE movies(
                    m_mid decimal (9,0),
                    m_title varchar(100) NOT NULL,
                    m_raid decimal(9,0) NOT NULL,
                    m_daid decimal (9,0) NOT NULL,
                    m_duid decimal (9,0) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE genre (
                    g_gid decimal (9,0),
                    g_gname char (25) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE movie_genre (
                    mg_mid decimal(9,0) NOT NULL,
                    mg_gid decimal (9,0) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE movie_director (
                    md_mid decimal(9,0) NOT NULL,
                    md_diid decimal (9,0) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE rated (
                    ra_raid decimal (9,0),
                    ra_ratings char(10) NOT NULL)"""
        _conn.execute(sql)


        sql = """CREATE TABLE director (
                    di_diid decimal (9,0),
                    di_diname varchar (50) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE user (
                    u_id INTEGER PRIMARY KEY,
                    u_mid decimal (9,0) NOT NULL,
                    u_watching Integer NOT NULL,
                    u_watched Integer NOT NULL,
                    u_towatch Integer NOT NULL)"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("successfully created tables")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE dates"
        _conn.execute(sql)
        sql = "DROP TABLE duration"
        _conn.execute(sql)
        sql = "DROP TABLE movies"
        _conn.execute(sql)
        sql = "DROP TABLE genre"
        _conn.execute(sql)
        sql = "DROP TABLE rated"
        _conn.execute(sql)
        sql = "DROP TABLE director"
        _conn.execute(sql)
        sql = "DROP TABLE user"
        _conn.execute(sql)
        sql = "DROP TABLE movie_genre"
        _conn.execute(sql)
        sql = "DROP TABLE movie_director"
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("successfully deleted tables")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createtest(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Inserting Test Values")
    try:
        
        values = [
            (1,'Toy Story', 2, 1, 1), (2,'Four Rooms', 2, 1, 2), (3, 'Jumanji', 2, 1, 3),
            (4, 'Fargo', 2, 2, 4), (5, "Miller's Crossing", 2, 19, 5), (6, 'The Big Lebowski', 2, 4, 6),
            (7, 'Phantoms', 2, 4, 7), (8, 'Hellraiser:Bloodline',2, 2, 8), (9, 'Spy Hard', 2, 2, 9),
            (10, 'Thinner', 2, 2, 10), (11, 'Sleeper', 2, 2, 11), (12, 'The Doors', 2, 20, 12),
            (13, 'Liar Liar',2, 3, 13), (14, 'Chinese Box',2, 3, 14), (15, 'Siblings', 2, 10, 15),
            (16, 'Creep', 2, 24, 16), (17, 'Brides',2, 10, 17), (18, 'Click',2, 12, 18),
        ]

        sql = "INSERT INTO movies VALUES(?,?,?,?,?)"
        _conn.executemany(sql, values)

        values = [
            (1,'Animation'), (2,'Comedy'), (3,'Family'),
            (4,'Adventure'), (5,"Fantasy"), (6,'Crime'),
            (7,'Drama'), (8,'Thriller'), (9,'Action'),
            (10,'Romance'), (11,'Sci-Fi'), (12,'Biography'),
            (13,'Mystery'), (14, 'History'), (15,'Horror'),
            (16,'Music'),(17,'Foreign')
            
        ]

        sql = "INSERT INTO genre VALUES(?, ?)"
        _conn.executemany(sql, values)


        values = [
            (1,'John Lasseter'), (2,'Allison Anders'), (3,'Joe Johnston'),
            (4,'James Fargo'), (5,'Alexandre Rockwell'), (6,'Joel Coen'),
            (7,'Joe Chappelle'), (8,'Kevin Yagher'), (9,'Rick Friedberg'),
            (10,'Tom Holland'), (11,'Woody Allen'), (12,'Oliver Stone'),
            (13,'Tom Shadyac'), (14,'Wayne Wang'), (15,'David Weaver'),
            (16,'Christopher Smith'), (17,'Pantelis Voulgaris'),
            (18,'Frank Coraci'), (19,'Robert Rodriguez'), (20, 'Quentin Tarantino')
        ]

        sql = "INSERT INTO director VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,'1995'),(2,'1996'),(3,'1997'),(4,'1998'),
            (5,'1999'),(6,'2000'),(7,'2001'),(8,'2002'),
            (9,'2003'),(10,'2004'),(11,'2005'),(12,'2006'),
            (13,'2007'),(14,'2008'),(15,'2009'),(16,'2010'),
            (17,'2011'),(18,'2012'),(18,'2013'),(19,'1990'),
            (20,'1991'),(21,'1992'),(22,'1993'),(23,'1994'),
            (24,'2014')
        ]

        sql = "INSERT INTO dates VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,81),(2,98),(3,104),(4,98),(5,115),
            (6,117),(7,91),(8,86),(9,81),(10,92),
            (11,89),(12,140),(13,86),(14,99),(15,85),
            (16,85),(17,128),(18,107),
        ]

        sql = "INSERT INTO duration VALUES(?, ?)"
        _conn.executemany(sql, values)


        values = [
            (1,"TRUE"),(2,"FALSE"),
        ]

        sql = "INSERT INTO rated VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,1),(1,2),(1,3),(2,6),(2,2),
            (3,3),(3,4),(3,5),(4,6),(4,7),
            (4,8),(5,6),(5,7),(5,8),(6,6),
            (6,2),(7,15),(7,11),(7,8),(8,15),
            (8,11),(8,8),(9,2),(9,9),(10,15),
            (10,8),(11,2),(11,10),(11,11),
            (12,7),(12,16),(13,2),(14,7),
            (14,10),(15,2),(16,15),(16,8),
            (16,13),(17,7),(17,10),(17,17),
            (18,2),(18,7),(18,5),(18,10),
        ]

        sql = "INSERT INTO movie_genre VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,1),(2,2),(2,5),(2,19),(2,20),
            (3,3),(4,6),(5,6),(6,6),(7,7),         
            (8,7),(8,8),(9,9),(10,10),(11,11),        
            (12,12),(13,12),(14,14),(15,15),        
            (16,16),(17,17),(18,18),        
        ]

        sql = "INSERT INTO movie_director VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1, 0, 1, 0),
            (2, 0, 0, 1),
            (3, 0, 0, 1),
            (4, 1, 0, 0),       
            (5, 1, 0, 0),
            (6, 0, 0, 1),
            (7, 1, 0, 0),
            (8, 0, 1, 0),
            (9, 0, 1, 0),
            (10, 1, 0, 0),
            (11, 0, 0, 1),
            (12, 0, 1, 0),
            (13, 0, 1, 0),
            (17, 0, 0, 1),
            (18, 0, 0, 1),
        ]

        sql = "INSERT INTO user(u_mid,u_watching,u_watched,u_towatch) VALUES(?,?,?,?)"
        _conn.executemany(sql, values)

        _conn.execute("COMMIT")
        print("successfully inputed test values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Queries1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Query 1: Search Movie based on User's Input for movie title ")
    cur=_conn.cursor()


    try:
       
        userInput = "T"       #Can be other string inputs
        cur.execute("""SELECT movies.m_mid,movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        WHERE instr(m_title, ?) """,[userInput])

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/1.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 2: Search movie based on User's Input for movie genre")

    try:

        userInput = 'Drama'      #can be any user input for genre search via check box
    
        cur.execute("""SELECT m_title, g_gname FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND
        genre.g_gname = ? ORDER BY m_title""", [userInput])

        rows = cur.fetchall()  
        results = "{:<0} {:>20}\n".format("movieTitle", "Genre")
        for row in rows:
            results += "{:<20} {:>11} \n".format(row[0], row[1])
        print(results)
        
        f = open("output/2.out", "w")
        f.write(results)
        f.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 3: Search movie based on User's Input for 2 movie genres")

    try:

        userInput = 'Drama'      #can be any user input for genre search check box
        userInput2 = 'Romance'
        both = userInput + " and " + userInput2
        cur.execute("""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?""", [userInput, userInput2])

        rows = cur.fetchall()  
        results = "{:<20} {:>20}\n".format("movieTitle","Genre")
        for row in rows:
            results += "{:<20} {:>33}\n".format(row[0], both)
        print(results)
        
        f = open("output/3.out", "w")
        f.write(results)
        f.close()
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 4: Search movie based on User's Input for 3 movie genres")

    try:

        userInput = 'Comedy'      #can be any user input for genre search check box
        userInput2 = 'Sci-Fi'
        userInput3 = 'Romance'
        both = userInput + " and " + userInput2 + " and " + userInput3
        cur.execute("""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?""", [userInput, userInput2, userInput3])

        rows = cur.fetchall()  
        results = "{:<10} {:>10}\n".format("movieTitle","Genre")
        for row in rows:
            results += "{:<15} {:<10}\n".format(row[0], both)
        print(results)
        
        f = open("output/4.out", "w")
        f.write(results)
        f.close()
    except Error as e:
        print(e)


    print("++++++++++++++++++++++++++++++++++")
    print("Query 5: Search movie based on User's Input for movie title and 1 genre input")

    try:
        userInput = "T"       #Can be other string inputs
        userInput2 = "Comedy"

        cur.execute("""SELECT m_title, g_gname FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, ?) AND g_gname = ?
        """, [userInput, userInput2])
        
        rows = cur.fetchall()  
        results = "{:<10} {:>10}\n".format("movieTitle", "Genre")
        for row in rows:
            results += "{:<15} {:<10}\n".format(row[0],userInput2)
        print(results)


        f = open("output/5.out", "w")
        f.write(results)
        f.close()
    
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Queries2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Query 6: Query a movie based on user input of title and 2 genres")
    cur=_conn.cursor()

    try:
       
        userInput = "C"       #Can be other string inputs
        userInput2 = "Romance"
        userInput3 = "Drama"
        both = userInput2 + " and " + userInput3

        cur.execute("""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, ?) AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, ?) AND g_gname = ?
        """, [userInput, userInput2, userInput, userInput3])

        rows = cur.fetchall()
        results = "{:<10} {:>10}\n".format("movieTitle", "Genre")
        for row in rows:
            results += "{:<15} {:<10}\n".format(row[0],both)
        print(results)
        
        f = open("output/6.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 7: Query a movie based on user input of title and 3 genres ")
    cur=_conn.cursor()

    try:
       
        userInput = "B"       #Can be other string inputs
        userInput2 = "Romance"
        userInput3 = "Drama"
        userInput4 = "Foreign"
        both = userInput2 + " and " + userInput3 + " and " + userInput4

        cur.execute("""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, ?) AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, ?) AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND instr(m_title, ?) AND g_gname = ?
        """, [userInput, userInput2, userInput, userInput3, userInput, userInput4])

        rows = cur.fetchall()
        results = "{:<10} {:>10}\n".format("movieTitle", "Genre")
        for row in rows:
            results += "{:<15} {:<10}\n".format(row[0],both)
        print(results)
        
        f = open("output/6.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    print("Query 8: Query a movie's genre that has 1 genres")
    cur=_conn.cursor()

    try:
       
        userInput = "Siblings"       #Can be other string inputs
        cur.execute("""SELECT movies.m_title, genre.g_gname FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND movies.m_title = ?
        LIMIT 1""",[userInput])

        rows = cur.fetchall()  
        results = "{:>0} {:>20}\n".format("movieTitle", "Genre")
        for row in rows:
            results += "{:<20} {:<20}\n".format(row[0], row[1])
        print(results)
        
        f = open("output/8.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 9: Query a movie's genre that has 2 genres")
    cur=_conn.cursor()

    try:
       
        userInput = "Four Rooms"       #Can be other string inputs
        cur.execute("""SELECT movies.m_title, genre1.g_gname, genre2.g_gname FROM movies, movie_genre AS movie_genre1, movie_genre AS movie_genre2, genre AS genre1, genre AS genre2
        WHERE movies.m_mid = movie_genre1.mg_mid AND movies.m_mid = movie_genre2.mg_mid AND
        genre1.g_gid = movie_genre1.mg_gid AND genre2.g_gid = movie_genre2.mg_gid AND 
        movies.m_title = ? AND genre1.g_gname IS NOT genre2.g_gname 
        LIMIT 1""",[userInput])

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} \n".format("movieTitle", "Genre", "Genre2")
        for row in rows:
            results += "{:<20} {:<20} {:>10} \n".format(row[0], row[1], row[2])
        print(results)
        
        f = open("output/9.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 10: Query a movie's genre that has 3 genres")
    cur=_conn.cursor()

    try:
       
        userInput = "Toy Story"       #Can be other string inputs
        cur.execute("""SELECT movies.m_title, genre1.g_gname, genre2.g_gname, genre3.g_gname FROM movies, movie_genre AS movie_genre1, movie_genre AS movie_genre2, movie_genre AS movie_genre3, genre AS genre1, genre AS genre2, genre AS genre3
        WHERE movies.m_mid = movie_genre1.mg_mid AND movies.m_mid = movie_genre2.mg_mid AND movies.m_mid = movie_genre3.mg_mid AND
        genre1.g_gid = movie_genre1.mg_gid AND genre2.g_gid = movie_genre2.mg_gid AND genre3.g_gid = movie_genre3.mg_gid AND 
        movies.m_title = ? AND genre1.g_gname IS NOT genre2.g_gname AND genre1.g_gname IS NOT genre3.g_gname AND genre3.g_gname IS NOT genre2.g_gname
        LIMIT 1""",[userInput])

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20}\n".format("movieTitle", "Genre", "Genre2", "Genre3")
        for row in rows:
            results += "{:<20} {:<20} {:>10} {:>20} \n".format(row[0], row[1], row[2], row[3])
        print(results)
        
        f = open("output/10.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

def Queries3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Query 11: Query director of a movie")
    cur=_conn.cursor()

    try:
       
        userInput = "Four Rooms"       #Can be other string inputs
        cur.execute("""SELECT total.di_diname AS D1 
        FROM (
        SELECT movies.m_mid, movies.m_title, director.di_diname FROM movies
        INNER JOIN director ON movie_director.md_diid = director.di_diid
        INNER JOIN movie_director ON movies.m_mid = movie_director.md_mid) AS total 
        WHERE total.m_title = ?""",[userInput])

        rows = cur.fetchall()  
        results = "{:>0} {:>20}\n".format("movieTitle", "movieDirectors")
        for row in rows:
            results += "{:<20} {:<20}\n".format(userInput, row[0])
        print(results)
        
        f = open("output/11.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 12: Query movie based on to watch list")
    cur=_conn.cursor()

    try:
        cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        INNER JOIN user ON movies.m_mid = user.u_mid
        WHERE u_towatch = 1""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/12.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    print("Query 13: Query movie list based on going to watch list")
    cur=_conn.cursor()

    try:
       
        
        cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        INNER JOIN user ON movies.m_mid = user.u_mid
        WHERE u_watching = 1;""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/13.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 14: Query movie list based on watched list")
    cur=_conn.cursor()

    try:
       
        userInput = "Toy Story"       #Can be other string inputs
        cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        INNER JOIN user ON movies.m_mid = user.u_mid
        WHERE u_watched = 1""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/14.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 15: Query movie list + remove movie if on any user lists (uses button idea*)")
    cur=_conn.cursor()

    try:
       
        userInput = "S"       #Can be other string inputs
        cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        WHERE m_mid NOT IN (SELECT u_mid FROM user);""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/15.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

def Queries4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Query 16: Query movie list, order by runtime")
    cur=_conn.cursor()

    try:
       
        userInput = "DESC"       #Can be DESC depending on user inputs
        if userInput == "ASC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY duration.du_runtime ASC""")
        if userInput == "DESC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY duration.du_runtime DESC""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/16.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 17: Query 16: Query movie list, order by date ")
    cur=_conn.cursor()

    try:
        userInput = "ASC"       #Can be DESC depending on user inputs
        if userInput == "ASC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY dates.da_releaseyear ASC""")
        if userInput == "DESC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY dates.da_releaseyear DESC""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/17.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    print("Query 18: Query Random Movie")
    cur=_conn.cursor()

    try:
       
        
        cur.execute("""SELECT m_mid, m_title, ra_ratings, du_runtime, da_releaseyear FROM movies
        INNER JOIN rated ON movies.m_raid = rated.ra_raid
        INNER JOIN duration ON movies.m_duid = duration.du_duid
        INNER JOIN dates ON movies.m_daid = dates.da_daid
        ORDER BY random() LIMIT 1""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/18.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 19: Query movie list, order alphabetically ")
    cur=_conn.cursor()

    try:
       
        userInput = "DESC"       #Can be DESC depending on user inputs
        if userInput == "ASC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY movies.m_title ASC""")
        if userInput == "DESC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY movies.m_title DESC""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/19.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 20: Query movie list, order by rating")
    cur=_conn.cursor()

    try:
       
        userInput = "DESC"       #Can be DESC depending on user inputs
        if userInput == "ASC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY rated.ra_ratings ASC""")
        if userInput == "DESC":
            cur.execute("""SELECT movies.m_mid, movies.m_title, rated.ra_ratings, duration.du_runtime, dates.da_releaseyear FROM movies
            INNER JOIN rated ON movies.m_raid = rated.ra_raid
            INNER JOIN duration ON movies.m_duid = duration.du_duid
            INNER JOIN dates ON movies.m_daid = dates.da_daid
            ORDER BY rated.ra_ratings DESC""")

        rows = cur.fetchall()  
        results = "{:>0} {:>20} {:>20} {:>20} {:>20}\n".format("movieId", "movieTitle", "movieRatings", "movieDuration", "MovieReleaseDate")
        for row in rows:
            results += "{:<20} {:<20} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3], row[4])
        print(results)
        
        f = open("output/20.out", "w")
        f.write(results)
        f.close()
  
    except Error as e:
        print(e)

def QueriesInsert(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Query 21: Insert movie into user watched list")
    cur=_conn.cursor()

    try:
       
        userInput = "14"    #movie id of the movie to be inserted
        

        cur.execute("""INSERT INTO user(u_mid,u_watching,u_watched,u_towatch) VALUES(?,0,1,0)""",[userInput])
        _conn.execute("COMMIT")
        print("Insert into watched list successful")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 22: Insert movie into user watching list")
    cur=_conn.cursor()

    try:
       
        userInput = "15"    #movie id of the movie to be inserted
        cur.execute("""INSERT INTO user(u_mid,u_watching,u_watched,u_towatch) VALUES(?,1,0,0)""",[userInput])
        _conn.execute("COMMIT")
        print("Insert into watching list successful")
        
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    print("Query 23: Insert movie into user going to watch list")
    cur=_conn.cursor()

    try:
       
        userInput = "16"    #movie id of the movie to be inserted
        cur.execute("""INSERT INTO user(u_mid,u_watching,u_watched,u_towatch) VALUES(?,0,0,1)""",[userInput])
        _conn.execute("COMMIT")
        print("Insert into going to watch list successful")
        
    except Error as e:
        print(e)

def QueriesDelete(_conn):
    print("Query 24: Delete movie into user list")
    cur=_conn.cursor()

    try:
       
        userInput = "14"    #movie id of the movie to be inserted
        
        cur.execute("""DELETE FROM user WHERE user.u_mid = ?""", [userInput])
        _conn.execute("COMMIT")
        print("Deleted movie id from watched list successful")

    except Error as e:
        print(e)

        
def main():
    database = r"test.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTables(conn)
        createtest(conn)
        #Queries1(conn)
        #Queries2(conn)
        #Queries3(conn)
        #Queries4(conn)
        #QueriesInsert(conn)
        #QueriesDelete(conn)


        


    closeConnection(conn, database)


if __name__ == '__main__':
    main()