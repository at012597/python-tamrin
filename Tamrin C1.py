#برنامه ساخت پسورد قوی  
#در این کد از حروف فارسی استفاده شده پس ممکنه در اجرای آن در محیط  وی اس کد به مشکل بخورید ، سعی کنید آن را در  پای چر اجرا کنید 
import random
import string
def generate_strong_password(length):
    """
    این تابع یک رمز عبور قوی با طول مشخص شده تولید می‌کند.
    """
    if length < 4:
       print("برای امنیت بیشتر، طول رمز عبور باید حداقل 4 باشد.")
       return None
    # مجموعه‌ای از کاراکترهای مجاز
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"
    # ترکیب همه کاراکترها
    all_chars = lower + upper + digits + symbols
    # اطمینان از وجود حداقل یک کاراکتر از هر نوع
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    # پر کردن بقیه رمز عبور با کاراکترهای تصادفی
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    # بر زدن لیست برای اینکه ترتیب قابل پیش‌بینی نباشد
    random.shuffle(password)
    # تبدیل لیست به رشته و بازگرداندن آن
    return "".join(password)
    # گرفتن ورودی از کاربر
try:
    password_length = int(input("طول رمز عبور مورد نظر خود را وارد کنید (مثلاً 12): "))
    generated_password = generate_strong_password(password_length)
    if generated_password:
        print(f"رمز عبور تولید شده برای شما: {generated_password}")
except ValueError:
    print("لطفاً یک عدد صحیح وارد کنید.")
