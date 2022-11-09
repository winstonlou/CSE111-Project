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
        sql = """CREATE TABLE date (
                    da_id decimal (9,0),
                    da_releaseyear Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE duration (
                    du_id decimal (9,0),
                    du_runtime Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE movies (
                    m_mid decimal (9,0),
                    m_gid decimal (9,0) NOT NULL,
                    di_id decimal (9,0) NOT NULL,
                    da_id decimal (9,0) NOT NULL,
                    du_id decimal (9,0) NOT NULL,
                    re_id decimal(9,0) NOT NULL,
                    ra_id decimal(9,0) NOT NULL,
                    m_title varchar(100) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE genre (
                    g_gid decimal (9,0),
                    g_gname char (25) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE ratings (
                    ra_id decimal (9,0),
                    ra_ratings char(10) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE reviews (
                    re_id decimal (9,0),
                    re_review decimal (9,0) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE director (
                    di_id decimal (9,0),
                    di_name varchar (50) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE user (
                    u_id decimal (9,0),
                    u_mid decimal (9,0) NOT NULL,
                    u_watching Integer NOT NULL,
                    u_watched Integer NOT NULL,
                    u_towatch Integer NOT NULL,
                    u_title varchar(100) NOT NULL,
                    u_gname char (25) NOT NULL,
                    u_name varchar (50) NOT NULL,
                    u_name2 varchar (50),
                    u_runtime Integer NOT NULL,
                    u_releaseyear Integer NOT NULL)"""
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
        sql = "DROP TABLE date"
        _conn.execute(sql)
        sql = "DROP TABLE duration"
        _conn.execute(sql)
        sql = "DROP TABLE movies"
        _conn.execute(sql)
        sql = "DROP TABLE genre"
        _conn.execute(sql)
        sql = "DROP TABLE ratings"
        _conn.execute(sql)
        sql = "DROP TABLE reviews"
        _conn.execute(sql)
        sql = "DROP TABLE director"
        _conn.execute(sql)
        sql = "DROP TABLE user"
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
            (1," "," ", 1,1,7, 2, 'Toy Story'),
            (2," "," ", " "," "," ", " ", 'Four Rooms'),
            (3," ", " ", " "," "," ", " ",  'Jumanji'),
            (4," ", " ", " "," "," ", " ", 'Fargo'),
            (5," "," ", " "," "," ", " ",  "Miller's Crossing"),
            (6," "," ", " "," "," ", " ",  'The Big Lebowski'),
            (7," ", " ", " "," "," ", " ", 'Phantoms'),
            (8," "," ", " "," "," ", " ",  'Hellraiser:Bloodline'),
            (9," ", " ", " "," "," ", " ", 'Spy Hard'),
            (10," "," ", " "," "," ", " ", 'Thinner'),
            (11," "," ", " "," "," ", " ", 'Sleeper'),
            (12," "," ", " "," "," ", " ", 'The Doors'),
            (13," ", " ", " "," "," ", " ", 'Liar Liar'),
            (14," "," ", " "," "," ", " ",  'Chinese Box'),
            (15," "," ", " "," "," ", " ", 'Siblings'),
            (16," "," ", " "," "," ", " ", 'Creep'),
            (17," "," ", " "," "," ", " ", 'Brides'),
            (18," "," ", " "," "," ", " ",  'Click'),
        ]

        sql = "INSERT INTO movies VALUES(?,?,?,?,?,?,?,?)"
        _conn.executemany(sql, values)

        values = [
            (1,'Animation'),
            (2,'Comedy'),
            (3,'Family'),
            (4,'Adventure'),
            (5,"Fantasy"),
            (6,'Crime'),
            (7,'Drama'),
            (8,'Thriller'),
            (9,'Action'),
            (10,'Romance'),
            (11,'Science Fiction'),
            (11,'Sci-Fi'),
            (12,'Biography'),
            (13,'Mystery'),
            (14, 'History'),
            
        ]

        sql = "INSERT INTO genre VALUES(?, ?)"
        _conn.executemany(sql, values)


        values = [
            (1,'John Lasseter'),
            (2,'Allison Anders'),
            (3,'Joe Johnston'),
            (4,'James Fargo'),
            (5,'Alexandre Rockwell'),
            (6,'Joel Coen'),
            (7,'Joe Chappelle'),
            (8,'Kevin Yagher'),
            (9,'Rick Friedberg'),
            (10,'Tom Holland'),
            (11,'Woody Allen'),
            (12,'Oliver Stone'),
            (13,'Tom Shadyac'),
            (14,'Wayne Wang'),
            (15,'David Weaver'),
            (16,'Christopher Smith'),
            (17,'Pantelis Voulgaris'),
            (18,'Frank Coraci'),
            (19,'Robert Rodriguez'),
            (20, 'Quentin Tarantino')
        ]

        sql = "INSERT INTO director VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,'1995'),
            (2,'1996'),
            (3,'1997'),
            (4,'1998'),
            (5,'1999'),
            (6,'2000'),
            (7,'2001'),
            (8,'2002'),
            (9,'2003'),
            (10,'2004'),
            (11,'2005'),
            (12,'2006'),
            (13,'2007'),
            (14,'2008'),
            (15,'2009'),
            (16,'2010'),
            (17,'2011'),
            (18,'2012'),
            (18,'2013'),
        ]

        sql = "INSERT INTO date VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,0),
            (2,0.5),
            (3,1),
            (4,1.5),
            (5,2),
            (6,2.5),
            (7,3),
            (8,3.5),
            (9,4),
            (10,4.5),
            (11,5),
        ]

        sql = "INSERT INTO reviews VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,81),
            (2,98),
            (3,104),
            (4,98),
            (5,115),
            (6,117),
            (7,91),
            (8,86),
            (9,81),
            (10,92),
            (11,89),
            (12,140),
            (13,86),
            (14,99),
            (15,85),
            (16,85),
            (17,128),
            (18,107),
        ]

        sql = "INSERT INTO duration VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,81),
            (2,98),
            (3,104),
            (4,98),
            (5,115),
            (6,117),
            (7,91),
            (8,86),
            (9,81),
            (10,92),
            (11,89),
            (12,140),
            (13,86),
            (14,99),
            (15,85),
            (16,85),
            (17,128),
            (18,107),
        ]

        sql = "INSERT INTO duration VALUES(?, ?)"
        _conn.executemany(sql, values)

        values = [
            (1,"TRUE"),
            (2,"FALSE"),
        ]

        sql = "INSERT INTO ratings VALUES(?, ?)"
        _conn.executemany(sql, values)



        _conn.execute("COMMIT")
        print("successfully inputed test values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")




def main():
    database = r"test.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTables(conn)
        createtest(conn)

        


    closeConnection(conn, database)


if __name__ == '__main__':
    main()