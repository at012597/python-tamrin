import tkinter as tk
from tkinter import messagebox

def common_words():
    text1_words = set(text1.get("1.0", tk.END).split())
    text2_words = set(text2.get("1.0", tk.END).split())
    common = text1_words.intersection(text2_words)
    messagebox.showinfo("کلمات مشترک", ", ".join(common) if common else "هیچ")

def unique_words():
    title = entry_title.get()
    article_words = set(text1.get("1.0", tk.END).split())
    messagebox.showinfo(f"کلمات منحصر {title}", f"تعداد: {len(article_words)}\nکلمات: {', '.join(article_words)}")

root = tk.Tk()
root.title("مقایسه مقالات")

tk.Label(root, text="مقاله اول:").pack()
text1 = tk.Text(root, height=5, width=50)
text1.pack()

tk.Label(root, text="مقاله دوم:").pack()
text2 = tk.Text(root, height=5, width=50)
text2.pack()

tk.Button(root, text="کلمات مشترک", command=common_words).pack(pady=5)

tk.Label(root, text="عنوان مقاله اول:").pack()
entry_title = tk.Entry(root)
entry_title.pack()
tk.Button(root, text="کلمات منحصر مقاله اول", command=unique_words).pack(pady=5)

root.mainloop()
