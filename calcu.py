import tkinter as tk
from tkinter import messagebox
import sys

active_entry = None

def on_click(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))

def check_script_name():
    if sys.argv[0].endswith("operator.py"):
        messagebox.showerror("Error", "Rename your script to avoid conflicts with built-in modules.")
        sys.exit(1)

def show_manual():
    messagebox.showinfo("Manual", "Enter two numbers and click an operation button to perform the calculation.")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

def add_to_entry(number):
    global active_entry
    if active_entry:
        current = active_entry.get()
        active_entry.delete(0, tk.END)
        active_entry.insert(tk.END, current + str(number))

def set_active_entry(entry):
    global active_entry
    active_entry = entry

check_script_name()

root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry1.bind("<FocusIn>", lambda e: set_active_entry(entry1))  # Set active entry when clicked

entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry2.bind("<FocusIn>", lambda e: set_active_entry(entry2))  # Also set entry2 as active when clicked

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text='+', width=5, command=lambda: on_click('+')).grid(row=0, column=0)
tk.Button(btn_frame, text='-', width=5, command=lambda: on_click('-')).grid(row=0, column=1)
tk.Button(btn_frame, text='*', width=5, command=lambda: on_click('*')).grid(row=0, column=2)
tk.Button(btn_frame, text='/', width=5, command=lambda: on_click('/')).grid(row=0, column=3)

number_pad = tk.Frame(root)
number_pad.pack()

for i in range(3):
    for j in range(3):
        num = 1 + i * 3 + j
        tk.Button(number_pad, text=str(num), width=5, command=lambda n=num: add_to_entry(n)).grid(row=i, column=j)

tk.Button(number_pad, text='0', width=5, command=lambda: add_to_entry(0)).grid(row=3, column=1)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14))
result_label.pack(pady=10)

manual_button = tk.Button(root, text="Manual", font=("Arial", 12), command=show_manual)
manual_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=clear_fields)
clear_button.pack(pady=5)

root.mainloop()
