import tkinter as tk
from tkinter import ttk

def show_table(steps, path, goal):
    root = tk.Tk()
    root.title("Climb Hill Output")

    path_text = " -> ".join(path) if path else "(không có đường đi)"
    status_text = "Đã tới đích" if path and path[-1] == goal else "Không tới được đích"

    tk.Label(root, text=f"Path: {path_text}", anchor="w").pack(fill="x", padx=8, pady=(8, 0))
    tk.Label(root, text=f"Trạng thái: {status_text}", anchor="w").pack(fill="x", padx=8, pady=(0, 8))

    tree = ttk.Treeview(root)

    tree["columns"] = ("1","2","3","4")
    tree.heading("#0", text="")
    tree.heading("1", text="Phát triển TT")
    tree.heading("2", text="Trạng thái kề")
    tree.heading("3", text="Danh sách L1")
    tree.heading("4", text="Danh sách L")

    for step in steps:
        tree.insert("", "end", values=(
            step["current"],
            ",".join(step["neighbors"]),
            ",".join(step["L1"]),
            ",".join(step["L"])
        ))
    
    tree.pack(fill="both", expand=True, padx=8, pady=8)
    root.mainloop()