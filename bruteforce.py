from itertools import combinations


def find_best_stocks(data, budget):
    best_profit = 0
    best_combination = []

    for i in range(len(data)):
        all_combinations = combinations(data, i)

        for combination in all_combinations:
            total_cost = sum(stock["price"] for stock in combination)
            total_profit = sum(
                stock["price"] * stock["profit"] for stock in combination
            )

            if total_cost <= budget and total_profit > best_profit:
                best_profit = total_profit
                best_combination = combination

    selected_stocks = [stock["stock"] for stock in best_combination]
    total_cost = sum(stock["price"] for stock in best_combination)

    return (
        selected_stocks,
        round(total_cost, 2),
        round(best_profit, 2),
    )
