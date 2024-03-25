import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sign-up Page")

# Labels and Entry widgets
labels = ["Name:", "Email:", "Password:"]
for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text, font=('Helvetica', 12))
    label.grid(row=i, column=0, padx=5, pady=5, sticky='w')
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)

# Sign Up button
signup_button = ttk.Button(root, text="Sign Up Now")
signup_button.grid(row=len(labels), column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
