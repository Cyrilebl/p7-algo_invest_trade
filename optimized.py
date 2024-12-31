def find_best_stocks(data, budget):
    for action in data:
        ratio = action["profit"] / action["price"]
        action["ratio"] = ratio

    selected_actions = []
    total_cost = 0
    total_profit = 0

    sorted_data = sorted(data, key=lambda x: x["ratio"], reverse=True)
    for action in sorted_data:
        cost = action["price"]
        if budget >= cost:
            selected_actions.append(action["stock"])
            budget -= cost
            total_cost += cost
            total_profit += cost * action["profit"]

    return selected_actions, round(total_cost, 2), round(total_profit, 2)


"""
Début
Fonction find_best_stocks(données, budget):

    Pour chaque action dans les données :
        Calculer le ratio = profit / prix
        Ajouter ce ratio à l'action (clé "ratio")
        
    Initialiser :
        - selected_actions comme une liste vide pour stocker les actions sélectionnées
        - total_cost à 0 pour le coût total des actions sélectionnées
        - total_profit à 0 pour le profit total des actions sélectionnées

    Trier les données par ratio (ordre décroissant)

    Pour chaque action dans les données triées :
        Si le budget est supérieur ou égal au prix de l'action :
            Ajouter l'action à selected_actions
            Réduire le budget du prix de l'action
            Ajouter le prix de l'action à total_cost
            Ajouter le profit (prix * ratio) à total_profit

    Retourner :
        - selected_actions
        - total_cost arrondi à deux décimales
        - total_profit arrondi à deux décimales
Fin
"""
