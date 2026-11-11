import csv
import os
from datetime import datetime

# File to store expense records
FILE_NAME = "expenses.csv"

# Available expense categories
CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Bills",
    "Entertainment",
    "Others"
]


# 1. Create the CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Date", "Category", "Description", "Amount"]
            )


# 2. Add a new expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        print("\nAvailable Categories:")
        for category in CATEGORIES:
            print("-", category)

        category = input("Enter category: ").strip().title()

        if category not in CATEGORIES:
            print("Invalid category.")
            return

        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty.")
            return

        date = input(
            "Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date, "%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [date, category, description, amount]
            )

        print("\nExpense added successfully!")

    except ValueError:
        print("Invalid amount or date. Please enter valid details.")

    except OSError as error:
        print("File error:", error)


# 3. View all expense records
def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

            if not expenses:
                print("\nNo expense records found.")
                return

            print("\n========== ALL EXPENSES ==========")

            for expense in expenses:
                print(
                    f"Date: {expense['Date']} | "
                    f"Category: {expense['Category']} | "
                    f"Description: {expense['Description']} | "
                    f"Amount: Rs. {expense['Amount']}"
                )

    except OSError as error:
        print("Unable to read file:", error)


# 4. Calculate total expenses
def calculate_total():
    total = 0

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                total += float(expense["Amount"])

        print("\nTotal Expenses: Rs.", round(total, 2))

    except (ValueError, OSError) as error:
        print("Error calculating expenses:", error)


# 5. Display category-wise expense summary
def category_summary():
    category_totals = {}

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        print("\n========== CATEGORY SUMMARY ==========")

        if not category_totals:
            print("No expense records found.")
            return

        for category, total in category_totals.items():
            print(f"{category}: Rs. {round(total, 2)}")

    except (ValueError, OSError) as error:
        print("Error generating summary:", error)


# 6. Search expenses by category
def search_expenses():
    search_category = input(
        "Enter category to search: "
    ).strip().title()

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            found = False

            print("\n========== SEARCH RESULTS ==========")

            for expense in reader:
                if expense["Category"] == search_category:
                    print(expense)
                    found = True

            if not found:
                print("No expenses found in this category.")

    except OSError as error:
        print("Search error:", error)


# 7. Main menu
def main():
    initialize_file()

    while True:
        print("\n================================")
        print("       PYTHON EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Category-wise Summary")
        print("5. Search Expenses")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            search_expenses()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")


# Starting point of the application
if __name__ == "__main__":
    main()
