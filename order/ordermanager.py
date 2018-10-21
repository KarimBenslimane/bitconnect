from .orderrepository import OrderRepository


class OrderManager:
    order_repo = None

    def __init__(self):
        self.order_repo = OrderRepository()

    def get_order(self, id):
        """
        Retrieve an exchange from database by id
        :param id:
        :return Exchange:
        """
        return self.order_repo.get(id)

    def get_orders(self, search_criteria):
        """
        Retrieve orders from database
        :return Order[]:
        """
        return self.order_repo.getList(search_criteria=search_criteria)

    def create_order(self, status, pair, order_type, side, price, amount, total, fee, bot_id):
        """
        Create a new order in the database
        :param status:
        :return Order:
        """
        if not status or not pair or not order_type or not side or not bot_id:
            raise Exception("Not all data given for creating order")
        else:
            return self.order_repo.create(status, pair, order_type, side, price, amount, total, fee, bot_id)

    def delete_order(self, order_id):
        """
        Delete an existing order from the database
        :param order_id:
        :return:
        """
        if order_id:
            self.order_repo.delete(order_id=order_id)
        else:
            raise Exception("No order_id found for deleting order.")
