"""Модуль для роботи з файлами первинних данних - зчитування та вивід на єкран """

def get_midlprice():
    """ повертає список кліентів який отримує з файлом 'client.txt'

    Returns:
    client_list: список кліентів """

    with open(".\data\midlprice.txt") as midlprice_file:
        from_file = midlprice_file.readlines()

# накопичувачь кліетнів
        midlprice_list = [] 

    for line in from_file:
#відрізки '\n' в кінці рядка
        line = line[:-2]

        line_list = line.split(';')
        midlprice_list.append(line_list)

    return midlprice_list

def get_orderstov():  
    
    
    with open(".\data\dovidnik.txt") as orderstov_file:
        from_file = orderstov_file.readlines()

# накопичувачь кліетнів
        orderstov_list = [] 

    for line in from_file:
#відрізки '\n' в кінці рядка
        line = line[:-2]

        line_list = line.split(';')
        orderstov_list.append(line_list)

    return orderstov_list  

def show_midlprice(midlprice):
                
    #"""Виводить на екран список клієнтів заданого діапазона"""

    #Args:
        #clients ([list]): список клієнтів
    

    midlprice_code_from = input("З якого кода? ")
    midlprice_code_to   = input("По який код? ") 

    kol_lines = 0

    for midlprice in midlprices:
        if  midlprice_code_from <= midlprice[0] <= midlprice_code_to: 
            print("код: {:4} ціна2007: {:17} ціна2008: {:17} ціна2011: {:17} ціна2017: {:17} наймринок: {:20}".format(midlprice[0], midlprice[1], midlprice[2], midlprice[3], midlprice[4], midlprice[5]))
            kol_lines += 1

        if kol_lines == 0:
            print("По вашому запиту нічого не знайдено!")        
                
midlprices = get_midlprices()
show_midlprices(midlprices)

def show_orderstovs(orderstovs):
    orderstov_code_from = input("З якого кода? ")
    orderstov_code_to   = input("По який код? ") 

    kol_lines = 0

    for orderstov in orderstovs:
        if  orderstov_code_from <= orderstov[0] <= orderstov_code_to: 
            print("код: {:4} назва: {:17} одиниця: {:17}".format(orderstov[0], orderstov[1], orderstov[2]))
            kol_lines += 1

        if kol_lines == 0:
            print("По вашому запиту нічого не знайдено!")        
                
orderstovs = get_orderstovs()
show_orderstovs(orderstovs)