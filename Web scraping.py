import pandas as pd
import requests
from bs4 import BeautifulSoup
product_names = []
prices = []
descriptions = []
reviews = []

for i in range(1,3):
    
    url="https://www.flipkart.com/search?q=laptop+under+40000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_6_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_4_6_na_na_ps&as-pos=4&as-type=RECENT&suggestionId=laptop+under+40000&requestId=22991cc9-9d40-4e48-bd36-c9f53f4c77e6&as-searchtext=laptop&page="+str(i)

    r=requests.get(url)

    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="DOjaWF gdgoEp")

    names=box.find_all("div",class_="KzDlHZ")

    for i in names:
        name=i.text
        product_names.append(name)

#print(product_names)
    price=box.find_all("div",class_="Nx9bqj _4b5DiR")

    for i in price:
        pr=i.text
        prices.append(pr)

    description=box.find_all("div",class_="_6NESgJ")

    for i in description:
        desc=i.text
        descriptions.append(desc)


print(len(product_names),len(prices),len(descriptions))

df=pd.DataFrame({'Product Name':product_names,'Price':prices,'Description':descriptions})
print(df)
df.to_csv(r'laptops_flipkart.csv',index=False)