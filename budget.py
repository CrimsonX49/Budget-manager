class BudgetManager:
    def __init__(self, amount):
        self.available = amount
        self.budget = {}
        self.expenses = {}

    def add_budget(self, name, amount):
        if name in self.budget:
            raise ValueError("This item has already been budgeted.")
        if amount > self.available:
            raise ValueError("Insufficient funds!")
        self.budget[name] = amount
        self.available -= amount
        self.expenses[name] = 0
        return self.available

    def add_expenses(self, name, amount):
        if name not in self.expenses:
            raise ValueError("No such item exists.")
        self.expenses[name] += amount
        budgeted = self.budget[name]
        spent = self.expenses[name]
        return budgeted - spent 

    def summary(self):
        print("Budget          Budgeted     Spent   Remaining")
        print("-------         --------     -----   ---------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budget:
            budgeted = self.budget[name]
            spent = self.expenses[name]
            remaining = budgeted - spent
            print(f"{name:13s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}")
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining
        print("-------         --------     -----   ---------")
        print(f"{"Total":15s} {total_budgeted:8.2f} {total_spent:10.2f} {total_budgeted - total_spent:10.2f}")

result = BudgetManager(2000)
print(result.available)
print(result.budget)
print(result.expenses)
print(result.add_budget("Groceries", 450))
print(result.add_budget("Rent", 800))
print(result.add_budget("Bills", 300))