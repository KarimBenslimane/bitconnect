from abc import ABCMeta, abstractmethod
from database.connection import Connection


class RepositoryInterface:
    __metaclass__ = ABCMeta
    connection = None
    tablename = None

    def __init__(self, tablename):
        self.connection = Connection(tablename=tablename)

    @abstractmethod
    def get(self, id):
        return

    @abstractmethod
    def getList(self, searchCriteria):
        return

    @abstractmethod
    def save(self, abstractobject):
        return
