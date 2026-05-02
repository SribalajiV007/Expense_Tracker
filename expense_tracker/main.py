expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added!")

def view_expenses():
    if not expenses:
        print("No Expenses found.")
        return
    
    for i, exp in enumerate(expenses, start = 1):
        print(f"{i}. {exp['category']} -${exp['amount']}")


def total_expense():
    #total = sum(exp["amount"] for exp in expenses)
    total = 0
    for exp in expenses:
        total += exp["amount"]
        
    print(f" Total spent: &{total}")

def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("GoodBye...")
            break
        else:
            print("Invalid Choice!")

menu()