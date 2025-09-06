#ما در این تمرین  قصد داریم  چنتا اسم رو در فایل با جیسون  ذخیره کنیم و دوباره فراخانی کنیم 
#کد اول نوشته فایل و جیسون ساخته شده و سپس کامنت میکنیم تا  از آنها استفاده کنیم 

import json 
from pathlib import Path
'''
members = [
{'mammad' : 'kod meli 428111111 , age 50 , numbe 091211111' },
{'mammad' : 'kod meli 428222222 , age 100 , numbe 091222222'} ,
{'mammad' : 'kod meli 428333333 , age 150 , numbe 091233333'} ,
{'mammad' : 'kod meli 428444444 , age 200 , numbe 091244444'} 

]
data = json.dumps(members)
print (data)
Path ("members.json").write_text(data)'''
data = Path("members.json").read_text ()

print (data)
