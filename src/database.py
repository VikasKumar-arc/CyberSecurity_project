import sqlite3
from datetime import datetime
from src.config import DB_PATH

def initialize_database():
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY,
    time TEXT,
    source TEXT,
    destination TEXT,
    protocol TEXT,
    severity TEXT,
    message TEXT)''')
    conn.commit()
    conn.close()

def save_event(data):
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("INSERT INTO events VALUES(NULL,?,?,?,?,?,?)",
    (datetime.now(),data['source'],data['destination'],data['protocol'],data['severity'],data['message']))
    conn.commit()
    conn.close()