import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import sqlite3

class CityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مدیریت شهرها")
        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        
        tk.Button(root, text="ثبت شهر جدید", command=self.add_city_form).pack(pady=5)
        tk.Label(root, text="جستجوی شهر:").pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        tk.Button(root, text="جستجو", command=self.search_city).pack(pady=5)

        tk.Label(root, text="انتخاب شهر:").pack()
        self.city_var = tk.StringVar()
        self.city_combo = ttk.Combobox(root, textvariable=self.city_var, state="readonly")
        self.city_combo.pack()
        self.city_combo.bind("<<ComboboxSelected>>", self.show_city_info)

        self.info_label = tk.Label(root, text="")
        self.info_label.pack(pady=10)
        self.load_cities()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            name TEXT PRIMARY KEY,
            population INTEGER,
            male INTEGER,
            female INTEGER
        )
        """)
        self.conn.commit()

    def load_cities(self):
        self.cursor.execute("SELECT name FROM cities")
        cities = [row[0] for row in self.cursor.fetchall()]
        self.city_combo['values'] = cities

    def show_city_info(self, event):
        name = self.city_var.get()
        self.cursor.execute("SELECT * FROM cities WHERE name=?", (name,))
        city = self.cursor.fetchone()
        if city:
            self.info_label.config(text=f"جمعیت: {city[1]}, مرد: {city[2]}, زن: {city[3]}")

    def add_city_form(self):
        name = simpledialog.askstring("نام شهر", "نام شهر:")
        if not name:
            return
        population = simpledialog.askinteger("جمعیت", "جمعیت:")
        male = simpledialog.askinteger("مرد", "تعداد مرد:")
        female = simpledialog.askinteger("زن", "تعداد زن:")
        try:
            self.cursor.execute("INSERT INTO cities VALUES (?, ?, ?, ?)", (name, population, male, female))
            self.conn.commit()
            messagebox.showinfo("موفقیت", "شهر ثبت شد.")
            self.load_cities()
        except sqlite3.IntegrityError:
            messagebox.showerror("خطا", "این شهر قبلاً ثبت شده است.")

    def search_city(self):
        name = self.search_entry.get()
        self.cursor.execute("SELECT * FROM cities WHERE name=?", (name,))
        city = self.cursor.fetchone()
        if city:
            self.info_label.config(text=f"جمعیت: {city[1]}, مرد: {city[2]}, زن: {city[3]}")
        else:
            messagebox.showinfo("نتیجه", "شهر یافت نشد.")

root = tk.Tk()
app = CityApp(root)
root.mainloop()
