import csv

def read_csv(file_name):
  with open(file_name, mode="r") as file:
    reader = csv.DictReader(file, delimiter=",")
    
    data = []
    
    for row in reader:
      stock = row["Actions #"]
      cost = int(row["Coût par action (en euros)"])
      profit = float(row["Bénéfice (après 2 ans)"].replace("%", "")) / 100
      
      data.append({"stock": stock, "cost": cost, "profit": profit})
      
    return data

def find_best_stock(data, budget):
  sorted_data = sorted(data, key=lambda x: x["profit"], reverse=True)

  selected_actions = []
  total_cost = 0
  total_profit = 0
  
  for action in sorted_data:
    cost = action["cost"]
     
    if budget >= cost:
      selected_actions.append(action["stock"])
      budget -= cost
      total_cost += cost
      total_profit += cost * action["profit"]
    
  return selected_actions, total_cost, total_profit

def main():
  file_name = "stocks.csv"
  budget = 500

  data = read_csv(file_name)
  selected_actions, total_cost, total_profit = find_best_stock(data, budget)
  
  print(f"Actions choisies: {selected_actions}")
  print(f"Coût total: {total_cost}€")
  print(f"Profit total (après 2 ans): {round(total_profit, 2)}€")

if __name__ == "__main__":
  main()
  