import csv
import time


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
            action = {"name": row[0], "cost": float(row[1]), "profit": float(row[2])}
            if action["cost"] > 0:
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
            if int(actions[i - 1]["cost"] * 100) <= j:
                dp[i][j] = max(
                    actions[i - 1]["profit"] + dp[i - 1][j - int(actions[i - 1]["cost"] * 100)], dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    selected_actions = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_actions.append(actions[i - 1])
            j -= int(actions[i - 1]["cost"] * 100)

    return selected_actions


# Lecture des données à partir d'un fichier CSV
actions = read_actions("actions.csv")


# Définition du budget maximum par client
budget_max = 50000
start_time = time.time()

# Recherche de la meilleure stratégie d'investissement
meilleur_portefeuille = best_choices(actions, budget_max)

end_time = time.time()
execution_time = end_time - start_time

# Affichage du meilleur investissement
print("Meilleur portefeuille d'actions :")
for action in meilleur_portefeuille:
    print(
        f"{action['name']} - Coût : {action['cost']} euros, Bénéfice : {action['cost'] * action['profit']/100} euros après 2 ans"
    )
print("Temps d'exécution : {:.2f} secondes".format(execution_time))

# Calcul du coût total et du profit maximal
cout_total = sum(action["cost"] for action in meilleur_portefeuille)
profit_maximal = sum(action["cost"] / 100 * action["profit"] for action in meilleur_portefeuille)

# Affichage du coût total et du profit maximal
print("Coût total des actions sélectionnées :", cout_total, "euros")
print("Profit maximal réalisé après 2 ans :", profit_maximal, "euros")
