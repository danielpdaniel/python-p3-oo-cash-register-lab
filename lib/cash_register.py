#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.transactions = []

  def add_item(self, title='', price=0, quantity=1):
    self.transactions.append({"title": title, "price": price, "quantity": quantity})
    for i in range(0, quantity):
      self.total += price
      self.items.append(title)


  def apply_discount(self):
    discount_total = (self.discount / 100) * self.total
    self.total = int(self.total - discount_total)
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    transaction = self.transactions[len(self.transactions) - 1]
    print(transaction)
    for i in range(0, transaction["quantity"]):
      self.total -= transaction["price"]

    self.transactions.pop()
