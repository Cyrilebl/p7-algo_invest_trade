import csv


def read_csv(file_name, stock_column, price_column, profit_column):
    data = []
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            stock = row[stock_column]
            price = float(row[price_column])
            profit = float(row[profit_column].replace("%", ""))
            if profit >= 1:
                profit /= 100

            if price > 0 and profit >= 0:
                data.append({"stock": stock, "price": price, "profit": profit})

        return data
