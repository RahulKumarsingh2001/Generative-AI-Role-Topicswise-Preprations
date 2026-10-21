
import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved expenses.")
    return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def get_next_id():
    return max((expense["id"] for expense in expenses), default=0) + 1


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        if not (0 < amount < float("inf")):
            print("Amount must be a positive, finite number.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    expense = {
        "id": get_next_id(),
        "amount": amount,
        "category": category,
        "description": description,
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"Amount: ₹{expense['amount']:.2f} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']} | "
            f"Date: {expense.get('date', 'N/A')}"
        )


def find_expense(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense
    return None


def update_expense():
    try:
        expense_id = int(input("Enter expense ID to update: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    expense = find_expense(expense_id)

    if expense is None:
        print("Expense not found.")
        return

    print("Leave a field blank to keep its current value.")

    amount_input = input(
        f"New amount (current: {expense['amount']}): "
    ).strip()

    if amount_input:
        try:
            amount = float(amount_input)
            if not (0 < amount < float("inf")):
                print("Amount must be positive and finite.")
                return
            expense["amount"] = amount
        except ValueError:
            print("Invalid amount.")
            return

    category = input(
        f"New category (current: {expense['category']}): "
    ).strip()

    description = input(
        f"New description (current: {expense['description']}): "
    ).strip()

    if category:
        expense["category"] = category

    if description:
        expense["description"] = description

    save_expenses()
    print("Expense updated successfully!")


def delete_expense():
    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    expense = find_expense(expense_id)

    if expense is None:
        print("Expense not found.")
        return

    confirm = input(
        f"Delete '{expense['description']}'? (y/n): "
    ).strip().lower()

    if confirm == "y":
        expenses.remove(expense)
        save_expenses()
        print("Expense deleted successfully!")
    else:
        print("Deletion cancelled.")


def search_expenses():
    keyword = input(
        "Search by category or description: "
    ).strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    results = [
        expense for expense in expenses
        if keyword in expense["category"].lower()
        or keyword in expense["description"].lower()
    ]

    if not results:
        print("No matching expenses found.")
        return

    print("\n--- Search Results ---")
    for expense in results:
        print(
            f"ID: {expense['id']} | "
            f"Amount: ₹{expense['amount']:.2f} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']} | "
            f"Date: {expense.get('date', 'N/A')}"
        )


def view_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ₹{total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Search Expense")
        print("6. View Total Expenses")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            search_expenses()
        elif choice == "6":
            view_total_expenses()
        elif choice == "7":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")


expenses = load_expenses()

if __name__ == "__main__":
    main()
