
"""Головне меню"""

import os
import process_data, data_service
from process_data import create_analiz
from data_service import show_midlprices, show_orderstovs, get_midlprices, get_orderstovs

 
 
MAIN_MENU = \
     """

~~~~~~ Аналіз зміни рівня цін на продовольчі товари ~~~~~~~~~~~

1 - вивід заявок на екран
2 - запис результата в файл
3 - вивід списка продовольчих товарів
4 - вивід списка товарів
0 - завершення роботи 
________________________
"""

TITEL = "Аналіз зміни рівня цін на продовольчі товари"

HEADER = \
    """
    =====================================================================================================================================================
    Найменування ринку | Найменування товара | Одиниця виміру |                                   Зміна рівня цін по рокам                               |
    =====================================================================================================================================================
                                                                 2007      |         2008              |           2011        |          2017           |
                                                                  uah      |   uah       |           % |   uah   |          %  |    uah   |          %   |
    =====================================================================================================================================================
        """

FOOTER = \
"""
=========================================================================================================================================================
"""

STOP_MESSAGE = "Для продовження натисніть клавішу Enter"

def show_analiz_table(analiz_list):

# """Вивід на екран таблиці заявок"""

    print(f"\n\n{TITEL:^92}")
    print(HEADER)

    for analiz in analiz_list:
        print(f"{analiz['namerunok']:15}",
              f"{analiz['nametovar']:10}",
              f"{analiz['kilogram']:^15}",
              f"{analiz['price2007']:4}", # число вирівнюється по середині
              f"{analiz['price2008']:4}", # число флов дріб 
              f"{analiz['procent2008']:^15f}",
              f"{analiz['price2011']:8}",
              f"{analiz['procent2011']:>15}",
              f"{analiz['price2017']:^15}",
              f"{analiz['procent2017']:>15}",
    )              
    #"""do formating for correct printing 'f-string' """

    print(FOOTER)

def write_analiz(analiz_list):
    """ запис заявок в файл 
    """
    with open(r'.\data\analiztab.txt', "w", encoding="utf8") as analiz_file:
        for analiz in analiz_list:
            line = analiz['namerunok'] + ';' +         \
                   analiz['nametovar'] + ';' +         \
                   analiz['kilogram'] + ';' +          \
                   str(analiz['price2007']) + ';' +    \
                   str(analiz['price2008']) + ';' +    \
                   str(analiz['procent2008']) + ';' +  \
                   str(analiz['price2011']) + ';' +    \
                   str(analiz['procent2011']) + ';' +  \
                   str(analiz['price2017']) + ';' +    \
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


    elif comand_number == '1':
        analiz_list = create_analiz()
        show_analiz_table(analiz_list)
        input(STOP_MESSAGE)

    elif comand_number == '2':
            analiz_list = create_analiz()
            write_analiz(analiz_list)
            input(STOP_MESSAGE)

    elif comand_number == '3':
        orderstov = get_orderstovs()
        show_orderstovs(orderstov)
        input(STOP_MESSAGE)


    elif comand_number == '4':
        midlprice = get_midlprices()
        show_midlprices(midlprice)
        input(STOP_MESSAGE)



        