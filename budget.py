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

print(add_budget("Groceries", 500))
print(add_expenses("Groceries", 400))



