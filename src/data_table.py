from tabulate import tabulate


def data_table(selected_actions):
    headers = ["Nom", "Coût", "Profit", "Ratio"]
    rows = []

    for action in selected_actions:
        rows.append(
            [
                action["stock"],
                action["price"],
                action["profit"],
                round(action["ratio"], 4) if "ratio" in action else None,
            ]
        )

    return print(tabulate(rows, headers, tablefmt="grid"))
