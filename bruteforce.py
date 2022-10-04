import csv
import itertools


list_of_actions_as_dict = []
actions_name = []
actions_value = []
actions_profit = []
compteur = 0
compteur_2 = 0
best_rentability = 0
best_choice = []
invest = 0


with open ("./DATASET/dataset_bruteforce.csv", 'r') as csvfile:
    """open the csv file and read it"""
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        """for each row in the csv file, add the name of the action in the list actions_name"""
        actions_name.append(row[0])
        actions_value.append(row[1])
        actions_profit.append(row[2])
for action in actions_value:
    """transform the list of string into a list of integer"""
    action = float(action)
for action in actions_profit:
    """transform the list of string into a list of integer"""
    action = float(action)
for i in range(len(actions_name)):
    """create a list of dictionary with actions name, value and profit"""
    list_of_actions_as_dict.append({"name": actions_name[i], "value": float(actions_value[i]), "profit": float(actions_profit[i])/100})
for i in range(len(list_of_actions_as_dict)):
    """calculate the sellable value of each action and add in the dictionary"""
    sellable_value = list_of_actions_as_dict[i]["value"] * (1+list_of_actions_as_dict[i]["profit"])
    list_of_actions_as_dict[i]["sellable_value"] = sellable_value
    print(list_of_actions_as_dict[i])
for l in range(len(list_of_actions_as_dict) + 1):
    """loop to create all length of combinations 0 -> 20 elements"""
    for subset in itertools.combinations(list_of_actions_as_dict, l):
        """for each subset of the list of actions, calculate the total value of the subset"""
        total_value = 0
        total_sellable_value = 0
        for action in subset:
            total_value += action["value"]
            total_sellable_value += action["sellable_value"]
        if total_value < 500:
            """if the total value of the subset is less than 500, calculate the rentability"""
            rentability = total_sellable_value - total_value
            if rentability > best_rentability:
                """if the rentability is better than the best rentability, change the best rentability and the best choice"""
                best_rentability = rentability
                best_choice = subset
for actions in best_choice:
    invest += actions["value"]
    
print(invest)
print(best_rentability)

with open("bruteforce_result.csv", 'w') as csvfile:
    """open a csv file to write the result"""
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(["name", "value", "profit", "sellable_value"])
    for action in best_choice:
        """write the best choice in the csv file"""
        csv_writer.writerow([action["name"], action["value"], action["profit"], action["sellable_value"]])
    csv_writer.writerow(["total", invest, best_rentability, invest + best_rentability])

