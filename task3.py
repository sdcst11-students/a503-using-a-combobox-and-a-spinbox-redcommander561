#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""

import tkinter as tk
from tkinter import ttk

def calculate_compound_interest():
    try:
        principal = float(principal_var.get())
        interest_rate = float(interest_rate_var.get()) / 100
        compounding_periods = int(compounding_periods_var.get())
        years = int(years_var.get())

        final_value = principal * (1 + interest_rate / compounding_periods) ** (compounding_periods * years)
        result_var.set(f"Final Value: {final_value:.2f}")
    except ValueError:
        result_var.set("Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Compound Interest Calculator")

# Variables
principal_var = tk.StringVar()
interest_rate_var = tk.StringVar()
compounding_periods_var = tk.StringVar(value='12')  # Monthly compounding by default
years_var = tk.StringVar()
result_var = tk.StringVar()

# Entry widgets and labels
tk.Entry(window, textvariable=principal_var).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(window, textvariable=interest_rate_var).grid(row=1, column=1, padx=10, pady=10)
ttk.Combobox(window, values=['12', '4', '1'], textvariable=compounding_periods_var).grid(row=2, column=1, padx=10, pady=10)
tk.Entry(window, textvariable=years_var).grid(row=3, column=1, padx=10, pady=10)

# Labels
tk.Label(window, text="Principal:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Interest Rate (%):").grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, text="Compounding Periods per Year:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(window, text="Number of Years:").grid(row=3, column=0, padx=10, pady=10)

# Button to calculate
tk.Button(window, text="Calculate", command=calculate_compound_interest).grid(row=4, column=0, columnspan=2, pady=10)

# Label to display the result
tk.Label(window, textvariable=result_var).grid(row=5, column=0, columnspan=2, pady=10)

# Start the main event loop
window.mainloop()

