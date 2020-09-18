from datetime import datetime
date1 = ('01/01/20 12:10:03.234567')
date_string2 = datetime.strftime(date1,'%d.%m.%Y %H:%M')
print(date_string2) 
# date_dt = date1.strptime( '%d/%m/%Y')
# print(date_dt)

dt_now = datetime.now()
print(dt_now.strftime('%d.%m.%Y %H:%M')) # '01.03.2020 11:10'
print(dt_now.strftime('%Y-%m-%d')) # '2020-03-01'
