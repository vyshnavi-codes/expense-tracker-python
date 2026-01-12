import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    description = desc_entry.get()
    amount_input = amount_entry.get()

    if not date or not category or not description or not amount_input:
        messagebox.showerror("Error", "All fields are required")
        return

    if not amount_input.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Amount must be a number")
        return

    amount = float(amount_input)

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    output_text.insert(tk.END, "Expense added successfully ✅\n")

    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def view_expenses():
    output_text.insert(tk.END, "\nYour Expenses:\n")
    if not expenses:
        output_text.insert(tk.END, "No expenses added.\n")
        return

    for i, exp in enumerate(expenses, start=1):
        output_text.insert(
            tk.END,
            f"{i}. {exp['date']} | {exp['category']} | {exp['description']} | ₹{exp['amount']}\n"
        )

def view_total():
    total = sum(exp["amount"] for exp in expenses)
    output_text.insert(tk.END, f"\nTotal Spending: ₹{total}\n")

# Main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

# Labels & Entries
tk.Label(root, text="Date").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Description").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Buttons
tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=5)
tk.Button(root, text="View Total", command=view_total).pack(pady=5)

# Output box
output_text = tk.Text(root, height=10)
output_text.pack()

root.mainloop()
