"""Модуль для роботи з файлами первинних данних - зчитування та вивід на єкран """

def get_clients():
    """ повертає список кліентів який отримує з файлом 'client.txt'

    Returns:
    client_list: список кліентів """

    with open(".\data\dvornik.txt") as clients_file:
        from_file = clients_file.readlines()

# накопичувачь кліетнів
        clients_list = [] 

        for line in from_file:
#відрізки '\n' в кінці рядка
            line = line[:-2]

            line_list = line.split(';')
            clients_list.append(line_list)

            return client_list

            def show_clients(clients):
                
"""виводить на екран список клієнтів заданого діапазона

    Args:
        clients ([list]): список клієнтів
    """

    client_code_from = input("З якого кода? ")
    client_code_to   = input("По який код? ") 

    for client in clients:
        if  client_code_from <= client[0] <= client_code_to: 
            print("код: {:4} назва: {:17} адреса: {:20}".format(client[0], client[1], client[2]))



                clients = get_clients()
                show_clients(clients)