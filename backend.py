import sqlite3

class Database:
    
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, quote text, movie text, character text, actor text)")
        self.conn.commit()

    def insert(self, quote, movie, character, actor):
        self.cur.execute("INSERT INTO quotes VALUES (NULL,?,?,?,?)",(quote, movie, character, actor))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM quotes")
        rows=self.cur.fetchall()
        return rows


    def search(self, quote="", movie="", character="", actor=""):
        self.cur.execute("SELECT * FROM quotes WHERE quote=? OR movie=? OR character=? OR actor=?", (quote, movie, character, actor))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM quotes WHERE id=?", (id,))
        self.conn.commit()

    def edit(self, id, quote, movie, character, actor):
        self.cur.execute("UPDATE quotes SET quote=?, movie=?, character=?, actor=? WHERE id=?",(quote, movie, character, actor, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close