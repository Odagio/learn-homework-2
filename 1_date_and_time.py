"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # from datetime import datetime, timedelta
    dt_now = datetime.now()
    delta1 = timedelta(days = 1)
    delta2 = timedelta(days = 30)
    dt_yesd = dt_now - delta1
    dt_30dago = dt_now - delta2
    print (f'сегодня {dt_now}, завтра {dt_yesd},когда то {dt_30dago}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    from datetime import datetime
    date_string = "01/01/20 12:10:03.234567"

    date_dt = datetime.strptime(date_string, '%d/%m/%Y %H:%m')
    print(date_dt)

    # from datetime import datetime
    # date1 = ('01/01/20 12:10:03.234567')
    # date_string2 = datetime.strftime(date1,'%d.%m.%Y %H:%M')
    # print(date_string2) 
    # # date_dt = date1.strptime( '%d/%m/%Y')
    # # print(date_dt)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))