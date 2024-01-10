#!/usr/bin/env python3

# class CashRegister:

#     def __init__(self, discount=0):
#         self.items = []
#         self.total = 0
#         self.discount = discount
#         self.last_transaction_amount = 0

#     def add_item(self, title, price, quantity=1):
#         item = {'title': title, 'price': price, 'quantity': quantity}
#         self.items.extend([item.copy() for _ in range(quantity)])
#         self.total += price * quantity
#         self.last_transaction_amount = price * quantity
#         return [item['title'] for _ in range(quantity)]

#     def calculate_discount(self):
#         if self.discount > 0:
#             return (self.discount / 100.0) * self.total
#         else:
#             return 0

#     def apply_discount(self):
#         discount_amount = self.calculate_discount()
#         if discount_amount > 0:
#             self.total -= discount_amount
#             self.total = int(self.total)  # Convert total to integer
#             print(f"After the discount, the total comes to ${self.total}.")
#         else:
#             print("There is no discount to apply.")

#     def void_last_transaction(self):
#         if self.items:
#             removed_item = self.items.pop()
#             self.total -= removed_item['price'] * removed_item['quantity']
#             self.last_transaction_amount = 0
#         else:
#             print("No transaction to void.")

class CashRegister:

    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.discount = discount
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)

        self.total += price * quantity
        self.last_transaction_amount = price * quantity

    
    def calculate_discount(self):
        if self.discount > 0:
            return (self.discount / 100.0) * self.total
        else:
            return 0

    def apply_discount(self):
        discount_amount = self.calculate_discount()
        if discount_amount > 0:
            self.total -= discount_amount
            self.total = int(self.total)  # Convert total to integer
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            removed_item_title = self.items.pop()
            for item in reversed(self.items):
                if item['title'] == removed_item_title:
                    price = item['price']
                    quantity = item['quantity']
                    break
                self.total -= price * quantity
                self.last_transaction_amount = 0
        else:
            print("No transaction to void.")




