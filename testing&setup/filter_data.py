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

def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE data1"
        _conn.execute(sql)
        sql = "DROP TABLE data2_filtered"
        _conn.execute(sql)
        sql = "DROP TABLE data2"
        _conn.execute(sql)
        sql = "DROP TABLE merged_data"
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("successfully deleted tables")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE data1 (
                    d1_id decimal (9,0),
                    d1_imbd_id VARCHAR(20) NOT NULL,
                    d1_title VARCHAR(100) NOT NULL,
                    d1_ryear Integer NOT NULL,
                    d1_genres_new VARCHAR(100),
                    d1_cast_new VARCHAR(100),
                    d1_director VARCHAR(100))"""
        _conn.execute(sql)

        sql = """CREATE TABLE data2 (
                    d2_id decimal (9,0),
                    d2_adult VARCHAR(20),
                    d2_collection VARCHAR(100),
                    d2_budget INTEGER,
                    d2_genres VARCHAR(100),
                    d2_homepage VARCHAR(100), 
                    d2_id2 INTEGER NOT NULL,
                    d2_imbd_id VARCHAR(20) NOT NULL,
                    d2_language VARCHAR(10),
                    d2_otitle VARCHAR(100) NOT NULL,
                    d2_overview VARCHAR(100),
                    d2_popularity VARCHAR(100),
                    d2_post_path VARCHAR(100),
                    d2_pcompany VARCHAR(100),
                    d2_pcountries VARCHAR(100),
                    d2_rdate VARCHAR(20) NOT NULL,
                    d2_revenue INTEGER,
                    d2_runtime INTEGER,
                    d2_slanguage VARCHAR(100),
                    d2_status VARCHAR(20),
                    d2_tagline VARCHAR(100),
                    d2_title VARCHAR(100) NOT NULL,
                    d2_video VARCHAR(10),
                    d2_vote_avg DECIMAL(9,2),
                    d2_vote_count DECIMAL(9,0))"""
        _conn.execute(sql)

        lines= """CREATE TABLE data2_filtered(
                d2f_id decimal (9,0),
                d2f_adult VARCHAR(20),
                d2f_imbd_id VARCHAR(20) NOT NULL,
                d2f_rdate VARCHAR(20) NOT NULL,
                d2f_title VARCHAR(100) NOT NULL,
                d2f_genres VARCHAR(100),
                d2f_runtime INTEGER)
                """
        _conn.execute(lines)
       

        lines= """CREATE TABLE merged_data(
                md_d1id decimal (9,0),
                md_d2id decimal (9,0),
                md_adult VARCHAR(20),
                md_imbd_id VARCHAR(20) NOT NULL,
                md_rdate VARCHAR(20) NOT NULL,
                md_title VARCHAR(100) NOT NULL,
                md_genres VARCHAR(100),
                md_director VARCHAR(100),
                md_runtime INTEGER)
                """
        _conn.execute(lines)




        _conn.execute("COMMIT")
        print("successfully created tables")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def addData(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    _conn.execute("BEGIN")
    try:
        print("Adding movielist.csv")
        f = open("database2/movie_list_1.csv")
        lines = csv.reader(f)
        sql = "INSERT INTO data1 (d1_id, d1_imbd_id, d1_title, d1_ryear, d1_genres_new, d1_cast_new, d1_director) VALUES(?,?, ?, ?, ?, ?, ?)"

        _conn.executemany(sql,lines)
        f.close()

        print("Adding movielist2.csv")
        f = open("database1/movies_metadata.csv")
        lines = csv.reader(f)
        sql = """INSERT INTO data2 (
                d2_id, d2_adult, d2_collection, d2_budget,
                d2_genres, d2_homepage, d2_id2, d2_imbd_id,
                d2_language, d2_otitle, d2_overview, d2_popularity,
                d2_post_path, d2_pcompany, d2_pcountries, d2_rdate, d2_revenue,
                d2_runtime, d2_slanguage, d2_status, d2_tagline, 
                d2_title, d2_video, d2_vote_avg, d2_vote_count)
                VALUES( 
                    ?, ?, ?, ?, 
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?, ?)"""

        _conn.executemany(sql,lines)
        f.close()


        _conn.execute("COMMIT")
        print("successfully created tables")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def filterData(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Deleting Useless Data")
    

    
    _conn.execute("BEGIN")
    try:

        sql = """
            INSERT INTO data2_filtered SELECT data2.d2_id, data2.d2_adult, data2.d2_imbd_id, data2.d2_rdate, data2.d2_title, data2.d2_genres, data2.d2_runtime FROM data2
            """
        
        _conn.execute(sql)
        
        #sql = """DROP TABLE data"""
        #_conn.execute(sql)
        #sql = """ALTER TABLE data_backup RENAME TO data"""
        #_conn.execute(sql)

        _conn.execute("COMMIT")
        print("successfully added filter") 
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def mergeData(_conn,):
    print("++++++++++++++++++++++++++++++++++")
    print("Getting Values where title is in both db's")

    try:

        sql = """
            INSERT INTO merged_data SELECT 
            data1.d1_id, data2_filtered.d2f_id, data2_filtered.d2f_adult ,data2_filtered.d2f_imbd_id, data1.d1_ryear, 
            data2_filtered.d2f_title, data1.d1_genres_new, data1.d1_director, data2_filtered.d2f_runtime 
            FROM data2_filtered,data1
            WHERE data2_filtered.d2f_imbd_id = data1.d1_imbd_id
            """
        _conn.execute(sql)

        print("successfully merged movies")
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
        addData(conn)
        filterData(conn)
        mergeData(conn)


    closeConnection(conn, database)


if __name__ == '__main__':
    main()