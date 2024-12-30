def find_best_stock(data, budget):
    for action in data:
        action["ratio"] = action["profit"] / action["price"]

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
