""" розрахунок заявок на товари по магазину"""

from data_service import get_clients, get_orders


# словник в якому будуть накоплюватись результати розрахунків
zajavka = {
'oborud' : "", # назва устаткування
'client' : "", #назва кліента
'zakaz' : "", #номер заказа
'kol' : 0, #кількість товару
'price' : 0.0, #ціна
'total' : 0.0  #сума
}

def create_zajavka():
    """формування списку заявок по магазину
    
    Returns:
    zajavka_list: список заявок
    """
def get_client_name(client_code):
    """знаходить
    
    Args:
       client_code ([Type]): [description]
       
       Returns:
       [type]: [description]
       """

    return client_name




# накопичувач заявок
zajavka_list = []

orders = get_orders()
client = get_clients()


for order in orders:


    zajavka_work = zajavka.copy()

    zajavka_work['oborud'] = order[2]
    zajavka_work['zakaz'] = order[1]
    zajavka_work['kol'] = order[3]
    zajavka_work['price'] = order[4]
    zajavka_work['total'] = zajavka_work['kol'] * zajavka_work['price']

    zajavka_list.append(zajavka_work)

return zajavka_list

zajavkas = create_zajavka()

for item in zajavkas:
    print(item)



