import csv
import time


def read_actions(filename):
    actions = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            action = {"name": row[0], "cost": float(row[1]), "profit": float(row[2]) / 100}
            if action["cost"] > 0:
                actions.append(action)
    return actions


def combinations(actions, r):
    if r == 0:
        return [[]]
    elif len(actions) == 0:
        return []
    else:
        result = []
        for i in range(len(actions)):
            first = actions[i]
            rest = actions[i + 1 :]
            for combination in combinations(rest, r - 1):
                result.append([first] + combination)
        return result


def find_best_investment(actions, max_budget):
    best_combination = None
    max_profit = 0

    start_time = time.time()
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            total_cost = sum(action["cost"] for action in combination)
            if total_cost <= max_budget:
                total_profit = sum(action["cost"] * action["profit"] for action in combination)
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_combination = combination
    end_time = time.time()
    execution_time = end_time - start_time

    return best_combination, execution_time


actions = read_actions("actions.csv")
max_budget = 500
total_cost = 0
total_profit = 0

best_investment, execution_time = find_best_investment(actions, max_budget)

if best_investment is None:
    print("Aucune combinaison d'actions ne convient avec le budget donné.")
else:
    print("Meilleure combinaison d'actions pour maximiser les bénéfices :")

    for action in best_investment:
        print(action["name"])
        total_cost = action["cost"] + total_cost
        print("Cout total: ", total_cost, "€")
        total_profit = (action["cost"] * action["profit"]) + total_profit
        print("Bénéfice total: ", total_profit, "€")

print("Temps d'exécution : {:.2f} secondes".format(execution_time))
