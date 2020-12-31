import  requests
from bs4 import BeautifulSoup


URL = "https://tutortop.ru/"

def get_html(url):
    result = requests.get(url)
    return result

def get_prog_courses(html): 
    soup = BeautifulSoup(html.text, 'lxml')
    div = soup.find_all('div', 'open')
    for k in range (len(div)):
        for i in div:
            li = i.find('li')
        print(li)
    courses = []

    print(li)

    for l in div:
        try:
            # print(l.get_text())
            courses.append (
                {
                 'name':l.get_text(),
                 'link_adress':l.find('ul').find('li').find('a').get('href')
                }
            )
        except AttributeError:
            print("OHMYGOD")
    return courses

def get_contact(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='direction__wrap__box__line')
    # items = soup.find_all('h2')
    cards = {}

    # print(items)
    for item in items:
        try:
            cards.append (
                {
                 'title':item.find('h2').get_text(),
                 'name_adress':item.find('li').get_text(),
                 'link_adress':item.find('li').find('a').get('href')
                }
            )
        except AttributeError:
            print("That shit")
    return cards

def get_all_courses(html):
    needl = []
    return needl
    

html = get_html(URL)
cards = []
cards = get_prog_courses(html)
for i in range (len(cards)):
    print(cards[i])