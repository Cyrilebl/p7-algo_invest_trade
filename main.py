import datetime
from read_csv import read_csv
from bruteforce import find_best_stocks as bruteforce_solution
from optimized import find_best_stocks as optimized_solution


def main():
    start_time = datetime.datetime.now()

    file_name = "dataset1.csv"
    stock_column = "name"
    price_column = "price"
    profit_column = "profit"

    data = read_csv(file_name, stock_column, price_column, profit_column)
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

    print(f"\nActions choisies: {selected_actions}")
    print(f"Coût total: {total_cost}€")
    print(f"Profit total (après 2 ans): {total_profit}€")

    end_time = datetime.datetime.now()
    print(f"\nTemps d'exécution: {end_time - start_time}")


if __name__ == "__main__":
    main()
