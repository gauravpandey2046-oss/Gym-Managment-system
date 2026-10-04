import tkinter as tk
from tkinter import messagebox
import mysql.connector


def add_member():
  name = entry_name.get()
  phone = entry_phone.get()
  package = entry_package.get()

  if name == "" or phone == "" or package == "":
    messagebox.showerror("Error", "Sabhi fields bharna zaroori hai!")
    return

  try:
    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="viratkohli1818",  # Apna MySQL password yahan daalein
        database="gym_db",
    )
    cursor = db.cursor()

    sql = "INSERT INTO members (name, phone, package) VALUES (%s, %s, %s)"
    val = (name, phone, package)

    cursor.execute(sql, val)
    db.commit()
    db.close()

    messagebox.showinfo("Success", "Member successfully added to database!")

    # Inputs ko clear karne ke liye
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_package.delete(0, tk.END)

  except Exception as e:
    messagebox.showerror("Error", f"Connection Error: {e}")


# Tkinter Window Setup
root = tk.Tk()
root.title("Gym Management System")
root.geometry("350x350")

tk.Label(root, text="Gym Management", font=("Arial", 16, "bold")).pack(
    pady=15
)

tk.Label(root, text="Member Name:", font=("Arial", 10)).pack()
entry_name = tk.Entry(root, width=25, font=("Arial", 11))
entry_name.pack(pady=5)

tk.Label(root, text="Phone Number:", font=("Arial", 10)).pack()
entry_phone = tk.Entry(root, width=25, font=("Arial", 11))
entry_phone.pack(pady=5)

tk.Label(root, text="Package (e.g., Gold/Monthly):", font=("Arial", 10)).pack()
entry_package = tk.Entry(root, width=25, font=("Arial", 11))
entry_package.pack(pady=5)

tk.Button(
    root,
    text="Add Member",
    command=add_member,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15,
).pack(pady=20)

root.mainloop()