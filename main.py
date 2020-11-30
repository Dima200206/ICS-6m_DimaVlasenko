
"""Головне меню"""

import os
from process_data import create_zajavka
from data_service import show_orders, show_clients, get_orders, get_clients
 MAIN_MENU = \

"""
~~~~~~ ОБРОБКА ЗАЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~~~~~

1 - вивід заявок на екран
2 - запис результата в файл
3 - вивід списка накладних
4 - вивід списка кліентів
0 - завершення роботи 
________________________
"""

TITEL = "Аналіз зміни рівня цін на продовольчі товари"

HEADER = \
    """
    ================================================================================
    Найменування ринку | Найменування товара | Одиниця виміру | Зміна рівня цін по рокам
    ====================================================================================
    """

FOOTER = \
"""

"""

STOP_MESSAGE = "Для продовження натисніть клавішу Enter"

def show_zajavka_table(zajavka_list)
"""вивід на екран таблиці заявок
"""
print(f"\n\n{TITEL:^92}")
print(HEADER)

for zajavka in zajavka_list:
    print(f"{zajavka[oborud]:20}",
    f"{zajavka['client']:20}",
    f"{zajavka['zakaz']}",
    f"{zajavka['kol']:>14}", # число вирівнюється по середині
    f"{zajavka['price']:>15.2f}", # число флов дріб 
    f"{zajavka['total']:>15.2f}",
    )              """do formating for correct printing 'f-string' """

print(FOOTER)

def write_zajavka(zajavka_list):
    """ запис заявок в файл 
    """
    with open('.\data\zajavka.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line = zajavka['oborud'] + ';' +      \
                   zajavka['client'] + ';' +      \
                   zajavka['zakaz'] + ';' +       \ 
                   str(zajavka['kol']) + ';' +    \
                   str(zajavka['price']) + ';' +  \
                   str(zajavka['total']) + '\n' 
            
            zajavka_file.write(line)

print("Файл успішно сформовано ...")

while True:

    os.system('cls')
    print(MAIN_MENU)
    comand_number = input("ВВедіть номер команди: ")
    
    # обробка команд користувача
    if comand_number = '0':
        print('\nПрограмма завершила роботу')
        exit()


    elif comand_number = '1':
        zajavka_list = create_zajavka()
        show_zajavka_table()
        input(STOP_MESSAGE)

    elif comand_number = '2':
            zajavka_list = create_zajavka()
            write_zajavka(zajavka_list)
            input(STOP_MESSAGE)

    elif comand_number = '3':
        orders = get_orders()
        show_orders(orders)
        input(STOP_MESSAGE)


    elif comand_number = '4':
        clients = get_clients()
        show_clients(clients)
        input(STOP_MESSAGE)



        