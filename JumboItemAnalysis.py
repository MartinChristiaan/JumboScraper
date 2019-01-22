from lxml import html
import requests
from multiprocessing import Pool
# to search 
import numpy as np
from PIL import Image
urls=["https://www.jumbo.com/jumbo-gelderse-rookworst-375g/162461ZK/","https://www.jumbo.com/jumbo-aardbei-yoghurt-griekse-stijl-1kg/187095EM/","https://www.jumbo.com/davitamon-junior-3-kauwvitamines-framboos-kauwtabletten-60-stuks-52g/495019STK/"]
import time

def analyse_url(url):    
    
    # What is the weight?
    # How many collumns are there in the table

    name = 0
    splitUrl= url.split('/')
    namepart = splitUrl[3]

    namepart =namepart.split('-')
    potentialWeigth = namepart[-1]
    hasWeight= False
    weight = 0

    if potentialWeigth[-2:] == 'kg':
        weight= float(potentialWeigth[:-2])
    elif potentialWeigth[-1] == 'g':
        weight=float(potentialWeigth[:-1])/1000 
    if weight > 0:
        del namepart[-1]
    namepart = [part.capitalize() for part in namepart]
    name =' '.join(namepart)



    return weight,name
    #print(weight)
import math   


    # Number of columns
def get_nutrition_values(tree):
    collumnHeaders = tree.xpath('//th[@class="jum-nutiriton-heading"]/text()')
    ncols = len(collumnHeaders)
    if "per 100 g" not in collumnHeaders:
        print("Not valid")
        return []
    values = tree.xpath('//td/text()')

    if "/kcal" in values[0]:
        print("Replaced")
        values[0] = values[0].replace("/kcal"," kcal")

    # Remove % RI Values 
    l1=len(values)
    values = [value for value in values if not value[-1]  == '%'] 
    if l1>len(values):
        ncols-=1
    
    values = [value for value in values if not "kJ" in value] # Remove kJ values
    values = values[::ncols] # Remove not 100g rows
    if len (values) > 8 :
        values=values[:8]

    float_values = []
    for value in values:
        try:
            float_values.append(float(value.split()[0])) 
        except Exception:
            float_values.append(float(value.split()[1]))

    return float_values

for url in urls:    
    page = requests.get(url)
    tree = html.fromstring(page.content)
    print(get_nutrition_values(tree))






    


# for urlpart in splitUrl:
#     urlpartpart = urlpart.split('/')
#     if urlpart[-1] = 'g' and 


        
# if len(values) >= 2*len(collumns):
#     values = values[1::2]

# if len(values)%len(collumns)==1:
#     del values[1] #"Remove second energy thing" 
# if "/kcal" in values[0]:
#     print("Replaced")
#     values[0] = values[0].replace("/kcal"," kcal")

# float_values = []
# print(values)
# try:
#     for value in values:
#         if value[0] == '<':
#             value = value[1:]

#         try:
#             float_values.append(float(value.split()[0])) 
#         except Exception:
#             float_values.append(float(value.split()[1]))
#     rows.append(np.array(float_values))       
# except Exception:
#     print(item + " did not work")


