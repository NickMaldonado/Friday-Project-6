import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login Page")

# Labels and Entry widgets
labels = ["Username:", "Password:"]
for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.place(x=20, y=30+i*50)
    entry = ttk.Entry(root)
    entry.place(x=120, y=30+i*50)

# Login button
login_button = ttk.Button(root, text="Login")
login_button.place(x=100, y=130)

root.mainloop()
