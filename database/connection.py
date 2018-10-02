from .database import Database


class Connection:
    TYPE_SELECT = 'select'
    TYPE_INSERT = 'insert'
    TYPE_DELETE = 'delete'
    TYPE_UPDATE = 'update'

    tablename = None
    database = None

    def __init__(self, tablename):
        self.database = Database()
        self.tablename = tablename

    def query(self, query_type, data, params):
        """
        Query the database and use fetchone
        :param params:
        :param query_type:
        :param data:
        :return list:
        """
        return self.database.query(query=self.get_query_string(query_type, data), params=params)

    def query_all(self, query_type, data, params):
        """
        Query the database and use fetchall
        :param query_type:
        :param data:
        :return list:
        """
        return self.database.query_all(query=self.get_query_string(query_type, data), params=params)

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
        elif query_type == self.TYPE_UPDATE:
            query = self.add_update_string(data)
        return query

    def add_select_string(self, data):
        """
        Create a select string with given data for where clause
        :param data:
        :return string:
        """
        string = "SELECT * FROM " + self.tablename
        return self.finish_with_where(string, data)

    def add_where_string(self, keys):
        """
        Create a where clause for a query string
        :param keys:
        :return string:
        """
        string = " WHERE "
        for key in keys:
            if keys.index(key) != 0:
                string += " AND "
            string += (key + " = %s")
        return string

    def add_insert_string(self, keys):
        """
        Create an insert string with given data
        :param keys:
        :return string:
        """
        string = "INSERT INTO " + self.tablename + " ("
        for key in keys:
            if keys.index(key) != 0:
                string += ", "
            string += key
        string += ") values("
        for key in keys:
            if keys.index(key) != 0:
                string += ", "
            string += "%s"
        string += ");"
        return string

    def add_delete_string(self, keys):
        """
        Create a delete string with given data
        :param keys:
        :return string:
        """
        string = "DELETE FROM " + self.tablename
        return self.finish_with_where(string, keys)

    def add_update_string(self, data):
        """
        Create an update string with given data
        :param dict data:
        :return:
        """
        if "identifier" not in list(data.keys()) and len(data["identifier"] != 1):
            raise Exception("No valid identifier found in update.")
        string = "UPDATE " + self.tablename + " SET "
        values = data["values"]
        identifier = data["identifier"]

        for key in values:
            string += (key + "= %s")
            if values.index(key) != (len(values)-1):
                string += ", "
        string += " WHERE " + identifier[0] + " = %s;"
        return string

    def finish_with_where(self, string, data):
        """
        Check if a where clause is needed, add semicolon to wrap up query
        :param string:
        :param data:
        :return string:
        """
        if len(data) > 0:
            string += self.add_where_string(data)
        string += ";"
        return string
