import csv
import time
import sys


if len(sys.argv) != 2:
    print("Veuillez fournir le nom du fichier CSV en tant qu'argumment")
    sys.exit(1)
print(sys.argv)


# Fonction pour lire les données à partir d'un fichier CSV
def read_actions(filename):
    """
    Extract list of actions from a csv file

    Args:
        filename (_type_): file's name

    Returns:
        actions(list): list of buyable actions (with cost and profit)
    """
    actions = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cost = int(float(row[1]) * 100)
            profit_float = float(row[1]) * (float(row[2]) / 100)
            profit = int(profit_float * 100)
            action = {"name": row[0], "cost": cost, "profit": profit}
            if cost > 0 and profit > 0:
                actions.append(action)
    return actions


def best_choices(actions: list, budget: int):
    """
    Knapsack algorithm.
    Creates a matrix where rows represent available actions and columns
    different possible budget of the wallet, from 0 to 'budget'.
    After filling out the matrix, the function traces back the selected actions
    to maximize the profit.

    Args:
        actions (list): List of actions
        budget (int): Max budget available

    Returns:
        list: selected actions for the best choice
    """
    n = len(actions)
    dp = [[0] * ((budget) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if actions[i - 1]["cost"] <= j:
                dp[i][j] = max(actions[i - 1]["profit"] + dp[i - 1][j - actions[i - 1]["cost"]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_actions = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_actions.append(actions[i - 1])
            j -= actions[i - 1]["cost"]

    return selected_actions


# Lecture des données à partir d'un fichier CSV

actions = read_actions(sys.argv[1])


# Définition du budget maximum par client
budget_max = 500 * 100
start_time = time.time()

# Recherche de la meilleure stratégie d'investissement
meilleur_portefeuille = best_choices(actions, budget_max)

end_time = time.time()
execution_time = end_time - start_time

# Affichage du meilleur investissement
print("Meilleur portefeuille d'actions :")
for action in meilleur_portefeuille:
    print(f"{action['name']} - Coût : {action['cost']/100} euros")
print("Temps d'exécution : {:.2f} secondes".format(execution_time))

# Calcul du coût total et du profit maximal
cout_total = sum(action["cost"] / 100 for action in meilleur_portefeuille)
profit_maximal = sum(action["profit"] / 100 for action in meilleur_portefeuille)

# Affichage du coût total et du profit maximal
print("Coût total des actions sélectionnées :", cout_total, "euros")
print("Profit maximal réalisé après 2 ans :", profit_maximal, "euros")
