from datetime import datetime

expenses = []


add_expense = lambda amount, category, date, desc: expenses.append({
    'amount': amount,
    'category': category,
    'date': datetime.strptime(date, "%Y-%m-%d"),
    'description': desc
})

total_expenses = lambda: sum(exp['amount'] for exp in expenses)

filter_by_category = lambda cat: list(filter(lambda e: e['category'].lower() == cat.lower(), expenses))

filter_by_date = lambda start, end: list(filter(lambda e: start <= e['date'] <= end, expenses))



def print_expenses(exp_list):
    if not exp_list:
        print("No expenses found.")
        return
    for e in exp_list:
        print(f"{e['date'].strftime('%Y-%m-%d')}: ${e['amount']:.2f} - {e['category']} - {e['description']}")


def main():
    print("Welcome to the ET (not the alien) (type 'q' to quit)")

    while True:
        print("\nOptions:")
        print("1 - Add Expense")
        print("2 - Show Total Expenses")
        print("3 - Show Expenses by Category")
        print("4 - Show Expenses by Date Range")
        print("q - Quit")

        choice = input("Select option: ").strip().lower()
        if choice == 'q':
            print("Exiting Ciao <3")
            break

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                date = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter description: ")
                add_expense(amount, category, date, description)
                print("Expense added")
            except Exception as ex:
                print("Error adding expense:", ex)

        elif choice == '2':
            print(f"Total Expenses: ${total_expenses():.2f}")

        elif choice == '3':
            cat = input("Enter category to filter: ")
            filtered = filter_by_category(cat)
            print_expenses(filtered)

        elif choice == '4':
            try:
                start_date = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d")
                filtered = filter_by_date(start_date, end_date)
                print_expenses(filtered)
            except Exception as ex:
                print("Invalid date format:", ex)

        else:
            print("Invalid. Try again.")


if __name__ == "__main__":
    main()
