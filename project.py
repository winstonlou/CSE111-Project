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
                    da_id decimal (9,0) NOT NULL,
                    da_mid decimal (9,0) NOT NULL,
                    da_releaseyear Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE duration (
                    du_id decimal (9,0) NOT NULL,
                    du_mid decimal (9,0) NOT NULL,
                    du_runtime Integer NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE movies (
                    m_mid decimal (9,0) NOT NULL,
                    m_gid decimal (9,0) NOT NULL,
                    m_title varchar(100) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE genre (
                    g_gid decimal (9,0) NOT NULL,
                    g_gname char (25) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE ratings (
                    ra_id decimal (9,0) NOT NULL,
                    ra_mid decimal (9,0) NOT NULL,
                    ra_ratings char(10) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE reviews (
                    re_id decimal (9,0) NOT NULL,
                    re_imbdid decimal (9,0) NOT NULL,
                    re_review decimal (9,0) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE director (
                    di_id decimal (9,0) NOT NULL,
                    di_mid decimal (9,0) NOT NULL,
                    di_name varchar (50) NOT NULL,
                    di_name2 varchar (50))"""
        _conn.execute(sql)

        sql = """CREATE TABLE user (
                    u_id decimal (9,0) NOT NULL,
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
        print("successfully created table warehouse")
    except Error as e:
        _conn.execute("ROLLBACK")
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