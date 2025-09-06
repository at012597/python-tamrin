#برنامه برای پیدا کردن اعداد زوج از صفر تا صد با حلقه 

print ('enter number =')
n= int (input())
number = 0
while  number < n :
    number +=1
    if number % 2 == 0 :
        print (number)
