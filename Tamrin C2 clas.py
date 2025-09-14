import tkinter as tk
from tkinter import messagebox, simpledialog

class ClassManager:
    def __init__(self, root):
        self.root = root
        self.root.title("مدیریت کلاس‌ها")
        
        self.classes = {}  

        tk.Button(root, text="افزودن کلاس", command=self.add_class).pack(pady=5)
        tk.Button(root, text="افزودن دانش آموز", command=self.add_student).pack(pady=5)
        tk.Button(root, text="نمایش دانش آموزان مشترک", command=self.show_common_students).pack(pady=5)

    def add_class(self):
        class_name = simpledialog.askstring("نام کلاس", "نام کلاس را وارد کنید:")
        if class_name:
            if class_name not in self.classes:
                self.classes[class_name] = set()
                messagebox.showinfo("موفقیت", f"کلاس '{class_name}' اضافه شد.")
            else:
                messagebox.showwarning("خطا", "این کلاس قبلاً اضافه شده است.")

    def add_student(self):
        if not self.classes:
            messagebox.showwarning("خطا", "ابتدا یک کلاس اضافه کنید.")
            return
        class_name = simpledialog.askstring("نام کلاس", f"کدام کلاس؟ {', '.join(self.classes.keys())}")
        if class_name not in self.classes:
            messagebox.showwarning("خطا", "کلاس وجود ندارد.")
            return
        student_name = simpledialog.askstring("نام دانش آموز", "نام دانش آموز را وارد کنید:")
        if student_name:
            self.classes[class_name].add(student_name)
            messagebox.showinfo("موفقیت", f"دانش آموز '{student_name}' به کلاس '{class_name}' اضافه شد.")

    def show_common_students(self):
        if len(self.classes) < 2:
            messagebox.showwarning("خطا", "حداقل دو کلاس لازم است.")
            return
        class_names = list(self.classes.keys())
        common_students = self.classes[class_names[0]].intersection(self.classes[class_names[1]])
        messagebox.showinfo("دانش آموزان مشترک", f"دانش آموزان مشترک:\n{', '.join(common_students) if common_students else 'هیچ'}")

root = tk.Tk()
app = ClassManager(root)
root.mainloop()
