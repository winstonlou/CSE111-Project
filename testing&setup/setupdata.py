import sqlite3
import csv
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
                    m_adid decimal(9,0) NOT NULL,
                    m_daid decimal (9,0) NOT NULL,
                    m_duid decimal(9,0) NOT NULL)"""
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

        sql = """CREATE TABLE adult(
                    ad_adid decimal (9,0),
                    ad_ratings char(10) NOT NULL)"""
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
        sql = "DROP TABLE adult"
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

def FillAdult(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Adult Table")

    _conn.execute("BEGIN")
    try:
        values = [
                (1,"TRUE"),(2,"FALSE"),
            ]

        sql = "INSERT INTO adult VALUES(?, ?)"
        _conn.executemany(sql, values)

        _conn.execute("COMMIT")
        print("successfully inputed adult table values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def FillDates(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Date Table")

    _conn.execute("BEGIN")
    try:
        data = []
        key = 0
        keys = 42
        startyr = 1971
        while key < keys:
            data = [(key,startyr + key)]
            key = key + 1
            sql = "INSERT INTO dates VALUES(?, ?)"
            _conn.executemany(sql, data)
            #print(key)
    

        _conn.execute("COMMIT")
        print("successfully inputed dates values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def FillDuration(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Duration Table")

    _conn.execute("BEGIN")
    try:
        cur = _conn.cursor()
        sql = "SELECT md_runtime FROM merged_data"
        cur.execute(sql)
        result2 = cur.fetchall()
        #print(result2)

        result3 = set(result2)
        #print(result3)
        #print(type(result3))
        result4 = list(result3)
        #print(type(result4))
        #print(type(result4[0]))
        data2 = []
        for result in result4:
            result = list(result)
            result = str(result)
            result = result.strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            data2.append(result)
        #print(data2)
        data2.sort()
        #print(data2)
        results = data2
        key = 0
        data = []
        for result in results:
            get = result
            #print(get)
            data = [(key,get)]
            #print(data)
            sql = """INSERT INTO duration VALUES(?,?)"""
            cur.executemany(sql,data)
            key = key + 1
    

        _conn.execute("COMMIT")
        print("successfully inputed duration values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def FillGenre(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Genre Table")

    _conn.execute("BEGIN")
    try:
        cur = _conn.cursor()
        sql = "SELECT md_genres FROM merged_data"
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        key = 0
        data = []
        data2 = []

        for result in results:
            #print(key)
            get = result[0]
            get1 = get.split(" ")
            #print(get)
            #print(len(get1))
            #print(get1[0])
            length = len(get1)
            start = 0
            while start < length:
                data.append(get1[start])
                start = start + 1
            key = key + 1
            
        #print(data)
        lists = set(data)
        #print(lists)
        key = 0
        lists.remove("Movie")
        lists.remove("TV")
        #print(lists)

        key = 0
        for list in lists:
            get = list
            #print(get)
            data = [(key,get)]
            #print(data)
            sql = """INSERT INTO genre VALUES(?,?)"""
            cur.executemany(sql,data)
            key = key + 1
        data = [(20 , "TV Movie")]
        sql = """INSERT INTO genre VALUES(?,?)"""
        cur.executemany(sql,data)


        _conn.execute("COMMIT")
        print("successfully inputed genre values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def FillGM(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Genre-Movie Table")

    _conn.execute("BEGIN")
    try:
        cur = _conn.cursor()
        sql = "SELECT md_genres FROM merged_data"
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        key = 0
    

        for result in results:
            #print(key)
            get = result[0]
            get1 = get.split(" ")
            #print(get)
            #print(len(get1))
            #print(get1[0])
            length = len(get1)
            start = 0
            while start < length:
                #print(get1[start])
                sql = f"""SELECT g_gid FROM genre WHERE g_gname = "{get1[start]}";"""
                cur.execute(sql)
                insert = cur.fetchall()
                insert2 = str(insert)
                insert2 = insert2.strip("[").strip("]").strip("(").strip(")").strip(",")
                #print(insert)
                post = [(key,insert2)]
                #print(post)
                sql = "INSERT INTO movie_genre VALUES(?,?)"
                cur.executemany(sql,post)
                start = start + 1
            key = key + 1
            
    


        _conn.execute("COMMIT")
        print("successfully inputed movie-genre values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def FillMovie(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Movie Table")

    _conn.execute("BEGIN")
    try:
        cur = _conn.cursor()
        #sql = """SELECT md_title, ad_adid, da_daid, du_duid FROM merged_data, dates, adult, duration
        #WHERE da_releaseyear = md_rdate AND md_adult = ad_ratings AND du_runtime = md_runtime;"""
        sql = """SELECT md_title, ad_adid, da_daid,du_duid FROM merged_data,adult,dates,duration
        WHERE md_adult = ad_ratings AND da_releaseyear = md_rdate AND md_runtime = du_runtime;"""
        cur.execute(sql)
        results = cur.fetchall()
        key = 0
        data = []
        for result in results:
            data = [(key,result[0],result[1],result[2],result[3])]
            #print(data)
            sql = """INSERT INTO movies VALUES(?,?,?,?,?)"""
            cur.executemany(sql,data)
            
            key = key + 1            


        _conn.execute("COMMIT")
        print("successfully inputed movie values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def FillDirector(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Director Table")

    _conn.execute("BEGIN")
    try:
        cur = _conn.cursor()
        sql = "SELECT md_director FROM merged_data"
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        key = 0
        data = []
        

        for result in results:      #just break it down one word at a time
            #print(key)
            get = result[0]
            get1 = get.split(" ")
            #print(get)
            #print(len(get1))
            #print(get1[0])
            length = len(get1)
            start = 0
            while start < length:
                data.append(get1[start])
                start = start + 1
            key = key + 1
        
        #print(data)
        lists = set(data)
        #print(type(lists))
        #print(lists)
        lista = sorted(lists)
        #print(lista)

        key = 0
        for list in lista:
            get = list
            #print(get)
            data = [(key,get)]
            #print(data)
            sql = """INSERT INTO director VALUES(?,?)"""
            cur.executemany(sql,data)
            key = key + 1

        _conn.execute("COMMIT")
        print("successfully inputed genre values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def FillDM(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Set up Director-Movie Table")

    _conn.execute("BEGIN")
    try:
        cur = _conn.cursor()
        sql = "SELECT md_director FROM merged_data"
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        key = 0
    

        for result in results:
            #print(key)
            get = result[0]
            get1 = get.split(" ")
            #print(get)
            #print(len(get1))
            #print(get1[0])
            length = len(get1)
            start = 0
            while start < length:
                #print(get1[start])
                sql = f"""SELECT di_diid FROM director WHERE di_diname = "{get1[start]}";"""
                cur.execute(sql)
                insert = cur.fetchall()
                insert2 = str(insert)
                insert2 = insert2.strip("[").strip("]").strip("(").strip(")").strip(",")
                #print(insert)
                post = [(key,insert2)]
                #print(post)
                sql = "INSERT INTO movie_director VALUES(?,?)"
                cur.executemany(sql,post)
                start = start + 1
            key = key + 1
            
    


        _conn.execute("COMMIT")
        print("successfully inputed movie-genre values")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"ml.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTables(conn)
        FillAdult(conn)
        FillDates(conn)
        FillDuration(conn)
        FillGenre(conn)
        FillGM(conn)
        FillMovie(conn)
        FillDirector(conn)
        FillDM(conn)


    closeConnection(conn, database)


if __name__ == '__main__':
    main()