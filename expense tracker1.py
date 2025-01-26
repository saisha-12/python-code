import json
import os

def load_expenses(filename):
    """Load expenses from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_expenses(expenses, filename):
    """Save expenses to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense to the expenses dictionary."""
    category = input("Enter the expense category (e.g., food, entertainment, utilities): ")
    amount = float(input("Enter the expense amount: "))
    
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]

def calculate_summary(expenses):
    """Calculate total, average, and categorized expenses."""
    total = 0
    count = 0
    categorized_expenses = {}

    for category, amounts in expenses.items():
        category_total = sum(amounts)
        total += category_total
        count += len(amounts)
        categorized_expenses[category] = category_total

    average = total / count if count > 0 else 0
    return total, average, categorized_expenses

def display_summary(total, average, categorized_expenses):
    """Display the summary of expenses."""
    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")
    print("\nCategorized Expenses:")
    for category, amount in categorized_expenses.items():
        print(f"{category}: ₹{amount:.2f}")

def main():
    filename = "expenses.json"
    expenses = load_expenses(filename)

    while True:
        print("\n--- Daily Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses, filename)
        elif choice == '2':
            total, average, categorized_expenses = calculate_summary(expenses)
            display_summary(total, average, categorized_expenses)
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()