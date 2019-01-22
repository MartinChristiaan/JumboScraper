from lxml import html
import requests

from googlesearch import search
import pandas as pd 
# to search 
import numpy as np
from PIL import Image
from pytesseract import image_to_string
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

groceries = image_to_string(Image.open("bonnetje.jpg"))
groceries=groceries.splitlines()
groceries= ["jumbo " + item for item in groceries]

page = requests.get("https://www.jumbo.com/jumbo-fijn-volkoren-heel-800g/39778STK/")
tree = html.fromstring(page.content)
collumns = tree.xpath('//th[@class="nutrition-title"]/text()')
print(collumns)
rows = []


def extract_value_from_string(values):
         
        try:
            values = [float(value.split()[0]) for value in values]
        except Exception:
            values = [float(value.split()[1]) for value in values]
        return values

for item in groceries[::2]:
    google_results = search(item, tld="co.in", num=3, stop=1, pause=1) 
    google_results= [ result for result in google_results if "jumbo" in result ]
    if len(google_results) > 0:
        page = requests.get(google_results[0])
        tree = html.fromstring(page.content)

        
        values = tree.xpath('//td/text()')
        if len(values)==0:
            print(item + " has no proper jumbo page")
        else:            
            if len(values) >= 2*len(collumns):
                values = values[1::2]
  
            if len(values)%len(collumns)==1:
                del values[1] #"Remove second energy thing" 
            if "/kcal" in values[0]:
                print("Replaced")
                values[0] = values[0].replace("/kcal"," kcal")



            
            float_values = []
            print(values)
            try:
                for value in values:
                    if value[0] == '<':
                        value = value[1:]

                    try:
                        float_values.append(float(value.split()[0])) 
                    except Exception:
                        float_values.append(float(value.split()[1]))
                rows.append(np.array(float_values))       
            except Exception:
                print(item + " did not work")

    else:
        print(item + " not found!")

rows = np.array(rows)
print(rows.shape)

df = pd.DataFrame(rows,columns=collumns)
df.to_csv('Nutrition_Results.csv')


# url = 'https://www.jumbo.com/producten?'
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page.read())
# links = soup.findAll("a")
# #print(soup.prettify())
# #%%
# categories = []
# for link in links:
#     try:
#         mylink=link["href"]
#         if "producten/categorieen" in mylink:
#             categories.append(mylink)
#     except Exception:
#         print("No Link")

# print(str(len(categories)) + " categorieen")


# page = urllib.request.urlopen(categories[0])
# soup = BeautifulSoup(page.read())
# links = soup.findAll("a")


# for link in links:
#     try:
#         mylink=link["href"]
#         print(mylink)
#     except Exception:
#         print("No Link")




