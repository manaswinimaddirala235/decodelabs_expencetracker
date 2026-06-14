# Expense Tracker Project

total = 0

print("=== Expense Tracker ===")

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        total += float(expense)
    except ValueError:
        print("Please enter a valid amount!")

print("\nTotal Spent: ₹", total)
