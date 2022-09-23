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

