from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .order import Order


class OrderRepository(RepositoryInterface):
    tablename = 'orders'

    def __init__(self):
        super().__init__(self.tablename)

    def get(self, id):
        """
        Retrieve an order from database by id
        :param id:
        :return Order:
        """
        order_data = self.connection.query(Connection.TYPE_SELECT, [Order.ORDER_ID], [id])
        return self.create_model(order_data)

    def getList(self, search_criteria):
        """
        Retrieve an order from database by searchCriteria
        :param search_criteria:
        :return Order[]:
        """
        keys = []
        values = []
        for key, value in search_criteria.items():
            keys.append(key)
            values.append(value)
        order_data = self.connection.query_all(Connection.TYPE_SELECT, keys, values)
        models = []
        if order_data:
            for exchange in order_data:
                model = self.create_model(exchange)
                models.append(model)
        return models

    def create(self, status, pair, order_type, side, price, amount, total, fee, bot_id):
        """
        Create an exchange in database and retrieve the Exchange
        :param bot_id:
        :param fee:
        :param total:
        :param amount:
        :param price:
        :param side:
        :param order_type:
        :param pair:
        :param status:
        :return Exchange:
        """
        self.connection.query(
            Connection.TYPE_INSERT,
            [
                Order.STATUS,
                Order.PAIR,
                Order.TYPE,
                Order.SIDE,
                Order.PRICE,
                Order.AMOUNT,
                Order.TOTAL,
                Order.FEE,
                Order.BOT_ID
            ],
            [
                status,
                pair,
                order_type,
                side,
                price,
                amount,
                total,
                fee,
                bot_id
            ]
        )
        # TODO: maybe replace last_insert_id with something specific
        # TODO: when many people will use the system to avoid wrong ids return
        return self.get(self.connection.query_last_insert_id())

    def create_model(self, data):
        """
        Create an Order model from database data
        :param data:
        :return Order:
        """
        model = Order()
        model.set_id(data[0])
        model.set_created_at(data[1])
        model.set_status(data[2])
        model.set_pair(data[3])
        model.set_type(data[4])
        model.set_side(data[5])
        model.set_price(data[6])
        model.set_amount(data[6])
        model.set_total(data[6])
        model.set_price(data[6])
        model.set_fee(data[6])
        model.set_bot_id(data[6])
        return model

    def delete(self, order_id):
        """
        Delete an order from the database
        :param order_id:
        """
        self.connection.query(
            Connection.TYPE_DELETE,
            [Order.ORDER_ID],
            [order_id]
        )
