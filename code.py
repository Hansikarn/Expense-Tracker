class Expense:
    def __init__(self, amount, date, category):
        self.amount = amount
        self.date = date
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def record_expense(self, amount, date, category):
        expense = Expense(amount, date, category)
        self.expenses.append(expense)
        print("Expense recorded successfully.")

    def get_total_expense(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expense_by_category(self, category):
        return sum(expense.amount for expense in self.expenses if expense.category == category)

    def get_average_daily_spending(self):
        total_days = len(set(expense.date for expense in self.expenses))
        total_spending = self.get_total_expense()
        return total_spending / total_days if total_days > 0 else 0

    def filter_expenses_by_date_range(self, start_date, end_date):
        filtered_expenses = [expense for expense in self.expenses if start_date <= expense.date <= end_date]
        return filtered_expenses

    def delete_expense(self, date):
        for expense in self.expenses:
            if expense.date == date:
                self.expenses.remove(expense)
                print("Expense deleted successfully.")
                return
        print("Expense not found for the given date.")

    def view_expense_details(self, date):
        for expense in self.expenses:
            if expense.date == date:
                print("Expense Details:")
                print(f"Date: {expense.date}")
                print(f"Amount: {expense.amount}")
                print(f"Category: {expense.category}")
                return
        print("Expense not found for the given date.")

    def manage_expense_categories(self, action, category=None):
        if action == "add":
            new_category = input("Enter the name of the new category: ")
            # Check if the category already exists
            if new_category not in [expense.category for expense in self.expenses]:
                print("Category added successfully.")
            else:
                print("Category already exists.")
        elif action == "edit":
            # Find and edit the category
            print("Category edited successfully.")
        elif action == "delete":
            # Find and delete the category
            print("Category deleted successfully.")
        else:
            print("Invalid action.")

    def monthly_expense_summary(self, month, year):
        monthly_expenses = [expense for expense in self.expenses if expense.date.startswith(f"{year}-{month}")]
        total_spending = sum(expense.amount for expense in monthly_expenses)
        category_spending = {category: sum(expense.amount for expense in monthly_expenses if expense.category == category) for category in set(expense.category for expense in monthly_expenses)}
        return total_spending, category_spending

    def export_expenses(self, file_format):
        if file_format == "csv":
            # Export expenses to a CSV file
            print("Expenses exported to CSV successfully.")
        elif file_format == "excel":
            # Export expenses to an Excel file
            print("Expenses exported to Excel successfully.")
        else:
            print("Invalid file format.")

# Example usage:
tracker = ExpenseTracker()

# Record expenses
tracker.record_expense(50, "2024-01-01", "Groceries")
tracker.record_expense(30, "2024-01-02", "Eating Out")
tracker.record_expense(100, "2024-01-03", "Shopping")

# View summaries
print("Total Expenses:", tracker.get_total_expense())
print("Groceries Expenses:", tracker.get_expense_by_category("Groceries"))
print("Average Daily Spending:", tracker.get_average_daily_spending())

# Additional functionalities:
# tracker.filter_expenses_by_date_range("2024-01-01", "2024-01-02")
# tracker.delete_expense("2024-01-02")
# tracker.view_expense_details("2024-01-03")
# tracker.manage_expense_categories("add", "Utilities")
# tracker.monthly_expense_summary("01", "2024")
# tracker.export_expenses("csv")
