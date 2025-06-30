# from expense import Expense

# def main():
#     print("print this ")
#     expense_file_path= "expenses.csv"


#     # Get user input
#     expense= get_user_input()
    


#     # Write the expenses in another file
#     # saving_expense(expense, expense_file_path)

#     # Read and summarize the contents of the file
#     read_and_summarizing(expense_file_path)


# def get_user_input():
#     print("user input")
#     expense_name = input("Enter the expense name: ")
    
#     while True:
#         try:
#             expense_amount = float(input("Enter the expense amount: "))
#             break  # Exit loop if valid input
#         except ValueError:
#             print("Invalid input! Please enter a valid number.")

#     print(f"You've entered {expense_name}, {expense_amount}")

#     expense_category = [
#         "food", "home", "college", "misc", "fun",
#     ]

#     while True:
#         print("select a category: ")
#         for i, category_name in enumerate(expense_category):
#             print(f"{i+1}.{category_name}")
        
#         value_range = f"(1-{len(expense_category)})"
#         try:
#             selected_index =int(input(f"Enter a category name {value_range}")) -1
#             if selected_index in range (len(expense_category)):
#                 selected_category = expense_category[selected_index]
#                 new_expense = Expense(name=expense_name, category=selected_category,amount=expense_amount)
#                 return new_expense
#             else:
#                 print("invalid catgory. please try again.")
#         except ValueError:
#             print("invalid input pls entre a number.")
            
        
        

    


# def saving_expense(expense: Expense,expenses_file_path):
#     print(f"Saving the expense: {expense} to{expenses_file_path}")
#     with open(expenses_file_path,"a")as f:
#         f.write(f"{expense.name},{expense.amount},{expense.category}\n")  





# def read_and_summarizing(expenses_file_path):
#     print("Reading and summarizing the expenses...")
#     with open (expenses_file_path,"r")as f:
#         lines = f.readlines()
#         for line in lines:
#             stripped_line=line.strip()
#             expense_name, expense_amount, expense_category = line.strip().split(",")
#             line_expenses= Expense(
#                 name= expense_name,
#                 amount= float(expense_amount),
#                 category=expense_category,
#             )
#             expenses.append(line_expenses)
            

# # Run the program
# if __name__ == "__main__":
#     main()

from expense import Expense  # Make sure you have this class defined properly

def main():
    print("Welcome to your Expense Tracker!")
    expense_file_path = "expenses.csv"

    # Get user input
    expense = get_user_input()

    # Write the expense to file
    saving_expense(expense, expense_file_path)

    # Read and summarize the contents of the file
    read_and_summarizing(expense_file_path)


def get_user_input():
    print("\nPlease enter your expense details.")
    expense_name = input("Enter the expense name: ")

    while True:
        try:
            expense_amount = float(input("Enter the expense amount: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    expense_category = ["food", "home", "college", "misc", "fun"]

    while True:
        print("\nSelect a category:")
        for i, category_name in enumerate(expense_category):
            print(f"{i + 1}. {category_name}")
        
        try:
            selected_index = int(input(f"Enter a category number (1-{len(expense_category)}): ")) - 1
            if 0 <= selected_index < len(expense_category):
                selected_category = expense_category[selected_index]
                return Expense(name=expense_name, amount=expense_amount, category=selected_category)
            else:
                print("❌ Invalid category number. Try again.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def saving_expense(expense: Expense, expenses_file_path: str):
    print(f"\n💾 Saving the expense: {expense} to {expenses_file_path}")
    with open(expenses_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def read_and_summarizing(expenses_file_path: str):
    print("\n📖 Reading and summarizing the expenses...")
    expenses = []

    try:
        with open(expenses_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():  # Skip blank lines
                    expense_name, expense_amount, expense_category = line.strip().split(",")
                    expenses.append(Expense(
                        name=expense_name,
                        amount=float(expense_amount),
                        category=expense_category
                    ))

        # Summarize
        print("\n📊 Expense Summary:")
        total_amount = sum(e.amount for e in expenses)
        print(f"Total Expenses: ₹{total_amount:.2f}")

        category_totals = {}
        for e in expenses:
            category_totals[e.category] = category_totals.get(e.category, 0) + e.amount

        for category, amount in category_totals.items():
            print(f"  {category}: ₹{amount:.2f}")

    except FileNotFoundError:
        print("⚠️ No expenses recorded yet. File not found.")


# Run the program
if __name__ == "__main__":
    main()
