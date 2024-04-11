import csv
import time

start_time = time.time()
csv_data = "actions.csv"

actions = []


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


# Fonction pour trouver la meilleure stratégie d'investissement
def meilleure_strategie(actions, budget_max):
    actions_triees = sorted(actions, key=lambda x: x["profit"] / x["cost"], reverse=True)
    portefeuille = []
    total_investi = 0
    for action in actions_triees:
        if total_investi + action["cost"] <= budget_max:
            portefeuille.append(action)
            total_investi += action["cost"]
    return portefeuille


# Lecture des données à partir d'un fichier CSV
actions = read_actions("actions.csv")


# Définition du budget maximum par client
budget_max = 500
start_time = time.time()

# Recherche de la meilleure stratégie d'investissement
meilleur_portefeuille = meilleure_strategie(actions, budget_max)

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
