import MySQLdb
from database import config


class Database:
    db = None

    def __init__(self):
        try:
            self.db = MySQLdb.connect(user=config.getUser(), passwd=config.getPass(), db="bitconnect")
        except Exception as e:
            print(e)
            print("Unexcepted error while connecting to the database.")

    def execute_query(self, query, params):
        c = self.db.cursor()
        c.execute("" + query + "", params)
        self.db.commit()
        return c

    def query(self, query, params):
        c = self.execute_query(query, params)
        return c.fetchone()

    def query_all(self, query, params):
        c = self.execute_query(query, params)
        return c.fetchall()
