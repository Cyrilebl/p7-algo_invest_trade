import csv


def find_stock(file_name, stock_column, price_column, profit_column, stock_name):
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            stock = row[stock_column]
            price = float(row[price_column])
            profit = float(row[profit_column])

            if stock == f"Share-{stock_name.upper()}":
                return {"stock": stock, "price": price, "profit": profit}


def main():
    file_name = "data/dataset2.csv"
    stock_column = "name"
    price_column = "price"
    profit_column = "profit"
    stock_name = "mlgm"

    result = find_stock(
        file_name, stock_column, price_column, profit_column, stock_name
    )

    print(
        f"Stock: {result['stock']}, Price: {result['price']}, Profit: {result['profit']}"
    )


main()
