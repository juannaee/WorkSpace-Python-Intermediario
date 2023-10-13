import string
import random


class Order_number:
    @classmethod
    def generate_order_number(cls):
        allowed_characters = string.ascii_letters + string.digits
        order_number = "".join(random.choice(allowed_characters) for _ in range(11))
        order_number += order_number[:11] + "-" + order_number[11:]
        order_number += "1"
        return order_number


class Sale_id:
    @classmethod
    def generate_id_number(cls):
        number_id = "".join([str(random.randint(0, 9)) for _ in range(11)])
        return number_id
