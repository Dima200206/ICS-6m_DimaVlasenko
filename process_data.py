""" розрахунок заявок на товари по магазину"""

from data_service import get_midlprices, get_orderstovs 


# словник в якому будуть накоплюватись результати розрахунків
analiz = {
'namerunok' : "",     # назва ринку
'nametovar' : "",     #назва товару
'kilogram' : "",      #одиниця
'price2007' : 0.0,    #ціна 2007
'price2008' : 0.0,    #ціна 2008
'procent2008' : 0.0,  #відсоток 2008
'price2011' : 0.0,    #ціна 2011
'procent2011' : 0.0,  #відсоток 2011
'price2017' : 0.0,    #ціна 2017
'procent2017' : 0.0   #відсоток 2017
}

midlprices = get_midlprices()
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
      
    for orderstov in orderstovs:
        if orderstov[0] == orderstov_code:
            return orderstov[1]

    return "назва не знайдена"



# накопичувач заявок
    analiz_list = []

    for midlprice in midlprices:


        analiz_work = analiz.copy()

        analiz_work['namerunok'] = zina[5]
        analiz_work['nametovar'] = get_orderstov_name(zina[1])
        analiz_work['kilogram'] = get_orderstov_name(zina[2])
        analiz_work['price2007'] = zina[1]
        analiz_work['price2008'] = zina[2]
        analiz_work['procent2008'] = prozent[1]
        analiz_work['price2011'] = zina[3]
        analiz_work['procent2011'] =  prozent[2]
        analiz_work['price2017'] = zina[4]
        analiz_work['procent2017'] =  prozent[3]

        analiz_list.append(analiz_work)

    return analiz_list

analizs = create_analiz()

   # for item in analizs:
    #    print(item)



