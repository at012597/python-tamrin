
#در این مسئله، ابتدا عدد ورودی را به صورت لیستی از کاراکترها در نظر می‌گیریم. سپس، تعداد دفعاتی که ارقام ۴ و ۷ ظاهر شده‌اند را می‌شماریم و آنها را با هم جمع می‌کنیم.


digits = input().strip()
lucky_count = sum(1 for d in digits if d in ('4', '7'))

if lucky_count in (4, 7):
    print("YES")
else:
    print("NO")
