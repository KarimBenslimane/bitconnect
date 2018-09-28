from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .exchange import Exchange


class ExchangeRepository(RepositoryInterface):
    tablename = 'exchanges'

    def __init__(self):
        super().__init__(self.tablename)

    def get(self, id):
        """
        Retrieve an exchange from database by id
        :param id:
        :return Exchange:
        """
        exchange_data = self.connection.query(Connection.TYPE_SELECT, {Exchange.EXCHANGE_ID: id})
        return self.create_model(exchange_data)

    def getList(self, search_criteria):
        """
        Retrieve an exchange from database by searchCriteria
        :param search_criteria:
        :return Exchange[]:
        """
        exchange_data = self.connection.query_all(Connection.TYPE_SELECT, search_criteria)
        models = []
        if exchange_data:
            for exchange in exchange_data:
                model = self.create_model(exchange)
                models.append(model)
        return models

    def create(self, exchangename, public_key, private_key, user_id, uid, pw):
        """
        Create an exchange in database and retrieve the Exchange
        :param exchangename:
        :param public_key:
        :param private_key:
        :return Exchange:
        """
        self.connection.query(
            Connection.TYPE_INSERT,
            {
                Exchange.EXCHANGE_NAME: exchangename,
                Exchange.EXCHANGE_PUBLIC: public_key,
                Exchange.EXCHANGE_PRIVATE: private_key,
                Exchange.EXCHANGE_USER: user_id,
                Exchange.EXCHANGE_UID: uid,
                Exchange.EXCHANGE_PW: pw
            }
        )
        # TODO: maybe replace last_insert_id with something specific
        # TODO: when many people will use the system to avoid wrong ids return
        return self.get(self.connection.query_last_insert_id())

    def create_model(self, data):
        """
        Create an Exchange model from database data (id, exchangename, public, private, user_id)
        :param data:
        :return Bot:
        """
        model = Exchange()
        model.set_id(data[0])
        model.set_name(data[1])
        model.set_public(data[2])
        model.set_private(data[3])
        model.set_user_id(data[4])
        model.set_uid(data[5])
        model.set_pw(data[6])
        return model

    def delete(self, exchange_id):
        """
        Delete an exchange from the database
        :param exchange_id:
        """
        self.connection.query(
            Connection.TYPE_DELETE,
            {
                Exchange.EXCHANGE_ID: exchange_id
            }
        )
