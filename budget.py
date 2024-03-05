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
    for name in budget:
        budgeted = budget[name]
        spent = expenses[name]
        remaining = budgeted - spent
        print(f"{name:13s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}")

print(add_budget("Rent", 900))
print(add_budget("Groceries", 450))
print(add_expenses("Rent", 830))
print(add_expenses("Groceries", 400))
print(summary()) 

