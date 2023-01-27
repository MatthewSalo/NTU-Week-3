import datetime

# Creating a class called 'Invoice'
import datetime

class Invoice:
    """
    The Invoice class represents an invoice for items sold by a bakery. It includes the following information:
    item type, quantity of item, a price per item and the date the order should be delivered.
    """
    def __init__(self, item_type, quantity, price_per_item, delivery_date):
        self.item_type = item_type
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.delivery_date = delivery_date

    def calculate_total_cost(self):
        # Calculates and returns the total cost of the order
        return self.quantity * self.price_per_item

    def get_invoice(self):
        # Calculates and returns the invoice amount
        return self.calculate_total_cost()

    def update_quantity(self, quantity):
        # raises ValueError if quantity is less than 0
        if quantity < 0:
            raise ValueError("Quantity must be a positive number.")
        self.quantity = quantity # returns updated quantity

    def get_item(self):
        # Returns the name of the item being ordered
        return self.item_type

    def get_quantity(self):
        # Returns the quantity of the item being ordered
        return self.quantity

    def __str__(self):
        # Returns a string representation of the invoice
        return f"Invoice for {self.quantity} {self.item_type} at {self.price_per_item} per item. " \
               f"Total cost: {self.calculate_total_cost()}. Delivery date: {self.delivery_date}."


def invoice_test():
    # Demonstrates the capabilities of the Invoice class
    delivery_date = datetime.datetime(2023, 3, 5)
    invoice = Invoice("Croissants", 50, 2.5, delivery_date)
    print(invoice)  # Prints invoice
    print("Invoice amount:", invoice.get_invoice())  # Prints invoice amount
    invoice.update_quantity(60)
    print("New quantity:", invoice.get_quantity())  # prints new invoice quantitiy
    print("Item:", invoice.get_item())  # prints item
    invoice.update_quantity(-1)  # Will demonstrate ValueError

invoice_test()


