import tkinter as tk
from tkinter import messagebox, simpledialog

students = {}

# Functions
def add_student():
    roll = simpledialog.askstring("Input", "Enter roll number:")
    if not roll:
        return
    name = simpledialog.askstring("Input", "Enter name:")
    if not name:
        return
    course = simpledialog.askstring("Input", "Enter course:")
    if not course:
        return
    
    students[roll] = {"name": name, "course": course}
    messagebox.showinfo("Success", "Student added successfully!")

def view_students():
    if not students:
        messagebox.showinfo("Student Records", "No records found!")
        return
    
    records = ""
    for roll, details in students.items():
        records += f"Roll: {roll}, Name: {details['name']}, Course: {details['course']}\n"
    
    messagebox.showinfo("Student Records", records)

def search_student():
    roll = simpledialog.askstring("Search", "Enter roll number to search:")
    if roll in students:
        s = students[roll]
        messagebox.showinfo("Found", f"Name: {s['name']}, Course: {s['course']}")
    else:
        messagebox.showwarning("Not Found", "Student not found!")

def delete_student():
    roll = simpledialog.askstring("Delete", "Enter roll number to delete:")
    if roll in students:
        del students[roll]
        messagebox.showinfo("Deleted", "Student deleted successfully!")
    else:
        messagebox.showwarning("Not Found", "Student not found!")

# GUI Setup
root = tk.Tk()
root.title("Student Management System Created by Anuj")
root.geometry("400x300")


# Heading
tk.Label(root, text="Student Management System", font=("Helvetica", 16, "bold")).pack(pady=20)

# Buttons
tk.Button(root, text="Add Student", width=25, command=add_student).pack(pady=5)
tk.Button(root, text="View Students", width=25, command=view_students).pack(pady=5)
tk.Button(root, text="Search Student", width=25, command=search_student).pack(pady=5)
tk.Button(root, text="Delete Student", width=25, command=delete_student).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

# Run the app
root.mainloop()
