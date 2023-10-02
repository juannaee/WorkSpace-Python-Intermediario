import string
import random


class Order_number:
    def generate_order_number():
        allowed_characters = string.ascii_letters + string.digits
        order_number = "".join(random.choice(allowed_characters) for _ in range(5))
        order_number += order_number[:5] + "-" + order_number[5:]
        order_number += "1"
        return order_number
