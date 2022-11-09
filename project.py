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
                    da_mid decimal (9,0) NOT NULL,
                    da_releaseyear Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE duration (
                    du_id decimal (9,0),
                    du_mid decimal (9,0) NOT NULL,
                    du_runtime Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE movies (
                    m_mid decimal (9,0),
                    m_gid decimal (9,0) NOT NULL,
                    m_title varchar(100) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE genre (
                    g_gid decimal (9,0),
                    g_gname char (25) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE ratings (
                    ra_id decimal (9,0),
                    ra_mid decimal (9,0) NOT NULL,
                    ra_ratings char(10) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE reviews (
                    re_id decimal (9,0),
                    re_imbdid decimal (9,0) NOT NULL,
                    re_review decimal (9,0) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE director (
                    di_id decimal (9,0),
                    di_mid decimal (9,0) NOT NULL,
                    di_name varchar (50) NOT NULL,
                    di_name2 varchar (50))"""
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

def createtest(_conn):
    print("++++++++++++++++++++++++++++++++++")

    try:
        
        values = [
            (1, "{1},{3},{2} ", 'Toy Story'),
            (2," ", 'Four Rooms'),
            (3," ", 'Jumanji'),
            (4," ", 'Fargo'),
            (5," ", "Miller's Crossing"),
            (6," ", 'The Big Lebowski'),
            (7," ", 'Phantoms'),
            (8," ", 'Hellraiser:Bloodline'),
            (9," ",'Spy Hard'),
            (10," ",'Thinner'),
            (11," ",'Sleeper'),
            (12," ",'The Doors'),
            (13," ",'Liar Liar'),
            (14," ",'Chinese Box'),
            (15," ",'Siblings'),
            (16," ",'Creep'),
            (17," ",'Brides'),
            (18," ",'Click'),
        ]


        sql = "INSERT INTO movie VALUES(?, ?)"
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
            (10,'Horror')
            (11,'Science Fiction'),
            (12,'Biography'),
            (13,'Mystery'),
            (14,'History'),
        ]


        sql = "INSERT INTO genre VALUES(?, ?)"
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
        createTables(conn)
        # addSampleData(conn)

        


    closeConnection(conn, database)


if __name__ == '__main__':
    main()