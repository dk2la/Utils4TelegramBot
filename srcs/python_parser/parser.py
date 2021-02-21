import requests
from bs4 import BeautifulSoup 
import csv


URL = "https://tutortop.ru/"
COURSE = "https://tutortop.ru/courses_selection/"
HEADERS = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}
CSV = 'dataa.csv'

# ['nameCourse',
                # 'Company', 'Rate', 'Price', 'Min. price', 'Start Date', 'Duration', 'link']

allLinks = []
tmp_allLinks = []
courses_prog = []
courses_uprv = []
courses_mark = []

# div class name = "m-course-name-link"
def get_html(url, params=''):
    result = requests.get(url, headers=HEADERS)
    return result.text

def get_all_links(html): 
    soup = BeautifulSoup(html.text, 'lxml')
    div = soup.find_all('div', class_="ac")
    courses = []
    count = 0

    for l in div:
        if count < 6:
            count += 1
            courses.append ( {'name':'---------------------------------------------------------------------',
                'link_adress':'----------------------------------------'} )
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

# Сделать массив имен исходя из названия профессий, и по индексу закидывать значения запаршенные по каждой ссылке

def getStatistic(html):
    soup = BeautifulSoup(html.text, 'lxml')
    div = soup.find_all('div', class_="tab-course-item")
    courses = []

    for l in div:
        try:
            courses.append (
                {
                    'nameCourse':l.find('div', class_="tab-course-col tab-course-col-name").find('div', class_="m-course-name-link").get_text(),
                    'Company':l.find('div', class_="tab-course-col tab-course-col-school").find('div',
                        class_="m-course-price-details").find('div', class_="course_box__top_school_header").find('a').get_text(),
                    'Rate':l.find('div', class_="tab-course-col tab-course-col-school").find('div',
                        class_="m-course-price-details").find('div', class_="course_box__top_school_header").find('div', class_="course__wrap__box__top_rating").get_text(),
                    'Price':l.find('div', class_="tab-course-col tab-course-col-flex tab-course-col-price").find('span').get_text(),
                    'Min. price':l.find('div', class_="tab-course-col tab-course-col-flex tab-course-col-rassrochka").find('span').get_text(),
                    'Start Date':l.find('div', class_="tab-course-col tab-course-col-date-t tab-course-col-date").get_text(),
                    'Duration':l.find('div', class_="tab-course-col tab-course-col-flex tab-course-col-dlitelnost").find('span').get_text(),
                    'link':l.find('div', class_="tab-course-col tab-course-col-link").find('a').get('href')
                }
            )
        except AttributeError:
            print('OH NO')
    return courses
    

def saveInformationAboutCourses(courses_uprv, path):
    with open(path, "w", newline='') as file:
        write = csv.writer(file, delimiter=' ')
        write.writerow(['name', 'nameCourse', 'Company', 'Rate', 'Price', 'Min. price', 'Start Date', 'Duration', 'link'])
        for l in courses_uprv:
            for k in l['info']:
                write.writerow([l['name'], k['nameCourse'], k['Company'], k['Rate'], k['Price'], k['Min. price'], k['Start Date'], k['Duration'], k['link']])
            write.writerow('\n\n\n')
            write.writerow(['name', 'nameCourse', 'Company', 'Rate', 'Price', 'Min. price', 'Start Date', 'Duration', 'link'])


def parser():
    mainHtml = get_html(URL)
    allLinks = get_all_links(mainHtml)
    for i in range(len(allLinks)):
        courses_prog.append(allLinks[i]['name'])
    for i in range(len(courses_prog)):
        if (allLinks[i]['link_adress'][:3] != "---"):
            new_html = get_html(allLinks[i]['link_adress'])
            courses_mark = getStatistic(new_html)
            courses_uprv.append({'name':courses_prog[i], 'info':courses_mark})
    saveInformationAboutCourses(courses_uprv, CSV)

parser()
