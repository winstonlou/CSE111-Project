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
    


if __name__ == '__main__':
    app.run(debug=True)