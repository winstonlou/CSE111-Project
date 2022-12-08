from flask import Flask
from flask import render_template, request, redirect, url_for
import sqlite3
import csv
from sqlite3 import Error
import json

URL = "http://127.0.0.1:5000/"
app = Flask(__name__)

def openConnection():
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: data.sqlite")

    conn = None
    try:
        conn = sqlite3.connect("data.sqlite")
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn
def closeConnection(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: data.sqlite")

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def displaySearch(results):
    conn = openConnection()
    cur = conn.cursor()
    print(results)
    datas =[]
    for result in results:
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'")
        datas.append(result)
    print(datas)
   
    finals = []
    for data in datas:
        totals = []
        final =[]
        print(data)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime FROM movies,dates,duration,adult 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND m_title ="{data}"; """
        cur.execute(sql)
        values = cur.fetchall()
        sql = f"""SELECT total.di_diname AS D1 
        FROM (
        SELECT movies.m_mid, movies.m_title, director.di_diname FROM movies
        INNER JOIN director ON movie_director.md_diid = director.di_diid
        INNER JOIN movie_director ON movies.m_mid = movie_director.md_mid) AS total 
        WHERE total.m_title ="{data}";"""
        cur.execute(sql)
        values2 = cur.fetchall()
        sql = f"""SELECT g_gname FROM genre
        INNER JOIN movies ON movie_genre.mg_mid = movies.m_mid
        INNER JOIN movie_genre ON genre.g_gid = movie_genre.mg_gid
        WHERE m_title = "{data}";"""
        cur.execute(sql)
        values3 = cur.fetchall()

        #print(values)
        #print(values2)
        #print(values3)
        totals += values + values2 + values3
        #print(total)
        counts = 0
        for total in totals:
            total = str(total)
            total = total.strip("(").strip(")").strip(",").strip("'")
            final.append(total)
            counts = counts + 1
        finals += final
    print(finals)
    closeConnection(conn)
    return finals
def CheckList(name,row):
    print("Checking User List First")
    conn = openConnection()
    cur = conn.cursor()
    sql = f"""SELECT m_mid FROM movies WHERE m_title LIKE '%{name}%';"""
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    key = 1
    row = int(row)
    for result in results:
        print(result)
        print(key)
        print(row)
        if key == row:
            print("got in!")
            result = str(result)
            result = result.strip("(").strip(")").strip(",").strip("'")
            print(result)
            cur.execute(f"""SELECT u_id FROM user WHERE u_mid ={result}""")
            check = cur.fetchall()
            print(check)
            if check:
                return 1
            if not check:
                return 0
            break
        key = key + 1
    closeConnection(conn)
    return 2


@app.route('/')
def index():
    #conn = openConnection()
    #closeConnection(conn)
    return render_template('Page.html')

@app.route('/displayMovie', methods = ["GET"])
def getMovieList():
    conn = openConnection()
    cur = conn.cursor()
    sql = """SELECT m_title FROM movies LIMIT 100"""
    cur.execute(sql)
    results = cur.fetchall()
    closeConnection(conn)
    
    return json.dumps(results)

@app.route('/nameSearch/<string:name>', methods = ["GET"])
def getName(name):
    conn = openConnection()
    cur = conn.cursor()
    sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
    WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
    genre.g_gid = movie_genre.mg_gid AND m_title LIKE '%{name}%';"""
    cur.execute(sql)
    results = cur.fetchall()
    closeConnection(conn)
    return json.dumps(results)

@app.route('/NaG1/<string:name>/<string:genre>', methods = ["GET"])
def getNameAndGenre1(name,genre):
    conn = openConnection()
    cur = conn.cursor()
    cur.execute(f"""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND 
        m_title LIKE '%{name}%' AND g_gname = "{genre}";""")
    results = cur.fetchall()
    #print(results)
    data =[]
    for result in results:
        #print(result)
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'")
        #print(result)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
        genre.g_gid = movie_genre.mg_gid AND m_title = "{result}";"""
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        data += results
    #print(data)
    closeConnection(conn)
    return json.dumps(data)

@app.route('/G1/<string:genre>', methods = ["GET"])
def Genre1(genre):
    conn = openConnection()
    cur = conn.cursor()
    cur.execute(f"""SELECT movies.m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND genre.g_gname = ?
        """,[genre])
    results = cur.fetchall()
    #print(results)
    data =[]
    for result in results:
        #print(result)
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'").strip('"')
        #print(result)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
        genre.g_gid = movie_genre.mg_gid AND m_title = "{result}";"""
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        data += results
    #print(data)
    closeConnection(conn)
    return json.dumps(data)

@app.route('/NaG2/<string:name>/<string:genre>/<string:genre2>', methods = ["GET"])
def getNameAndGenre2(name,genre,genre2):
    conn = openConnection()
    cur = conn.cursor()
    cur.execute(f"""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND m_title LIKE '%{name}%' AND g_gname ='{genre}'
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND m_title LIKE '%{name}%' AND g_gname = '{genre2}'
        """)
    results = cur.fetchall()
    #print(results)
    data =[]
    for result in results:
        #print(result)
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'")
        #print(result)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
        genre.g_gid = movie_genre.mg_gid AND m_title = '{result}';"""
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        data += results
    #print(data)
    closeConnection(conn)
    return json.dumps(data)

@app.route('/G2/<string:genre>/<string:genre2>', methods = ["GET"])
def Genre2(genre,genre2):
    conn = openConnection()
    cur = conn.cursor()
    cur.execute("""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?""", [genre, genre2])
    results = cur.fetchall()
    #print(results)
    data =[]
    for result in results:
        #print(result)
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'").strip('"')
        #print(result)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
        genre.g_gid = movie_genre.mg_gid AND m_title = "{result}";"""
        cur.execute(sql)
        results = cur.fetchall()
        print(results)
        data += results
    #print(data)
    closeConnection(conn)
    return json.dumps(data)


@app.route('/NaG3/<string:name>/<string:genre>/<string:genre2>/<string:genre3>', methods = ["GET"])
def getNameAndGenre3(name,genre,genre2,genre3):
    conn = openConnection()
    cur = conn.cursor()
    cur.execute(f"""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND m_title LIKE '%{name}%' AND g_gname ='{genre}'
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND m_title LIKE '%{name}%' AND g_gname = '{genre2}'
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND m_title LIKE '%{name}%' AND g_gname = '{genre3}'""")
    results = cur.fetchall()
    #print(results)
    data =[]
    for result in results:
        print(result)
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'")
        print(result)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
        genre.g_gid = movie_genre.mg_gid AND m_title = '{result}';"""
        cur.execute(sql)
        results = cur.fetchall()
        print(results)
        data += results
    #print(data)
    closeConnection(conn)
    return json.dumps(data)

@app.route('/G3/<string:genre>/<string:genre2>/<string:genre3>', methods = ["GET"])
def Genre3(genre,genre2,genre3):
    conn = openConnection()
    cur = conn.cursor()
    cur.execute("""SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?
        INTERSECT
        SELECT m_title FROM movies, movie_genre, genre
        WHERE movies.m_mid = movie_genre.mg_mid AND genre.g_gid = movie_genre.mg_gid AND g_gname = ?""", [genre, genre2, genre3])
    results = cur.fetchall()
    #print(results)
    data =[]
    for result in results:
        #print(result)
        result = str(result)
        result = result.strip("(").strip(")").strip(",").strip("'").strip('"')
        #print(result)
        sql = f"""SELECT m_title, ad_ratings, da_releaseyear, du_runtime, g_gname FROM movies,adult,dates,duration,genre,movie_genre 
        WHERE m_adid = ad_adid AND m_duid = du_duid AND m_daid = da_daid AND movie_genre.mg_mid = movies.m_mid AND
        genre.g_gid = movie_genre.mg_gid AND m_title = "{result}";"""
        cur.execute(sql)
        results = cur.fetchall()
        #print(results)
        data += results
    #print(data)
    closeConnection(conn)
    return json.dumps(data)

@app.route('/addCurrentMovie/<string:name>/<row>', methods = ["POST"])
def addCurrentMovie(name,row):
    print("before check")
    checker = CheckList(name,row)
    if checker == 0:
        conn = openConnection()
        cur = conn.cursor()
        sql = f"""SELECT m_mid FROM movies WHERE m_title LIKE '%{name}%';"""
        cur.execute(sql)
        results = cur.fetchall()
        print(results)
        key = 1
        row = int(row)
        for result in results:
            print(result)
            print(key)
            print(row)
            if key == row:
                print("got in!")
                result = str(result)
                result = result.strip("(").strip(")").strip(",").strip("'")
                cur.execute("""INSERT INTO user(u_mid,u_watching,u_watched,u_towatch) VALUES(?,0,1,0)""",[result])
                conn.execute("COMMIT")
                break
            key = key + 1
        closeConnection(conn)
        return json.dumps({"status": 200})
    else:
        return json.dumps({"Error":0})


if __name__ == '__main__':
    app.run(debug=True)