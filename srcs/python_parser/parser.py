import requests
from bs4 import BeautifulSoup


# URL = "https://tutortop.ru/"

# def get_html(url):
#     result = requests.get(url)
#     return result

# def get_prog_courses(html): 
#     soup = BeautifulSoup(html.text, 'lxml')
#     div = soup.find_all('div', 'open')
#     for k in range (len(div)):
#         for i in div:
#             li = i.find('li')
#         print(li)
#     courses = []

#     print(li)

#     for l in div:
#         try:
#             # print(l.get_text())
#             courses.append (
#                 {
#                  'name':l.get_text(),
#                  'link_adress':l.find('ul').find('li').find('a').get('href')
#                 }
#             )
#         except AttributeError:
#             print("OHMYGOD")
#     return courses

# def get_contact(html):
#     soup = BeautifulSoup(html.text, 'html.parser')
#     items = soup.find_all('div', class_='direction__wrap__box__line')
#     # items = soup.find_all('h2')
#     cards = {}

#     # print(items)
#     for item in items:
#         try:
#             cards.append (
#                 {
#                  'title':item.find('h2').get_text(),
#                  'name_adress':item.find('li').get_text(),
#                  'link_adress':item.find('li').find('a').get('href')
#                 }
#             )
#         except AttributeError:
#             print("That shit")
#     return cards

# def get_all_courses(html):
#     needl = []
#     return needl
    

# html = get_html(URL)
# cards = []
# cards = get_prog_courses(html)
# for i in range (len(cards)):
#     print(cards[i])


URL = "https://tutortop.ru/"
COURSE = "https://tutortop.ru/courses_selection/"
allLinks = []
tmp_allLinks = []
courses_prog = []
courses_uprv = []
courses_mark = []
courses_desg = []
courses_anlt = []
courses_makecontent = []

def get_html(url):
    result = requests.get(url)
    return result

def get_all_links(html): 
    soup = BeautifulSoup(html.text, 'lxml')
    div = soup.find_all('div', class_="ac")
    courses = []
    count = 0

    for l in div:
        if count < 6:
            count += 1
            courses.append ( {'name':'---------------------------------------------------------------------'})
            li = l.find('div', class_="ac-a").find('nav').find('ul').find_all('li')
            for k in li:
                try:
                    if (k.get_text()[:13] == "Все курсы про"):
                        None
                    else:
                        courses.append (
                            {
                            'name':k.get_text(),
                            'link_adress':k.find('a').get('href')
                            }
                        )
                except AttributeError:
                    None
        else:
            break
    return courses

mainHtml = get_html(URL)
allLinks = get_all_links(mainHtml)
# for kek in allLinks:
#     if (kek['name'][:13] == "Все курсы про"):
#         tmp_allLinks.append(kek)
# for kek in allLinks:
#     if len(tmp_allLinks) == 0:
#         tmp_allLinks.append(kek)
#     else:
#         for j in tmp_allLinks:
#             if kek['link_adress'] == j['link_adress']:
#                 tmp_allLinks.remove(j)
#         tmp_allLinks.append(kek)
for i in range(len(allLinks)):
    print(allLinks[i])
     







# if (allLinks[i]['link_adress'][:38] == COURSE):
#     print(allLinks[i]['name'])


# for kek in allLinks:
#     if len(tmp_allLinks) == 0:
#         tmp_allLinks.append(kek)
#     else:
#         for j in tmp_allLinks:
#             if kek['name'] == j['name']:
#                 tmp_allLinks.remove(j)
#         tmp_allLinks.append(kek)