import tkinter as tk
from tkinter import messagebox
import csv
import os

def init_file():
    if not os.path.exists("gym_members.csv"):
        with open("gym_members.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Phone", "Plan"])

def register_member():
    name = entry_name.get()
    age = entry_age.get()
    phone = entry_phone.get()
    plan = entry_plan.get()

    if not name or not age or not phone or not plan:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    with open("gym_members.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, phone, plan])

    messagebox.showinfo("Success", f"Member {name} registered successfully!")
    
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_plan.delete(0, tk.END)

init_file()

root = tk.Tk()
root.title("Gym Management System")
root.geometry("450x450")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="🏋️‍♂️ Gym Member Registration", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Full Name:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=8)
entry_name = tk.Entry(frame, font=("Arial", 11), width=22)
entry_name.grid(row=0, column=1, pady=8)

tk.Label(frame, text="Age:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=8)
entry_age = tk.Entry(frame, font=("Arial", 11), width=22)
entry_age.grid(row=1, column=1, pady=8)

tk.Label(frame, text="Phone Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=8)
entry_phone = tk.Entry(frame, font=("Arial", 11), width=22)
entry_phone.grid(row=2, column=1, pady=8)

tk.Label(frame, text="Membership Plan:", font=("Arial", 11), bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=8)
entry_plan = tk.Entry(frame, font=("Arial", 11), width=22)
entry_plan.grid(row=3, column=1, pady=8)

btn_submit = tk.Button(root, text="Register Member", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=20, command=register_member)
btn_submit.pack(pady=20)

root.mainloop()