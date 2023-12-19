#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""

import tkinter as tk
from tkinter import ttk



def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operators[spinbox.get()]
        result = eval(f"{num1} {operator} {num2}")
        resultlabel.config(text=f"Result: {result}")
    except ValueError:
        resultlabel.config(text="Please enter valid numbers")
    except ZeroDivisionError:
        resultlabel.config(text="Cannot divide by zero")


window = tk.Tk()
window.title("Simple Calculator")


entry1 = tk.Entry(window, width=10)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(window, width=10)
entry2.grid(row=0, column=2, padx=10, pady=10)


operators = {'+': '+', '-': '-', '*': '*', '/': '/'}
spinbox = tk.Spinbox(window, values=list(operators.keys()), width=5)
spinbox.grid(row=0, column=1, padx=10, pady=10)


calculatebutton = tk.Button(window, text="Calculate", command=calculate)
calculatebutton.grid(row=1, column=0, columnspan=3, pady=10)


resultlabel = tk.Label(window, text="Result: ")
resultlabel.grid(row=2, column=0, columnspan=3)


window.mainloop()

