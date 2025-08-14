
'''
مشکل: تراموا

توضیح راه حل:
ابتدا، یک حلقه می‌نویسیم تا تعداد مسافرانی که در هر ایستگاه پیاده و سوار می‌شوند را به عنوان ورودی دریافت کند.

سپس محاسبه می‌کنیم که بعد از هر ایستگاه چند مسافر در تراموا باقی می‌مانند.

تعداد مسافران بعد از اولین ایستگاه را در متغیری که حداکثر ظرفیت تراموا را ثبت می‌کند، ذخیره می‌کنیم.

در هر ایستگاه جدید، تعداد فعلی مسافران را با این متغیر مقایسه می‌کنیم تا در صورت نیاز آن را به‌روزرسانی کنیم،

تا زمانی که به آخرین ایستگاه برسیم.
'''



station_count = int(input())
max_people = 0
current_people = 0

for _ in range(station_count):
    out_count, in_count = map(int, input().split())
    current_people = (current_people - out_count) + in_count
    if max_people < current_people:
        max_people = current_people

print(max_people)
