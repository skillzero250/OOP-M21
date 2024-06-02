import copy

class OrderPrototype:
    def __init__(self):
        self.order_number = None
        self.products = []
        self.total_price = 0.0

    def clone(self):
        return copy.deepcopy(self)

class Order(OrderPrototype):
    def __init__(self, prototype):
        super().__init__()
        self.__dict__ = prototype.__dict__.copy()

# Создайте прототип заказа
prototype_order = OrderPrototype()
prototype_order.order_number = 1001
prototype_order.products = ["Product A", "Product B", "Product C"]
prototype_order.total_price = 150.00

# Создайте новый заказ на основе прототипа
order1 = Order(prototype_order.clone())
order1.order_number = 1002  # Change the order number
order1.total_price = 200.00  # Change the total price

# Создайте еще один новый заказ на основе прототипа
order2 = Order(prototype_order.clone())
order2.order_number = 1003  # Change the order number
order2.products.append("Product D")  # Add a new product

# Распечатайте информацию о заказе
print("Order 1:")
print("Order Number:", order1.order_number)
print("Products:", order1.products)
print("Total Price:", order1.total_price)

print("\nOrder 2:")
print("Order Number:", order2.order_number)
print("Products:", order2.products)
print("Total Price:", order2.total_price)