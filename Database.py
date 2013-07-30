
import sqlite3

class Database:
    def __init__(self):
        self.filename = 'db/database.sqllite'
        self.ver = 1
        self.conn = sqlite3.connect(self.filename)
        # next line avoids the 
        # OperationalError: Could not decode to UTF-8 column 'right_threshold_result' with text...
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()

    def run(self, command, list = ()):
        print self.filename
        self.cursor.close()
        self.cursor = self.conn.cursor()
        print "Database.run: " + command
        print list
        result = self.cursor.execute(command, list)
        self.conn.commit()
        print 'Returning result\n\n\n'
        return result



