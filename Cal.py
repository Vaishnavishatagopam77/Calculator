import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Casio fx-82ES PLUS - Clone")
root.geometry("400x600")
root.configure(bg="black")

expression = ""

def click(key):
    global expression
    if key == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result
        except:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            entry_var.set("")
    elif key == "AC":
        expression = ""
        entry_var.set("")
    elif key == "DEL":
        expression = expression[:-1]
        entry_var.set(expression)
    else:
        expression += key
        entry_var.set(expression)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, bg="white", justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Casio-style layout
buttons = [
    ['AC', 'DEL', '(', ')', '/'],
    ['7', '8', '9', '*', '√'],
    ['4', '5', '6', '-', '^'],
    ['1', '2', '3', '+', 'π'],
    ['0', '.', '=', 'Ans', 'e'],
]

# Create buttons
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(root, text=btn_text, font=("Arial", 18), bg="#333", fg="white", width=5, height=2,
                        command=lambda text=btn_text: click(text))
        btn.grid(row=i+1, column=j, padx=3, pady=3, sticky="nsew")

# Expand rows and columns
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
