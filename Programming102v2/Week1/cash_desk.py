class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
        self.cash = 0

    def take_money(self, new_money):
        for new_coin in new_money:
            self.money[new_coin] += new_money[new_coin]

    def total(self):
        total_money = 0
        for money in self.money:
            total_money += money * self.money[money]

        return total_money

    def can_withdraw_money(self, amount):
        pass

my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cash_desk.total())
my_cash_desk.can_withdraw_money(30)  # False
my_cash_desk.can_withdraw_money(70)  # True
