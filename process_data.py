""" розрахунок заявок на товари по магазину"""

from data_service import get_tovars, get_orderstovs


# словник в якому будуть накоплюватись результати розрахунків
analiz = {
'namerunok' : "", # назва устаткування!!! rewrite !!!!
'nametovar' : "", #назва кліента
'kol' : "", #номер заказа
'price2007' : 0, #кількість товару
'price2008' : 0.0, #ціна
'procent2008' : 0.0  #сума
'price2011' : 0.0  #сума
'procent2011' : 0.0  #сума
'price2017' : 0.0  #сума
'procent2017' : 0.0  #сума
}

tovars = get_tovars()
orderstovs = get_orderstovs()

def create_analiz():
    """формування списку заявок по магазину
    
    Returns:
    zajavka_list: список заявок
    """
def get_tovar_name(tovar_code):
    """знаходить назву клыента по коду
    
    Args:
       client_code ([Type]): код клыента
       
       Returns:
       [type]: назва клыента
       """
      
           for tovar in tovars:
            if tovar_code = tovar[0]:
               return tovar[1]

   #     return "*** назва не знайдена"




# накопичувач заявок
analiz_list = []




for orderstov in orderstovs:


    analiz_work = analiz.copy()

    analiz_work['namerunok'] = order[2]
    analiz_work['nametovar'] = order[1]
    analiz_work['kol'] = order[3]
    analiz_work['price2007'] = price[7]
    analiz_work['price2008'] = price[8] #zajavka_work['kol'] * zajavka_work['price']
    analiz_work['procent2008'] = order[4]
    analiz_work['price2011'] = price[11]
    analiz_work['procent2011'] = order[4]
    analiz_work['price2017'] = price[17]
    analiz_work['procent2017'] = get_client_name(order[0])

    analiz_list.append(analiz_work)

return analiz_list

analizs = create_analiz()

for item in analizs:
    print(item)



