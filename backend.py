import sqlite3

def connect():
    conn=sqlite3.connect("quotes.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, quote text, movie text, character text, actor text)")
    conn.commit()
    conn.close()

def insert(quote, movie, character, actor):
    conn=sqlite3.connect("quotes.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO quotes VALUES (NULL,?,?,?,?)",(quote, movie, character, actor))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("quotes.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM quotes")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(quote="", movie="", character="", actor=""):
    conn=sqlite3.connect("quotes.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM quotes WHERE quote=? OR movie=? OR character=? OR actor=?", (quote, movie, character, actor))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("quotes.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM quotes WHERE id=?", (id,))
    conn.commit()
    conn.close()

def edit(id, quote, movie, character, actor):
    conn=sqlite3.connect("quotes.db")
    cur=conn.cursor()
    cur.execute("UPDATE quotes SET quote=?, movie=?, character=?, actor=? WHERE id=?",(quote, movie, character, actor, id))
    conn.commit()
    conn.close()


connect()
