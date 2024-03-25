import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Grouped Calculator")

# Entry box
entry = ttk.Entry(root, state='disabled')
entry.pack(pady=10)

# Numbers grouped together
number_buttons = ["7", "8", "9",
                  "4", "5", "6",
                  "1", "2", "3",
                  "C", "0", "="]

for text in number_buttons:
    btn = ttk.Button(root, text=text)
    btn.pack(side='left', fill='x', padx=5, pady=2)
    if text == "3" or text == "=":
        ttk.Separator(root, orient='vertical').pack(side='left', fill='y', padx=5)

# Other buttons grouped together
operation_buttons = ["+", "-", "x", "/"]

for text in operation_buttons:
    btn = ttk.Button(root, text=text)
    btn.pack(side='left', fill='x', padx=5, pady=2)

root.mainloop()
