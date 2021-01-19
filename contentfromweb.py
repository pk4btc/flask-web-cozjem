import requests,json
from bs4 import BeautifulSoup



class content_foods:

    #the targer i want to open
    url='https://www.kwestiasmaku.com/blog-kulinarny/category/dania-obiadowe'
    respons_web=requests.get(url)

    tabObiadek ={}
    tabObiadek['obiadek']= []

    tabObiadekImg ={}
    tabObiadekImg['obiadekImg']= []

    if respons_web.status_code==200:
        print('webbsite opened')


    soup=BeautifulSoup(respons_web.text,'html.parser')

    recipe=soup.find("div",{"class":"views-bootstrap-grid-plugin-style"})
    img=soup.find("div",{"class":"views-bootstrap-grid-plugin-style"})



    for i in recipe.select("div > span:nth-child(1) > a:nth-child(1)"):
        tabObiadek['obiadek'].append(i.text)


    else:
        print("Error")

    for link in img.find_all('img'):
        tabObiadekImg['obiadekImg'].append(link.get('src'))

    else:        print("Error img")



    for i in tabObiadek['obiadek']:
        print(tabObiadek)

    for i in  tabObiadekImg['obiadekImg']:
            print(tabObiadekImg)

    def metodatabObiadek(a):
        return a

    def metodatabObiadekImg(a):
        return a


    with open('contentfromweb.json', 'w') as json_file:
        json.dump(tabObiadek, json_file)


    with open('contentfromweb.json', 'a') as json_file:
        json.dump(tabObiadekImg, json_file)


    metodatabObiadek(tabObiadek)
    metodatabObiadekImg(tabObiadekImg)


class content_breakfast:

    #the targer i want to open
    url='https://www.kwestiasmaku.com/dania_dla_dwojga/sniadania/przepisy.html'
    respons_web=requests.get(url)

    tabSniadanie = {}
    tabSniadanie['sniadanie'] = []
    # tabSniadanie= []

    tabSniadanieImg= {}
    tabSniadanieImg['sniadanieImg'] = []

    if respons_web.status_code==200:
        print('webbsite opened')


    soup=BeautifulSoup(respons_web.text,'html.parser')

    recipe=soup.find("div",{"class":"views-bootstrap-grid-plugin-style"})
    img=soup.find("div",{"class":"views-bootstrap-grid-plugin-style"})



    for i in recipe.select("div > span:nth-child(1) > a:nth-child(1)"):
        tabSniadanie['sniadanie'].append(i.text)


    else:
        print("Error")

    for link in img.find_all('img'):
        tabSniadanieImg['sniadanieImg'].append(link.get('src'))

    else:        print("Error img")



    for i in tabSniadanie['sniadanie']:
        print(tabSniadanie)

    for i in tabSniadanieImg['sniadanieImg']:
        print(i)

    def metodatabSniadanie(a):
        return a

    def metodatabSniadanieImg(a):
        return a
    #zapisywanie do json
    with open('contentfromweb.json', 'a') as json_file:
        json.dump(tabSniadanie, json_file)


    with open('contentfromweb.json', 'a') as json_file:
        json.dump(tabSniadanieImg, json_file)

    metodatabSniadanie(tabSniadanie)
    metodatabSniadanieImg(tabSniadanieImg)


class content_kolacja:

    #the targer i want to open
    url='https://www.kwestiasmaku.com/przepisy/kolacje'
    respons_web=requests.get(url)

    tabKolacja = {}
    tabKolacja['kolacja'] = []
    # tabSniadanie= []

    tabKolacjaImg= {}
    tabKolacjaImg['kolacjaImg'] = []

    if respons_web.status_code==200:
        print('webbsite opened')


    soup=BeautifulSoup(respons_web.text,'html.parser')

    recipe=soup.find("div",{"class":"views-bootstrap-grid-plugin-style"})
    img=soup.find("div",{"class":"views-bootstrap-grid-plugin-style"})



    for i in recipe.select("div > span:nth-child(1) > a:nth-child(1)"):
        tabKolacja['kolacja'].append(i.text)


    else:
        print("Error")

    for link in img.find_all('img'):
        tabKolacjaImg['kolacjaImg'].append(link.get('src'))

    else:        print("Error img")



    for i in tabKolacja['kolacja']:
        print(tabKolacja)

    for i in tabKolacjaImg['kolacjaImg']:
        print(i)

    def metodatabKolacja(a):
        return a

    def metodatabKolacjaImg(a):
        return a
    #zapisywanie do json
    with open('contentfromweb.json', 'a') as json_file:
        json.dump(tabKolacja, json_file)


    with open('contentfromweb.json', 'a') as json_file:
        json.dump(tabKolacjaImg, json_file)

    metodatabKolacja(tabKolacja)
    metodatabKolacjaImg(tabKolacjaImg)

