class Order:
    ORDER_ID = 'order_id'
    CREATED_AT = 'created_at'
    STATUS = ' '
    PAIR = 'pair'
    TYPE = 'type'
    SIDE = 'side'
    PRICE = 'price'
    AMOUNT = 'amount'
    TOTAL = 'total'
    FEE = 'fee'
    BOT_ID = 'bot_id'

    TYPE_SELL = 0
    TYPE_BUY = 1

    STATUS_OPEN = 0
    STATUS_CLOSED = 1
    STATUS_CANCELED = 2

    order_id = ''
    created_at = ''
    status = ''
    pair = ''
    type = ''
    side = ''
    price = ''
    amount = ''
    total = ''
    fee = ''
    bot_id = ''

    def set_id(self, order_id):
        self.order_id = order_id
        return self

    def set_created_at(self, created_at):
        self.created_at = created_at
        return self

    def set_status(self, status):
        self.status = status
        return self

    def set_pair(self, pair):
        self.pair = pair
        return self

    def set_type(self, type):
        self.type = type
        return self

    def set_side(self, side):
        self.side = side
        return self

    def set_price(self, price):
        self.price = price
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_total(self, total):
        self.total = total
        return self

    def set_fee(self, fee):
        self.fee = fee
        return self

    def set_bot_id(self, bot_id):
        self.bot_id = bot_id
        return self

    def get_id(self):
        return self.order_id

    def get_created_at(self):
        return self.created_at

    def get_status(self):
        return self.status

    def get_pair(self):
        return self.pair

    def get_type(self):
        return self.type

    def get_side(self):
        return self.side

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount

    def get_total(self):
        return self.total

    def get_fee(self):
        return self.fee

    def get_bot_id(self):
        return self.bot_id
