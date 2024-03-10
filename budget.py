available = 3000.00
budget = {}
expenses = {}

def add_budget(name, amount):
    global available
    if name in budget:
        raise ValueError("This item has already been budgeted.")
    if amount > available:
        raise ValueError("Insufficient funds!")
    budget[name] = amount
    available -= amount
    expenses[name] = 0
    return available

def add_expenses(name, amount):
    if name not in expenses:
        raise ValueError("No such item exists.")
    expenses[name] += amount
    budgeted = budget[name]
    spent = expenses[name]
    return budgeted - spent 

def summary():
    print("Budget          Budgeted     Spent   Remaining")
    print("-------         --------     -----   ---------")
    total_budgeted = 0
    total_spent = 0
    total_remaining = 0
    for name in budget:
        budgeted = budget[name]
        spent = expenses[name]
        remaining = budgeted - spent
        print(f"{name:13s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}")
        total_budgeted += budgeted
        total_spent += spent
        total_remaining += remaining
    print("-------         --------     -----   ---------")
    print(f"{"Total":15s} {total_budgeted:8.2f} {total_spent:10.2f} {total_budgeted - total_spent:10.2f}")

(add_budget("Rent", 900))
(add_budget("Groceries", 450))
(add_expenses("Rent", 830))
(add_expenses("Groceries", 400))
print(summary()) 

