#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def get_name(self):
        return self.name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True

        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount, to_category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {to_category.get_name()}"})
            to_category.deposit(amount, f"Transfer from {self.get_name()}")
            return True

        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


    def get_withdraws(self):
        withdraws = 0
        for item in self.ledger:
            if item["amount"] < 0:
                withdraws += -item["amount"]

        return withdraws

    def __str__(self):
        print_text = self.get_name().center(30, '*') + '\n'
        total = 0
        for item in self.ledger:
            amount = item["amount"]
            total += amount
            description = item["description"]

            print_text += description.ljust(23)[:23] + f"{amount:.2f}".rjust(7) + '\n'

        print_text += f"Total: {total:.2f}"

        return print_text


def create_spend_chart(categories):
    n_categories = len(categories)
    max_lenght = max([len(category.get_name()) for category in categories])

    list_categories = [category.get_name().ljust(max_lenght) for category in categories]

    list_categories_perc = [category.get_withdraws() for category in categories]
    total_withdraws = sum(list_categories_perc)
    list_categories_perc = [cat_perc/total_withdraws * 100 for cat_perc in list_categories_perc]

    plot = "Percentage spent by category\n"
    y_axis_space = 4
    for percentage in range(100, -1, -10):
        plot += f"{percentage}|".rjust(y_axis_space)
        for cat_perc in list_categories_perc:
            if cat_perc >= percentage:
                plot += f" o "
            else:
                plot += "   "
        plot += " \n"
    plot += ' ' * y_axis_space + '-' * (n_categories * 3 + 1) + '\n'

    for i in range(max_lenght):
        plot += ' ' * 3
        for category in list_categories:
            plot += f'  {category[i]}'
        plot += '  \n'
    return plot[:-1]