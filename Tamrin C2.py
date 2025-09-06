#یه ماشین حسابه که با محیط کنسول میاد 4 عمل اصلی رو انجام میده 
#در این کد هر عملگر به صورت یه تابع در نظر گرفته شده تا یکم کد زنی رو پیشرفته تر کنیم 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر ممکن نیست!"
    return x / y
print("ماشین حساب ساده پایتون")
print("عملگرها: + (جمع), - (تفریق), * (ضرب), / (تقسیم)")
try:
    num1 = float(input("عدد اول را وارد کنید: "))
    operator = input("یکی از عملگرها را وارد کنید: ")
    num2 = float(input("عدد دوم را وارد کنید: "))
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = "عملگر وارد شده نامعتبر است."
    print(f"نتیجه: {result}")
except ValueError:
    print("خطا: لطفاً فقط عدد وارد کنید.")
