from statistics import mean


class Order():

    def __init__(self,customer_name, order_date, menu_item, quantity):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.menu_item = menu_item

        