import csv
import datetime


def read_csv(file_name, stock_column, price_column, profit_column):
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file, delimiter=",")

        data = []

        for row in reader:
            stock = row[stock_column]
            price = float(row[price_column])
            profit = float(row[profit_column].replace("%", ""))
            if profit >= 1:
                profit /= 100

            if price > 0 and profit >= 0:
                data.append({"stock": stock, "price": price, "profit": profit})

        return data


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


# "Actions #"
# "Coût par action (en euros)"
# "Bénéfice (après 2 ans)"
def main():
    start_time = datetime.datetime.now()

    file_name = "dataset3.csv"
    stock_column = "name"
    price_column = "price"
    profit_column = "profit"

    data = read_csv(file_name, stock_column, price_column, profit_column)
    budget = 500

    selected_actions, total_cost, total_profit = find_best_stock(data, budget)

    print(f"Actions choisies: {selected_actions}")
    print(f"Coût total: {total_cost}€")
    print(f"Profit total (après 2 ans): {total_profit}€")

    end_time = datetime.datetime.now()
    print(end_time - start_time)


if __name__ == "__main__":
    main()
