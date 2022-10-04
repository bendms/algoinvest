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

def dynamic_function(wallet, list_of_actions_as_dict):
    matrice = [[0 for x in range(wallet + 1)] for x in range(len(list_of_actions_as_dict) + 1)]
    
    for i in range(1, len(list_of_actions_as_dict) + 1):
        """for each action in the list of actions"""
        for w in range(1, wallet + 1):
            """for each wallet value"""
            if int(list_of_actions_as_dict[i-1]['value']) <= w:
                """if the value of the action is less than the wallet value"""
                matrice[i][w] = max(int(list_of_actions_as_dict[i-1]["sellable_value"]) + matrice[i-1][w - int(list_of_actions_as_dict[i-1]['value'])], matrice[i-1][w])
                """the value of the cell is the max between the sellable value of the action + the value of the cell in the same row but with the wallet value - 
                the value of the action and the value of the cell in the row above"""
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
            """if the value of the action is less than the w value"""
            list_of_actions_to_buy.append(e)
            w -= (e["value"])
        
        n -= 1
    return list_of_actions_to_buy

with open ("./DATASET/dataset2_Python+P7.csv", 'r') as csvfile:
    """open the csv file and read it"""
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        if float(row[1]) > 0 and float(row[2]) > 1:
            """for each row in the csv file, add the name, price and profit of the action in corresponding lists"""
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
list_of_actions_to_buy = dynamic_function(wallet, list_of_actions_as_dict)
wallet = wallet / 100

for action in list_of_actions_to_buy:
    """switch the value of the action to the real value and calculate the rentability, then print the result"""
    action["value"] = action["value"] / 100
    action["profit"] = action["profit"] / 100
    action["sellable_value"] = action["value"] * (1 + action["profit"]/100)
    wallet -= action["value"]
    rentability += action["sellable_value"] - action["value"]
    print(action, "wallet", 500-wallet, "rentability", rentability)
    with open("dataset_2_optimized.csv", "a") as csvfile:
        """write the result in a csv file"""
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow([action["name"], action["value"], action["profit"], action["sellable_value"], wallet])