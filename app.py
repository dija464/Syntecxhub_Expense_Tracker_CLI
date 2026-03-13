from flask import Flask, render_template, request, jsonify, redirect
import sqlite3
import pandas as pd

app = Flask(__name__)

def connect():
    return sqlite3.connect("database.db")

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/registerpage")
def register_page():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/register", methods=["POST"])
def register():

    data=request.json

    conn=connect()
    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(email TEXT,password TEXT)")
    cur.execute("INSERT INTO users VALUES (?,?)",(data["email"],data["password"]))

    conn.commit()
    conn.close()

    return jsonify({"message":"registered"})


@app.route("/login",methods=["POST"])
def login():

    data=request.json

    conn=connect()
    cur=conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=? AND password=?",
                (data["email"],data["password"]))

    user=cur.fetchone()

    conn.close()

    if user:
        return jsonify({"status":"success"})
    else:
        return jsonify({"status":"fail"})


@app.route("/add",methods=["POST"])
def add():

    data=request.json

    conn=connect()
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions
    (date TEXT,type TEXT,category TEXT,amount REAL)
    """)

    cur.execute("INSERT INTO transactions VALUES (?,?,?,?)",
                (data["date"],data["type"],data["category"],data["amount"]))

    conn.commit()
    conn.close()

    return jsonify({"message":"added"})


@app.route("/transactions")
def transactions():

    conn=connect()

    df=pd.read_sql_query("SELECT * FROM transactions",conn)

    conn.close()

    return df.to_json(orient="records")


@app.route("/export")
def export():

    conn=connect()

    df=pd.read_sql_query("SELECT * FROM transactions",conn)

    df.to_excel("expenses.xlsx",index=False)

    return jsonify({"message":"excel exported"})


app.run(debug=True)