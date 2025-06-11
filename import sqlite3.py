import sqlite3
import tkinter as tk

# Database Setup
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)''')
conn.commit()

# Function to Add Student
def add_student():
    name, age, grade = name_entry.get(), age_entry.get(), grade_entry.get()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    status_label.config(text="Student Added Successfully!")

# GUI Setup
root = tk.Tk()
root.title("Student Management System")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

grade_label = tk.Label(root, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()