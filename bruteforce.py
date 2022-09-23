# ## Bruteforce solution to the algoinvest problem
# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount
    
#     def buy(self, price):
#         self.amount -= price

# class Action:
#     def __init__(self, action, amount, profit, selling_price):
#         self.action = action
#         self.amount = amount
#         self.profit = profit
#         self.selling_price = selling_price

#     def __str__(self):
#         return f"{self.action} {self.amount}"
    
#     def profit_calc_after_2_years(self):
#         self.selling_price = ((self.profit * self.amount)-self.amount)/self.amount*100
#         return self.selling_price


# wallet = 500
# actions = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]

# def bruteforce():
#     while wallet > 0:
#         for action in actions:
#             if action < wallet:
#                 print(Action("buy", action, action*0.1, action))
#                 wallet.buy(action)
#                 print(wallet.amount)
#             else:
#                 print("not enough money")
                
# bruteforce()


from itertools import combinations
wallet = 500
actions_list = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
list_combinations = list()
compteur = 0
for n in range(len(actions_list) + 1):
    list_combinations += list(combinations(actions_list, n))
for i in list_combinations:
    if sum(i) < wallet:
        total_of_investments = sum(i)
        print(i, total_of_investments)
        compteur += 1
        print(compteur)

