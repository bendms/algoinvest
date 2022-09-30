import csv


list_of_actions_as_dict = []
actions_name = []
actions_value = []
actions_profit = []
compteur = 0
compteur_2 = 0
best_rentability = 0
best_choice = []
invest = 0
wallet = 500

def dynamic_function(wallet, list_of_actions_as_dict):
    compteur = 0
    compteur_2 = 0
    matrice = [[0 for x in range(wallet + 1)] for x in range(len(list_of_actions_as_dict) + 1)]
    
    for i in range(1, len(list_of_actions_as_dict) + 1):
        """for each action in the list of actions"""
        for w in range(1, wallet + 1):
            """for each wallet value"""
            print(list_of_actions_as_dict[i - 1]["value"])
            if list_of_actions_as_dict[i-1]['value'] <= w:
                """if the value of the action is less than the wallet value"""
                # print(max(list_of_actions_as_dict[i-1]["sellable_value"] + matrice[i-1][w - list_of_actions_as_dict[i-1]['value']], matrice[i-1][w]))
                matrice[i][w] = max(list_of_actions_as_dict[i-1]["sellable_value"] + matrice[i-1][w - list_of_actions_as_dict[i-1]['value']], matrice[i-1][w])
            else:
                """if the value of the action is more than the wallet value"""
                matrice[i][w] = matrice[i-1][w]

        
        w = wallet
        n = len(list_of_actions_as_dict)
        list_of_actions_to_buy = []
        
    while w >= 0 and n >= 0:
        """ while the wallet is more than 0 and the list of actions is more than 0"""
        e = list_of_actions_as_dict[n - 1]
        if matrice[n][w] == matrice[n - 1][w - e["value"]] + e["sellable_value"]:
            print("condition if ok")
            """if the value of the action is less than the w value"""
            list_of_actions_to_buy.append(e)
            w -= e["value"]
        
        n -= 1
    return matrice[-1][-1], list_of_actions_to_buy

with open ("dataset1_PythonP7.csv", 'r') as csvfile:
    """open the csv file and read it"""
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        """for each row in the csv file, add the name of the action in the list actions_name"""
        actions_name.append(row[0])
        actions_value.append(row[1])
        actions_profit.append(row[2])
for action in actions_value:
    """transform the list of string into a list of float"""
    action = float(action)
for action in actions_profit:
    """transform the list of string into a list of float"""
    action = float(action)
for i in range(len(actions_name)):
    """create a list of dictionary with actions name, value and profit"""
    # print([int(float(action)*100) for action in actions_profit])
    list_of_actions_as_dict.append({"name": actions_name[i], "value": float(actions_value[i]), "profit": float(actions_profit[i])/100})
for action in list_of_actions_as_dict:
    if action["value"] <= 0 or action["profit"] < 1:
        """if the value of the action is 0 or the profit is more than 1, delete the action"""
        list_of_actions_as_dict.remove(action)
list_of_actions_as_dict.sort(key=lambda x: x["value"], reverse=True)
[print(action["value"]) for action in list_of_actions_as_dict]
for i in range(len(list_of_actions_as_dict)):
    """calculate the sellable value of each action and add in the dictionary"""
    sellable_value = list_of_actions_as_dict[i]["value"] * (1+list_of_actions_as_dict[i]["profit"])
    list_of_actions_as_dict[i]["sellable_value"] = sellable_value
dynamic_function(wallet, list_of_actions_as_dict)
# print("The best rentability is", best_rentability, "and the best choice is", best_choice)
# matrice = [[0 for x in range(5)] for x in range(4)]
# print(matrice)


