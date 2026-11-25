from flask import Flask,render_template
import sqlite3

app=Flask(__name__)

@app.route('/')
def home():
    conn=sqlite3.connect('../database/security_events.db')
    rows=conn.execute('select * from events order by id desc limit 10').fetchall()
    return render_template('dashboard.html',events=rows)

app.run(debug=True)