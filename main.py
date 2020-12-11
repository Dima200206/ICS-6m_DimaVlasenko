
"""Головне меню"""

import os
from process_data import create_zajavka
from data_service import show_orders, show_clients, get_orders, get_clients
 
 
 MAIN_MENU = """

~~~~~~ Аналіз зміни рівня цін на продовольчі товари ~~~~~~~~~~~

1 - вивід заявок на екран
2 - запис результата в файл
3 - вивід списка продовольчих товарів
4 - вивід списка товарів
0 - завершення роботи 
________________________
"""

TITEL = "Аналіз зміни рівня цін на продовольчі товари"

HEADER = 
    """
    ======================================================================================================
    Найменування ринку | Найменування товара | Одиниця виміру | Зміна рівня цін по рокам                 |
    ======================================================================================================
                                                               2007 |   2008     |   2011   |   2017     |
                                                                urn |   urn | %   | urn |  %  | urn | %  |
    ======================================================================================================
    """

FOOTER = \
"""
===========================================================================================================
"""

STOP_MESSAGE = "Для продовження натисніть клавішу Enter"

def show_analiz_table(analiz_list)
"""вивід на екран таблиці заявок
"""
print(f"\n\n{TITEL:^92}")
print(HEADER)

for analiz in analiz_list:
    print(f"{analiz[namerunok]:20}",
    f"{analiz['nametovar']:20}",
    f"{analiz['kol']}",
    f"{analiz['price2007']:>14}", # число вирівнюється по середині
    f"{analiz['price2008']:>15.2f}", # число флов дріб 
    f"{analiz['procent2008']:>15.2f}",
    f"{analiz['price2011']:>15.2f}",
    f"{analiz['procent2011']:>15.2f}",
    f"{analiz['price2017']:>15.2f}",
    f"{analiz['procent2017']:>15.2f}",
    )              """do formating for correct printing 'f-string' """

print(FOOTER)

def write_analiz(analiz_list):
    """ запис заявок в файл 
    """
    with open('.\data\analiz.txt', "w") as analiz_file:
        for analiz in analiz_list:
            line = analiz['namerunok'] + ';' +      \
                   analiz['nametovar'] + ';' +      \
                   analiz['kol'] + ';' +       \ 
                   str(analiz['price2007']) + ';' +    \
                   str(analiz['price2008']) + ';' +  \
                   str(analiz['procent2008']) + ';' +  \
                   str(analiz['price2011']) + ';' +  \
                   str(analiz['procent2011']) + ';' +  \    
                   str(analiz['price2017']) + ';' +  \
                   str(analiz['procent2017']) + '\n' 
            
            analiz_file.write(line)

print("Файл успішно сформовано ...")

while True:

    os.system('cls')
    print(MAIN_MENU)
    comand_number = input("ВВедіть номер команди: ")
    
    # обробка команд користувача
    if comand_number == '0':
        print('\nПрограмма завершила роботу')
        exit()


    elif comand_number = '1':
        analiz_list = create_analiz()
        show_analiz_table()
        input(STOP_MESSAGE)

    elif comand_number = '2':
            analiz_list = create_analiz()
            write_analiz(analiz_list)
            input(STOP_MESSAGE)

    elif comand_number = '3':
        orderstov = get_orderstov()
        show_orderstov(orderstov)
        input(STOP_MESSAGE)


    elif comand_number = '4':
        tovar = get_tovar()
        show_tovar(tovar)
        input(STOP_MESSAGE)



        