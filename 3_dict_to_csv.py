"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv
    user_list =[
    {'name':'Andre','age':'28','job':'Worker'},
    {'name':'Ivan','age':'17','job':'Sitter'},
    {'name':'Volo','age':'38','job':'Zhdun'},
    {'name':'Alfa','age':'78','job':'Trener'},
    {'name':'Paul','age':'28','job':'Worker'}
    ]

    with open('dict.csv', 'w', encoding='utf8') as f:
        rields = ['name','age','job']
        transport = csv.DictWriter(f,rields, delimiter=';')
        transport.writeheader()
        for user in user_list:
            transport.writerow(user)
if __name__ == "__main__":
    main()
