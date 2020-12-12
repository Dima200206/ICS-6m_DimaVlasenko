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



def create_analiz():
    """формування списку заявок по магазину
    
    Returns:
    zajavka_list: список заявок
    """
def get_orderstov_name(orderstov_code):
    """знаходить назву клыента по коду
    
    Args:
       client_code ([Type]): код клыента
       
       Returns:
       [type]: назва клыента
       """
      
    for orderstov in orderstovs:
        if orderstov_code == orderstov[0]:
            return orderstov[1]

    return "назва не знайдена"

#def get_midlprices


# накопичувач заявок
    analiz_list = []

    midlprices = get_midlprices()
    orderstovs = get_orderstovs()

    for midlprice in midlprices:


        analiz_work = analiz.copy()

        analiz_work['namerunok'] = midlprice[5]
        analiz_work['nametovar'] = get_orderstov_name(midlprice[1])
        analiz_work['kilogram'] = get_orderstov_name(midlprice[2])
        analiz_work['price2007'] = midlprice[1]
        analiz_work['price2008'] = midlprice[2]
        analiz_work['procent2008'] = float(analiz_work['price2007']) / float(analiz_work['price2008'])* 100
        analiz_work['price2011'] = midlprice[3]
        analiz_work['procent2011'] =  float(analiz_work['price2008']) / float(analiz_work['price2011'])* 100
        analiz_work['price2017'] = midlprice[4]
        analiz_work['procent2017'] =  float(analiz_work['price2011']) / float(analiz_work['price2017'])* 100

        analiz_list.append(analiz_work)

    return analiz_list

#analizs = create_analiz()

   # for item in analizs:
    #    print(item)



