import datetime
from src.read_csv import read_csv
from src.bruteforce import find_best_stocks as bruteforce_solution
from src.optimized import find_best_stocks as optimized_solution
from src.data_table import data_table


def main():
    start_time = datetime.datetime.now()

    file_name = "data/dataset3.csv"
    stock_column = "name"
    price_column = "price"
    profit_column = "profit"

    data, outliers = read_csv(file_name, stock_column, price_column, profit_column)
    budget = 500

    while True:
        user_choice = input(
            "Choisissez la solution : 'bruteforce' (1) ou 'optimisée' (2): "
        )
        match user_choice:
            case "1":
                selected_actions, total_cost, total_profit = bruteforce_solution(
                    data, budget
                )
                break
            case "2":
                selected_actions, total_cost, total_profit = optimized_solution(
                    data, budget
                )
                break
            case _:
                print("Choix invalide. Veuillez entrer '1' ou '2'.")

    print(f"\nActions choisies:")
    data_table(selected_actions)
    print(f"\nCoût total: {total_cost}€")
    print(f"Profit total (après 2 ans): {total_profit}€")
    print(f"\nNombre d'actions choisies: {len(selected_actions)}")
    print(f"Nombre de valeurs aberrantes: {len(outliers)}")
    print(f"Coût moyen d'une action: {round(total_cost / len(selected_actions),2)}€")
    print(f"Profit moyen : {round((total_profit / total_cost) * 100, 2)}%")

    end_time = datetime.datetime.now()
    print(f"\nTemps d'exécution: {end_time - start_time}")


if __name__ == "__main__":
    main()
