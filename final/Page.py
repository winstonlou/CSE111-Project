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
def getGenre(name):
    conn = openConnection()
    cur = conn.cursor()
    sql = f"""SELECT m_title FROM movies WHERE m_title LIKE '{name}%';"""
    cur.execute(sql)
    results = cur.fetchall()
    closeConnection(conn)    
    return results



if __name__ == '__main__':
    app.run(debug=True)