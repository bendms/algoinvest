import csv


list_of_actions_as_dict = []
actions_name = []
actions_value = []
actions_profit = []
actions_sellable_value = []
rentability = 0
best_rentability = 0
best_choice = []
invest = 0
wallet = 50000

def which_actions_should_I_buy(list_of_actions_as_dict, wallet):
    invest = 0
    compteur = 0
    list_of_actions_to_buy = []
    for action in list_of_actions_as_dict:
        roi = ((action['sellable_value'] - action['value']) - action['value'])/ action['value']
        action['roi'] = roi
        print("compteur :", compteur)
        compteur += 1
    list_of_actions_as_dict.sort(key=lambda x: x['roi'], reverse=True)
    [print(action) for action in list_of_actions_as_dict]
    for action in list_of_actions_as_dict:
        if wallet >= action['value']:
            wallet -= action['value']
            invest += action['value']
            print(action['name'], action['value'])
            print(invest)
            list_of_actions_to_buy.append(action)
            print("compteur :", compteur)
            compteur += 1
    return list_of_actions_to_buy
            


with open ("dataset1_Python+P7.csv", 'r') as csvfile:
    """open the csv file and read it"""
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        if float(row[1]) > float(0) and float(row[2]) > float(1):
            """for each row in the csv file, add the name of the action in the list actions_name"""
            actions_name.append(row[0])
            row[1] = float(row[1])
            row[1] = row[1] * 100
            row[1] = int(row[1])
            actions_value.append(row[1])
            row[2] = float(row[2])
            row[2] = row[2] * 100
            row[2] = int(row[2])
            actions_profit.append(row[2])
            sellable_value = int(row[1]) * (1+int(row[2]))
            actions_sellable_value.append(sellable_value)
for i in range(len(actions_name)):
    """create a list of dictionary with actions name, value and profit"""
    list_of_actions_as_dict.append({"name": actions_name[i], "value": actions_value[i], "profit": actions_profit[i], "sellable_value": actions_sellable_value[i]})
    print(list_of_actions_as_dict[i])
list_of_actions_to_buy = which_actions_should_I_buy(list_of_actions_as_dict, wallet)
wallet = wallet / 100

for action in list_of_actions_to_buy:
    action["value"] = action["value"] / 100
    action["profit"] = action["profit"] / 100
    action["sellable_value"] = action["value"] * (1 + action["profit"]/100)
    wallet -= action["value"]
    rentability += action["sellable_value"] - action["value"]
    print(action, "wallet", 500-wallet, "rentability", rentability)



