"""Модуль для роботи з файлами первинних данних - зчитування та вивід на єкран """

def get_tovar():
    """ повертає список кліентів який отримує з файлом 'client.txt'

    Returns:
    client_list: список кліентів """

    with open(".\data\dvornik.txt") as tovar_file:
        from_file = tovar_file.readlines()

# накопичувачь кліетнів
        tovar_list = [] 

        for line in from_file:
#відрізки '\n' в кінці рядка
            line = line[:-2]

            line_list = line.split(';')
            tovar_list.append(line_list)

            return tovar_list

            def show_tovar(tovar):
                
    #"""Виводить на екран список клієнтів заданого діапазона"""

    #Args:
        #clients ([list]): список клієнтів
    

    tovar_code_from = input("З якого кода? ")
    tovar_code_to   = input("По який код? ") 

    for tovar in tovars:
        if  tovar_code_from <= tovar[0] <= tovar_code_to: 
            print("код: {:4} назва: {:17} адреса: {:20}".format(client[0], client[1], client[2]))!!!!



                tovars = get_tovars()
                show_tovars(tovars)