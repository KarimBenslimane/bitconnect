from .database import Database


class Connection:
    TYPE_SELECT = 'select'
    TYPE_INSERT = 'insert'
    TYPE_DELETE = 'delete'

    tablename = None
    database = None

    def __init__(self, tablename):
        self.database = Database()
        self.tablename = tablename

    def query(self, query_type, data):
        """
        Query the database and use fetchone
        :param query_type:
        :param data:
        :return list:
        """
        return self.database.query(query=self.get_query_string(query_type, data), params=self.get_params(data))

    def query_all(self, query_type, data):
        """
        Query the database and use fetchall
        :param query_type:
        :param data:
        :return list:
        """
        return self.database.query_all(query=self.get_query_string(query_type, data), params=self.get_params(data))

    def query_last_insert_id(self):
        """
        Retrieve the last created ID
        :return string:
        """
        return self.database.query(query="SELECT LAST_INSERT_ID();", params=[])

    def get_query_string(self, query_type, data):
        """
        Create the string for a given query type
        :param query_type:
        :param data:
        :return string:
        """
        query = ""
        if query_type == self.TYPE_SELECT:
            query = self.add_select_string(data)
        elif query_type == self.TYPE_INSERT:
            query = self.add_insert_string(data)
        elif query_type == self.TYPE_DELETE:
            query = self.add_delete_string(data)
        return query

    def add_select_string(self, data):
        """
        Create a select string with given data for where clause
        :param data:
        :return string:
        """
        string = "SELECT * FROM " + self.tablename
        return self.finish_with_where(string, data)

    def add_where_string(self, data):
        """
        Create a where clause for a query string
        :param data:
        :return string:
        """
        string = " WHERE "
        for key, value in data.items():
            if list(data.keys()).index(key) != 0:
                string += " AND "
            string += (key + " = %s")
        return string

    def add_insert_string(self, data):
        """
        Create an insert string with given data
        :param data:
        :return string:
        """
        string = "INSERT INTO " + self.tablename + " ("
        for key, value in data.items():
            if list(data.keys()).index(key) != 0:
                string += ", "
            string += key
        string += ") values("
        for key, value in data.items():
            if list(data.keys()).index(key) != 0:
                string += ", "
            string += "%s"
        string += ");"
        return string

    def add_delete_string(self, data):
        """
        Create a delete string with given data
        :param data:
        :return string:
        """
        string = "DELETE FROM " + self.tablename
        return self.finish_with_where(string, data)

    def finish_with_where(self, string, data):
        """
        Check if a where clause is needed, add semiclon to wrap up query
        :param string:
        :param data:
        :return string: 
        """
        if len(data) > 0:
            string += self.add_where_string(data)
        string += ";"
        return string

    def get_params(self, data):
        """
        Create params list for the query string
        :param data:
        :return []:
        """
        params = []
        if data:
            for key, value in data.items():
                params.append(value)
        return params
